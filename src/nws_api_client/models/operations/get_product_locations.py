"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from nws_api_client.models.components import (
    textproductlocationcollection as components_textproductlocationcollection,
)
from nws_api_client.types import BaseModel
from typing import Dict, List
from typing_extensions import TypedDict


class GetProductLocationsResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: (
        components_textproductlocationcollection.TextProductLocationCollectionTypedDict
    )


class GetProductLocationsResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: components_textproductlocationcollection.TextProductLocationCollection
