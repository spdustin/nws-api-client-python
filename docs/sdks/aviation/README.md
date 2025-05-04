# Aviation
(*aviation*)

## Overview

Operations related to aviation weather

### Available Operations

* [get_aviation_cwa](#get_aviation_cwa) - Returns a list of CWAs from a CWSU for a specific date and sequence
* [get_aviation_sigmet](#get_aviation_sigmet) - Returns a specific SIGMET/AIRMET
* [get_aviation_sigmets_by_atsu_for_date](#get_aviation_sigmets_by_atsu_for_date) - Returns a list of SIGMET/AIRMETs for the specified ATSU for the specified date
* [get_center_weather_advisories](#get_center_weather_advisories) - Returns a list of Center Weather Advisories from a CWSU
* [get_cwsu](#get_cwsu) - Returns metadata about a Center Weather Service Unit
* [get_sigmets_by_atsu](#get_sigmets_by_atsu) - Returns a list of SIGMET/AIRMETs for the specified ATSU
* [get_taf](#get_taf) - Returns a single Terminal Aerodrome Forecast
* [get_tafs](#get_tafs) - Returns Terminal Aerodrome Forecasts for the specified airport station.
* [list_sigmets](#list_sigmets) - Returns a list of SIGMET/AIRMETs

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

    res = nac_client.aviation.get_aviation_cwa(cwsu_id=components.NWSCenterWeatherServiceUnitID.ZSE, date_=date.fromisoformat("2025-02-23"), sequence=510643)

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

    res = nac_client.aviation.get_aviation_sigmet(atsu="KKCI", date_=date.fromisoformat("2025-02-23"), time="0419")

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

    res = nac_client.aviation.get_aviation_sigmets_by_atsu_for_date(atsu="KKCI", date_=date.fromisoformat("2025-02-23"))

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

    res = nac_client.aviation.get_center_weather_advisories(cwsu_id=components.NWSCenterWeatherServiceUnitID.ZDC)

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

    res = nac_client.aviation.get_cwsu(cwsu_id=components.NWSCenterWeatherServiceUnitID.ZHU)

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

## get_sigmets_by_atsu

Returns a list of SIGMET/AIRMETs for the specified ATSU

### Example Usage

```python
from nws_api_client import NwsAPIClient
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.aviation.get_sigmets_by_atsu(atsu="KKCI")

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

    res = nac_client.aviation.get_taf(station_id="KORD", date_=date.fromisoformat("2024-02-29"), time="<value>")

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

    res = nac_client.aviation.get_tafs(station_id="KORD")

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

    res = nac_client.aviation.list_sigmets(start="0419", end="0419", date_=date.fromisoformat("2025-02-23"), atsu="KKCI", sequence="29W")

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