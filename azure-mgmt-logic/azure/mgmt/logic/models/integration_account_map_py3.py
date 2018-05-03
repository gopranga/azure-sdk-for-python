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


class IntegrationAccountMap(Resource):
    """The integration account map.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The resource id.
    :vartype id: str
    :ivar name: Gets the resource name.
    :vartype name: str
    :ivar type: Gets the resource type.
    :vartype type: str
    :param location: The resource location.
    :type location: str
    :param tags: The resource tags.
    :type tags: dict[str, str]
    :param map_type: Required. The map type. Possible values include:
     'NotSpecified', 'Xslt'
    :type map_type: str or ~azure.mgmt.logic.models.MapType
    :param parameters_schema: The parameters schema of integration account
     map.
    :type parameters_schema:
     ~azure.mgmt.logic.models.IntegrationAccountMapPropertiesParametersSchema
    :ivar created_time: The created time.
    :vartype created_time: datetime
    :ivar changed_time: The changed time.
    :vartype changed_time: datetime
    :param content: The content.
    :type content: str
    :param content_type: The content type.
    :type content_type: str
    :ivar content_link: The content link.
    :vartype content_link: ~azure.mgmt.logic.models.ContentLink
    :param metadata: The metadata.
    :type metadata: object
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'map_type': {'required': True},
        'created_time': {'readonly': True},
        'changed_time': {'readonly': True},
        'content_link': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'map_type': {'key': 'properties.mapType', 'type': 'MapType'},
        'parameters_schema': {'key': 'properties.parametersSchema', 'type': 'IntegrationAccountMapPropertiesParametersSchema'},
        'created_time': {'key': 'properties.createdTime', 'type': 'iso-8601'},
        'changed_time': {'key': 'properties.changedTime', 'type': 'iso-8601'},
        'content': {'key': 'properties.content', 'type': 'str'},
        'content_type': {'key': 'properties.contentType', 'type': 'str'},
        'content_link': {'key': 'properties.contentLink', 'type': 'ContentLink'},
        'metadata': {'key': 'properties.metadata', 'type': 'object'},
    }

    def __init__(self, *, map_type, location: str=None, tags=None, parameters_schema=None, content: str=None, content_type: str=None, metadata=None, **kwargs) -> None:
        super(IntegrationAccountMap, self).__init__(location=location, tags=tags, **kwargs)
        self.map_type = map_type
        self.parameters_schema = parameters_schema
        self.created_time = None
        self.changed_time = None
        self.content = content
        self.content_type = content_type
        self.content_link = None
        self.metadata = metadata
