"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from nws_api_client.types import BaseModel
from nws_api_client.utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import Any, Dict, List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class GetRadarStationsRequestTypedDict(TypedDict):
    station_type: NotRequired[List[str]]
    r"""Limit results to a specific station type or types"""
    reporting_host: NotRequired[str]
    r"""Show records from specific reporting host"""
    host: NotRequired[str]
    r"""Show latency info from specific LDM host"""


class GetRadarStationsRequest(BaseModel):
    station_type: Annotated[
        Optional[List[str]],
        pydantic.Field(alias="stationType"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""Limit results to a specific station type or types"""

    reporting_host: Annotated[
        Optional[str],
        pydantic.Field(alias="reportingHost"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Show records from specific reporting host"""

    host: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Show latency info from specific LDM host"""


GetRadarStationsResponseResultTypedDict = TypeAliasType(
    "GetRadarStationsResponseResultTypedDict", Union[Any, Any]
)


GetRadarStationsResponseResult = TypeAliasType(
    "GetRadarStationsResponseResult", Union[Any, Any]
)


class GetRadarStationsResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: GetRadarStationsResponseResultTypedDict


class GetRadarStationsResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: GetRadarStationsResponseResult
