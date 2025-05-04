# Geographic
(*geographic*)

## Overview

Operations that return data specific to NWS zones, counties, states, NWS grid points, or latitude/longitude coordinates

### Available Operations

* [get](#get) - Returns a textual forecast for a 2.5km grid area
* [get_active](#get_active) - Returns filtered (or all) currently active alerts
* [get_active_by_region](#get_active_by_region) - Returns active alerts for the given marine region
* [get_active_for_zone](#get_active_for_zone) - Returns active alerts for the given NWS public zone/county identifier
* [get_cwsu](#get_cwsu) - Returns metadata about a Center Weather Service Unit
* [get_hourly](#get_hourly) - Returns a textual hourly forecast for a 2.5km grid area
* [get_latest_observation](#get_latest_observation) - Returns the latest observation for a station
* [get_observation](#get_observation) - Returns a single observation
* [get_office](#get_office) - Returns metadata about a NWS forecast office
* [get_point_info](#get_point_info) - Returns metadata (inc. forecast gridpoint) about a given lat,long pair
* [get_raw](#get_raw) - Returns raw numerical forecast data for a 2.5km grid area
* [get_zone](#get_zone) - Returns metadata about a given zone
* [get_zone_forecast](#get_zone_forecast) - Returns the current zone forecast for a given zone
* [get_zone_stations](#get_zone_stations) - Returns a list of observation stations for a given zone
* [get_zones_by_type](#get_zones_by_type) - Returns a list of zones of a given type
* [list_active_for_area](#list_active_for_area) - Returns active alerts for the given state or marine area
* [list_gridpoint_stations](#list_gridpoint_stations) - Returns a list of observation stations usable for a given 2.5km grid area
* [list_observation_stations](#list_observation_stations) - Returns a list of observation stations.
* [list_zone_observations](#list_zone_observations) - Returns a list of observations for a given zone
* [list_zones](#list_zones) - Returns a list of zones

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

    res = nac_client.geographic.get(wfo=components.NWSForecastOfficeID.LOT, gridpoint="<value>")

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

## get_active

Returns filtered (or all) currently active alerts

### Example Usage

```python
from nws_api_client import NwsAPIClient
from nws_api_client.models import components
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.geographic.get_active(region=[
        components.MarineRegionCode.GL,
    ])

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                               | Type                                                                                                                                    | Required                                                                                                                                | Description                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `status`                                                                                                                                | List[[components.AlertStatusParameter](../../models/components/alertstatusparameter.md)]                                                | :heavy_minus_sign:                                                                                                                      | Status (actual, exercise, system, test, draft)                                                                                          |
| `message_type`                                                                                                                          | List[[components.AlertMessageTypeParameter](../../models/components/alertmessagetypeparameter.md)]                                      | :heavy_minus_sign:                                                                                                                      | Message type (alert, update, cancel)                                                                                                    |
| `event`                                                                                                                                 | List[*str*]                                                                                                                             | :heavy_minus_sign:                                                                                                                      | Event name                                                                                                                              |
| `code`                                                                                                                                  | List[*str*]                                                                                                                             | :heavy_minus_sign:                                                                                                                      | Event code                                                                                                                              |
| `area`                                                                                                                                  | List[[components.AreaCode](../../models/components/areacode.md)]                                                                        | :heavy_minus_sign:                                                                                                                      | State/territory code or marine area code This parameter is incompatible with the following parameters: point, region, region_type, zone |
| `point`                                                                                                                                 | *Optional[str]*                                                                                                                         | :heavy_minus_sign:                                                                                                                      | Point (latitude,longitude) This parameter is incompatible with the following parameters: area, region, region_type, zone                |
| `region`                                                                                                                                | List[[components.MarineRegionCode](../../models/components/marineregioncode.md)]                                                        | :heavy_minus_sign:                                                                                                                      | Marine region code This parameter is incompatible with the following parameters: area, point, region_type, zone                         |
| `region_type`                                                                                                                           | [Optional[components.AlertRegionType]](../../models/components/alertregiontype.md)                                                      | :heavy_minus_sign:                                                                                                                      | Region type (land or marine) This parameter is incompatible with the following parameters: area, point, region, zone                    |
| `zone`                                                                                                                                  | List[*str*]                                                                                                                             | :heavy_minus_sign:                                                                                                                      | Zone ID (forecast or county) This parameter is incompatible with the following parameters: area, point, region, region_type             |
| `urgency`                                                                                                                               | List[[components.AlertUrgency](../../models/components/alerturgency.md)]                                                                | :heavy_minus_sign:                                                                                                                      | Urgency (immediate, expected, future, past, unknown)                                                                                    |
| `severity`                                                                                                                              | List[[components.AlertSeverity](../../models/components/alertseverity.md)]                                                              | :heavy_minus_sign:                                                                                                                      | Severity (extreme, severe, moderate, minor, unknown)                                                                                    |
| `certainty`                                                                                                                             | List[[components.AlertCertainty](../../models/components/alertcertainty.md)]                                                            | :heavy_minus_sign:                                                                                                                      | Certainty (observed, likely, possible, unlikely, unknown)                                                                               |
| `limit`                                                                                                                                 | *Optional[int]*                                                                                                                         | :heavy_minus_sign:                                                                                                                      | Limit                                                                                                                                   |
| `retries`                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                        | :heavy_minus_sign:                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                     |

### Response

**[operations.GetActiveAlertsResponse](../../models/operations/getactivealertsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ProblemDetailError | 400                       | application/problem+json  |
| errors.NWSAPIError        | 4XX, 5XX                  | \*/\*                     |

## get_active_by_region

Returns active alerts for the given marine region

### Example Usage

```python
from nws_api_client import NwsAPIClient
from nws_api_client.models import components
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.geographic.get_active_by_region(region=components.MarineRegionCode.GL)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                | Example                                                                    |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `region`                                                                   | [components.MarineRegionCode](../../models/components/marineregioncode.md) | :heavy_check_mark:                                                         | Marine region ID                                                           | GL                                                                         |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |                                                                            |

### Response

**[operations.GetActiveAlertsByMarineRegionResponse](../../models/operations/getactivealertsbymarineregionresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ProblemDetailError | 400                       | application/problem+json  |
| errors.NWSAPIError        | 4XX, 5XX                  | \*/\*                     |

## get_active_for_zone

Returns active alerts for the given NWS public zone/county identifier

### Example Usage

```python
from nws_api_client import NwsAPIClient
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.geographic.get_active_for_zone(zone_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `zone_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | NWS public zone/county identifier                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetActiveAlertsByZoneResponse](../../models/operations/getactivealertsbyzoneresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ProblemDetailError | 400                       | application/problem+json  |
| errors.NWSAPIError        | 4XX, 5XX                  | \*/\*                     |

## get_cwsu

Returns metadata about a Center Weather Service Unit

### Example Usage

```python
from nws_api_client import NwsAPIClient
from nws_api_client.models import components
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.geographic.get_cwsu(cwsu_id=components.NWSCenterWeatherServiceUnitID.ZHU)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `cwsu_id`                                                                                            | [components.NWSCenterWeatherServiceUnitID](../../models/components/nwscenterweatherserviceunitid.md) | :heavy_check_mark:                                                                                   | NWS CWSU ID                                                                                          |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.GetCwsuResponse](../../models/operations/getcwsuresponse.md)**

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

    res = nac_client.geographic.get_hourly(wfo=components.NWSForecastOfficeID.LOT, gridpoint="<value>")

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

## get_latest_observation

Returns the latest observation for a station

### Example Usage

```python
from nws_api_client import NwsAPIClient
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.geographic.get_latest_observation(station_id="KORD")

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

    res = nac_client.geographic.get_observation(station_id="KORD", timestamp=parse_datetime("2024-07-10T15:49:23.313Z"))

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

    res = nac_client.geographic.get_office(office_id=components.NWSOfficeID.GGW)

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

    res = nac_client.geographic.get_point_info(point="<value>")

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

    res = nac_client.geographic.get_raw(wfo=components.NWSForecastOfficeID.LOT, gridpoint="<value>")

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

    res = nac_client.geographic.get_zone(type_=components.NWSZoneType.COUNTY, zone_id="<id>")

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

## get_zone_forecast

Returns the current zone forecast for a given zone

### Example Usage

```python
from nws_api_client import NwsAPIClient
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.geographic.get_zone_forecast(type_="<value>", zone_id="<id>")

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

## get_zone_stations

Returns a list of observation stations for a given zone

### Example Usage

```python
from nws_api_client import NwsAPIClient
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.geographic.get_zone_stations(zone_id="<id>")

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

## get_zones_by_type

Returns a list of zones of a given type

### Example Usage

```python
from nws_api_client import NwsAPIClient
from nws_api_client.models import components
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.geographic.get_zones_by_type(type_path_parameter=components.NWSZoneType.COUNTY, region=[
        components.MarineRegionCode.GL,
        components.MarineRegionCode.GL,
        components.MarineRegionCode.GL,
    ], type_query_parameter=[
        components.NWSZoneType.COUNTY,
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            | Example                                                                |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `type_path_parameter`                                                  | [components.NWSZoneType](../../models/components/nwszonetype.md)       | :heavy_check_mark:                                                     | Zone type                                                              | county                                                                 |
| `id`                                                                   | List[*str*]                                                            | :heavy_minus_sign:                                                     | Zone ID (forecast or county)                                           |                                                                        |
| `area`                                                                 | List[[components.AreaCode](../../models/components/areacode.md)]       | :heavy_minus_sign:                                                     | State/marine area code                                                 |                                                                        |
| `region`                                                               | List[[components.RegionCode](../../models/components/regioncode.md)]   | :heavy_minus_sign:                                                     | Region code                                                            |                                                                        |
| `type_query_parameter`                                                 | List[[components.NWSZoneType](../../models/components/nwszonetype.md)] | :heavy_minus_sign:                                                     | Zone type                                                              |                                                                        |
| `point`                                                                | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | Point (latitude,longitude)                                             |                                                                        |
| `include_geometry`                                                     | *Optional[bool]*                                                       | :heavy_minus_sign:                                                     | Include geometry in results (true/false)                               |                                                                        |
| `limit`                                                                | *Optional[int]*                                                        | :heavy_minus_sign:                                                     | Limit                                                                  |                                                                        |
| `effective`                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects)   | :heavy_minus_sign:                                                     | Effective date/time                                                    |                                                                        |
| `retries`                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)       | :heavy_minus_sign:                                                     | Configuration to override the default retry behavior of the client.    |                                                                        |

### Response

**[operations.GetZonesByTypeResponse](../../models/operations/getzonesbytyperesponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ProblemDetailError | 400                       | application/problem+json  |
| errors.NWSAPIError        | 4XX, 5XX                  | \*/\*                     |

## list_active_for_area

Returns active alerts for the given state or marine area

### Example Usage

```python
from nws_api_client import NwsAPIClient
from nws_api_client.models import components
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.geographic.list_active_for_area(area=components.AreaCode.VT)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `area`                                                              | [components.AreaCode](../../models/components/areacode.md)          | :heavy_check_mark:                                                  | State or Marine Area ID                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetActiveAlertsByAreaResponse](../../models/operations/getactivealertsbyarearesponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ProblemDetailError | 400                       | application/problem+json  |
| errors.NWSAPIError        | 4XX, 5XX                  | \*/\*                     |

## list_gridpoint_stations

Returns a list of observation stations usable for a given 2.5km grid area

### Example Usage

```python
from nws_api_client import NwsAPIClient
from nws_api_client.models import components
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.geographic.list_gridpoint_stations(wfo=components.NWSForecastOfficeID.LOT, gridpoint="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             | Example                                                                                 |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `wfo`                                                                                   | [components.NWSForecastOfficeID](../../models/components/nwsforecastofficeid.md)        | :heavy_check_mark:                                                                      | Forecast office ID                                                                      | LOT                                                                                     |
| `gridpoint`                                                                             | *str*                                                                                   | :heavy_check_mark:                                                                      | Forecast gridpoint pair(see https://weather-gov.github.io/api/gridpoints for more info) |                                                                                         |
| `limit`                                                                                 | *Optional[int]*                                                                         | :heavy_minus_sign:                                                                      | Limit                                                                                   |                                                                                         |
| `cursor`                                                                                | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | Pagination cursor                                                                       |                                                                                         |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |                                                                                         |

### Response

**[operations.GetGridpointObservationStationsResponse](../../models/operations/getgridpointobservationstationsresponse.md)**

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

    res = nac_client.geographic.list_observation_stations()

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

## list_zone_observations

Returns a list of observations for a given zone

### Example Usage

```python
from nws_api_client import NwsAPIClient
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.geographic.list_zone_observations(zone_id="<id>", start="0419", end="0419")

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

## list_zones

Returns a list of zones

### Example Usage

```python
from nws_api_client import NwsAPIClient
from nws_api_client.models import components
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.geographic.list_zones(region=[
        components.MarineRegionCode.GL,
    ], type_=[
        components.NWSZoneType.COUNTY,
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `id`                                                                   | List[*str*]                                                            | :heavy_minus_sign:                                                     | Zone ID (forecast or county)                                           |
| `area`                                                                 | List[[components.AreaCode](../../models/components/areacode.md)]       | :heavy_minus_sign:                                                     | State/marine area code                                                 |
| `region`                                                               | List[[components.RegionCode](../../models/components/regioncode.md)]   | :heavy_minus_sign:                                                     | Region code                                                            |
| `type`                                                                 | List[[components.NWSZoneType](../../models/components/nwszonetype.md)] | :heavy_minus_sign:                                                     | Zone type                                                              |
| `point`                                                                | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | Point (latitude,longitude)                                             |
| `include_geometry`                                                     | *Optional[bool]*                                                       | :heavy_minus_sign:                                                     | Include geometry in results (true/false)                               |
| `limit`                                                                | *Optional[int]*                                                        | :heavy_minus_sign:                                                     | Limit                                                                  |
| `effective`                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects)   | :heavy_minus_sign:                                                     | Effective date/time                                                    |
| `retries`                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)       | :heavy_minus_sign:                                                     | Configuration to override the default retry behavior of the client.    |

### Response

**[operations.GetZonesResponse](../../models/operations/getzonesresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ProblemDetailError | 400                       | application/problem+json  |
| errors.NWSAPIError        | 4XX, 5XX                  | \*/\*                     |