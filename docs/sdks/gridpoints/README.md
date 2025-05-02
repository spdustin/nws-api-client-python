# Gridpoints
(*gridpoints*)

## Overview

Operations related to gridpoints (X,Y)

### Available Operations

* [get_gridpoint_raw_forecast](#get_gridpoint_raw_forecast) - Returns raw numerical forecast data for a 2.5km grid area
* [get_gridpoint_forecast](#get_gridpoint_forecast) - Returns a textual forecast for a 2.5km grid area
* [get_gridpoint_hourly_forecast](#get_gridpoint_hourly_forecast) - Returns a textual hourly forecast for a 2.5km grid area
* [list_observation_stations_by_gridpoint](#list_observation_stations_by_gridpoint) - Returns a list of observation stations usable for a given 2.5km grid area

## get_gridpoint_raw_forecast

Returns raw numerical forecast data for a 2.5km grid area

### Example Usage

```python
from nws_api_client import NwsClient, models
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.gridpoints.get_gridpoint_raw_forecast(wfo=models.NWSForecastOfficeID.BOX, point=[])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `wfo`                                                               | [models.NWSForecastOfficeID](../../models/nwsforecastofficeid.md)   | :heavy_check_mark:                                                  | Forecast office ID                                                  |
| `point`                                                             | List[*int*]                                                         | :heavy_check_mark:                                                  | Two-element array encoding grid X and Y (comma-separated)           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetGridpointRawForecastResponse](../../models/getgridpointrawforecastresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_gridpoint_forecast

Returns a textual forecast for a 2.5km grid area

### Example Usage

```python
from nws_api_client import NwsClient, models
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.gridpoints.get_gridpoint_forecast(wfo=models.NWSForecastOfficeID.PQR, point=[
        594606,
        731727,
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                             | Type                                                                                                                                                                                                                  | Required                                                                                                                                                                                                              | Description                                                                                                                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `wfo`                                                                                                                                                                                                                 | [models.NWSForecastOfficeID](../../models/nwsforecastofficeid.md)                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                                    | Forecast office ID                                                                                                                                                                                                    |
| `point`                                                                                                                                                                                                               | List[*int*]                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                    | Two-element array encoding grid X and Y (comma-separated)                                                                                                                                                             |
| `feature_flags`                                                                                                                                                                                                       | List[[models.GridpointForecastFeatureFlags](../../models/gridpointforecastfeatureflags.md)]                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                    | Enable future and experimental features (see documentation for more info):<br/>* forecast_temperature_qv: Represent temperature as QuantitativeValue<br/>* forecast_wind_speed_qv: Represent wind speed as QuantitativeValue<br/> |
| `units`                                                                                                                                                                                                               | [Optional[models.GridpointForecastUnits]](../../models/gridpointforecastunits.md)                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                    | Use US customary or SI (metric) units in textual output                                                                                                                                                               |
| `retries`                                                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                                                   |

### Response

**[models.GetGridpointForecastResponse](../../models/getgridpointforecastresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_gridpoint_hourly_forecast

Returns a textual hourly forecast for a 2.5km grid area

### Example Usage

```python
from nws_api_client import NwsClient, models
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.gridpoints.get_gridpoint_hourly_forecast(wfo=models.NWSForecastOfficeID.GID, point=[])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                             | Type                                                                                                                                                                                                                  | Required                                                                                                                                                                                                              | Description                                                                                                                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `wfo`                                                                                                                                                                                                                 | [models.NWSForecastOfficeID](../../models/nwsforecastofficeid.md)                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                                    | Forecast office ID                                                                                                                                                                                                    |
| `point`                                                                                                                                                                                                               | List[*int*]                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                    | Two-element array encoding grid X and Y (comma-separated)                                                                                                                                                             |
| `feature_flags`                                                                                                                                                                                                       | List[[models.GridpointForecastFeatureFlags](../../models/gridpointforecastfeatureflags.md)]                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                    | Enable future and experimental features (see documentation for more info):<br/>* forecast_temperature_qv: Represent temperature as QuantitativeValue<br/>* forecast_wind_speed_qv: Represent wind speed as QuantitativeValue<br/> |
| `units`                                                                                                                                                                                                               | [Optional[models.GridpointForecastUnits]](../../models/gridpointforecastunits.md)                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                    | Use US customary or SI (metric) units in textual output                                                                                                                                                               |
| `retries`                                                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                                                   |

### Response

**[models.GetGridpointHourlyForecastResponse](../../models/getgridpointhourlyforecastresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_observation_stations_by_gridpoint

Returns a list of observation stations usable for a given 2.5km grid area

### Example Usage

```python
from nws_api_client import NwsClient, models
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.gridpoints.list_observation_stations_by_gridpoint(wfo=models.NWSForecastOfficeID.IND, point=[
        739417,
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `wfo`                                                               | [models.NWSForecastOfficeID](../../models/nwsforecastofficeid.md)   | :heavy_check_mark:                                                  | Forecast office ID                                                  |
| `point`                                                             | List[*int*]                                                         | :heavy_check_mark:                                                  | Two-element array encoding grid X and Y (comma-separated)           |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Limit                                                               |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Pagination cursor                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListObservationStationsByGridpointResponse](../../models/listobservationstationsbygridpointresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |