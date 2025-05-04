# GetProductsRequest


## Fields

| Field              | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `location`         | List[*str*]        | :heavy_minus_sign: | Location id        |                    |
| `start`            | *Optional[str]*    | :heavy_minus_sign: | Start time         | 0419               |
| `end`              | *Optional[str]*    | :heavy_minus_sign: | End time           | 0419               |
| `office`           | List[*str*]        | :heavy_minus_sign: | Issuing office     |                    |
| `wmoid`            | List[*str*]        | :heavy_minus_sign: | WMO id code        |                    |
| `type`             | List[*str*]        | :heavy_minus_sign: | Product code       |                    |
| `limit`            | *Optional[int]*    | :heavy_minus_sign: | Limit              |                    |