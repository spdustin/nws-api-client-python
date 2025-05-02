<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from nws_api_client import NwsClient
import os


with NwsClient(
    user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
) as nws_client:

    res = nws_client.alerts_query()

    assert res is not None

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from nws_api_client import NwsClient
import os

async def main():

    async with NwsClient(
        user_agent=os.getenv("NWSCLIENT_USER_AGENT", ""),
    ) as nws_client:

        res = await nws_client.alerts_query_async()

        assert res is not None

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->