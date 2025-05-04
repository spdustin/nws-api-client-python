# Metadata
(*metadata*)

## Overview

Operations that return metadata about an NWS resource/entity

### Available Operations

* [get_office](#get_office) - Returns metadata about a NWS forecast office
* [get_point_info](#get_point_info) - Returns metadata (inc. forecast gridpoint) about a given lat,long pair
* [get_profiler](#get_profiler) - Returns metadata about a given radar wind profiler
* [get_queue](#get_queue) - Returns metadata about a given radar queue
* [get_radar_station](#get_radar_station) - Returns metadata about a given radar station
* [get_server](#get_server) - Returns metadata about a given radar server
* [get_station_alarms](#get_station_alarms) - Returns metadata about a given radar station alarms
* [get_zone](#get_zone) - Returns metadata about a given zone
* [get_zone_stations](#get_zone_stations) - Returns a list of observation stations for a given zone
* [list_observation_stations](#list_observation_stations) - Returns a list of observation stations.
* [list_servers](#list_servers) - Returns a list of radar servers
* [list_stations](#list_stations) - Returns a list of radar stations

## get_office

Returns metadata about a NWS forecast office

### Example Usage

```python
from nws_api_client import NwsAPIClient
from nws_api_client.models import components
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.metadata.get_office(office_id=components.NWSOfficeID.GGW)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `office_id`                                                                | [Optional[components.NWSOfficeID]](../../models/components/nwsofficeid.md) | :heavy_minus_sign:                                                         | NWS office ID                                                              |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[operations.GetOfficeInfoResponse](../../models/operations/getofficeinforesponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ProblemDetailError | 400                       | application/problem+json  |
| errors.NWSAPIError        | 4XX, 5XX                  | \*/\*                     |

## get_point_info

Returns metadata (inc. forecast gridpoint) about a given lat,long pair

### Example Usage

```python
from nws_api_client import NwsAPIClient
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.metadata.get_point_info(point="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `point`                                                             | *str*                                                               | :heavy_check_mark:                                                  | Point (latitude, longitude)                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetLatLongInfoResponse](../../models/operations/getlatlonginforesponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ProblemDetailError | 400                       | application/problem+json  |
| errors.NWSAPIError        | 4XX, 5XX                  | \*/\*                     |

## get_profiler

Returns metadata about a given radar wind profiler

### Example Usage

```python
from nws_api_client import NwsAPIClient
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.metadata.get_profiler(station_id="<id>", time="2007-03-01T13:00:00Z/2008-05-11T15:30:00Z", interval="P2DT12H")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `station_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Profiler station ID                                                 |                                                                     |
| `time`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Time interval                                                       | 2007-03-01T13:00:00Z/2008-05-11T15:30:00Z                           |
| `interval`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Averaging interval                                                  | P2DT12H                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.GetRadarProfilerInfoResponse](../../models/operations/getradarprofilerinforesponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ProblemDetailError | 400                       | application/problem+json  |
| errors.NWSAPIError        | 4XX, 5XX                  | \*/\*                     |

## get_queue

Returns metadata about a given radar queue

### Example Usage

```python
from nws_api_client import NwsAPIClient
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.metadata.get_queue(host="faraway-hierarchy.biz", arrived="2007-03-01T13:00:00Z/2008-05-11T15:30:00Z", created="2007-03-01T13:00:00Z/2008-05-11T15:30:00Z", published="2007-03-01T13:00:00Z/2008-05-11T15:30:00Z")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `host`                                                              | *str*                                                               | :heavy_check_mark:                                                  | LDM host                                                            |                                                                     |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Limit                                                               |                                                                     |
| `arrived`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Range for arrival time                                              | 2007-03-01T13:00:00Z/2008-05-11T15:30:00Z                           |
| `created`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Range for creation time                                             | 2007-03-01T13:00:00Z/2008-05-11T15:30:00Z                           |
| `published`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Range for publish time                                              | 2007-03-01T13:00:00Z/2008-05-11T15:30:00Z                           |
| `station`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Station identifier                                                  |                                                                     |
| `type`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Record type                                                         |                                                                     |
| `feed`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Originating product feed                                            |                                                                     |
| `resolution`                                                        | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Resolution version                                                  |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.GetRadarStationQueueResponse](../../models/operations/getradarstationqueueresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ProblemDetailError | 400                       | application/problem+json  |
| errors.NWSAPIError        | 4XX, 5XX                  | \*/\*                     |

## get_radar_station

Returns metadata about a given radar station

### Example Usage

```python
from nws_api_client import NwsAPIClient
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.metadata.get_radar_station(station_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `station_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Radar station ID                                                    |
| `reporting_host`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Show RDA and latency info from specific reporting host              |
| `host`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Show latency info from specific LDM host                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetRadarStationInfoResponse](../../models/operations/getradarstationinforesponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ProblemDetailError | 400                       | application/problem+json  |
| errors.NWSAPIError        | 4XX, 5XX                  | \*/\*                     |

## get_server

Returns metadata about a given radar server

### Example Usage

```python
from nws_api_client import NwsAPIClient
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.metadata.get_server(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Server ID                                                           |
| `reporting_host`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Show records from specific reporting host                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetRadarServerResponse](../../models/operations/getradarserverresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ProblemDetailError | 400                       | application/problem+json  |
| errors.NWSAPIError        | 4XX, 5XX                  | \*/\*                     |

## get_station_alarms

Returns metadata about a given radar station alarms

### Example Usage

```python
from nws_api_client import NwsAPIClient
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.metadata.get_station_alarms(station_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `station_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Radar station ID                                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetRadarStationAlarmsResponse](../../models/operations/getradarstationalarmsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ProblemDetailError | 400                       | application/problem+json  |
| errors.NWSAPIError        | 4XX, 5XX                  | \*/\*                     |

## get_zone

Returns metadata about a given zone

### Example Usage

```python
from nws_api_client import NwsAPIClient
from nws_api_client.models import components
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.metadata.get_zone(type_=components.NWSZoneType.COUNTY, zone_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `type`                                                               | [components.NWSZoneType](../../models/components/nwszonetype.md)     | :heavy_check_mark:                                                   | Zone type                                                            | county                                                               |
| `zone_id`                                                            | *str*                                                                | :heavy_check_mark:                                                   | NWS public zone/county identifier                                    |                                                                      |
| `effective`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | Effective date/time                                                  |                                                                      |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |                                                                      |

### Response

**[operations.GetZoneInfoResponse](../../models/operations/getzoneinforesponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ProblemDetailError | 400                       | application/problem+json  |
| errors.NWSAPIError        | 4XX, 5XX                  | \*/\*                     |

## get_zone_stations

Returns a list of observation stations for a given zone

### Example Usage

```python
from nws_api_client import NwsAPIClient
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.metadata.get_zone_stations(zone_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `zone_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | NWS public zone/county identifier                                   |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Limit                                                               |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Pagination cursor                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetZoneStationsResponse](../../models/operations/getzonestationsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ProblemDetailError | 400                       | application/problem+json  |
| errors.NWSAPIError        | 4XX, 5XX                  | \*/\*                     |

## list_observation_stations

Returns a list of observation stations.

### Example Usage

```python
from nws_api_client import NwsAPIClient
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.metadata.list_observation_stations()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | List[*str*]                                                         | :heavy_minus_sign:                                                  | Filter by observation station ID                                    |
| `state`                                                             | List[[components.AreaCode](../../models/components/areacode.md)]    | :heavy_minus_sign:                                                  | Filter by state/marine area code                                    |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Limit                                                               |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Pagination cursor                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetObservationStationsResponse](../../models/operations/getobservationstationsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ProblemDetailError | 400                       | application/problem+json  |
| errors.NWSAPIError        | 4XX, 5XX                  | \*/\*                     |

## list_servers

Returns a list of radar servers

### Example Usage

```python
from nws_api_client import NwsAPIClient
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.metadata.list_servers()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `reporting_host`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Show records from specific reporting host                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetRadarServersResponse](../../models/operations/getradarserversresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ProblemDetailError | 400                       | application/problem+json  |
| errors.NWSAPIError        | 4XX, 5XX                  | \*/\*                     |

## list_stations

Returns a list of radar stations

### Example Usage

```python
from nws_api_client import NwsAPIClient
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.metadata.list_stations()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `station_type`                                                      | List[*str*]                                                         | :heavy_minus_sign:                                                  | Limit results to a specific station type or types                   |
| `reporting_host`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Show records from specific reporting host                           |
| `host`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Show latency info from specific LDM host                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetRadarStationsResponse](../../models/operations/getradarstationsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ProblemDetailError | 400                       | application/problem+json  |
| errors.NWSAPIError        | 4XX, 5XX                  | \*/\*                     |