# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.31.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import kubernetes_asyncio.client
from kubernetes_asyncio.client.api.admissionregistration_v1_api import AdmissionregistrationV1Api  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException


class TestAdmissionregistrationV1Api(unittest.IsolatedAsyncioTestCase):
    """AdmissionregistrationV1Api unit test stubs"""

    async def asyncSetUp(self):
        self.api = kubernetes_asyncio.client.api.admissionregistration_v1_api.AdmissionregistrationV1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_mutating_webhook_configuration(self):
        """Test case for create_mutating_webhook_configuration

        """
        pass

    def test_create_validating_admission_policy(self):
        """Test case for create_validating_admission_policy

        """
        pass

    def test_create_validating_admission_policy_binding(self):
        """Test case for create_validating_admission_policy_binding

        """
        pass

    def test_create_validating_webhook_configuration(self):
        """Test case for create_validating_webhook_configuration

        """
        pass

    def test_delete_collection_mutating_webhook_configuration(self):
        """Test case for delete_collection_mutating_webhook_configuration

        """
        pass

    def test_delete_collection_validating_admission_policy(self):
        """Test case for delete_collection_validating_admission_policy

        """
        pass

    def test_delete_collection_validating_admission_policy_binding(self):
        """Test case for delete_collection_validating_admission_policy_binding

        """
        pass

    def test_delete_collection_validating_webhook_configuration(self):
        """Test case for delete_collection_validating_webhook_configuration

        """
        pass

    def test_delete_mutating_webhook_configuration(self):
        """Test case for delete_mutating_webhook_configuration

        """
        pass

    def test_delete_validating_admission_policy(self):
        """Test case for delete_validating_admission_policy

        """
        pass

    def test_delete_validating_admission_policy_binding(self):
        """Test case for delete_validating_admission_policy_binding

        """
        pass

    def test_delete_validating_webhook_configuration(self):
        """Test case for delete_validating_webhook_configuration

        """
        pass

    def test_get_api_resources(self):
        """Test case for get_api_resources

        """
        pass

    def test_list_mutating_webhook_configuration(self):
        """Test case for list_mutating_webhook_configuration

        """
        pass

    def test_list_validating_admission_policy(self):
        """Test case for list_validating_admission_policy

        """
        pass

    def test_list_validating_admission_policy_binding(self):
        """Test case for list_validating_admission_policy_binding

        """
        pass

    def test_list_validating_webhook_configuration(self):
        """Test case for list_validating_webhook_configuration

        """
        pass

    def test_patch_mutating_webhook_configuration(self):
        """Test case for patch_mutating_webhook_configuration

        """
        pass

    def test_patch_validating_admission_policy(self):
        """Test case for patch_validating_admission_policy

        """
        pass

    def test_patch_validating_admission_policy_binding(self):
        """Test case for patch_validating_admission_policy_binding

        """
        pass

    def test_patch_validating_admission_policy_status(self):
        """Test case for patch_validating_admission_policy_status

        """
        pass

    def test_patch_validating_webhook_configuration(self):
        """Test case for patch_validating_webhook_configuration

        """
        pass

    def test_read_mutating_webhook_configuration(self):
        """Test case for read_mutating_webhook_configuration

        """
        pass

    def test_read_validating_admission_policy(self):
        """Test case for read_validating_admission_policy

        """
        pass

    def test_read_validating_admission_policy_binding(self):
        """Test case for read_validating_admission_policy_binding

        """
        pass

    def test_read_validating_admission_policy_status(self):
        """Test case for read_validating_admission_policy_status

        """
        pass

    def test_read_validating_webhook_configuration(self):
        """Test case for read_validating_webhook_configuration

        """
        pass

    def test_replace_mutating_webhook_configuration(self):
        """Test case for replace_mutating_webhook_configuration

        """
        pass

    def test_replace_validating_admission_policy(self):
        """Test case for replace_validating_admission_policy

        """
        pass

    def test_replace_validating_admission_policy_binding(self):
        """Test case for replace_validating_admission_policy_binding

        """
        pass

    def test_replace_validating_admission_policy_status(self):
        """Test case for replace_validating_admission_policy_status

        """
        pass

    def test_replace_validating_webhook_configuration(self):
        """Test case for replace_validating_webhook_configuration

        """
        pass


if __name__ == '__main__':
    unittest.main()
