# GetZoneMetadataRequest


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `type`                                                               | [models.NWSZoneType](../models/nwszonetype.md)                       | :heavy_check_mark:                                                   | Zone type                                                            |
| `zone_id`                                                            | *str*                                                                | :heavy_check_mark:                                                   | NWS public zone/county identifier                                    |
| `effective`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | Effective date/time                                                  |