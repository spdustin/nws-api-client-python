# AlertCollectionJSONLd


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `title`                                                                | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | A title describing the alert collection                                |
| `updated`                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects)   | :heavy_minus_sign:                                                     | The last time a change occurred to this collection                     |
| `pagination`                                                           | [Optional[models.PaginationInfo]](../models/paginationinfo.md)         | :heavy_minus_sign:                                                     | Links for retrieving more data from paged data sets                    |
| `at_context`                                                           | [Optional[models.JSONLdContextUnion]](../models/jsonldcontextunion.md) | :heavy_minus_sign:                                                     | N/A                                                                    |
| `at_graph`                                                             | List[[models.Alert](../models/alert.md)]                               | :heavy_minus_sign:                                                     | N/A                                                                    |