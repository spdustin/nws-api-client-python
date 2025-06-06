# GetObservationStationsRequest


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `id`                                                             | List[*str*]                                                      | :heavy_minus_sign:                                               | Filter by observation station ID                                 |
| `state`                                                          | List[[components.AreaCode](../../models/components/areacode.md)] | :heavy_minus_sign:                                               | Filter by state/marine area code                                 |
| `limit`                                                          | *Optional[int]*                                                  | :heavy_minus_sign:                                               | Limit                                                            |
| `cursor`                                                         | *Optional[str]*                                                  | :heavy_minus_sign:                                               | Pagination cursor                                                |