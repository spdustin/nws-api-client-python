# Conditions
(*conditions*)

## Overview

Operations related to current conditions

### Available Operations

* [get_latest_observation](#get_latest_observation) - Returns the latest observation for a station
* [get_observation](#get_observation) - Returns a single observation
* [list_zone_observations](#list_zone_observations) - Returns a list of observations for a given zone

## get_latest_observation

Returns the latest observation for a station

### Example Usage

```python
from nws_api_client import NwsAPIClient
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.conditions.get_latest_observation(station_id="KORD")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `station_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Observation station ID                                              | KORD                                                                |
| `require_qc`                                                        | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Require QC                                                          |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.GetLatestObservationResponse](../../models/operations/getlatestobservationresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ProblemDetailError | 400                       | application/problem+json  |
| errors.NWSAPIError        | 4XX, 5XX                  | \*/\*                     |

## get_observation

Returns a single observation

### Example Usage

```python
from nws_api_client import NwsAPIClient
from nws_api_client.utils import parse_datetime
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.conditions.get_observation(station_id="KORD", timestamp=parse_datetime("2024-07-10T15:49:23.313Z"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            | Example                                                                                |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `station_id`                                                                           | *str*                                                                                  | :heavy_check_mark:                                                                     | Observation station ID                                                                 | KORD                                                                                   |
| `timestamp`                                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects)                   | :heavy_check_mark:                                                                     | Timestamp of requested observation (YYYY-MM-DDThh:mm:ssZ or YYYY-MM-DDThh:mm:ss+hh:mm) |                                                                                        |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |                                                                                        |

### Response

**[operations.GetObservationResponse](../../models/operations/getobservationresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ProblemDetailError | 400                       | application/problem+json  |
| errors.NWSAPIError        | 4XX, 5XX                  | \*/\*                     |

## list_zone_observations

Returns a list of observations for a given zone

### Example Usage

```python
from nws_api_client import NwsAPIClient
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.conditions.list_zone_observations(zone_id="<id>", start="0419", end="0419")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `zone_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | NWS public zone/county identifier                                   |                                                                     |
| `start`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Start time                                                          | 0419                                                                |
| `end`                                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | End time                                                            | 0419                                                                |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Limit                                                               |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.GetZoneObservationsResponse](../../models/operations/getzoneobservationsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ProblemDetailError | 400                       | application/problem+json  |
| errors.NWSAPIError        | 4XX, 5XX                  | \*/\*                     |