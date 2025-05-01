# NwsClient SDK

## Overview

weather.gov API: weather.gov API

Full API documentation
<https://www.weather.gov/documentation/services-web-api>

### Available Operations

* [alerts_query](#alerts_query) - Returns all alerts
* [alerts_active](#alerts_active) - Returns all currently active alerts
* [alerts_active_count](#alerts_active_count) - Returns info on the number of active alerts
* [alerts_active_zone](#alerts_active_zone) - Returns active alerts for the given NWS public zone or county
* [alerts_active_area](#alerts_active_area) - Returns active alerts for the given area (state or marine area)
* [alerts_active_region](#alerts_active_region) - Returns active alerts for the given marine region
* [alerts_types](#alerts_types) - Returns a list of alert types
* [alerts_single](#alerts_single) - Returns a specific alert
* [cwsu](#cwsu) - Returns metadata about a Center Weather Service Unit
* [cwas](#cwas) - Returns a list of Center Weather Advisories from a CWSU
* [cwa](#cwa) - Returns a list of Center Weather Advisories from a CWSU
* [sigmet_query](#sigmet_query) - Returns a list of SIGMET/AIRMETs
* [sigmets_by_atsu](#sigmets_by_atsu) - Returns a list of SIGMET/AIRMETs for the specified ATSU
* [sigmets_by_atsu_by_date](#sigmets_by_atsu_by_date) - Returns a list of SIGMET/AIRMETs for the specified ATSU for the specified date
* [sigmet](#sigmet) - Returns a specific SIGMET/AIRMET
* [glossary](#glossary) - Returns glossary terms
* [gridpoint](#gridpoint) - Returns raw numerical forecast data for a 2.5km grid area
* [gridpoint_forecast](#gridpoint_forecast) - Returns a textual forecast for a 2.5km grid area
* [gridpoint_forecast_hourly](#gridpoint_forecast_hourly) - Returns a textual hourly forecast for a 2.5km grid area
* [gridpoint_stations](#gridpoint_stations) - Returns a list of observation stations usable for a given 2.5km grid area
* [~~icons~~](#icons) - Returns a forecast icon. Icon services in API are deprecated. :warning: **Deprecated**
* [~~icons_dual_condition~~](#icons_dual_condition) - Returns a forecast icon. Icon services in API are deprecated. :warning: **Deprecated**
* [~~icons_summary~~](#icons_summary) - Returns a list of icon codes and textual descriptions. Icon services in API are deprecated. :warning: **Deprecated**
* [~~satellite_thumbnails~~](#satellite_thumbnails) - Returns a thumbnail image for a satellite region. Image services in API are deprecated. :warning: **Deprecated**
* [station_observation_list](#station_observation_list) - Returns a list of observations for a given station
* [station_observation_latest](#station_observation_latest) - Returns the latest observation for a station
* [station_observation_time](#station_observation_time) - Returns a single observation.
* [tafs](#tafs) - Returns Terminal Aerodrome Forecasts for the specified airport station.
* [taf](#taf) - Returns a single Terminal Aerodrome Forecast.
* [obs_stations](#obs_stations) - Returns a list of observation stations.
* [obs_station](#obs_station) - Returns metadata about a given observation station
* [office](#office) - Returns metadata about a NWS forecast office
* [office_headline](#office_headline) - Returns a specific news headline for a given NWS office
* [office_headlines](#office_headlines) - Returns a list of news headlines for a given NWS office
* [point](#point) - Returns metadata about a given latitude/longitude point
* [~~point_stations~~](#point_stations) - Returns a list of observation stations for a given point :warning: **Deprecated**
* [radar_servers](#radar_servers) - Returns a list of radar servers
* [radar_server](#radar_server) - Returns metadata about a given radar server
* [radar_stations](#radar_stations) - Returns a list of radar stations
* [radar_station](#radar_station) - Returns metadata about a given radar station
* [radar_station_alarms](#radar_station_alarms) - Returns metadata about a given radar station alarms
* [radar_queue](#radar_queue) - Returns metadata about a given radar queue
* [radar_profiler](#radar_profiler) - Returns metadata about a given radar wind profiler
* [products_query](#products_query) - Returns a list of text products
* [product_locations](#product_locations) - Returns a list of valid text product issuance locations
* [product_types](#product_types) - Returns a list of valid text product types and codes
* [product](#product) - Returns a specific text product
* [products_type](#products_type) - Returns a list of text products of a given type
* [products_type_locations](#products_type_locations) - Returns a list of valid text product issuance locations for a given product type
* [location_products](#location_products) - Returns a list of valid text product types for a given issuance location
* [products_type_location](#products_type_location) - Returns a list of text products of a given type for a given issuance location
* [zone_list](#zone_list) - Returns a list of zones
* [zone_list_type](#zone_list_type) - Returns a list of zones of a given type
* [zone](#zone) - Returns metadata about a given zone
* [zone_forecast](#zone_forecast) - Returns the current zone forecast for a given zone
* [zone_obs](#zone_obs) - Returns a list of observations for a given zone
* [zone_stations](#zone_stations) - Returns a list of observation stations for a given zone

## alerts_query

Returns all alerts

### Example Usage

```python
from nws_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.alerts_query()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                               | Type                                                                                                                                                                                    | Required                                                                                                                                                                                | Description                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `active`                                                                                                                                                                                | *Optional[bool]*                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                      | : warning: ** DEPRECATED **: This will be removed in a future release, please migrate away from it as soon as possible.<br/><br/>List only active alerts (use /alerts/active endpoints instead) |
| `start`                                                                                                                                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                      | Start time                                                                                                                                                                              |
| `end`                                                                                                                                                                                   | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                      | End time                                                                                                                                                                                |
| `status`                                                                                                                                                                                | List[[models.AlertStatusParameter](../../models/alertstatusparameter.md)]                                                                                                               | :heavy_minus_sign:                                                                                                                                                                      | Status (actual, exercise, system, test, draft)                                                                                                                                          |
| `message_type`                                                                                                                                                                          | List[[models.AlertMessageTypeParameter](../../models/alertmessagetypeparameter.md)]                                                                                                     | :heavy_minus_sign:                                                                                                                                                                      | Message type (alert, update, cancel)                                                                                                                                                    |
| `event`                                                                                                                                                                                 | List[*str*]                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                      | Event name                                                                                                                                                                              |
| `code`                                                                                                                                                                                  | List[*str*]                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                      | Event code                                                                                                                                                                              |
| `area`                                                                                                                                                                                  | List[[models.AreaCode](../../models/areacode.md)]                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                      | State/territory code or marine area code<br/>This parameter is incompatible with the following parameters: point, region, region_type, zone<br/>                                        |
| `point`                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                      | Point (latitude,longitude)<br/>This parameter is incompatible with the following parameters: area, region, region_type, zone<br/>                                                       |
| `region`                                                                                                                                                                                | List[[models.MarineRegionCode](../../models/marineregioncode.md)]                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                      | Marine region code<br/>This parameter is incompatible with the following parameters: area, point, region_type, zone<br/>                                                                |
| `region_type`                                                                                                                                                                           | [Optional[models.AlertRegionType]](../../models/alertregiontype.md)                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                      | Region type (land or marine)<br/>This parameter is incompatible with the following parameters: area, point, region, zone<br/>                                                           |
| `zone`                                                                                                                                                                                  | List[*str*]                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                      | Zone ID (forecast or county)<br/>This parameter is incompatible with the following parameters: area, point, region, region_type<br/>                                                    |
| `urgency`                                                                                                                                                                               | List[[models.AlertUrgency](../../models/alerturgency.md)]                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                      | Urgency (immediate, expected, future, past, unknown)                                                                                                                                    |
| `severity`                                                                                                                                                                              | List[[models.AlertSeverity](../../models/alertseverity.md)]                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                      | Severity (extreme, severe, moderate, minor, unknown)                                                                                                                                    |
| `certainty`                                                                                                                                                                             | List[[models.AlertCertainty](../../models/alertcertainty.md)]                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                      | Certainty (observed, likely, possible, unlikely, unknown)                                                                                                                               |
| `limit`                                                                                                                                                                                 | *Optional[int]*                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                      | Limit                                                                                                                                                                                   |
| `cursor`                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                      | Pagination cursor                                                                                                                                                                       |
| `retries`                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                     |

### Response

**[models.AlertsQueryResponse](../../models/alertsqueryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## alerts_active

Returns all currently active alerts

### Example Usage

```python
from nws_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.alerts_active()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                | Type                                                                                                                                     | Required                                                                                                                                 | Description                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `status`                                                                                                                                 | List[[models.AlertStatusParameter](../../models/alertstatusparameter.md)]                                                                | :heavy_minus_sign:                                                                                                                       | Status (actual, exercise, system, test, draft)                                                                                           |
| `message_type`                                                                                                                           | List[[models.AlertMessageTypeParameter](../../models/alertmessagetypeparameter.md)]                                                      | :heavy_minus_sign:                                                                                                                       | Message type (alert, update, cancel)                                                                                                     |
| `event`                                                                                                                                  | List[*str*]                                                                                                                              | :heavy_minus_sign:                                                                                                                       | Event name                                                                                                                               |
| `code`                                                                                                                                   | List[*str*]                                                                                                                              | :heavy_minus_sign:                                                                                                                       | Event code                                                                                                                               |
| `area`                                                                                                                                   | List[[models.AreaCode](../../models/areacode.md)]                                                                                        | :heavy_minus_sign:                                                                                                                       | State/territory code or marine area code<br/>This parameter is incompatible with the following parameters: point, region, region_type, zone<br/> |
| `point`                                                                                                                                  | *Optional[str]*                                                                                                                          | :heavy_minus_sign:                                                                                                                       | Point (latitude,longitude)<br/>This parameter is incompatible with the following parameters: area, region, region_type, zone<br/>        |
| `region`                                                                                                                                 | List[[models.MarineRegionCode](../../models/marineregioncode.md)]                                                                        | :heavy_minus_sign:                                                                                                                       | Marine region code<br/>This parameter is incompatible with the following parameters: area, point, region_type, zone<br/>                 |
| `region_type`                                                                                                                            | [Optional[models.AlertRegionType]](../../models/alertregiontype.md)                                                                      | :heavy_minus_sign:                                                                                                                       | Region type (land or marine)<br/>This parameter is incompatible with the following parameters: area, point, region, zone<br/>            |
| `zone`                                                                                                                                   | List[*str*]                                                                                                                              | :heavy_minus_sign:                                                                                                                       | Zone ID (forecast or county)<br/>This parameter is incompatible with the following parameters: area, point, region, region_type<br/>     |
| `urgency`                                                                                                                                | List[[models.AlertUrgency](../../models/alerturgency.md)]                                                                                | :heavy_minus_sign:                                                                                                                       | Urgency (immediate, expected, future, past, unknown)                                                                                     |
| `severity`                                                                                                                               | List[[models.AlertSeverity](../../models/alertseverity.md)]                                                                              | :heavy_minus_sign:                                                                                                                       | Severity (extreme, severe, moderate, minor, unknown)                                                                                     |
| `certainty`                                                                                                                              | List[[models.AlertCertainty](../../models/alertcertainty.md)]                                                                            | :heavy_minus_sign:                                                                                                                       | Certainty (observed, likely, possible, unlikely, unknown)                                                                                |
| `limit`                                                                                                                                  | *Optional[int]*                                                                                                                          | :heavy_minus_sign:                                                                                                                       | Limit                                                                                                                                    |
| `retries`                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                         | :heavy_minus_sign:                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                      |

### Response

**[models.AlertsActiveResponse](../../models/alertsactiveresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## alerts_active_count

Returns info on the number of active alerts

### Example Usage

```python
from nws_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.alerts_active_count()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AlertsActiveCountResponse](../../models/alertsactivecountresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## alerts_active_zone

Returns active alerts for the given NWS public zone or county

### Example Usage

```python
from nws_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.alerts_active_zone(zone_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `zone_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | NWS public zone/county identifier                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AlertsActiveZoneResponse](../../models/alertsactivezoneresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## alerts_active_area

Returns active alerts for the given area (state or marine area)

### Example Usage

```python
from nws_client import NwsClient, models
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.alerts_active_area(area=models.AlertsActiveAreaArea.AL)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `area`                                                              | [models.AlertsActiveAreaArea](../../models/alertsactiveareaarea.md) | :heavy_check_mark:                                                  | State or marine area code                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AlertsActiveAreaResponse](../../models/alertsactivearearesponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## alerts_active_region

Returns active alerts for the given marine region

### Example Usage

```python
from nws_client import NwsClient, models
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.alerts_active_region(region=models.MarineRegionCode.GM)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `region`                                                            | [models.MarineRegionCode](../../models/marineregioncode.md)         | :heavy_check_mark:                                                  | Marine region ID                                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AlertsActiveRegionResponse](../../models/alertsactiveregionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## alerts_types

Returns a list of alert types

### Example Usage

```python
from nws_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.alerts_types()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AlertsTypesResponse](../../models/alertstypesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## alerts_single

Returns a specific alert

### Example Usage

```python
from nws_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.alerts_single(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Alert identifier                                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AlertsSingleResponse](../../models/alertssingleresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## cwsu

Returns metadata about a Center Weather Service Unit

### Example Usage

```python
from nws_client import NwsClient, models
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.cwsu(cwsu_id=models.NWSCenterWeatherServiceUnitID.ZNY)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `cwsu_id`                                                                             | [models.NWSCenterWeatherServiceUnitID](../../models/nwscenterweatherserviceunitid.md) | :heavy_check_mark:                                                                    | NWS CWSU ID                                                                           |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.CwsuResponse](../../models/cwsuresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## cwas

Returns a list of Center Weather Advisories from a CWSU

### Example Usage

```python
from nws_client import NwsClient, models
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.cwas(cwsu_id=models.NWSCenterWeatherServiceUnitID.ZMA)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `cwsu_id`                                                                             | [models.NWSCenterWeatherServiceUnitID](../../models/nwscenterweatherserviceunitid.md) | :heavy_check_mark:                                                                    | NWS CWSU ID                                                                           |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.CwasResponse](../../models/cwasresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## cwa

Returns a list of Center Weather Advisories from a CWSU

### Example Usage

```python
from datetime import date
from nws_client import NwsClient, models
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.cwa(cwsu_id=models.NWSCenterWeatherServiceUnitID.ZAB, date_=date.fromisoformat("2024-05-15"), sequence=342163)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `cwsu_id`                                                                             | [models.NWSCenterWeatherServiceUnitID](../../models/nwscenterweatherserviceunitid.md) | :heavy_check_mark:                                                                    | NWS CWSU ID                                                                           |
| `date_`                                                                               | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)          | :heavy_check_mark:                                                                    | Date (YYYY-MM-DD format)                                                              |
| `sequence`                                                                            | *int*                                                                                 | :heavy_check_mark:                                                                    | Sequence number                                                                       |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.CwaResponse](../../models/cwaresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## sigmet_query

Returns a list of SIGMET/AIRMETs

### Example Usage

```python
from nws_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.sigmet_query()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `start`                                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects)         | :heavy_minus_sign:                                                           | Start time                                                                   |
| `end`                                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects)         | :heavy_minus_sign:                                                           | End time                                                                     |
| `date_`                                                                      | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) | :heavy_minus_sign:                                                           | Date (YYYY-MM-DD format)                                                     |
| `atsu`                                                                       | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | ATSU identifier                                                              |
| `sequence`                                                                   | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | SIGMET sequence number                                                       |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[models.SigmetQueryResponse](../../models/sigmetqueryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## sigmets_by_atsu

Returns a list of SIGMET/AIRMETs for the specified ATSU

### Example Usage

```python
from nws_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.sigmets_by_atsu(atsu="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `atsu`                                                              | *str*                                                               | :heavy_check_mark:                                                  | ATSU identifier                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SigmetsByATSUResponse](../../models/sigmetsbyatsuresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## sigmets_by_atsu_by_date

Returns a list of SIGMET/AIRMETs for the specified ATSU for the specified date

### Example Usage

```python
from datetime import date
from nws_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.sigmets_by_atsu_by_date(atsu="<value>", date_=date.fromisoformat("2024-02-27"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `atsu`                                                                       | *str*                                                                        | :heavy_check_mark:                                                           | ATSU identifier                                                              |
| `date_`                                                                      | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) | :heavy_check_mark:                                                           | Date (YYYY-MM-DD format)                                                     |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[models.SigmetsByATSUByDateResponse](../../models/sigmetsbyatsubydateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## sigmet

Returns a specific SIGMET/AIRMET

### Example Usage

```python
from datetime import date
from nws_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.sigmet(atsu="<value>", date_=date.fromisoformat("2024-03-15"), time="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `atsu`                                                                       | *str*                                                                        | :heavy_check_mark:                                                           | ATSU identifier                                                              |
| `date_`                                                                      | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) | :heavy_check_mark:                                                           | Date (YYYY-MM-DD format)                                                     |
| `time`                                                                       | *str*                                                                        | :heavy_check_mark:                                                           | Time (HHMM format). This time is always specified in UTC (Zulu) time.        |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[models.SigmetResponse](../../models/sigmetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## glossary

Returns glossary terms

### Example Usage

```python
from nws_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.glossary()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GlossaryResponse](../../models/glossaryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## gridpoint

Returns raw numerical forecast data for a 2.5km grid area

### Example Usage

```python
from nws_client import NwsClient, models
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.gridpoint(wfo=models.NWSForecastOfficeID.CYS, point=[
        734140,
        33787,
    ])

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

**[models.GridpointResponse](../../models/gridpointresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## gridpoint_forecast

Returns a textual forecast for a 2.5km grid area

### Example Usage

```python
from nws_client import NwsClient, models
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.gridpoint_forecast(wfo=models.NWSForecastOfficeID.AFG, point=[
        199671,
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

**[models.GridpointForecastResponse](../../models/gridpointforecastresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## gridpoint_forecast_hourly

Returns a textual hourly forecast for a 2.5km grid area

### Example Usage

```python
from nws_client import NwsClient, models
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.gridpoint_forecast_hourly(wfo=models.NWSForecastOfficeID.CRP, point=[
        476077,
        18384,
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

**[models.GridpointForecastHourlyResponse](../../models/gridpointforecasthourlyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## gridpoint_stations

Returns a list of observation stations usable for a given 2.5km grid area

### Example Usage

```python
from nws_client import NwsClient, models
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.gridpoint_stations(wfo=models.NWSForecastOfficeID.LZK, point=[
        661110,
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

**[models.GridpointStationsResponse](../../models/gridpointstationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## ~~icons~~

Returns a forecast icon. Icon services in API are deprecated.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
from nws_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.icons(set="<value>", time_of_day="<value>", first="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `set`                                                               | *str*                                                               | :heavy_check_mark:                                                  | .                                                                   |
| `time_of_day`                                                       | *str*                                                               | :heavy_check_mark:                                                  | .                                                                   |
| `first`                                                             | *str*                                                               | :heavy_check_mark:                                                  | .                                                                   |
| `size`                                                              | [Optional[models.IconsSize]](../../models/iconssize.md)             | :heavy_minus_sign:                                                  | Font size                                                           |
| `fontsize`                                                          | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Font size                                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.IconsResponse](../../models/iconsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## ~~icons_dual_condition~~

Returns a forecast icon. Icon services in API are deprecated.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
from nws_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.icons_dual_condition(set="<value>", time_of_day="<value>", first="<value>", second="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `set`                                                                             | *str*                                                                             | :heavy_check_mark:                                                                | .                                                                                 |
| `time_of_day`                                                                     | *str*                                                                             | :heavy_check_mark:                                                                | .                                                                                 |
| `first`                                                                           | *str*                                                                             | :heavy_check_mark:                                                                | .                                                                                 |
| `second`                                                                          | *str*                                                                             | :heavy_check_mark:                                                                | .                                                                                 |
| `size`                                                                            | [Optional[models.IconsDualConditionSize]](../../models/iconsdualconditionsize.md) | :heavy_minus_sign:                                                                | Font size                                                                         |
| `fontsize`                                                                        | *Optional[int]*                                                                   | :heavy_minus_sign:                                                                | Font size                                                                         |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.IconsDualConditionResponse](../../models/iconsdualconditionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## ~~icons_summary~~

Returns a list of icon codes and textual descriptions. Icon services in API are deprecated.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
from nws_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.icons_summary()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.IconsSummaryResponse](../../models/iconssummaryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## ~~satellite_thumbnails~~

Returns a thumbnail image for a satellite region. Image services in API are deprecated.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
from nws_client import NwsClient, models
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.satellite_thumbnails(area=models.SatelliteThumbnailsArea.G)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `area`                                                                    | [models.SatelliteThumbnailsArea](../../models/satellitethumbnailsarea.md) | :heavy_check_mark:                                                        | .                                                                         |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.SatelliteThumbnailsResponse](../../models/satellitethumbnailsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## station_observation_list

Returns a list of observations for a given station

### Example Usage

```python
from nws_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.station_observation_list(station_id="<id>")

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

**[models.StationObservationListResponse](../../models/stationobservationlistresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## station_observation_latest

Returns the latest observation for a station

### Example Usage

```python
from nws_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.station_observation_latest(station_id="<id>")

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

**[models.StationObservationLatestResponse](../../models/stationobservationlatestresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## station_observation_time

Returns a single observation.

### Example Usage

```python
from nws_client import NwsClient
from nws_client.utils import parse_datetime
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.station_observation_time(station_id="<id>", time=parse_datetime("2024-09-26T15:08:58.988Z"))

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

**[models.StationObservationTimeResponse](../../models/stationobservationtimeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## tafs

Returns Terminal Aerodrome Forecasts for the specified airport station.

### Example Usage

```python
from nws_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.tafs(station_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `station_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Observation station ID                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TafsResponse](../../models/tafsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## taf

Returns a single Terminal Aerodrome Forecast.

### Example Usage

```python
from datetime import date
from nws_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.taf(station_id="<id>", date_=date.fromisoformat("2023-06-14"), time="<value>")

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

**[models.TafResponse](../../models/tafresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## obs_stations

Returns a list of observation stations.

### Example Usage

```python
from nws_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.obs_stations()

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

**[models.ObsStationsResponse](../../models/obsstationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## obs_station

Returns metadata about a given observation station

### Example Usage

```python
from nws_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.obs_station(station_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `station_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Observation station ID                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ObsStationResponse](../../models/obsstationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## office

Returns metadata about a NWS forecast office

### Example Usage

```python
from nws_client import NwsClient, models
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.office(office_id=models.NWSOfficeID.MFR)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `office_id`                                                         | [models.NWSOfficeID](../../models/nwsofficeid.md)                   | :heavy_check_mark:                                                  | NWS office ID                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.OfficeResponse](../../models/officeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## office_headline

Returns a specific news headline for a given NWS office

### Example Usage

```python
from nws_client import NwsClient, models
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.office_headline(office_id=models.NWSOfficeID.SEW, headline_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `office_id`                                                         | [models.NWSOfficeID](../../models/nwsofficeid.md)                   | :heavy_check_mark:                                                  | NWS office ID                                                       |
| `headline_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Headline record ID                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.OfficeHeadlineResponse](../../models/officeheadlineresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## office_headlines

Returns a list of news headlines for a given NWS office

### Example Usage

```python
from nws_client import NwsClient, models
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.office_headlines(office_id=models.NWSOfficeID.ALY)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `office_id`                                                         | [models.NWSOfficeID](../../models/nwsofficeid.md)                   | :heavy_check_mark:                                                  | NWS office ID                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.OfficeHeadlinesResponse](../../models/officeheadlinesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## point

Returns metadata about a given latitude/longitude point

### Example Usage

```python
from nws_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.point(point="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `point`                                                             | *str*                                                               | :heavy_check_mark:                                                  | Point (latitude, longitude)                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PointResponse](../../models/pointresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## ~~point_stations~~

Returns a list of observation stations for a given point

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
from nws_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.point_stations(point="<value>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `point`                                                             | *str*                                                               | :heavy_check_mark:                                                  | Point (latitude, longitude)                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PointStationsResponse](../../models/pointstationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## radar_servers

Returns a list of radar servers

### Example Usage

```python
from nws_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.radar_servers()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `reporting_host`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Show records from specific reporting host                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RadarServersResponse](../../models/radarserversresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## radar_server

Returns metadata about a given radar server

### Example Usage

```python
from nws_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.radar_server(id="<id>")

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

**[models.RadarServerResponse](../../models/radarserverresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## radar_stations

Returns a list of radar stations

### Example Usage

```python
from nws_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.radar_stations()

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

**[models.RadarStationsResponse](../../models/radarstationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## radar_station

Returns metadata about a given radar station

### Example Usage

```python
from nws_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.radar_station(station_id="<id>")

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

**[models.RadarStationResponse](../../models/radarstationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## radar_station_alarms

Returns metadata about a given radar station alarms

### Example Usage

```python
from nws_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.radar_station_alarms(station_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `station_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Radar station ID                                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RadarStationAlarmsResponse](../../models/radarstationalarmsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## radar_queue

Returns metadata about a given radar queue

### Example Usage

```python
from nws_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.radar_queue(host="polite-mythology.org", arrived="2007-03-01T13:00:00Z/2008-05-11T15:30:00Z", created="2007-03-01T13:00:00Z/2008-05-11T15:30:00Z", published="2007-03-01T13:00:00Z/2008-05-11T15:30:00Z")

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

**[models.RadarQueueResponse](../../models/radarqueueresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## radar_profiler

Returns metadata about a given radar wind profiler

### Example Usage

```python
from nws_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.radar_profiler(station_id="<id>", time="2007-03-01T13:00:00Z/2008-05-11T15:30:00Z", interval="P2DT12H")

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

**[models.RadarProfilerResponse](../../models/radarprofilerresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## products_query

Returns a list of text products

### Example Usage

```python
from nws_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.products_query()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `location`                                                           | List[*str*]                                                          | :heavy_minus_sign:                                                   | Location id                                                          |
| `start`                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | Start time                                                           |
| `end`                                                                | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | End time                                                             |
| `office`                                                             | List[*str*]                                                          | :heavy_minus_sign:                                                   | Issuing office                                                       |
| `wmoid`                                                              | List[*str*]                                                          | :heavy_minus_sign:                                                   | WMO id code                                                          |
| `type`                                                               | List[*str*]                                                          | :heavy_minus_sign:                                                   | Product code                                                         |
| `limit`                                                              | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | Limit                                                                |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Response

**[models.ProductsQueryResponse](../../models/productsqueryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## product_locations

Returns a list of valid text product issuance locations

### Example Usage

```python
from nws_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.product_locations()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ProductLocationsResponse](../../models/productlocationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## product_types

Returns a list of valid text product types and codes

### Example Usage

```python
from nws_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.product_types()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ProductTypesResponse](../../models/producttypesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## product

Returns a specific text product

### Example Usage

```python
from nws_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.product(product_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `product_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | .                                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ProductResponse](../../models/productresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## products_type

Returns a list of text products of a given type

### Example Usage

```python
from nws_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.products_type(type_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `type_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | .                                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ProductsTypeResponse](../../models/productstyperesponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## products_type_locations

Returns a list of valid text product issuance locations for a given product type

### Example Usage

```python
from nws_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.products_type_locations(type_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `type_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | .                                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ProductsTypeLocationsResponse](../../models/productstypelocationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## location_products

Returns a list of valid text product types for a given issuance location

### Example Usage

```python
from nws_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.location_products(location_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `location_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | .                                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LocationProductsResponse](../../models/locationproductsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## products_type_location

Returns a list of text products of a given type for a given issuance location

### Example Usage

```python
from nws_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.products_type_location(type_id="<id>", location_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `type_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | .                                                                   |
| `location_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | .                                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ProductsTypeLocationResponse](../../models/productstypelocationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## zone_list

Returns a list of zones

### Example Usage

```python
from nws_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.zone_list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | List[*str*]                                                          | :heavy_minus_sign:                                                   | Zone ID (forecast or county)                                         |
| `area`                                                               | List[[models.AreaCode](../../models/areacode.md)]                    | :heavy_minus_sign:                                                   | State/marine area code                                               |
| `region`                                                             | List[[models.RegionCode](../../models/regioncode.md)]                | :heavy_minus_sign:                                                   | Region code                                                          |
| `type`                                                               | List[[models.NWSZoneType](../../models/nwszonetype.md)]              | :heavy_minus_sign:                                                   | Zone type                                                            |
| `point`                                                              | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Point (latitude,longitude)                                           |
| `include_geometry`                                                   | *Optional[bool]*                                                     | :heavy_minus_sign:                                                   | Include geometry in results (true/false)                             |
| `limit`                                                              | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | Limit                                                                |
| `effective`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | Effective date/time                                                  |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Response

**[models.ZoneListResponse](../../models/zonelistresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## zone_list_type

Returns a list of zones of a given type

### Example Usage

```python
from nws_client import NwsClient, models
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.zone_list_type(type_path_parameter=models.NWSZoneType.LAND)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `type_path_parameter`                                                | [models.NWSZoneType](../../models/nwszonetype.md)                    | :heavy_check_mark:                                                   | Zone type                                                            |
| `id`                                                                 | List[*str*]                                                          | :heavy_minus_sign:                                                   | Zone ID (forecast or county)                                         |
| `area`                                                               | List[[models.AreaCode](../../models/areacode.md)]                    | :heavy_minus_sign:                                                   | State/marine area code                                               |
| `region`                                                             | List[[models.RegionCode](../../models/regioncode.md)]                | :heavy_minus_sign:                                                   | Region code                                                          |
| `type_query_parameter`                                               | List[[models.NWSZoneType](../../models/nwszonetype.md)]              | :heavy_minus_sign:                                                   | Zone type                                                            |
| `point`                                                              | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Point (latitude,longitude)                                           |
| `include_geometry`                                                   | *Optional[bool]*                                                     | :heavy_minus_sign:                                                   | Include geometry in results (true/false)                             |
| `limit`                                                              | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | Limit                                                                |
| `effective`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | Effective date/time                                                  |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Response

**[models.ZoneListTypeResponse](../../models/zonelisttyperesponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## zone

Returns metadata about a given zone

### Example Usage

```python
from nws_client import NwsClient, models
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.zone(type_=models.NWSZoneType.MARINE, zone_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `type`                                                               | [models.NWSZoneType](../../models/nwszonetype.md)                    | :heavy_check_mark:                                                   | Zone type                                                            |
| `zone_id`                                                            | *str*                                                                | :heavy_check_mark:                                                   | NWS public zone/county identifier                                    |
| `effective`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | Effective date/time                                                  |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Response

**[models.ZoneResponse](../../models/zoneresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## zone_forecast

Returns the current zone forecast for a given zone

### Example Usage

```python
from nws_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.zone_forecast(type_="<value>", zone_id="<id>")

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

**[models.ZoneForecastResponse](../../models/zoneforecastresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## zone_obs

Returns a list of observations for a given zone

### Example Usage

```python
from nws_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.zone_obs(zone_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `zone_id`                                                            | *str*                                                                | :heavy_check_mark:                                                   | NWS public zone/county identifier                                    |
| `start`                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | Start date/time                                                      |
| `end`                                                                | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | End date/time                                                        |
| `limit`                                                              | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | Limit                                                                |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Response

**[models.ZoneObsResponse](../../models/zoneobsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## zone_stations

Returns a list of observation stations for a given zone

### Example Usage

```python
from nws_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nc_client:

    res = nc_client.zone_stations(zone_id="<id>")

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

**[models.ZoneStationsResponse](../../models/zonestationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |