# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ErrorDetails(Model):
    """The details of the error.

    :param code: One of a server-defined set of error codes.
    :type code: str
    :param message: A human-readable representation of the error.
    :type message: str
    :param details: A human-readable representation of the error's details.
    :type details: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'details': {'key': 'details', 'type': 'str'},
    }

    def __init__(self, *, code: str=None, message: str=None, details: str=None, **kwargs) -> None:
        super(ErrorDetails, self).__init__(**kwargs)
        self.code = code
        self.message = message
        self.details = details
