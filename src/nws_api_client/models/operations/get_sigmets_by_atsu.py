"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from nws_api_client.models.components import (
    sigmetcollectiongeojson as components_sigmetcollectiongeojson,
)
from nws_api_client.types import BaseModel
from nws_api_client.utils import FieldMetadata, PathParamMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class GetSigmetsByAtsuRequestTypedDict(TypedDict):
    atsu: str
    r"""ATSU identifier"""


class GetSigmetsByAtsuRequest(BaseModel):
    atsu: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ATSU identifier"""


class GetSigmetsByAtsuResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: components_sigmetcollectiongeojson.SigmetCollectionGeoJSONTypedDict


class GetSigmetsByAtsuResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: components_sigmetcollectiongeojson.SigmetCollectionGeoJSON
