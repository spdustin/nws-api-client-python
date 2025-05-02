# Zones
(*zones*)

## Overview

Operations related to zones

### Available Operations

* [list_zones](#list_zones) - Returns a list of zones
* [list_zones_by_type](#list_zones_by_type) - Returns a list of zones of a given type
* [get_zone_metadata](#get_zone_metadata) - Returns metadata about a given zone
* [get_zone_forecast](#get_zone_forecast) - Returns the current zone forecast for a given zone
* [list_observations_by_zone](#list_observations_by_zone) - Returns a list of observations for a given zone
* [list_observation_stations_by_zone](#list_observation_stations_by_zone) - Returns a list of observation stations for a given zone

## list_zones

Returns a list of zones

### Example Usage

```python
from nws_api_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.zones.list_zones()

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

**[models.ListZonesResponse](../../models/listzonesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_zones_by_type

Returns a list of zones of a given type

### Example Usage

```python
from nws_api_client import NwsClient, models
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.zones.list_zones_by_type(type_path_parameter=models.NWSZoneType.MARINE)

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

**[models.ListZonesByTypeResponse](../../models/listzonesbytyperesponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_zone_metadata

Returns metadata about a given zone

### Example Usage

```python
from nws_api_client import NwsClient, models
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.zones.get_zone_metadata(type_=models.NWSZoneType.PUBLIC, zone_id="<id>")

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

**[models.GetZoneMetadataResponse](../../models/getzonemetadataresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_zone_forecast

Returns the current zone forecast for a given zone

### Example Usage

```python
from nws_api_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.zones.get_zone_forecast(type_="<value>", zone_id="<id>")

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

**[models.GetZoneForecastResponse](../../models/getzoneforecastresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_observations_by_zone

Returns a list of observations for a given zone

### Example Usage

```python
from nws_api_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.zones.list_observations_by_zone(zone_id="<id>")

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

**[models.ListObservationsByZoneResponse](../../models/listobservationsbyzoneresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_observation_stations_by_zone

Returns a list of observation stations for a given zone

### Example Usage

```python
from nws_api_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.zones.list_observation_stations_by_zone(zone_id="<id>")

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

**[models.ListObservationStationsByZoneResponse](../../models/listobservationstationsbyzoneresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |