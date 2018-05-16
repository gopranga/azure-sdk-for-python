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

from msrest.service_client import SDKClient
from msrest import Configuration, Serializer, Deserializer
from .version import VERSION
from msrest.pipeline import ClientRawResponse
from . import models


class OperationalInsightsDataClientConfiguration(Configuration):
    """Configuration for OperationalInsightsDataClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if not base_url:
            base_url = 'https://api.loganalytics.io/v1'

        super(OperationalInsightsDataClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-operationalinsights/{}'.format(VERSION))

        self.credentials = credentials


class OperationalInsightsDataClient(SDKClient):
    """Operational Insights Data Client

    :ivar config: Configuration for client.
    :vartype config: OperationalInsightsDataClientConfiguration

    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        self.config = OperationalInsightsDataClientConfiguration(credentials, base_url)
        super(OperationalInsightsDataClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = 'v1'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)


    def query(
            self, workspace_id, body, custom_headers=None, raw=False, **operation_config):
        """Execute an Analytics query.

        Executes an Analytics query for data.
        [Here](/documentation/2-Using-the-API/Query) is an example for using
        POST with an Analytics query.

        :param workspace_id: ID of the workspace. This is Workspace ID from
         the Properties blade in the Azure portal.
        :type workspace_id: str
        :param body: The Analytics query. Learn more about the [Analytics
         query
         syntax](https://azure.microsoft.com/documentation/articles/app-insights-analytics-reference/)
        :type body: ~azure.operationalinsights.models.QueryBody
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: QueryResults or ClientRawResponse if raw=true
        :rtype: ~azure.operationalinsights.models.QueryResults or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.operationalinsights.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.query.metadata['url']
        path_format_arguments = {
            'workspaceId': self._serialize.url("workspace_id", workspace_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(body, 'QueryBody')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('QueryResults', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    query.metadata = {'url': '/workspaces/{workspaceId}/query'}
