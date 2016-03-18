#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
certifi.py
~~~~~~~~~~

This module returns the installation location of cacert.pem.
"""
import os
import warnings

DEB_SSL_CA_FILE = '/etc/ssl/certs/ca-certificates.crt'


class DeprecatedBundleWarning(DeprecationWarning):
    """
    The weak security bundle is being deprecated. Please bother your service
    provider to get them to stop using cross-signed roots.
    """


def where():
    if os.path.exists(DEB_SSL_CA_FILE):
        return DEB_SSL_CA_FILE

    f = os.path.split(__file__)[0]

    return os.path.join(f, 'cacert.pem')


def old_where():
    warnings.warn(
        "The weak security bundle is being deprecated.",
        DeprecatedBundleWarning
    )
    f = os.path.split(__file__)[0]
    return os.path.join(f, 'weak.pem')

if __name__ == '__main__':
    print(where())
