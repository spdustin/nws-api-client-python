# Alerts
(*alerts*)

## Overview

Operations related to alerts

### Available Operations

* [list_active_alerts](#list_active_alerts) - Returns all currently active alerts
* [list_active_alert_counts](#list_active_alert_counts) - Returns info on the number of active alerts
* [list_active_alerts_by_zone](#list_active_alerts_by_zone) - Returns active alerts for the given NWS public zone or county
* [list_active_alerts_by_area](#list_active_alerts_by_area) - Returns active alerts for the given area (state or marine area)
* [list_active_alerts_by_region](#list_active_alerts_by_region) - Returns active alerts for the given marine region
* [list_alert_types](#list_alert_types) - Returns a list of alert types
* [get_alert](#get_alert) - Returns a specific alert

## list_active_alerts

Returns all currently active alerts

### Example Usage

```python
from nws_api_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.alerts.list_active_alerts()

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

**[models.ListActiveAlertsResponse](../../models/listactivealertsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_active_alert_counts

Returns info on the number of active alerts

### Example Usage

```python
from nws_api_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.alerts.list_active_alert_counts()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListActiveAlertCountsResponse](../../models/listactivealertcountsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_active_alerts_by_zone

Returns active alerts for the given NWS public zone or county

### Example Usage

```python
from nws_api_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.alerts.list_active_alerts_by_zone(zone_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `zone_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | NWS public zone/county identifier                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListActiveAlertsByZoneResponse](../../models/listactivealertsbyzoneresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_active_alerts_by_area

Returns active alerts for the given area (state or marine area)

### Example Usage

```python
from nws_api_client import NwsClient, models
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.alerts.list_active_alerts_by_area(area=models.Area.PH)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `area`                                                              | [models.Area](../../models/area.md)                                 | :heavy_check_mark:                                                  | State or marine area code                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListActiveAlertsByAreaResponse](../../models/listactivealertsbyarearesponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_active_alerts_by_region

Returns active alerts for the given marine region

### Example Usage

```python
from nws_api_client import NwsClient, models
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.alerts.list_active_alerts_by_region(region=models.MarineRegionCode.AT)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `region`                                                            | [models.MarineRegionCode](../../models/marineregioncode.md)         | :heavy_check_mark:                                                  | Marine region ID                                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListActiveAlertsByRegionResponse](../../models/listactivealertsbyregionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_alert_types

Returns a list of alert types

### Example Usage

```python
from nws_api_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.alerts.list_alert_types()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListAlertTypesResponse](../../models/listalerttypesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_alert

Returns a specific alert

### Example Usage

```python
from nws_api_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.alerts.get_alert(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Alert identifier                                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetAlertResponse](../../models/getalertresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |