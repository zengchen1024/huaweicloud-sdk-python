# coding: utf-8
import datetime
import six

from huaweicloud.common.basic_model import BasicModel
from huaweicloud.common.exception import HuaweiCloudSDKException
from huaweicloud.common import util


class CreateKeyPairReq(BasicModel):
    """CreateKeyPairReq

    """

    def __init__(self):
        """
        :param keypair:
        :type keypair: CreateKeyPairReqObject
        """

        self.keypair = None

    def serialize(self):
        if self.keypair is None:
            raise HuaweiCloudSDKException(
                message="The parameter(keypair) is required")
        if not isinstance(self.keypair, CreateKeyPairReqObject):
            raise HuaweiCloudSDKException(
                message="The datatype of parameter(keypair) "
                        "is not CreateKeyPairReqObject")

        obj = {
            "keypair": self.keypair,
        }
        return util.serialize(
            {k: v for k, v in obj.items() if v is not None})


class CreateKeyPairReqObject(BasicModel):
    """CreateKeyPairReqObject

    """

    def __init__(self):
        """
        :param name: A name for the keypair which will be used to reference it later.
        :type name: str
        :param public_key: The public ssh key to import. If you omit this value, a keypair is generated for you.
        :type public_key: str
        :param type: The type of the keypair.
        :type type: str
        :param user_id: The user_id for a keypair.
        :type user_id: str
        """

        self.name = None
        self.public_key = None
        self.type = None
        self.user_id = None

    def serialize(self):
        if self.name is None:
            raise HuaweiCloudSDKException(
                message="The parameter(name) is required")
        if not isinstance(self.name, str):
            raise HuaweiCloudSDKException(
                message="The datatype of parameter(name) "
                        "is not str")

        if self.public_key is not None:
            if not isinstance(self.public_key, str):
                raise HuaweiCloudSDKException(
                    message="The datatype of parameter(public_key) "
                            "is not str")

        if self.type is not None:
            if not isinstance(self.type, str):
                raise HuaweiCloudSDKException(
                    message="The datatype of parameter(type) "
                            "is not str")

        if self.user_id is not None:
            if not isinstance(self.user_id, str):
                raise HuaweiCloudSDKException(
                    message="The datatype of parameter(user_id) "
                            "is not str")

        obj = {
            "name": self.name,
            "public_key": self.public_key,
            "type": self.type,
            "user_id": self.user_id,
        }
        return util.serialize(
            {k: v for k, v in obj.items() if v is not None})


class CreateKeyPairResp(BasicModel):
    """CreateKeyPairResp

    """

    def __init__(self):
        """
        :param keypair:
        :type keypair: CreateKeyPairRespObject
        """

        self.keypair = None

    def deserialize(self, data):
        if not isinstance(data, dict):
            return None

        self.keypair = CreateKeyPairRespObject().deserialize(
            data.get("keypair"))

        return self


class CreateKeyPairRespObject(BasicModel):
    """CreateKeyPairRespObject

    """

    def __init__(self):
        """
        :param created_at: The date and time when the resource was created.
        :type created_at: datetime
        :param deleted: A boolean indicates whether this keypair is deleted or not.
        :type deleted: bool
        :param fingerprint: The fingerprint for the keypair.
        :type fingerprint: str
        :param id: The keypair ID.
        :type id: str
        :param name: A name for the keypair which will be used to reference it later.
        :type name: str
        :param public_key: The keypair public key.
        :type public_key: str
        :param user_id: The user_id for a keypair.
        :type user_id: str
        :param type: The type of the keypair.
        :type type: str
        """

        self.created_at = None
        self.deleted = None
        self.fingerprint = None
        self.id = None
        self.name = None
        self.public_key = None
        self.user_id = None
        self.type = None

    def deserialize(self, data):
        if not isinstance(data, dict):
            return None

        self.created_at = util.deserialize_datetime(
            data.get("created_at"))

        self.deleted = util.deserialize_primitive(
            data.get("deleted"), bool)

        self.fingerprint = util.deserialize_primitive(
            data.get("fingerprint"), str)

        self.id = util.deserialize_primitive(
            data.get("id"), str)

        self.name = util.deserialize_primitive(
            data.get("name"), str)

        self.public_key = util.deserialize_primitive(
            data.get("public_key"), str)

        self.user_id = util.deserialize_primitive(
            data.get("user_id"), str)

        self.type = util.deserialize_primitive(
            data.get("type"), str)

        return self


