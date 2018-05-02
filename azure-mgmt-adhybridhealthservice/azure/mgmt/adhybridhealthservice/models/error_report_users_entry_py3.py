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


class ErrorReportUsersEntry(Model):
    """The bad password login attempt details.

    :param user_id: The user ID value.
    :type user_id: str
    :param ip_address: The Ip address corresponding to the last error event.
    :type ip_address: str
    :param last_updated: The date and time when the last error event was
     logged.
    :type last_updated: datetime
    :param unique_id_addresses: The list of unique IP addresses.
    :type unique_id_addresses: str
    :param total_error_attempts: The total count of specific error events.
    :type total_error_attempts: int
    """

    _attribute_map = {
        'user_id': {'key': 'userId', 'type': 'str'},
        'ip_address': {'key': 'ipAddress', 'type': 'str'},
        'last_updated': {'key': 'lastUpdated', 'type': 'iso-8601'},
        'unique_id_addresses': {'key': 'uniqueIdAddresses', 'type': 'str'},
        'total_error_attempts': {'key': 'totalErrorAttempts', 'type': 'int'},
    }

    def __init__(self, *, user_id: str=None, ip_address: str=None, last_updated=None, unique_id_addresses: str=None, total_error_attempts: int=None, **kwargs) -> None:
        super(ErrorReportUsersEntry, self).__init__(**kwargs)
        self.user_id = user_id
        self.ip_address = ip_address
        self.last_updated = last_updated
        self.unique_id_addresses = unique_id_addresses
        self.total_error_attempts = total_error_attempts