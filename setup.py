# coding: utf-8

import os
from setuptools import setup, find_packages

import huaweicloud

ROOT = os.path.dirname(__file__)

setup(
    name='huaweicloud-sdk-python',
    version=huaweicloud.__version__,
    description="Huawei Cloud SDK for Python",
    long_description = "",
    author="Huawei Cloud",
    url="https://github.com/huaweicloud/huaweicloud-sdk-python",
    maintainer_email="support@huaweicloud.com",
    packages=find_packages(exclude=["tests*"]),
    license="Apache License 2.0",
    platforms='any',
    install_requires=["six >= 1.10", "python-dateutil"],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