class GetKeyPairResp(BasicModel):
    """GetKeyPairResp

    """

    def __init__(self):
        """
        :param keypair:
        :type keypair: GetKeyPairRespObject
        """

        self.keypair = None

    def deserialize(self, data):
        if not isinstance(data, dict):
            return None

        self.keypair = GetKeyPairRespObject().deserialize(
            data.get("keypair"))

        return self


class GetKeyPairRespObject(BasicModel):
    """GetKeyPairRespObject

    """

    def __init__(self):
        """
        :param created_at: The date and time when the resource was created.
        :type created_at: datetime
        :param deleted: A boolean indicates whether this keypair is deleted or not.
        :type deleted: bool
        :param fingerprint: The fingerprint for the keypair.
        :type fingerprint: str
        :param id: The keypair ID.
        :type id: str
        :param name: A name for the keypair which will be used to reference it later.
        :type name: str
        :param public_key: The keypair public key.
        :type public_key: str
        :param user_id: The user_id for a keypair.
        :type user_id: str
        :param type: The type of the keypair.
        :type type: str
        """

        self.created_at = None
        self.deleted = None
        self.fingerprint = None
        self.id = None
        self.name = None
        self.public_key = None
        self.user_id = None
        self.type = None

    def deserialize(self, data):
        if not isinstance(data, dict):
            return None

        self.created_at = util.deserialize_datetime(
            data.get("created_at"))

        self.deleted = util.deserialize_primitive(
            data.get("deleted"), bool)

        self.fingerprint = util.deserialize_primitive(
            data.get("fingerprint"), str)

        self.id = util.deserialize_primitive(
            data.get("id"), str)

        self.name = util.deserialize_primitive(
            data.get("name"), str)

        self.public_key = util.deserialize_primitive(
            data.get("public_key"), str)

        self.user_id = util.deserialize_primitive(
            data.get("user_id"), str)

        self.type = util.deserialize_primitive(
            data.get("type"), str)

        return self


class KeyPairLinkItem(BasicModel):
    """KeyPairLinkItem

    """

    def __init__(self):
        """
        :param href:
        :type href: str
        :param rel:
        :type rel: str
        """

        self.href = None
        self.rel = None

    def deserialize(self, data):
        if not isinstance(data, dict):
            return None

        self.href = util.deserialize_primitive(
            data.get("href"), str)

        self.rel = util.deserialize_primitive(
            data.get("rel"), str)

        return self


class ListKeyPairItem(BasicModel):
    """ListKeyPairItem

    """

    def __init__(self):
        """
        :param keypair:
        :type keypair: ListKeyPairObject
        """

        self.keypair = None

    def deserialize(self, data):
        if not isinstance(data, dict):
            return None

        self.keypair = ListKeyPairObject().deserialize(
            data.get("keypair"))

        return self


class ListKeyPairObject(BasicModel):
    """ListKeyPairObject

    """

    def __init__(self):
        """
        :param name: A name for the keypair which will be used to reference it later.
        :type name: str
        :param public_key: The keypair public key.
        :type public_key: str
        :param fingerprint: The fingerprint for the keypair.
        :type fingerprint: str
        :param type: The type of the keypair.
        :type type: str
        """

        self.name = None
        self.public_key = None
        self.fingerprint = None
        self.type = None

    def deserialize(self, data):
        if not isinstance(data, dict):
            return None

        self.name = util.deserialize_primitive(
            data.get("name"), str)

        self.public_key = util.deserialize_primitive(
            data.get("public_key"), str)

        self.fingerprint = util.deserialize_primitive(
            data.get("fingerprint"), str)

        self.type = util.deserialize_primitive(
            data.get("type"), str)

        return self


class ListKeyPairResp(BasicModel):
    """ListKeyPairResp

    """

    def __init__(self):
        """
        :param keypairs:
        :type keypairs: list[ListKeyPairItem]
        :param keypairs_links:
        :type keypairs_links: list[KeyPairLinkItem]
        """

        self.keypairs = None
        self.keypairs_links = None

    def deserialize(self, data):
        if not isinstance(data, dict):
            return None

        if isinstance(data.get("keypairs"), list):
            self.keypairs = [
                ListKeyPairItem().deserialize(v)
                for v in data["keypairs"]]

        if isinstance(data.get("keypairs_links"), list):
            self.keypairs_links = [
                KeyPairLinkItem().deserialize(v)
                for v in data["keypairs_links"]]

        return self
