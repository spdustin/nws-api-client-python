# Aviation
(*aviation*)

## Overview

Operations related to aviation weather

### Available Operations

* [get_cwsu](#get_cwsu) - Returns metadata about a Center Weather Service Unit
* [list_cwas](#list_cwas) - Returns a list of Center Weather Advisories from a CWSU
* [list_cwas_by_date_and_sequence](#list_cwas_by_date_and_sequence) - Returns a list of Center Weather Advisories from a CWSU
* [list_sigmets](#list_sigmets) - Returns a list of SIGMET/AIRMETs
* [list_sigmets_by_atsu](#list_sigmets_by_atsu) - Returns a list of SIGMET/AIRMETs for the specified ATSU
* [list_sigmets_by_atsu_and_date](#list_sigmets_by_atsu_and_date) - Returns a list of SIGMET/AIRMETs for the specified ATSU for the specified date
* [get_sigmet](#get_sigmet) - Returns a specific SIGMET/AIRMET

## get_cwsu

Returns metadata about a Center Weather Service Unit

### Example Usage

```python
from nws_api_client import NwsClient, models
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.aviation.get_cwsu(cwsu_id=models.NWSCenterWeatherServiceUnitID.ZHU)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `cwsu_id`                                                                             | [models.NWSCenterWeatherServiceUnitID](../../models/nwscenterweatherserviceunitid.md) | :heavy_check_mark:                                                                    | NWS CWSU ID                                                                           |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.GetCwsuResponse](../../models/getcwsuresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_cwas

Returns a list of Center Weather Advisories from a CWSU

### Example Usage

```python
from nws_api_client import NwsClient, models
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.aviation.list_cwas(cwsu_id=models.NWSCenterWeatherServiceUnitID.ZBW)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `cwsu_id`                                                                             | [models.NWSCenterWeatherServiceUnitID](../../models/nwscenterweatherserviceunitid.md) | :heavy_check_mark:                                                                    | NWS CWSU ID                                                                           |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.ListCwasResponse](../../models/listcwasresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_cwas_by_date_and_sequence

Returns a list of Center Weather Advisories from a CWSU

### Example Usage

```python
from datetime import date
from nws_api_client import NwsClient, models
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.aviation.list_cwas_by_date_and_sequence(cwsu_id=models.NWSCenterWeatherServiceUnitID.ZJX, date_=date.fromisoformat("2023-12-27"), sequence=109102)

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

**[models.ListCwasByDateAndSequenceResponse](../../models/listcwasbydateandsequenceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_sigmets

Returns a list of SIGMET/AIRMETs

### Example Usage

```python
from nws_api_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.aviation.list_sigmets()

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

**[models.ListSigmetsResponse](../../models/listsigmetsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_sigmets_by_atsu

Returns a list of SIGMET/AIRMETs for the specified ATSU

### Example Usage

```python
from nws_api_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.aviation.list_sigmets_by_atsu(atsu="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `atsu`                                                              | *str*                                                               | :heavy_check_mark:                                                  | ATSU identifier                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListSigmetsByAtsuResponse](../../models/listsigmetsbyatsuresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_sigmets_by_atsu_and_date

Returns a list of SIGMET/AIRMETs for the specified ATSU for the specified date

### Example Usage

```python
from datetime import date
from nws_api_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.aviation.list_sigmets_by_atsu_and_date(atsu="<value>", date_=date.fromisoformat("2024-10-13"))

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

**[models.ListSigmetsByAtsuAndDateResponse](../../models/listsigmetsbyatsuanddateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_sigmet

Returns a specific SIGMET/AIRMET

### Example Usage

```python
from datetime import date
from nws_api_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.aviation.get_sigmet(atsu="<value>", date_=date.fromisoformat("2024-12-28"), time="<value>")

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

**[models.GetSigmetResponse](../../models/getsigmetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |