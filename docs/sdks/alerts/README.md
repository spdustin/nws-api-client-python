# Alerts
(*alerts*)

## Overview

Operations related to alerts, advisories, SIGMETS, etc.

### Available Operations

* [get](#get) - Returns a specific alert
* [get_active](#get_active) - Returns filtered (or all) currently active alerts
* [get_active_by_region](#get_active_by_region) - Returns active alerts for the given marine region
* [get_active_count](#get_active_count) - Returns info on the number of active alerts
* [get_active_for_zone](#get_active_for_zone) - Returns active alerts for the given NWS public zone/county identifier
* [get_aviation_cwa](#get_aviation_cwa) - Returns a list of CWAs from a CWSU for a specific date and sequence
* [get_aviation_sigmet](#get_aviation_sigmet) - Returns a specific SIGMET/AIRMET
* [get_aviation_sigmets_by_atsu_for_date](#get_aviation_sigmets_by_atsu_for_date) - Returns a list of SIGMET/AIRMETs for the specified ATSU for the specified date
* [get_center_weather_advisories](#get_center_weather_advisories) - Returns a list of Center Weather Advisories from a CWSU
* [get_sigmets_by_atsu](#get_sigmets_by_atsu) - Returns a list of SIGMET/AIRMETs for the specified ATSU
* [list_active_for_area](#list_active_for_area) - Returns active alerts for the given state or marine area
* [list_sigmets](#list_sigmets) - Returns a list of SIGMET/AIRMETs
* [list_types](#list_types) - Returns a list of alert types

## get

Returns a specific alert

### Example Usage

```python
from nws_api_client import NwsAPIClient
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.alerts.get(id="urn:oid:2.49.0.1.840.0.404b3149af6da23b497bb9705fadc6ead564a967.005.1")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           | Example                                                               |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `id`                                                                  | *str*                                                                 | :heavy_check_mark:                                                    | Alert identifier                                                      | urn:oid:2.49.0.1.840.0.404b3149af6da23b497bb9705fadc6ead564a967.005.1 |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |                                                                       |

### Response

**[operations.GetAlertResponse](../../models/operations/getalertresponse.md)**

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

    res = nac_client.alerts.get_active(region=[
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

    res = nac_client.alerts.get_active_by_region(region=components.MarineRegionCode.GL)

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

## get_active_count

Returns info on the number of active alerts

### Example Usage

```python
from nws_api_client import NwsAPIClient
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.alerts.get_active_count()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetActiveAlertsCountResponse](../../models/operations/getactivealertscountresponse.md)**

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

    res = nac_client.alerts.get_active_for_zone(zone_id="<id>")

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

## get_aviation_cwa

Returns a list of CWAs from a CWSU for a specific date and sequence

### Example Usage

```python
from datetime import date
from nws_api_client import NwsAPIClient
from nws_api_client.models import components
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.alerts.get_aviation_cwa(cwsu_id=components.NWSCenterWeatherServiceUnitID.ZSE, date_=date.fromisoformat("2025-02-23"), sequence=510643)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          | Example                                                                                              |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `cwsu_id`                                                                                            | [components.NWSCenterWeatherServiceUnitID](../../models/components/nwscenterweatherserviceunitid.md) | :heavy_check_mark:                                                                                   | NWS CWSU ID                                                                                          |                                                                                                      |
| `date_`                                                                                              | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                         | :heavy_check_mark:                                                                                   | Date (YYYY-MM-DD format)                                                                             | 2025-02-23                                                                                           |
| `sequence`                                                                                           | *int*                                                                                                | :heavy_check_mark:                                                                                   | Sequence number                                                                                      |                                                                                                      |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |                                                                                                      |

### Response

**[operations.GetCwasByCwsuForDateAndSequenceResponse](../../models/operations/getcwasbycwsufordateandsequenceresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ProblemDetailError | 400                       | application/problem+json  |
| errors.NWSAPIError        | 4XX, 5XX                  | \*/\*                     |

## get_aviation_sigmet

Returns a specific SIGMET/AIRMET

### Example Usage

```python
from datetime import date
from nws_api_client import NwsAPIClient
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.alerts.get_aviation_sigmet(atsu="KKCI", date_=date.fromisoformat("2025-02-23"), time="0419")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  | Example                                                                      |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `atsu`                                                                       | *str*                                                                        | :heavy_check_mark:                                                           | ATSU identifier                                                              | KKCI                                                                         |
| `date_`                                                                      | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) | :heavy_check_mark:                                                           | Date (YYYY-MM-DD format)                                                     | 2025-02-23                                                                   |
| `time`                                                                       | *str*                                                                        | :heavy_check_mark:                                                           | Time (HHMM format). This time is always specified in UTC (Zulu) time.        | 0419                                                                         |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |                                                                              |

### Response

**[operations.GetSigmetResponse](../../models/operations/getsigmetresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ProblemDetailError | 400                       | application/problem+json  |
| errors.NWSAPIError        | 4XX, 5XX                  | \*/\*                     |

## get_aviation_sigmets_by_atsu_for_date

Returns a list of SIGMET/AIRMETs for the specified ATSU for the specified date

### Example Usage

```python
from datetime import date
from nws_api_client import NwsAPIClient
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.alerts.get_aviation_sigmets_by_atsu_for_date(atsu="KKCI", date_=date.fromisoformat("2025-02-23"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  | Example                                                                      |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `atsu`                                                                       | *str*                                                                        | :heavy_check_mark:                                                           | ATSU identifier                                                              | KKCI                                                                         |
| `date_`                                                                      | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) | :heavy_check_mark:                                                           | Date (YYYY-MM-DD format)                                                     | 2025-02-23                                                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |                                                                              |

### Response

**[operations.GetSigmetsByAtsuForDateResponse](../../models/operations/getsigmetsbyatsufordateresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ProblemDetailError | 400                       | application/problem+json  |
| errors.NWSAPIError        | 4XX, 5XX                  | \*/\*                     |

## get_center_weather_advisories

Returns a list of Center Weather Advisories from a CWSU

### Example Usage

```python
from nws_api_client import NwsAPIClient
from nws_api_client.models import components
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.alerts.get_center_weather_advisories(cwsu_id=components.NWSCenterWeatherServiceUnitID.ZDC)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `cwsu_id`                                                                                            | [components.NWSCenterWeatherServiceUnitID](../../models/components/nwscenterweatherserviceunitid.md) | :heavy_check_mark:                                                                                   | NWS CWSU ID                                                                                          |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.GetCwasByCwsuResponse](../../models/operations/getcwasbycwsuresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ProblemDetailError | 400                       | application/problem+json  |
| errors.NWSAPIError        | 4XX, 5XX                  | \*/\*                     |

## get_sigmets_by_atsu

Returns a list of SIGMET/AIRMETs for the specified ATSU

### Example Usage

```python
from nws_api_client import NwsAPIClient
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.alerts.get_sigmets_by_atsu(atsu="KKCI")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `atsu`                                                              | *str*                                                               | :heavy_check_mark:                                                  | ATSU identifier                                                     | KKCI                                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.GetSigmetsByAtsuResponse](../../models/operations/getsigmetsbyatsuresponse.md)**

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

    res = nac_client.alerts.list_active_for_area(area=components.AreaCode.VT)

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

## list_sigmets

Returns a list of SIGMET/AIRMETs

### Example Usage

```python
from datetime import date
from nws_api_client import NwsAPIClient
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.alerts.list_sigmets(start="0419", end="0419", date_=date.fromisoformat("2025-02-23"), atsu="KKCI", sequence="29W")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  | Example                                                                      |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `start`                                                                      | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | Start time                                                                   | 0419                                                                         |
| `end`                                                                        | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | End time                                                                     | 0419                                                                         |
| `date_`                                                                      | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) | :heavy_minus_sign:                                                           | Date (YYYY-MM-DD format)                                                     | 2025-02-23                                                                   |
| `atsu`                                                                       | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | ATSU identifier                                                              | KKCI                                                                         |
| `sequence`                                                                   | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | SIGMET sequence number                                                       | 29W                                                                          |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |                                                                              |

### Response

**[operations.GetSigmetsResponse](../../models/operations/getsigmetsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ProblemDetailError | 400                       | application/problem+json  |
| errors.NWSAPIError        | 4XX, 5XX                  | \*/\*                     |

## list_types

Returns a list of alert types

### Example Usage

```python
from nws_api_client import NwsAPIClient
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.alerts.list_types()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetAlertTypesResponse](../../models/operations/getalerttypesresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ProblemDetailError | 400                       | application/problem+json  |
| errors.NWSAPIError        | 4XX, 5XX                  | \*/\*                     |