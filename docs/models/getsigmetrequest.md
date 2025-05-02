# GetSigmetRequest


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `atsu`                                                                       | *str*                                                                        | :heavy_check_mark:                                                           | ATSU identifier                                                              |
| `date_`                                                                      | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) | :heavy_check_mark:                                                           | Date (YYYY-MM-DD format)                                                     |
| `time`                                                                       | *str*                                                                        | :heavy_check_mark:                                                           | Time (HHMM format). This time is always specified in UTC (Zulu) time.        |