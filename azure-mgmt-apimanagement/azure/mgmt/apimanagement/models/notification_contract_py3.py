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

from .resource import Resource


class NotificationContract(Resource):
    """Notification details.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type for API Management resource.
    :vartype type: str
    :param title: Required. Title of the Notification.
    :type title: str
    :param description: Description of the Notification.
    :type description: str
    :param recipients: Recipient Parameter values.
    :type recipients:
     ~azure.mgmt.apimanagement.models.RecipientsContractProperties
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'title': {'required': True, 'max_length': 1000, 'min_length': 1},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'title': {'key': 'properties.title', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'recipients': {'key': 'properties.recipients', 'type': 'RecipientsContractProperties'},
    }

    def __init__(self, *, title: str, description: str=None, recipients=None, **kwargs) -> None:
        super(NotificationContract, self).__init__(**kwargs)
        self.title = title
        self.description = description
        self.recipients = recipients