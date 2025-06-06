"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import date
from nws_api_client.models.components import sigmetgeojson as components_sigmetgeojson
from nws_api_client.types import BaseModel
from nws_api_client.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing import Dict, List, Union
from typing_extensions import Annotated, TypeAliasType, TypedDict


class GetSigmetRequestTypedDict(TypedDict):
    atsu: str
    r"""ATSU identifier"""
    date_: date
    r"""Date (YYYY-MM-DD format)"""
    time: str
    r"""Time (HHMM format). This time is always specified in UTC (Zulu) time."""


class GetSigmetRequest(BaseModel):
    atsu: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ATSU identifier"""

    date_: Annotated[
        date,
        pydantic.Field(alias="date"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Date (YYYY-MM-DD format)"""

    time: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Time (HHMM format). This time is always specified in UTC (Zulu) time."""


GetSigmetResponseResultTypedDict = TypeAliasType(
    "GetSigmetResponseResultTypedDict",
    Union[components_sigmetgeojson.SigmetGeoJSONTypedDict, bytes],
)


GetSigmetResponseResult = TypeAliasType(
    "GetSigmetResponseResult", Union[components_sigmetgeojson.SigmetGeoJSON, bytes]
)


class GetSigmetResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: GetSigmetResponseResultTypedDict


class GetSigmetResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: GetSigmetResponseResult
