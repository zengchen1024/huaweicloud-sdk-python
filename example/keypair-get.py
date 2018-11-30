import os

from huaweipythonsdkcore import configuration
from huaweipythonsdkcore import credential
from huaweipythonsdkcore import client

from huaweicloud.compute.v2 import api
from huaweicloud.compute.v2 import models


def get_key_pair(api_client, keypair_name):
    print "\n** get_key_pair **\n"
    try:
        ret = api_client.get_key_pair(keypair_name)
        for k, v in vars(ret.keypair).items():
            print k, ": ", v
    except Exception as err:
        print(err)

    print "\n** get_key_pair end **\n"


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

    get_key_pair(api_client, keypair_name)

