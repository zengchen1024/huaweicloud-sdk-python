import os

from huaweipythonsdkcore import configuration
from huaweipythonsdkcore import credential
from huaweipythonsdkcore import client

from huaweicloud.compute.v1_0_0 import api
from huaweicloud.compute.v1_0_0 import models


def create_key_pair(api_client, keypair_name):
    obj = models.CreateKeyPairReqObject()
    obj.name = keypair_name
    create_body = models.CreateKeyPairReq()
    create_body.keypair = obj

    print "\n** create_key_pair **\n"

    try:
        ret = api_client.create_key_pair(create_body)
        for k, v in vars(ret.keypair).items():
            print k, ": ", v
    except Exception as err:
        print(err)

    print "\n** create_key_pair end **\n"


def get_key_pair(api_client, keypair_name):
    print "\n** get_key_pair **\n"
    try:
        ret = api_client.get_key_pair(keypair_name)
        for k, v in vars(ret.keypair).items():
            print k, ": ", v
    except Exception as err:
        print(err)

    print "\n** get_key_pair end **\n"


def list_key_pair(api_client):
    print "\n** list_key_pair **\n"
    try:
        ret = api_client.list_key_pair()
        print "-- keypairs_links --"
        if ret.keypairs_links is not None:
            for i in ret.keypairs_links:
                for k, v in vars(i).items():
                    print k, ": ", v
                print "\n\n"

        print "-- keypairs --"
        if ret.keypairs is not None:
            for i in ret.keypairs:
                for k, v in vars(i.keypair).items():
                    print k, ": ", v
                print "\n\n"
    except Exception as err:
        print(err)

    print "\n** list_key_pair end **\n"


def delete_key_pair(api_client, keypair_name):
    try:
        api_client.delete_key_pair(keypair_name)
    except Exception as err:
        print(err)
    print "\n** delete_key_pair end **\n"


if __name__ == "__main__":

    # Initialize the client
    demo_client = client.Client(
        auth_url='https://iam.cn-north-1.myhwclouds.com:443/v3',
        credential=credential.AccessKeyCredential(
            access_key_id=os.environ['access_key_id'],
            access_key_secret=os.environ['access_key_secret'],
        ),
        region='cn-north-1',
        configuration=configuration.Configuration(**{
            'verify_ssl': True}))

    api_client = api.Api(demo_client)

    keypair_name = "keypair-test"

    create_key_pair(api_client, keypair_name)

    get_key_pair(api_client, keypair_name)

    list_key_pair(api_client)

    delete_key_pair(api_client, keypair_name)
