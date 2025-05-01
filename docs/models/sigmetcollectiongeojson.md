# SigmetCollectionGeoJSON

A GeoJSON feature collection. Please refer to IETF RFC 7946 for information on the GeoJSON format.


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `at_context`                                                                   | [Optional[models.JSONLdContextUnion]](../models/jsonldcontextunion.md)         | :heavy_minus_sign:                                                             | N/A                                                                            |
| `type`                                                                         | [models.SigmetCollectionGeoJSONType](../models/sigmetcollectiongeojsontype.md) | :heavy_check_mark:                                                             | N/A                                                                            |
| `features`                                                                     | List[[models.SigmetGeoJSON](../models/sigmetgeojson.md)]                       | :heavy_check_mark:                                                             | N/A                                                                            |