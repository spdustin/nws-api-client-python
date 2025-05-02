# Observationstations
(*observationstations*)

## Overview

Operations related to observationstations

### Available Operations

* [list_observations_by_station](#list_observations_by_station) - Returns a list of observations for a given station
* [get_latest_observation_by_station](#get_latest_observation_by_station) - Returns the latest observation for a station
* [get_observation_by_station](#get_observation_by_station) - Returns a single observation.
* [list_tafs](#list_tafs) - Returns Terminal Aerodrome Forecasts for the specified airport station.
* [get_taf](#get_taf) - Returns a single Terminal Aerodrome Forecast.
* [list_observation_stations](#list_observation_stations) - Returns a list of observation stations.
* [get_observation_station_metadata](#get_observation_station_metadata) - Returns metadata about a given observation station

## list_observations_by_station

Returns a list of observations for a given station

### Example Usage

```python
from nws_api_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.observationstations.list_observations_by_station(station_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `station_id`                                                         | *str*                                                                | :heavy_check_mark:                                                   | Observation station ID                                               |
| `start`                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | Start time                                                           |
| `end`                                                                | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | End time                                                             |
| `limit`                                                              | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | Limit                                                                |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Response

**[models.ListObservationsByStationResponse](../../models/listobservationsbystationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_latest_observation_by_station

Returns the latest observation for a station

### Example Usage

```python
from nws_api_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.observationstations.get_latest_observation_by_station(station_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `station_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Observation station ID                                              |
| `require_qc`                                                        | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Require QC                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetLatestObservationByStationResponse](../../models/getlatestobservationbystationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_observation_by_station

Returns a single observation.

### Example Usage

```python
from nws_api_client import NwsClient
from nws_api_client.utils import parse_datetime
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.observationstations.get_observation_by_station(station_id="<id>", time=parse_datetime("2025-02-15T11:07:35.928Z"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `station_id`                                                         | *str*                                                                | :heavy_check_mark:                                                   | Observation station ID                                               |
| `time`                                                               | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Timestamp of requested observation                                   |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Response

**[models.GetObservationByStationResponse](../../models/getobservationbystationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_tafs

Returns Terminal Aerodrome Forecasts for the specified airport station.

### Example Usage

```python
from nws_api_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.observationstations.list_tafs(station_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `station_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Observation station ID                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListTafsResponse](../../models/listtafsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_taf

Returns a single Terminal Aerodrome Forecast.

### Example Usage

```python
from datetime import date
from nws_api_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.observationstations.get_taf(station_id="<id>", date_=date.fromisoformat("2024-02-29"), time="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `station_id`                                                                 | *str*                                                                        | :heavy_check_mark:                                                           | Observation station ID                                                       |
| `date_`                                                                      | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) | :heavy_check_mark:                                                           | Date (YYYY-MM-DD format)                                                     |
| `time`                                                                       | *str*                                                                        | :heavy_check_mark:                                                           | Time (HHMM format). This time is always specified in UTC (Zulu) time.        |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[models.GetTafResponse](../../models/gettafresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_observation_stations

Returns a list of observation stations.

### Example Usage

```python
from nws_api_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.observationstations.list_observation_stations()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | List[*str*]                                                         | :heavy_minus_sign:                                                  | Filter by observation station ID                                    |
| `state`                                                             | List[[models.AreaCode](../../models/areacode.md)]                   | :heavy_minus_sign:                                                  | Filter by state/marine area code                                    |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Limit                                                               |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Pagination cursor                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListObservationStationsResponse](../../models/listobservationstationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_observation_station_metadata

Returns metadata about a given observation station

### Example Usage

```python
from nws_api_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.observationstations.get_observation_station_metadata(station_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `station_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Observation station ID                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetObservationStationMetadataResponse](../../models/getobservationstationmetadataresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |