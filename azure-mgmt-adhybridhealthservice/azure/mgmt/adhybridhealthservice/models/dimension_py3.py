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


class Dimension(Model):
    """The connector object error.

    :param status: The health status for the domain controller. Possible
     values include: 'Healthy', 'Warning', 'Error', 'NotMonitored', 'Missing'
    :type status: str or ~azure.mgmt.adhybridhealthservice.models.HealthStatus
    :param simple_properties: List of service specific configuration
     properties.
    :type simple_properties: object
    :param active_alerts: The count of alerts that are currently active for
     the service.
    :type active_alerts: int
    :param additional_information: The additional information related to the
     service.
    :type additional_information: str
    :param last_updated: The date or time , in UTC, when the service
     properties were last updated.
    :type last_updated: datetime
    :param display_name: The display name of the service.
    :type display_name: str
    :param resolved_alerts: The total count of alerts that has been resolved
     for the service.
    :type resolved_alerts: int
    :param signature: The signature of the service.
    :type signature: str
    :param type: The service type for the services onboarded to Azure Active
     Directory Connect Health. Depending on whether the service is monitoring,
     ADFS, Sync or ADDS roles, the service type can either be
     AdFederationService or AadSyncService or AdDomainService.
    :type type: str
    """

    _attribute_map = {
        'status': {'key': 'status', 'type': 'str'},
        'simple_properties': {'key': 'simpleProperties', 'type': 'object'},
        'active_alerts': {'key': 'activeAlerts', 'type': 'int'},
        'additional_information': {'key': 'additionalInformation', 'type': 'str'},
        'last_updated': {'key': 'lastUpdated', 'type': 'iso-8601'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'resolved_alerts': {'key': 'resolvedAlerts', 'type': 'int'},
        'signature': {'key': 'signature', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, *, status=None, simple_properties=None, active_alerts: int=None, additional_information: str=None, last_updated=None, display_name: str=None, resolved_alerts: int=None, signature: str=None, type: str=None, **kwargs) -> None:
        super(Dimension, self).__init__(**kwargs)
        self.status = status
        self.simple_properties = simple_properties
        self.active_alerts = active_alerts
        self.additional_information = additional_information
        self.last_updated = last_updated
        self.display_name = display_name
        self.resolved_alerts = resolved_alerts
        self.signature = signature
        self.type = type