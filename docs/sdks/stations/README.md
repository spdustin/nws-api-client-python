# Stations
(*stations*)

## Overview

### Available Operations

* [get_observations](#get_observations) - Returns a list of observations for a given station
* [get_station](#get_station) - Returns metadata about a given observation station

## get_observations

Returns a list of observations for a given station

### Example Usage

```python
from nws_api_client import NwsAPIClient
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.stations.get_observations(station_id="KORD", start="0419", end="0419")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `station_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Observation station ID                                              | KORD                                                                |
| `start`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Start time                                                          | 0419                                                                |
| `end`                                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | End time                                                            | 0419                                                                |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Limit                                                               |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.GetObservationsResponse](../../models/operations/getobservationsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ProblemDetailError | 400                       | application/problem+json  |
| errors.NWSAPIError        | 4XX, 5XX                  | \*/\*                     |

## get_station

Returns metadata about a given observation station

### Example Usage

```python
from nws_api_client import NwsAPIClient
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.stations.get_station(station_id="KORD")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `station_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Observation station ID                                              | KORD                                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.GetObservationStationInfoResponse](../../models/operations/getobservationstationinforesponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ProblemDetailError | 400                       | application/problem+json  |
| errors.NWSAPIError        | 4XX, 5XX                  | \*/\*                     |