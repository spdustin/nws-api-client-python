# ZoneForecast

An object representing a zone area forecast.


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `at_context`                                                           | [Optional[models.JSONLdContextUnion]](../models/jsonldcontextunion.md) | :heavy_minus_sign:                                                     | N/A                                                                    |
| `geometry`                                                             | *OptionalNullable[str]*                                                | :heavy_minus_sign:                                                     | A geometry represented in Well-Known Text (WKT) format.                |
| `periods`                                                              | List[[models.Period](../models/period.md)]                             | :heavy_minus_sign:                                                     | An array of forecast periods.                                          |
| `updated`                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects)   | :heavy_minus_sign:                                                     | The time this zone forecast product was published.                     |
| `zone`                                                                 | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | An API link to the zone this forecast is for.                          |