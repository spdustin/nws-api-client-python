# ListRadarStationsRequest


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `station_type`                                         | List[*str*]                                            | :heavy_minus_sign:                                     | Limit results to a specific station type or types      |
| `reporting_host`                                       | *Optional[str]*                                        | :heavy_minus_sign:                                     | Show RDA and latency info from specific reporting host |
| `host`                                                 | *Optional[str]*                                        | :heavy_minus_sign:                                     | Show latency info from specific LDM host               |