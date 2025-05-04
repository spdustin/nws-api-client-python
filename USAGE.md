<!-- Start SDK Example Usage [usage] -->
### Text Products

Get your local NWS office's Area Forecast Discussion

```python
# Synchronous Example
from nws_api_client import NwsAPIClient
import os


with NwsAPIClient(
    user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
) as nac_client:

    res = nac_client.products.get_available(type_id="AFD", location_id="LOT")

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from nws_api_client import NwsAPIClient
import os

async def main():

    async with NwsAPIClient(
        user_agent=os.getenv("NWS_API_CLIENT_USER_AGENT", ""),
    ) as nac_client:

        res = await nac_client.products.get_available_async(type_id="AFD", location_id="LOT")

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->