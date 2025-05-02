# GetGridpointRawForecastRequest


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `wfo`                                                          | [models.NWSForecastOfficeID](../models/nwsforecastofficeid.md) | :heavy_check_mark:                                             | Forecast office ID                                             |
| `point`                                                        | List[*int*]                                                    | :heavy_check_mark:                                             | Two-element array encoding grid X and Y (comma-separated)      |