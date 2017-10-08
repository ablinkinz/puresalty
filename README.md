# puresalty
SaltStack module for interacting with PureStorage

PureStorage Module for SaltStack
===================

.. versionadded:: TBD

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

