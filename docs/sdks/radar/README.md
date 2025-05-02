# Radar
(*radar*)

## Overview

Operations related to radar stations

### Available Operations

* [list_radar_servers](#list_radar_servers) - Returns a list of radar servers
* [get_radar_server_metadata](#get_radar_server_metadata) - Returns metadata about a given radar server
* [list_radar_stations](#list_radar_stations) - Returns a list of radar stations
* [get_radar_station_metadata](#get_radar_station_metadata) - Returns metadata about a given radar station
* [get_radar_station_alarms_metadata](#get_radar_station_alarms_metadata) - Returns metadata about a given radar station alarms
* [get_radar_queue_metadata](#get_radar_queue_metadata) - Returns metadata about a given radar queue
* [get_radar_wind_profiler_metadata](#get_radar_wind_profiler_metadata) - Returns metadata about a given radar wind profiler

## list_radar_servers

Returns a list of radar servers

### Example Usage

```python
from nws_api_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.radar.list_radar_servers()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `reporting_host`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Show records from specific reporting host                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListRadarServersResponse](../../models/listradarserversresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_radar_server_metadata

Returns metadata about a given radar server

### Example Usage

```python
from nws_api_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.radar.get_radar_server_metadata(id="<id>")

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

**[models.GetRadarServerMetadataResponse](../../models/getradarservermetadataresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_radar_stations

Returns a list of radar stations

### Example Usage

```python
from nws_api_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.radar.list_radar_stations()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `station_type`                                                      | List[*str*]                                                         | :heavy_minus_sign:                                                  | Limit results to a specific station type or types                   |
| `reporting_host`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Show RDA and latency info from specific reporting host              |
| `host`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Show latency info from specific LDM host                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListRadarStationsResponse](../../models/listradarstationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_radar_station_metadata

Returns metadata about a given radar station

### Example Usage

```python
from nws_api_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.radar.get_radar_station_metadata(station_id="<id>")

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

**[models.GetRadarStationMetadataResponse](../../models/getradarstationmetadataresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_radar_station_alarms_metadata

Returns metadata about a given radar station alarms

### Example Usage

```python
from nws_api_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.radar.get_radar_station_alarms_metadata(station_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `station_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Radar station ID                                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetRadarStationAlarmsMetadataResponse](../../models/getradarstationalarmsmetadataresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_radar_queue_metadata

Returns metadata about a given radar queue

### Example Usage

```python
from nws_api_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.radar.get_radar_queue_metadata(host="apt-chow.info", arrived="2007-03-01T13:00:00Z/2008-05-11T15:30:00Z", created="2007-03-01T13:00:00Z/2008-05-11T15:30:00Z", published="2007-03-01T13:00:00Z/2008-05-11T15:30:00Z")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `host`                                                              | *str*                                                               | :heavy_check_mark:                                                  | LDM host                                                            |                                                                     |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Record limit                                                        |                                                                     |
| `arrived`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Range for arrival time                                              | 2007-03-01T13:00:00Z/2008-05-11T15:30:00Z                           |
| `created`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Range for creation time                                             | 2007-03-01T13:00:00Z/2008-05-11T15:30:00Z                           |
| `published`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Range for publish time                                              | 2007-03-01T13:00:00Z/2008-05-11T15:30:00Z                           |
| `station`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Station identifier                                                  |                                                                     |
| `type`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Record type                                                         |                                                                     |
| `feed`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Originating product feed                                            |                                                                     |
| `resolution`                                                        | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Resolution version                                                  |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetRadarQueueMetadataResponse](../../models/getradarqueuemetadataresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_radar_wind_profiler_metadata

Returns metadata about a given radar wind profiler

### Example Usage

```python
from nws_api_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.radar.get_radar_wind_profiler_metadata(station_id="<id>", time="2007-03-01T13:00:00Z/2008-05-11T15:30:00Z", interval="P2DT12H")

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

**[models.GetRadarWindProfilerMetadataResponse](../../models/getradarwindprofilermetadataresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |