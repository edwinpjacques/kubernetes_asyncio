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


class V1RBDVolumeSource(object):
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
        'fs_type': 'str',
        'image': 'str',
        'keyring': 'str',
        'monitors': 'list[str]',
        'pool': 'str',
        'read_only': 'bool',
        'secret_ref': 'V1LocalObjectReference',
        'user': 'str'
    }

    attribute_map = {
        'fs_type': 'fsType',
        'image': 'image',
        'keyring': 'keyring',
        'monitors': 'monitors',
        'pool': 'pool',
        'read_only': 'readOnly',
        'secret_ref': 'secretRef',
        'user': 'user'
    }

    def __init__(self, fs_type=None, image=None, keyring=None, monitors=None, pool=None, read_only=None, secret_ref=None, user=None, local_vars_configuration=None):  # noqa: E501
        """V1RBDVolumeSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default()
        self.local_vars_configuration = local_vars_configuration

        self._fs_type = None
        self._image = None
        self._keyring = None
        self._monitors = None
        self._pool = None
        self._read_only = None
        self._secret_ref = None
        self._user = None
        self.discriminator = None

        if fs_type is not None:
            self.fs_type = fs_type
        self.image = image
        if keyring is not None:
            self.keyring = keyring
        self.monitors = monitors
        if pool is not None:
            self.pool = pool
        if read_only is not None:
            self.read_only = read_only
        if secret_ref is not None:
            self.secret_ref = secret_ref
        if user is not None:
            self.user = user

    @property
    def fs_type(self):
        """Gets the fs_type of this V1RBDVolumeSource.  # noqa: E501

        fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#rbd  # noqa: E501

        :return: The fs_type of this V1RBDVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._fs_type

    @fs_type.setter
    def fs_type(self, fs_type):
        """Sets the fs_type of this V1RBDVolumeSource.

        fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#rbd  # noqa: E501

        :param fs_type: The fs_type of this V1RBDVolumeSource.  # noqa: E501
        :type fs_type: str
        """

        self._fs_type = fs_type

    @property
    def image(self):
        """Gets the image of this V1RBDVolumeSource.  # noqa: E501

        image is the rados image name. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it  # noqa: E501

        :return: The image of this V1RBDVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this V1RBDVolumeSource.

        image is the rados image name. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it  # noqa: E501

        :param image: The image of this V1RBDVolumeSource.  # noqa: E501
        :type image: str
        """
        if self.local_vars_configuration.client_side_validation and image is None:  # noqa: E501
            raise ValueError("Invalid value for `image`, must not be `None`")  # noqa: E501

        self._image = image

    @property
    def keyring(self):
        """Gets the keyring of this V1RBDVolumeSource.  # noqa: E501

        keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it  # noqa: E501

        :return: The keyring of this V1RBDVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._keyring

    @keyring.setter
    def keyring(self, keyring):
        """Sets the keyring of this V1RBDVolumeSource.

        keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it  # noqa: E501

        :param keyring: The keyring of this V1RBDVolumeSource.  # noqa: E501
        :type keyring: str
        """

        self._keyring = keyring

    @property
    def monitors(self):
        """Gets the monitors of this V1RBDVolumeSource.  # noqa: E501

        monitors is a collection of Ceph monitors. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it  # noqa: E501

        :return: The monitors of this V1RBDVolumeSource.  # noqa: E501
        :rtype: list[str]
        """
        return self._monitors

    @monitors.setter
    def monitors(self, monitors):
        """Sets the monitors of this V1RBDVolumeSource.

        monitors is a collection of Ceph monitors. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it  # noqa: E501

        :param monitors: The monitors of this V1RBDVolumeSource.  # noqa: E501
        :type monitors: list[str]
        """
        if self.local_vars_configuration.client_side_validation and monitors is None:  # noqa: E501
            raise ValueError("Invalid value for `monitors`, must not be `None`")  # noqa: E501

        self._monitors = monitors

    @property
    def pool(self):
        """Gets the pool of this V1RBDVolumeSource.  # noqa: E501

        pool is the rados pool name. Default is rbd. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it  # noqa: E501

        :return: The pool of this V1RBDVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._pool

    @pool.setter
    def pool(self, pool):
        """Sets the pool of this V1RBDVolumeSource.

        pool is the rados pool name. Default is rbd. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it  # noqa: E501

        :param pool: The pool of this V1RBDVolumeSource.  # noqa: E501
        :type pool: str
        """

        self._pool = pool

    @property
    def read_only(self):
        """Gets the read_only of this V1RBDVolumeSource.  # noqa: E501

        readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it  # noqa: E501

        :return: The read_only of this V1RBDVolumeSource.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this V1RBDVolumeSource.

        readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it  # noqa: E501

        :param read_only: The read_only of this V1RBDVolumeSource.  # noqa: E501
        :type read_only: bool
        """

        self._read_only = read_only

    @property
    def secret_ref(self):
        """Gets the secret_ref of this V1RBDVolumeSource.  # noqa: E501


        :return: The secret_ref of this V1RBDVolumeSource.  # noqa: E501
        :rtype: V1LocalObjectReference
        """
        return self._secret_ref

    @secret_ref.setter
    def secret_ref(self, secret_ref):
        """Sets the secret_ref of this V1RBDVolumeSource.


        :param secret_ref: The secret_ref of this V1RBDVolumeSource.  # noqa: E501
        :type secret_ref: V1LocalObjectReference
        """

        self._secret_ref = secret_ref

    @property
    def user(self):
        """Gets the user of this V1RBDVolumeSource.  # noqa: E501

        user is the rados user name. Default is admin. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it  # noqa: E501

        :return: The user of this V1RBDVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this V1RBDVolumeSource.

        user is the rados user name. Default is admin. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it  # noqa: E501

        :param user: The user of this V1RBDVolumeSource.  # noqa: E501
        :type user: str
        """

        self._user = user

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
        if not isinstance(other, V1RBDVolumeSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1RBDVolumeSource):
            return True

        return self.to_dict() != other.to_dict()
