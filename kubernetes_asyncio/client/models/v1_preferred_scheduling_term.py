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


class V1PreferredSchedulingTerm(object):
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
        'preference': 'V1NodeSelectorTerm',
        'weight': 'int'
    }

    attribute_map = {
        'preference': 'preference',
        'weight': 'weight'
    }

    def __init__(self, preference=None, weight=None, local_vars_configuration=None):  # noqa: E501
        """V1PreferredSchedulingTerm - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default()
        self.local_vars_configuration = local_vars_configuration

        self._preference = None
        self._weight = None
        self.discriminator = None

        self.preference = preference
        self.weight = weight

    @property
    def preference(self):
        """Gets the preference of this V1PreferredSchedulingTerm.  # noqa: E501


        :return: The preference of this V1PreferredSchedulingTerm.  # noqa: E501
        :rtype: V1NodeSelectorTerm
        """
        return self._preference

    @preference.setter
    def preference(self, preference):
        """Sets the preference of this V1PreferredSchedulingTerm.


        :param preference: The preference of this V1PreferredSchedulingTerm.  # noqa: E501
        :type preference: V1NodeSelectorTerm
        """
        if self.local_vars_configuration.client_side_validation and preference is None:  # noqa: E501
            raise ValueError("Invalid value for `preference`, must not be `None`")  # noqa: E501

        self._preference = preference

    @property
    def weight(self):
        """Gets the weight of this V1PreferredSchedulingTerm.  # noqa: E501

        Weight associated with matching the corresponding nodeSelectorTerm, in the range 1-100.  # noqa: E501

        :return: The weight of this V1PreferredSchedulingTerm.  # noqa: E501
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this V1PreferredSchedulingTerm.

        Weight associated with matching the corresponding nodeSelectorTerm, in the range 1-100.  # noqa: E501

        :param weight: The weight of this V1PreferredSchedulingTerm.  # noqa: E501
        :type weight: int
        """
        if self.local_vars_configuration.client_side_validation and weight is None:  # noqa: E501
            raise ValueError("Invalid value for `weight`, must not be `None`")  # noqa: E501

        self._weight = weight

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
        if not isinstance(other, V1PreferredSchedulingTerm):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1PreferredSchedulingTerm):
            return True

        return self.to_dict() != other.to_dict()
