# coding: utf-8

import json
import six
from six.moves.urllib.parse import quote

from huaweicloud.common.exception import HuaweiCloudSDKException
from huaweicloud.common import util
from huaweicloud.compute.v1_0_0 import models


class Api(object):
    def __init__(self, api_client):
        self.api_client = api_client

    def create_key_pair(self, keypair, **kwargs):
        """Add a new keypair

        :param keypair: the request parameters to create keypair
        :type keypair: CreateKeyPairReq
        :rtype: CreateKeyPairResp
        """

        if not isinstance(keypair, models.CreateKeyPairReq):
            raise HuaweiCloudSDKException(
                message="The datatype of parameter(keypair) "
                        "is not CreateKeyPairReq")
        body_params = keypair.serialize()

        header_params = {}
        header_params['Accept'] = util.select_header_accept(
            ['application/xml', 'application/json'])

        header_params['Content-Type'] = util.select_header_content_type(
            ['application/json', 'application/xml'])

        return_code, return_data, _ = self.api_client.handle_raw_request(
            'compute', 'POST',
            '/os-keypairs',
            headers=header_params,
            body=body_params,
            timeout=kwargs.get('_request_timeout', None),
            _preload_content=kwargs.get('_preload_content', True))

        if return_data is not None:
            return_data = json.loads(return_data)
        else:
            return_data = {}
        if return_code not in [200, 201]:
            raise HuaweiCloudSDKException(
                return_code,
                "Run create_key_pair failed, "
                "message=%s" % return_data.get("message"))
        return models.CreateKeyPairResp().deserialize(return_data)

    def delete_key_pair(self, keypair_name, user_id=None, **kwargs):
        """delete a keypair

        :param keypair_name: The keypair name.
        :type keypair_name: str
        :param user_id: This allows administrative users to operate key-pairs of specified user ID.
        :type user_id: str
        :rtype: None
        """

        path_params = {}
        if not isinstance(keypair_name, str):
            raise HuaweiCloudSDKException(
                message="The datatype of parameter(keypair_name) is not "
                        "str")
        path_params["keypair_name"] = quote(str(keypair_name))

        url = '/os-keypairs/{keypair_name}'.format(**path_params)

        query_params = []
        if user_id is not None:
            if not isinstance(user_id, str):
                raise HuaweiCloudSDKException(
                    message="The datatype of parameter(user_id) "
                            "is not str")
            query_params.append(("user_id", user_id))

        header_params = {}
        header_params['Accept'] = util.select_header_accept(
            ['application/xml', 'application/json'])

        return_code, return_data, _ = self.api_client.handle_raw_request(
            'compute', 'DELETE', url,
            headers=header_params,
            query_params=query_params,
            timeout=kwargs.get('_request_timeout', None),
            _preload_content=kwargs.get('_preload_content', True))

        if return_code not in [202, 204]:
            if return_data is not None:
                return_data = json.loads(return_data)
            else:
                return_data = {}
            raise HuaweiCloudSDKException(
                return_code,
                "Run delete_key_pair failed, "
                "message=%s" % return_data.get("message"))

    def get_key_pair(self, keypair_name, user_id=None, **kwargs):
        """get a keypair

        :param keypair_name: The keypair name.
        :type keypair_name: str
        :param user_id: This allows administrative users to operate key-pairs of specified user ID.
        :type user_id: str
        :rtype: GetKeyPairResp
        """

        path_params = {}
        if not isinstance(keypair_name, str):
            raise HuaweiCloudSDKException(
                message="The datatype of parameter(keypair_name) is not "
                        "str")
        path_params["keypair_name"] = quote(str(keypair_name))

        url = '/os-keypairs/{keypair_name}'.format(**path_params)

        query_params = []
        if user_id is not None:
            if not isinstance(user_id, str):
                raise HuaweiCloudSDKException(
                    message="The datatype of parameter(user_id) "
                            "is not str")
            query_params.append(("user_id", user_id))

        header_params = {}
        header_params['Accept'] = util.select_header_accept(
            ['application/xml', 'application/json'])

        return_code, return_data, _ = self.api_client.handle_raw_request(
            'compute', 'GET', url,
            headers=header_params,
            query_params=query_params,
            timeout=kwargs.get('_request_timeout', None),
            _preload_content=kwargs.get('_preload_content', True))

        if return_data is not None:
            return_data = json.loads(return_data)
        else:
            return_data = {}
        if return_code not in [200]:
            raise HuaweiCloudSDKException(
                return_code,
                "Run get_key_pair failed, "
                "message=%s" % return_data.get("message"))
        return models.GetKeyPairResp().deserialize(return_data)

    def list_key_pair(self, user_id=None, limit=None, marker=None, **kwargs):
        """list keypairs

        :param user_id: This allows administrative users to operate key-pairs of specified user ID.
        :type user_id: str
        :param limit: Requests a page size of items.
        :type limit: int
        :param marker: The last-seen item.
        :type marker: str
        :rtype: ListKeyPairResp
        """

        query_params = []
        if user_id is not None:
            if not isinstance(user_id, str):
                raise HuaweiCloudSDKException(
                    message="The datatype of parameter(user_id) "
                            "is not str")
            query_params.append(("user_id", user_id))

        if limit is not None:
            if not isinstance(limit, int):
                raise HuaweiCloudSDKException(
                    message="The datatype of parameter(limit) "
                            "is not int")
            query_params.append(("limit", limit))

        if marker is not None:
            if not isinstance(marker, str):
                raise HuaweiCloudSDKException(
                    message="The datatype of parameter(marker) "
                            "is not str")
            query_params.append(("marker", marker))

        header_params = {}
        header_params['Accept'] = util.select_header_accept(
            ['application/xml', 'application/json'])

        return_code, return_data, _ = self.api_client.handle_raw_request(
            'compute', 'GET',
            '/os-keypairs',
            headers=header_params,
            query_params=query_params,
            timeout=kwargs.get('_request_timeout', None),
            _preload_content=kwargs.get('_preload_content', True))

        if return_data is not None:
            return_data = json.loads(return_data)
        else:
            return_data = {}
        if return_code not in [200]:
            raise HuaweiCloudSDKException(
                return_code,
                "Run list_key_pair failed, "
                "message=%s" % return_data.get("message"))
        return models.ListKeyPairResp().deserialize(return_data)
