# nws-api-client

Type-safe and developer-friendly Python client for the National Weather Service API.

> [!INFO]
> The first pass was built with Speakeasy, and I've been making some major quality-of-life adjustments.

> [!NOTE]
> The National Weather Service would like to know who is using their API. Please include a user agent with all API requests where value = your company name and email (a contactable email address). This is the same as the HTTP header 'User-Agent'. They'd also like to be able to contact you if there's an issue with your use of the API.

<!-- Start Summary [summary] -->
## Summary

weather.gov API: weather.gov API

For more information about the API: [Full API documentation](https://www.weather.gov/documentation/services-web-api)
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [nws-api-client](#nws-api-client)
  * [SDK Installation](#sdk-installation)
  * [SDK Example Usage](#sdk-example-usage)
  * [Authentication](#authentication)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->


## SDK Installation

### uv

[uv](https://docs.astral.sh/uv/) is the Python package manager I use and recommend.

```bash
uv add nws-api-client
```

### PIP

```bash
pip install nws-api-client
```

### Poetry

```bash
poetry add nws-api-client
```
<!-- No SDK Installation [installation] -->
<!-- No IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Get Locations for a Text Product Type

Get a list of locations that issue a particular forecast text product (like "AFD" for "Area Forecast Discussion")

```python
# Synchronous Example
from nws_api_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.products.list_locations_by_product_type(type_id="AFD")

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from nws_api_client import NwsClient
import os

async def main():

    async with NwsClient(
        user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
    ) as nws_client:

        res = await nws_client.products.list_locations_by_product_type_async(type_id="AFD")

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->


<!-- No Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [alerts](docs/sdks/alerts/README.md)

* [list_active_alerts](docs/sdks/alerts/README.md#list_active_alerts) - Returns all currently active alerts
* [list_active_alert_counts](docs/sdks/alerts/README.md#list_active_alert_counts) - Returns info on the number of active alerts
* [list_active_alerts_by_zone](docs/sdks/alerts/README.md#list_active_alerts_by_zone) - Returns active alerts for the given NWS public zone or county
* [list_active_alerts_by_area](docs/sdks/alerts/README.md#list_active_alerts_by_area) - Returns active alerts for the given area (state or marine area)
* [list_active_alerts_by_region](docs/sdks/alerts/README.md#list_active_alerts_by_region) - Returns active alerts for the given marine region
* [list_alert_types](docs/sdks/alerts/README.md#list_alert_types) - Returns a list of alert types
* [get_alert](docs/sdks/alerts/README.md#get_alert) - Returns a specific alert

### [aviation](docs/sdks/aviation/README.md)

* [get_cwsu](docs/sdks/aviation/README.md#get_cwsu) - Returns metadata about a Center Weather Service Unit
* [list_cwas](docs/sdks/aviation/README.md#list_cwas) - Returns a list of Center Weather Advisories from a CWSU
* [list_cwas_by_date_and_sequence](docs/sdks/aviation/README.md#list_cwas_by_date_and_sequence) - Returns a list of Center Weather Advisories from a CWSU
* [list_sigmets](docs/sdks/aviation/README.md#list_sigmets) - Returns a list of SIGMET/AIRMETs
* [list_sigmets_by_atsu](docs/sdks/aviation/README.md#list_sigmets_by_atsu) - Returns a list of SIGMET/AIRMETs for the specified ATSU
* [list_sigmets_by_atsu_and_date](docs/sdks/aviation/README.md#list_sigmets_by_atsu_and_date) - Returns a list of SIGMET/AIRMETs for the specified ATSU for the specified date
* [get_sigmet](docs/sdks/aviation/README.md#get_sigmet) - Returns a specific SIGMET/AIRMET

### [glossary](docs/sdks/glossarysdk/README.md)

* [list_terms](docs/sdks/glossarysdk/README.md#list_terms) - Returns glossary terms

### [gridpoints](docs/sdks/gridpoints/README.md)

* [get_gridpoint_raw_forecast](docs/sdks/gridpoints/README.md#get_gridpoint_raw_forecast) - Returns raw numerical forecast data for a 2.5km grid area
* [get_gridpoint_forecast](docs/sdks/gridpoints/README.md#get_gridpoint_forecast) - Returns a textual forecast for a 2.5km grid area
* [get_gridpoint_hourly_forecast](docs/sdks/gridpoints/README.md#get_gridpoint_hourly_forecast) - Returns a textual hourly forecast for a 2.5km grid area
* [list_observation_stations_by_gridpoint](docs/sdks/gridpoints/README.md#list_observation_stations_by_gridpoint) - Returns a list of observation stations usable for a given 2.5km grid area


### [observationstations](docs/sdks/observationstations/README.md)

* [list_observations_by_station](docs/sdks/observationstations/README.md#list_observations_by_station) - Returns a list of observations for a given station
* [get_latest_observation_by_station](docs/sdks/observationstations/README.md#get_latest_observation_by_station) - Returns the latest observation for a station
* [get_observation_by_station](docs/sdks/observationstations/README.md#get_observation_by_station) - Returns a single observation.
* [list_tafs](docs/sdks/observationstations/README.md#list_tafs) - Returns Terminal Aerodrome Forecasts for the specified airport station.
* [get_taf](docs/sdks/observationstations/README.md#get_taf) - Returns a single Terminal Aerodrome Forecast.
* [list_observation_stations](docs/sdks/observationstations/README.md#list_observation_stations) - Returns a list of observation stations.
* [get_observation_station_metadata](docs/sdks/observationstations/README.md#get_observation_station_metadata) - Returns metadata about a given observation station

### [offices](docs/sdks/offices/README.md)

* [get_office_metadata](docs/sdks/offices/README.md#get_office_metadata) - Returns metadata about a NWS forecast office
* [get_office_headline](docs/sdks/offices/README.md#get_office_headline) - Returns a specific news headline for a given NWS office
* [list_office_headlines](docs/sdks/offices/README.md#list_office_headlines) - Returns a list of news headlines for a given NWS office

### [points](docs/sdks/points/README.md)

* [get_point_metadata](docs/sdks/points/README.md#get_point_metadata) - Returns metadata about a given latitude/longitude point

### [products](docs/sdks/products/README.md)

* [list_products](docs/sdks/products/README.md#list_products) - Returns a list of text products
* [list_product_locations](docs/sdks/products/README.md#list_product_locations) - Returns a list of valid text product issuance locations
* [list_product_types](docs/sdks/products/README.md#list_product_types) - Returns a list of valid text product types and codes
* [get_product_by_id](docs/sdks/products/README.md#get_product_by_id) - Returns a specific text product
* [list_products_by_type](docs/sdks/products/README.md#list_products_by_type) - Returns a list of text products of a given type
* [list_locations_by_product_type](docs/sdks/products/README.md#list_locations_by_product_type) - Returns a list of valid text product issuance locations for a given product type
* [list_product_types_by_location](docs/sdks/products/README.md#list_product_types_by_location) - Returns a list of valid text product types for a given issuance location
* [list_products_by_type_and_location](docs/sdks/products/README.md#list_products_by_type_and_location) - Returns a list of text products of a given type for a given issuance location

### [radar](docs/sdks/radar/README.md)

* [list_radar_servers](docs/sdks/radar/README.md#list_radar_servers) - Returns a list of radar servers
* [get_radar_server_metadata](docs/sdks/radar/README.md#get_radar_server_metadata) - Returns metadata about a given radar server
* [list_radar_stations](docs/sdks/radar/README.md#list_radar_stations) - Returns a list of radar stations
* [get_radar_station_metadata](docs/sdks/radar/README.md#get_radar_station_metadata) - Returns metadata about a given radar station
* [get_radar_station_alarms_metadata](docs/sdks/radar/README.md#get_radar_station_alarms_metadata) - Returns metadata about a given radar station alarms
* [get_radar_queue_metadata](docs/sdks/radar/README.md#get_radar_queue_metadata) - Returns metadata about a given radar queue
* [get_radar_wind_profiler_metadata](docs/sdks/radar/README.md#get_radar_wind_profiler_metadata) - Returns metadata about a given radar wind profiler

### [zones](docs/sdks/zones/README.md)

* [list_zones](docs/sdks/zones/README.md#list_zones) - Returns a list of zones
* [list_zones_by_type](docs/sdks/zones/README.md#list_zones_by_type) - Returns a list of zones of a given type
* [get_zone_metadata](docs/sdks/zones/README.md#get_zone_metadata) - Returns metadata about a given zone
* [get_zone_forecast](docs/sdks/zones/README.md#get_zone_forecast) - Returns the current zone forecast for a given zone
* [list_observations_by_zone](docs/sdks/zones/README.md#list_observations_by_zone) - Returns a list of observations for a given zone
* [list_observation_stations_by_zone](docs/sdks/zones/README.md#list_observation_stations_by_zone) - Returns a list of observation stations for a given zone

</details>
<!-- End Available Resources and Operations [operations] -->


<!-- No Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an exception.

By default, an API error will raise a errors.APIError exception, which has the following properties:

| Property        | Type             | Description           |
|-----------------|------------------|-----------------------|
| `.status_code`  | *int*            | The HTTP status code  |
| `.message`      | *str*            | The error message     |
| `.raw_response` | *httpx.Response* | The raw HTTP response |
| `.body`         | *str*            | The response content  |

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `list_active_alerts_async` method may raise the following exceptions:

| Error Type      | Status Code | Content Type |
| --------------- | ----------- | ------------ |
| errors.APIError | 4XX, 5XX    | \*/\*        |

### Example

```python
from nws_api_client import NwsClient, errors
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:
    res = None
    try:

        res = nws_client.alerts.list_active_alerts()

        # Handle response
        print(res)

    except errors.APIError as e:
        # handle exception
        raise(e)
```
<!-- End Error Handling [errors] -->

<!-- No Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from nws_api_client import NwsClient
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = NwsClient(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from nws_api_client import NwsClient
from nws_api_client.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = NwsClient(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `NwsClient` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from nws_api_client import NwsClient
import os
def main():

    with NwsClient(
        user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
    ) as nws_client:
        # Rest of application here...


# Or when using async:
async def amain():

    async with NwsClient(
        user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
    ) as nws_client:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from nws_api_client import NwsClient
import logging

logging.basicConfig(level=logging.DEBUG)
s = NwsClient(debug_logger=logging.getLogger("nws_api_client"))
```

You can also enable a default debug logger by setting an environment variable `NWSCLIENT_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, I recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While I value open-source contributions to this SDK, this library is *currently* generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### Initial SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=nws-api-client&utm_campaign=python)
