# Geocode

Lists of codes for NWS public zones and counties affected by the alert.


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `ugc`                                                                        | List[*str*]                                                                  | :heavy_minus_sign:                                                           | A list of NWS public zone or county identifiers.                             |
| `same`                                                                       | List[*str*]                                                                  | :heavy_minus_sign:                                                           | A list of SAME (Specific Area Message Encoding) codes for affected counties. |