# Points
(*points*)

## Overview

Operations related to geographic points (lat,lon)

### Available Operations

* [get_point_metadata](#get_point_metadata) - Returns metadata about a given latitude/longitude point

## get_point_metadata

Returns metadata about a given latitude/longitude point

### Example Usage

```python
from nws_api_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.points.get_point_metadata(point="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `point`                                                             | *str*                                                               | :heavy_check_mark:                                                  | Point (latitude, longitude)                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetPointMetadataResponse](../../models/getpointmetadataresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |