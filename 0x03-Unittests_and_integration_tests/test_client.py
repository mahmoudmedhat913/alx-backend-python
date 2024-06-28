#!/usr/bin/env python3
"""A module for testing the client module"""
import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
from unittest.mock import PropertyMock
from parameterized import parameterized, parameterized_class
from typing import Dict, List
from requests import HTTPError

import client
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """testing the test Github Org Client class"""
    @parameterized.expand(["google", "abc"])
    @patch('client.get_json')
    def test_org(self, org: str, getJson: MagicMock) -> None:
        """test the test org method functionality"""
        gitClient = GithubOrgClient(org)
        self.assertEqual(gitClient.org, getJson.return_value)
        getJson.assert_called_once_with(gitClient.ORG_URL.format(org=org))

    def test_public_repos_url(self) -> None:
        """test the test public repos url property"""
        config = {
            'return_value.repos_url': "https://api.github.com/slam/repos/alx"
        }
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock, **config) as mockOrg:
            test = GithubOrgClient('alx')
            self.assertEqual(
                test._public_repos_url,
                mockOrg.return_value['repos_url']
            )

    @patch('client.get_json')
    def test_public_repos(self, mockGetJson: MagicMock) -> None:
        """test the test public repos method functionality"""
        mockGetJson.return_value = [
            {'name': 'cpp-netlib', 'license': {'key': 'bsl-1.0'}},
            {'name': 'dagger', 'license': {'key': 'apache-2.0'}},
            {'name': 'dot-net', 'license': {'key': 'bsl-1.0'}}
        ]
        propValue = {
            'return_value': 'https://api.github.com/orgs/google/repos'
        }
        with patch('client.GithubOrgClient._public_repos_url',
                new_callable=PropertyMock, **propValue) as mockPublicRepo:
            test = GithubOrgClient('google')
            self.assertEqual(
                test.public_repos(), ['cpp-netlib', 'dagger', 'dot-net']
            )
            mockPublicRepo.assert_called_once()
        mockGetJson.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': "my_license"}}, "my_license", True),
        ({'license': {'key': "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, license: Dict,
                         key: str, expected: bool) -> None:
        """test the test has license method functionality"""
        gh_org_client = GithubOrgClient("google")
        client_has_licence = gh_org_client.has_license(repo, key)
        self.assertEqual(
            GithubOrgClient.has_license(license, key), expected
        )


@parameterized_class(('org_payload', 'repos_payload',
                      'expected_repos', 'apache2_repos'), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """perform integeration tests for Github Org Client class"""
    @classmethod
    def setUpClass(cls) -> None:
        """sets up class fixtures before running testing"""
        def response(url):
            """mock request.get url"""
            config = {'json.return_value': []}
            for payload in TEST_PAYLOAD:
                if url == payload[0]['repos_url']:
                    config = {'json.return_value': payload[1]}
                    break
            return MagicMock(**config)

        cls.get_patcher = patch('requests.get', side_effect=response)
        cls.org_patcher = patch(
            'client.GithubOrgClient.org',
            new_callable=PropertyMock, **{'return_value': cls.org_payload}
        )
        cls.get_patcher.start()
        cls.org_patcher.start()

    def test_public_repos(self) -> None:
        """test the test public repos method"""
        test = GithubOrgClient('google/repos')
        self.assertEqual(
            self.expected_repos,
            test.public_repos(license=None)
        )

    def test_public_repos_with_license(self) -> None:
        """test the public repos with license method"""
        test = GithubOrgClient('google/repos')
        self.assertEqual(
            self.apache2_repos,
            test.public_repos(license="apache-2.0")
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """remove class fixtures after running all tests"""
        cls.get_patcher.stop()
        cls.org_patcher.stop()
