# Forecasts
(*forecasts*)

## Overview

Operations related to forecasts

### Available Operations

* [get](#get) - Returns a textual forecast for a 2.5km grid area
* [get_hourly](#get_hourly) - Returns a textual hourly forecast for a 2.5km grid area
* [get_raw](#get_raw) - Returns raw numerical forecast data for a 2.5km grid area
* [get_taf](#get_taf) - Returns a single Terminal Aerodrome Forecast
* [get_tafs](#get_tafs) - Returns Terminal Aerodrome Forecasts for the specified airport station.
* [get_zone_forecast](#get_zone_forecast) - Returns the current zone forecast for a given zone

## get

Returns a textual forecast for a 2.5km grid area

### Example Usage

```python
from nws_api_client import NwsAPIClient
from nws_api_client.models import components
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.forecasts.get(wfo=components.NWSForecastOfficeID.LOT, gridpoint="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                             | Type                                                                                                                                                                                                                  | Required                                                                                                                                                                                                              | Description                                                                                                                                                                                                           | Example                                                                                                                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `wfo`                                                                                                                                                                                                                 | [components.NWSForecastOfficeID](../../models/components/nwsforecastofficeid.md)                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                    | Forecast office ID                                                                                                                                                                                                    | LOT                                                                                                                                                                                                                   |
| `gridpoint`                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                    | Forecast gridpoint pair(see https://weather-gov.github.io/api/gridpoints for more info)                                                                                                                               |                                                                                                                                                                                                                       |
| `feature_flags`                                                                                                                                                                                                       | List[[components.GridpointForecastFeatureFlags](../../models/components/gridpointforecastfeatureflags.md)]                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                    | Enable future and experimental features (see documentation for more info): * forecast_temperature_qv: Represent temperature as QuantitativeValue * forecast_wind_speed_qv: Represent wind speed as QuantitativeValue<br/> |                                                                                                                                                                                                                       |
| `units`                                                                                                                                                                                                               | [Optional[components.GridpointForecastUnits]](../../models/components/gridpointforecastunits.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                    | Use US customary or SI (metric) units in textual output                                                                                                                                                               |                                                                                                                                                                                                                       |
| `retries`                                                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                                                   |                                                                                                                                                                                                                       |

### Response

**[operations.GetForecastResponse](../../models/operations/getforecastresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ProblemDetailError | 400                       | application/problem+json  |
| errors.NWSAPIError        | 4XX, 5XX                  | \*/\*                     |

## get_hourly

Returns a textual hourly forecast for a 2.5km grid area

### Example Usage

```python
from nws_api_client import NwsAPIClient
from nws_api_client.models import components
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.forecasts.get_hourly(wfo=components.NWSForecastOfficeID.LOT, gridpoint="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                             | Type                                                                                                                                                                                                                  | Required                                                                                                                                                                                                              | Description                                                                                                                                                                                                           | Example                                                                                                                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `wfo`                                                                                                                                                                                                                 | [components.NWSForecastOfficeID](../../models/components/nwsforecastofficeid.md)                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                    | Forecast office ID                                                                                                                                                                                                    | LOT                                                                                                                                                                                                                   |
| `gridpoint`                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                    | Forecast gridpoint pair(see https://weather-gov.github.io/api/gridpoints for more info)                                                                                                                               |                                                                                                                                                                                                                       |
| `feature_flags`                                                                                                                                                                                                       | List[[components.GridpointForecastFeatureFlags](../../models/components/gridpointforecastfeatureflags.md)]                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                    | Enable future and experimental features (see documentation for more info): * forecast_temperature_qv: Represent temperature as QuantitativeValue * forecast_wind_speed_qv: Represent wind speed as QuantitativeValue<br/> |                                                                                                                                                                                                                       |
| `units`                                                                                                                                                                                                               | [Optional[components.GridpointForecastUnits]](../../models/components/gridpointforecastunits.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                    | Use US customary or SI (metric) units in textual output                                                                                                                                                               |                                                                                                                                                                                                                       |
| `retries`                                                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                                                   |                                                                                                                                                                                                                       |

### Response

**[operations.GetHourlyForecastResponse](../../models/operations/gethourlyforecastresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ProblemDetailError | 400                       | application/problem+json  |
| errors.NWSAPIError        | 4XX, 5XX                  | \*/\*                     |

## get_raw

Returns raw numerical forecast data for a 2.5km grid area

### Example Usage

```python
from nws_api_client import NwsAPIClient
from nws_api_client.models import components
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.forecasts.get_raw(wfo=components.NWSForecastOfficeID.LOT, gridpoint="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             | Example                                                                                 |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `wfo`                                                                                   | [components.NWSForecastOfficeID](../../models/components/nwsforecastofficeid.md)        | :heavy_check_mark:                                                                      | Forecast office ID                                                                      | LOT                                                                                     |
| `gridpoint`                                                                             | *str*                                                                                   | :heavy_check_mark:                                                                      | Forecast gridpoint pair(see https://weather-gov.github.io/api/gridpoints for more info) |                                                                                         |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |                                                                                         |

### Response

**[operations.GetForecastRawResponse](../../models/operations/getforecastrawresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ProblemDetailError | 400                       | application/problem+json  |
| errors.NWSAPIError        | 4XX, 5XX                  | \*/\*                     |

## get_taf

Returns a single Terminal Aerodrome Forecast

### Example Usage

```python
from datetime import date
from nws_api_client import NwsAPIClient
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.forecasts.get_taf(station_id="KORD", date_=date.fromisoformat("2024-02-29"), time="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  | Example                                                                      |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `station_id`                                                                 | *str*                                                                        | :heavy_check_mark:                                                           | Observation station ID                                                       | KORD                                                                         |
| `date_`                                                                      | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) | :heavy_check_mark:                                                           | Date (YYYY-MM-DD format)                                                     | 2025-02-23                                                                   |
| `time`                                                                       | *str*                                                                        | :heavy_check_mark:                                                           | Time (HHMM format). This time is always specified in UTC (Zulu) time.        | 0419                                                                         |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |                                                                              |

### Response

**[operations.GetTafResponse](../../models/operations/gettafresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ProblemDetailError | 400                       | application/problem+json  |
| errors.NWSAPIError        | 4XX, 5XX                  | \*/\*                     |

## get_tafs

Returns Terminal Aerodrome Forecasts for the specified airport station.

### Example Usage

```python
from nws_api_client import NwsAPIClient
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.forecasts.get_tafs(station_id="KORD")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `station_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Observation station ID                                              | KORD                                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.GetTafsResponse](../../models/operations/gettafsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ProblemDetailError | 400                       | application/problem+json  |
| errors.NWSAPIError        | 4XX, 5XX                  | \*/\*                     |

## get_zone_forecast

Returns the current zone forecast for a given zone

### Example Usage

```python
from nws_api_client import NwsAPIClient
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.forecasts.get_zone_forecast(type_="<value>", zone_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `type`                                                              | *str*                                                               | :heavy_check_mark:                                                  | Zone type                                                           |
| `zone_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | NWS public zone/county identifier                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetZoneForecastResponse](../../models/operations/getzoneforecastresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ProblemDetailError | 400                       | application/problem+json  |
| errors.NWSAPIError        | 4XX, 5XX                  | \*/\*                     |