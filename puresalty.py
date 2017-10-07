# -*- coding: utf-8 -*-
'''
PureStorage Module
===================

.. versionadded:: 0yxgen

The puresalty module allows you to interact with your PureStorage array(s).

:codeauthor: Stephan Looney <slooney@stephanlooney.com>


Dependencies
============

- purestorage

PureStorage SDK
-------

purestorage can be installed via pip:

.. code-block:: bash

    pip install purestorage

.. note::
  For sdk reference see: http://pure-storage-python-rest-client.readthedocs.io/


Configuration
=============

To use this module: set up the purestorage api token,hostname/IP, user, and password in the
master configuration at
``/etc/salt/master`` or ``/etc/salt/master.d``:

.. code-block:: yaml

    puresalty.user: myuser
    puresalty.password: verybadpass
    puresalty.host: 10.0.0.1
    puresalty.token: 6e1b80a1-cd63-de90-b74a-7fc16d034016
'''

# Import python libs
from __future__ import absolute_import
import logging
import json
# Import salt libs
import importlib
from salt.exceptions import SaltCloudSystemExit
# Import salt cloud libs
import salt.config as config
#import purestorage libs
import purestorage

__virtualname__ = 'puresalty'

def get_creds():
    if not user:
        user = __salt__['config.option']('puresalty.user')
    if not password:
        password = __salt__['config.option']('puresalty.password')
    if not host:
        host = __salt__['config.option']('puresalty.host')
    if not token:
        token = __salt__['config.option']('puresalty.token')
    return {"user": user, "password": password, "host": host, "token": token}

def test_connection():
    from purestorage import FlashArray
    creds = get_creds()
    array = purestorage.FlashArray(creds["host"], creds["user"], creds["password"])
    array_info = array.get()
    return "FlashArray {} (version {}) REST session established!".format(array_info['array_name'], array_info['version'])