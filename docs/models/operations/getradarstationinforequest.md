# GetRadarStationInfoRequest


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `station_id`                                           | *str*                                                  | :heavy_check_mark:                                     | Radar station ID                                       |
| `reporting_host`                                       | *Optional[str]*                                        | :heavy_minus_sign:                                     | Show RDA and latency info from specific reporting host |
| `host`                                                 | *Optional[str]*                                        | :heavy_minus_sign:                                     | Show latency info from specific LDM host               |