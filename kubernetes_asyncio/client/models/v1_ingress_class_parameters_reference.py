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


class V1IngressClassParametersReference(object):
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
        'api_group': 'str',
        'kind': 'str',
        'name': 'str',
        'namespace': 'str',
        'scope': 'str'
    }

    attribute_map = {
        'api_group': 'apiGroup',
        'kind': 'kind',
        'name': 'name',
        'namespace': 'namespace',
        'scope': 'scope'
    }

    def __init__(self, api_group=None, kind=None, name=None, namespace=None, scope=None, local_vars_configuration=None):  # noqa: E501
        """V1IngressClassParametersReference - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default()
        self.local_vars_configuration = local_vars_configuration

        self._api_group = None
        self._kind = None
        self._name = None
        self._namespace = None
        self._scope = None
        self.discriminator = None

        if api_group is not None:
            self.api_group = api_group
        self.kind = kind
        self.name = name
        if namespace is not None:
            self.namespace = namespace
        if scope is not None:
            self.scope = scope

    @property
    def api_group(self):
        """Gets the api_group of this V1IngressClassParametersReference.  # noqa: E501

        apiGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required.  # noqa: E501

        :return: The api_group of this V1IngressClassParametersReference.  # noqa: E501
        :rtype: str
        """
        return self._api_group

    @api_group.setter
    def api_group(self, api_group):
        """Sets the api_group of this V1IngressClassParametersReference.

        apiGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required.  # noqa: E501

        :param api_group: The api_group of this V1IngressClassParametersReference.  # noqa: E501
        :type api_group: str
        """

        self._api_group = api_group

    @property
    def kind(self):
        """Gets the kind of this V1IngressClassParametersReference.  # noqa: E501

        kind is the type of resource being referenced.  # noqa: E501

        :return: The kind of this V1IngressClassParametersReference.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1IngressClassParametersReference.

        kind is the type of resource being referenced.  # noqa: E501

        :param kind: The kind of this V1IngressClassParametersReference.  # noqa: E501
        :type kind: str
        """
        if self.local_vars_configuration.client_side_validation and kind is None:  # noqa: E501
            raise ValueError("Invalid value for `kind`, must not be `None`")  # noqa: E501

        self._kind = kind

    @property
    def name(self):
        """Gets the name of this V1IngressClassParametersReference.  # noqa: E501

        name is the name of resource being referenced.  # noqa: E501

        :return: The name of this V1IngressClassParametersReference.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1IngressClassParametersReference.

        name is the name of resource being referenced.  # noqa: E501

        :param name: The name of this V1IngressClassParametersReference.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this V1IngressClassParametersReference.  # noqa: E501

        namespace is the namespace of the resource being referenced. This field is required when scope is set to \"Namespace\" and must be unset when scope is set to \"Cluster\".  # noqa: E501

        :return: The namespace of this V1IngressClassParametersReference.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this V1IngressClassParametersReference.

        namespace is the namespace of the resource being referenced. This field is required when scope is set to \"Namespace\" and must be unset when scope is set to \"Cluster\".  # noqa: E501

        :param namespace: The namespace of this V1IngressClassParametersReference.  # noqa: E501
        :type namespace: str
        """

        self._namespace = namespace

    @property
    def scope(self):
        """Gets the scope of this V1IngressClassParametersReference.  # noqa: E501

        scope represents if this refers to a cluster or namespace scoped resource. This may be set to \"Cluster\" (default) or \"Namespace\".  # noqa: E501

        :return: The scope of this V1IngressClassParametersReference.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this V1IngressClassParametersReference.

        scope represents if this refers to a cluster or namespace scoped resource. This may be set to \"Cluster\" (default) or \"Namespace\".  # noqa: E501

        :param scope: The scope of this V1IngressClassParametersReference.  # noqa: E501
        :type scope: str
        """

        self._scope = scope

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
        if not isinstance(other, V1IngressClassParametersReference):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1IngressClassParametersReference):
            return True

        return self.to_dict() != other.to_dict()
