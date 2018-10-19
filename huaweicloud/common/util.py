# coding: utf-8
# Copyright (c) 2018 Huawei Technologies Co., Ltd.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


import datetime
from dateutil.parser import parse as date_parse
import inspect
import re
import six

from huaweicloud.common.basic_model import BasicModel
from huaweicloud.common.exception import HuaweiCloudSDKException

PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types

NATIVE_TYPES_MAPPING = {
    'int': int,
    'long': int if six.PY3 else long,
    'float': float,
    'str': str,
    'bool': bool,
    'date': datetime.date,
    'datetime': datetime.datetime,
    'object': object,
}


def deserialize(data, datatype, inner_class=None):
    """Deserializes dict, list, str into an object.

    :param data: data to be deserialized.
    :param datatype: datatype which the data will be deserialized to.
    :param inner_class: inner_class is a subclass of BasicModel.

    :return: object.
    """

    if data is None:
        return None

    if type(datatype) == str:
        if datatype.startswith('list['):
            sub_datatype = re.match(r"list\[(.*)\]", datatype).group(1)
            return [
                deserialize(sub_data, sub_datatype, inner_class)
                for sub_data in data]

        if datatype.startswith('dict('):
            sub_datatype = re.match(
                r"dict\(([^,]*), (.*)\)", datatype).group(2)
            return {k: deserialize(v, sub_datatype, inner_class)
                    for k, v in six.iteritems(data)}

        # convert str to class
        if datatype in NATIVE_TYPES_MAPPING:
            datatype = NATIVE_TYPES_MAPPING[datatype]
        else:
            if not (inspect.isclass(inner_class) and (
                    issubclass(inner_class, BasicModel)) and (
                    datatype == inner_class.__name__)):
                raise HuaweiCloudSDKException(
                    message="Encounter an invalid inner datatype(%s) to "
                            "desrialize data" % datatype)
            datatype = inner_class

    if datatype in PRIMITIVE_TYPES:
        return deserialize_primitive(data, datatype)
    elif datatype == object:
        return deserialize_object(data)
    elif datatype == datetime.date:
        return deserialize_date(data)
    elif datatype == datetime.datetime:
        return deserialize_datetime(data)
    elif inspect.isclass(datatype) and issubclass(datatype, BasicModel):
        return datatype().deserialize(data)

    raise HuaweiCloudSDKException(
        message="Can't deserialize data(%s) with unknown "
                "datatype(%s)" % (data, str(datatype)))


def deserialize_primitive(data, datatype):
    """Deserializes string to primitive type.

    :param data: str.
    :param datatype: class literal.

    :return: int, long, float, str, bool.
    """

    if data is None:
        return None

    try:
        return datatype(data)
    except UnicodeEncodeError:
        return six.text_type(data)
    except TypeError:
        raise HuaweiCloudSDKException(
            message="Deserialize data(%s) with unmatched datatype(%s)" % (
                data, str(datatype)))


def deserialize_object(value):
    """Return a original value.

    :return: object.
    """

    return value


def deserialize_date(data):
    """Deserializes data to date.

    :param data: str.
    :return: date.
    """

    if data is None:
        return None

    try:
        return date_parse(data).date()
    except ImportError:
        return data
    except ValueError:
        raise HuaweiCloudSDKException(
            message="Failed to parse `{0}` as date object".format(data)
        )


def deserialize_datetime(data):
    """Deserializes data to datetime.

    :param data: str, it should be in iso8601 datetime format..
    :return: datetime.
    """

    if data is None:
        return None

    try:
        return date_parse(data)
    except ImportError:
        return data
    except ValueError:
        raise HuaweiCloudSDKException(
            message="Failed to parse `{0}` as datetime object".format(data))


def check_datatype(name, param, datatype, inner_class=None):
    """Check datatype.

    :param name: the name of param
    :param param: dict, list or str.
    :param datatype: class literal, or string of class name.
    :param inner_class: inner_class is a subclass of BasicModel.
    """

    if type(datatype) == str:
        if datatype.startswith('list['):
            sub_datatype = re.match(r"list\[(.*)\]", datatype).group(1)
            for sub_data in param:
                check_datatype(name, sub_data, sub_datatype, inner_class)

        if datatype.startswith('dict('):
            sub_datatype = re.match(
                r"dict\(([^,]*), (.*)\)", datatype).group(2)
            for v in six.itervalues(param):
                check_datatype(name, v, sub_datatype, inner_class)

        # convert str to class
        if datatype in NATIVE_TYPES_MAPPING:
            datatype = NATIVE_TYPES_MAPPING[datatype]
        else:
            if not (inspect.isclass(inner_class) and (
                    issubclass(inner_class, BasicModel)) and (
                    datatype == inner_class.__name__)):
                raise HuaweiCloudSDKException(
                    message="Encounter an invalid inner datatype(%s) to check "
                            "datatype of parameter(%s)" % (datatype, name))

            datatype = inner_class

    try:
        if not isinstance(param, datatype):
            raise HuaweiCloudSDKException(
                message="The datatype of parameter(%s) is not %s" % (
                    name, str(datatype)))
    except TypeError:
        raise HuaweiCloudSDKException(
            message="Can't check datatype of parameter(%s) with invalid "
                    "datatype(%s)" % (name, str(datatype)))


def serialize(obj):
    """Builds a JSON POST object.

    :param obj: The data to serialize.
    :return: The serialized form of data.
    """

    if obj is None:
        return None
    elif isinstance(obj, PRIMITIVE_TYPES):
        return obj
    elif isinstance(obj, (datetime.datetime, datetime.date)):
        return obj.isoformat()
    elif isinstance(obj, BasicModel):
        return obj.serialize()
    elif isinstance(obj, dict):
        return {k: serialize(v) for k, v in six.iteritems(obj)}
    elif isinstance(obj, list):
        return [serialize(sub_obj) for sub_obj in obj]
    elif isinstance(obj, tuple):
        return tuple(serialize(sub_obj) for sub_obj in obj)

    raise HuaweiCloudSDKException(
        message="Can't serialize object with unknown datatype(%s)" % type(obj))


def select_header_accept(accepts):
    """Returns `Accept` based on an array of accepts provided.

    :param accepts: List of headers.
    :return: Accept (e.g. application/json).
    """

    if not accepts:
        return

    accepts = [x.lower() for x in accepts]

    if 'application/json' in accepts:
        return 'application/json'
    else:
        return ', '.join(accepts)


def select_header_content_type(content_types):
    """Returns `Content-Type` based on an array of content_types provided.

    :param content_types: List of content-types.
    :return: Content-Type (e.g. application/json).
    """

    if not content_types:
        return 'application/json'

    content_types = [x.lower() for x in content_types]

    if 'application/json' in content_types or '*/*' in content_types:
        return 'application/json'
    else:
        return content_types[0]


def get_collect_format(collection_format):
    cf = {
        'csv': ',',
        'ssv': ' ',
        'tsv': '\t',
        'pipes': '|',
    }
    return cf.get(collection_format, ',')
