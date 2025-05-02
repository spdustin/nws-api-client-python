# Points
(*points*)

## Overview

Operations related to geographic points (lat,lon)

### Available Operations

* [get_metadata](#get_metadata) - Returns metadata about a given latitude/longitude point

## get_metadata

Returns metadata about a given latitude/longitude point

### Example Usage

```python
from nws_api_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.points.get_metadata(point="<value>")

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

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.NotFoundError         | 404                          | application/json             |
| errors.UnauthorizedError     | 401, 403, 407                | application/json             |
| errors.TimeoutErrorT         | 408                          | application/json             |
| errors.RateLimitedError      | 429                          | application/json             |
| errors.BadRequestError       | 400, 413, 414, 415, 422, 431 | application/json             |
| errors.TimeoutErrorT         | 504                          | application/json             |
| errors.NotFoundError         | 501, 505                     | application/json             |
| errors.InternalServerError   | 500, 502, 503, 506, 507, 508 | application/json             |
| errors.BadRequestError       | 510                          | application/json             |
| errors.UnauthorizedError     | 511                          | application/json             |
| errors.APIError              | 4XX, 5XX                     | \*/\*                        |