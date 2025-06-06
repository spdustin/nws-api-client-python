"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from nws_api_client.models.components import (
    zoneforecast as components_zoneforecast,
    zoneforecastgeojson as components_zoneforecastgeojson,
)
from nws_api_client.types import BaseModel
from nws_api_client.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing import Dict, List, Union
from typing_extensions import Annotated, TypeAliasType, TypedDict


class GetZoneForecastRequestTypedDict(TypedDict):
    type: str
    r"""Zone type"""
    zone_id: str
    r"""NWS public zone/county identifier"""


class GetZoneForecastRequest(BaseModel):
    type: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Zone type"""

    zone_id: Annotated[
        str,
        pydantic.Field(alias="zoneId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""NWS public zone/county identifier"""


GetZoneForecastResponseResultTypedDict = TypeAliasType(
    "GetZoneForecastResponseResultTypedDict",
    Union[
        components_zoneforecast.ZoneForecastTypedDict,
        components_zoneforecastgeojson.ZoneForecastGeoJSONTypedDict,
    ],
)


GetZoneForecastResponseResult = TypeAliasType(
    "GetZoneForecastResponseResult",
    Union[
        components_zoneforecast.ZoneForecast,
        components_zoneforecastgeojson.ZoneForecastGeoJSON,
    ],
)


class GetZoneForecastResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: GetZoneForecastResponseResultTypedDict


class GetZoneForecastResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: GetZoneForecastResponseResult
