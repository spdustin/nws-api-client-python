# AlertsActiveCountResponseBody

A data structure showing the counts of active alerts broken down by various categories


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `total`                                                  | *Optional[int]*                                          | :heavy_minus_sign:                                       | The total number of active alerts                        |
| `land`                                                   | *Optional[int]*                                          | :heavy_minus_sign:                                       | The total number of active alerts affecting land zones   |
| `marine`                                                 | *Optional[int]*                                          | :heavy_minus_sign:                                       | The total number of active alerts affecting marine zones |
| `regions`                                                | Dict[str, *int*]                                         | :heavy_minus_sign:                                       | Active alerts by marine region                           |
| `areas`                                                  | Dict[str, *int*]                                         | :heavy_minus_sign:                                       | Active alerts by area (state/territory)                  |
| `zones`                                                  | Dict[str, *int*]                                         | :heavy_minus_sign:                                       | Active alerts by NWS public zone or county code          |