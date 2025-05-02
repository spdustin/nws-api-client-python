# Offices
(*offices*)

## Overview

Operations related to offices

### Available Operations

* [get_office_metadata](#get_office_metadata) - Returns metadata about a NWS forecast office
* [get_office_headline](#get_office_headline) - Returns a specific news headline for a given NWS office
* [list_office_headlines](#list_office_headlines) - Returns a list of news headlines for a given NWS office

## get_office_metadata

Returns metadata about a NWS forecast office

### Example Usage

```python
from nws_api_client import NwsClient, models
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.offices.get_office_metadata(office_id=models.NWSOfficeID.NWS)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `office_id`                                                         | [models.NWSOfficeID](../../models/nwsofficeid.md)                   | :heavy_check_mark:                                                  | NWS office ID                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetOfficeMetadataResponse](../../models/getofficemetadataresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_office_headline

Returns a specific news headline for a given NWS office

### Example Usage

```python
from nws_api_client import NwsClient, models
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.offices.get_office_headline(office_id=models.NWSOfficeID.MKX, headline_id="<id>")

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

**[models.GetOfficeHeadlineResponse](../../models/getofficeheadlineresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_office_headlines

Returns a list of news headlines for a given NWS office

### Example Usage

```python
from nws_api_client import NwsClient, models
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.offices.list_office_headlines(office_id=models.NWSOfficeID.HPA)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `office_id`                                                         | [models.NWSOfficeID](../../models/nwsofficeid.md)                   | :heavy_check_mark:                                                  | NWS office ID                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListOfficeHeadlinesResponse](../../models/listofficeheadlinesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |