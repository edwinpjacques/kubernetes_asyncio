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


class V1APIGroup(object):
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
        'api_version': 'str',
        'kind': 'str',
        'name': 'str',
        'preferred_version': 'V1GroupVersionForDiscovery',
        'server_address_by_client_cidrs': 'list[V1ServerAddressByClientCIDR]',
        'versions': 'list[V1GroupVersionForDiscovery]'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'kind': 'kind',
        'name': 'name',
        'preferred_version': 'preferredVersion',
        'server_address_by_client_cidrs': 'serverAddressByClientCIDRs',
        'versions': 'versions'
    }

    def __init__(self, api_version=None, kind=None, name=None, preferred_version=None, server_address_by_client_cidrs=None, versions=None, local_vars_configuration=None):  # noqa: E501
        """V1APIGroup - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default()
        self.local_vars_configuration = local_vars_configuration

        self._api_version = None
        self._kind = None
        self._name = None
        self._preferred_version = None
        self._server_address_by_client_cidrs = None
        self._versions = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if kind is not None:
            self.kind = kind
        self.name = name
        if preferred_version is not None:
            self.preferred_version = preferred_version
        if server_address_by_client_cidrs is not None:
            self.server_address_by_client_cidrs = server_address_by_client_cidrs
        self.versions = versions

    @property
    def api_version(self):
        """Gets the api_version of this V1APIGroup.  # noqa: E501

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :return: The api_version of this V1APIGroup.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this V1APIGroup.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :param api_version: The api_version of this V1APIGroup.  # noqa: E501
        :type api_version: str
        """

        self._api_version = api_version

    @property
    def kind(self):
        """Gets the kind of this V1APIGroup.  # noqa: E501

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :return: The kind of this V1APIGroup.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1APIGroup.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :param kind: The kind of this V1APIGroup.  # noqa: E501
        :type kind: str
        """

        self._kind = kind

    @property
    def name(self):
        """Gets the name of this V1APIGroup.  # noqa: E501

        name is the name of the group.  # noqa: E501

        :return: The name of this V1APIGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1APIGroup.

        name is the name of the group.  # noqa: E501

        :param name: The name of this V1APIGroup.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def preferred_version(self):
        """Gets the preferred_version of this V1APIGroup.  # noqa: E501


        :return: The preferred_version of this V1APIGroup.  # noqa: E501
        :rtype: V1GroupVersionForDiscovery
        """
        return self._preferred_version

    @preferred_version.setter
    def preferred_version(self, preferred_version):
        """Sets the preferred_version of this V1APIGroup.


        :param preferred_version: The preferred_version of this V1APIGroup.  # noqa: E501
        :type preferred_version: V1GroupVersionForDiscovery
        """

        self._preferred_version = preferred_version

    @property
    def server_address_by_client_cidrs(self):
        """Gets the server_address_by_client_cidrs of this V1APIGroup.  # noqa: E501

        a map of client CIDR to server address that is serving this group. This is to help clients reach servers in the most network-efficient way possible. Clients can use the appropriate server address as per the CIDR that they match. In case of multiple matches, clients should use the longest matching CIDR. The server returns only those CIDRs that it thinks that the client can match. For example: the master will return an internal IP CIDR only, if the client reaches the server using an internal IP. Server looks at X-Forwarded-For header or X-Real-Ip header or request.RemoteAddr (in that order) to get the client IP.  # noqa: E501

        :return: The server_address_by_client_cidrs of this V1APIGroup.  # noqa: E501
        :rtype: list[V1ServerAddressByClientCIDR]
        """
        return self._server_address_by_client_cidrs

    @server_address_by_client_cidrs.setter
    def server_address_by_client_cidrs(self, server_address_by_client_cidrs):
        """Sets the server_address_by_client_cidrs of this V1APIGroup.

        a map of client CIDR to server address that is serving this group. This is to help clients reach servers in the most network-efficient way possible. Clients can use the appropriate server address as per the CIDR that they match. In case of multiple matches, clients should use the longest matching CIDR. The server returns only those CIDRs that it thinks that the client can match. For example: the master will return an internal IP CIDR only, if the client reaches the server using an internal IP. Server looks at X-Forwarded-For header or X-Real-Ip header or request.RemoteAddr (in that order) to get the client IP.  # noqa: E501

        :param server_address_by_client_cidrs: The server_address_by_client_cidrs of this V1APIGroup.  # noqa: E501
        :type server_address_by_client_cidrs: list[V1ServerAddressByClientCIDR]
        """

        self._server_address_by_client_cidrs = server_address_by_client_cidrs

    @property
    def versions(self):
        """Gets the versions of this V1APIGroup.  # noqa: E501

        versions are the versions supported in this group.  # noqa: E501

        :return: The versions of this V1APIGroup.  # noqa: E501
        :rtype: list[V1GroupVersionForDiscovery]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """Sets the versions of this V1APIGroup.

        versions are the versions supported in this group.  # noqa: E501

        :param versions: The versions of this V1APIGroup.  # noqa: E501
        :type versions: list[V1GroupVersionForDiscovery]
        """
        if self.local_vars_configuration.client_side_validation and versions is None:  # noqa: E501
            raise ValueError("Invalid value for `versions`, must not be `None`")  # noqa: E501

        self._versions = versions

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
        if not isinstance(other, V1APIGroup):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1APIGroup):
            return True

        return self.to_dict() != other.to_dict()
