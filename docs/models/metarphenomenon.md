# MetarPhenomenon

An object representing a decoded METAR phenomenon string.


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `in_vicinity`                                                                      | *Optional[bool]*                                                                   | :heavy_minus_sign:                                                                 | N/A                                                                                |
| `intensity`                                                                        | [Nullable[models.MetarPhenomenonIntensity]](../models/metarphenomenonintensity.md) | :heavy_check_mark:                                                                 | N/A                                                                                |
| `modifier`                                                                         | [Nullable[models.Modifier]](../models/modifier.md)                                 | :heavy_check_mark:                                                                 | N/A                                                                                |
| `raw_string`                                                                       | *str*                                                                              | :heavy_check_mark:                                                                 | N/A                                                                                |
| `weather`                                                                          | [models.MetarPhenomenonWeather](../models/metarphenomenonweather.md)               | :heavy_check_mark:                                                                 | N/A                                                                                |