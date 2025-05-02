# ListObservationsByStationRequest


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `station_id`                                                         | *str*                                                                | :heavy_check_mark:                                                   | Observation station ID                                               |
| `start`                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | Start time                                                           |
| `end`                                                                | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | End time                                                             |
| `limit`                                                              | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | Limit                                                                |