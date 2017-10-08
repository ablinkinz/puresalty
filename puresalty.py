# -*- coding: utf-8 -*-
'''
PureStorage Module
===================

.. versionadded:: 0yxgen

The puresalty module allows you to interact with your PureStorage array(s).

:codeauthor: Stephan Looney <ablinkin@me.com>


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


def create_volume(name, size):
    #size can be an integer or string. String for a 1TB volume would be "1T"
    from purestorage import FlashArray, purestorage
    creds = get_creds()
    array = purestorage.FlashArray(creds["host"], creds["user"], creds["password"])
    vol_created = array.create_volume(name,size)
    return vol_created


def extend_volume(name,size):
    from purestorage import FlashArray, purestorage
    creds = get_creds()
    array = purestorage.FlashArray(creds["host"], creds["user"], creds["password"])
    extend_array = array.extend_volume(name,size)
    return extend_array


def destroy_volume(name):
    #WARNING: this will destroy and eradicate the volume
    from purestorage import FlashArray, purestorage
    creds = get_creds()
    array = purestorage.FlashArray(creds["host"], creds["user"], creds["password"])
    array.destroy_volume(name)
    array.eradicate_volume(name)
    return {"Volume Deleted and Eradicated": {"Name": name}}


def show_host_connections(name):
    from purestorage import FlashArray, purestorage
    creds = get_creds()
    array = purestorage.FlashArray(creds["host"], creds["user"], creds["password"])
    host_connections = array.list_host_connections(name)
    return host_connections


def list_volume_snapshots():
    from purestorage import FlashArray, purestorage
    creds = get_creds()
    array = purestorage.FlashArray(creds["host"], creds["user"], creds["password"])
    volume_snaps = array.list_volumes(snap=True)
    return volume_snaps


def create_volume_snapshots(name):
    from purestorage import FlashArray, purestorage
    creds = get_creds()
    array = purestorage.FlashArray(creds["host"], creds["user"], creds["password"])
    volume_snap = array.create_snapshot(name)
    return volume_snap


def create_alert_recipient(email):
    from purestorage import FlashArray, purestorage
    creds = get_creds()
    array = purestorage.FlashArray(creds["host"], creds["user"], creds["password"])
    create_alert = array.create_alert_recipient(email)
    return create_alert


def show_alert_recipients():
    from purestorage import FlashArray, purestorage
    creds = get_creds()
    array = purestorage.FlashArray(creds["host"], creds["user"], creds["password"])
    recipients = array.list_alert_recipients()
    return recipients


def test_alerts():
    from purestorage import FlashArray, purestorage
    creds = get_creds()
    array = purestorage.FlashArray(creds["host"], creds["user"], creds["password"])
    alerts = array.test_alert()
    return alerts


def get_alerts():
    from purestorage import FlashArray, purestorage
    creds = get_creds()
    array = purestorage.FlashArray(creds["host"], creds["user"], creds["password"])
    alerts = array.list_messages()
    return alerts

def show_all_volumes():
    from purestorage import FlashArray, purestorage
    creds = get_creds()
    array = purestorage.FlashArray(creds["host"], creds["user"], creds["password"])
    volumes = array.list_volumes()
    return volumes


def recover_volume(name):
    from purestorage import FlashArray, purestorage
    creds = get_creds()
    array = purestorage.FlashArray(creds["host"], creds["user"], creds["password"])
    recovery = array.recover_volume(name)
    return recovery


def get_hosts():
    from purestorage import FlashArray, purestorage
    creds = get_creds()
    array = purestorage.FlashArray(creds["host"], creds["user"], creds["password"])
    hosts = array.list_hosts()
    return hosts