#-*- coding:utf-8 -*-

##
# Copyright (c) 2012 Norman Krämer. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##

from setuptools import setup

long_description = """
This Python package is API level equivalent to the kerberos python package but instead
of using the MIT krb5 package it uses the windows sspi functionality.
That allows your server and/or client that uses the kerberos package to run under windows
by alternatively loading kerberos-sspi instead of the kerberos package.
"""

setup (
    name = "kerberos-sspi",
    version = "0.1",
    description = "Kerberos high-level windows interface",
    long_description=long_description,
    author='Norman Krämer',
    author_email='kraemer.norman@googlemail.com',
    url="https://github.com/may-day/kerberos-sspi",
    py_modules=["kerberos_sspi"],
    license='Apache Software License 2.0',
    classifiers = [
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 2",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Systems Administration :: Authentication/Directory"
        ],
    install_requires = ["pywin32"]
)
