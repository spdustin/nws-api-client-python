# GetRadarQueueMetadataRequest


## Fields

| Field                                     | Type                                      | Required                                  | Description                               | Example                                   |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| `host`                                    | *str*                                     | :heavy_check_mark:                        | LDM host                                  |                                           |
| `limit`                                   | *Optional[int]*                           | :heavy_minus_sign:                        | Record limit                              |                                           |
| `arrived`                                 | *Optional[str]*                           | :heavy_minus_sign:                        | Range for arrival time                    | 2007-03-01T13:00:00Z/2008-05-11T15:30:00Z |
| `created`                                 | *Optional[str]*                           | :heavy_minus_sign:                        | Range for creation time                   | 2007-03-01T13:00:00Z/2008-05-11T15:30:00Z |
| `published`                               | *Optional[str]*                           | :heavy_minus_sign:                        | Range for publish time                    | 2007-03-01T13:00:00Z/2008-05-11T15:30:00Z |
| `station`                                 | *Optional[str]*                           | :heavy_minus_sign:                        | Station identifier                        |                                           |
| `type`                                    | *Optional[str]*                           | :heavy_minus_sign:                        | Record type                               |                                           |
| `feed`                                    | *Optional[str]*                           | :heavy_minus_sign:                        | Originating product feed                  |                                           |
| `resolution`                              | *Optional[int]*                           | :heavy_minus_sign:                        | Resolution version                        |                                           |