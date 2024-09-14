# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.31.1
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from kubernetes_asyncio.client.configuration import Configuration


class V1CustomResourceValidation(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'open_apiv3_schema': 'V1JSONSchemaProps'
    }

    attribute_map = {
        'open_apiv3_schema': 'openAPIV3Schema'
    }

    def __init__(self, open_apiv3_schema=None, local_vars_configuration=None):  # noqa: E501
        """V1CustomResourceValidation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default()
        self.local_vars_configuration = local_vars_configuration

        self._open_apiv3_schema = None
        self.discriminator = None

        if open_apiv3_schema is not None:
            self.open_apiv3_schema = open_apiv3_schema

    @property
    def open_apiv3_schema(self):
        """Gets the open_apiv3_schema of this V1CustomResourceValidation.  # noqa: E501


        :return: The open_apiv3_schema of this V1CustomResourceValidation.  # noqa: E501
        :rtype: V1JSONSchemaProps
        """
        return self._open_apiv3_schema

    @open_apiv3_schema.setter
    def open_apiv3_schema(self, open_apiv3_schema):
        """Sets the open_apiv3_schema of this V1CustomResourceValidation.


        :param open_apiv3_schema: The open_apiv3_schema of this V1CustomResourceValidation.  # noqa: E501
        :type open_apiv3_schema: V1JSONSchemaProps
        """

        self._open_apiv3_schema = open_apiv3_schema

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1CustomResourceValidation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1CustomResourceValidation):
            return True

        return self.to_dict() != other.to_dict()
