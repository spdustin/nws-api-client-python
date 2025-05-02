# ListObservationsByZoneRequest


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `zone_id`                                                            | *str*                                                                | :heavy_check_mark:                                                   | NWS public zone/county identifier                                    |
| `start`                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | Start date/time                                                      |
| `end`                                                                | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | End date/time                                                        |
| `limit`                                                              | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | Limit                                                                |