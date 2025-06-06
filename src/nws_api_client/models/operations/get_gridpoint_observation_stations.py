"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from nws_api_client.models.components import (
    nwsforecastofficeid as components_nwsforecastofficeid,
    observationstationcollectiongeojson as components_observationstationcollectiongeojson,
    observationstationcollectionjsonld as components_observationstationcollectionjsonld,
)
from nws_api_client.types import BaseModel
from nws_api_client.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
from typing import Dict, List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class GetGridpointObservationStationsRequestTypedDict(TypedDict):
    wfo: components_nwsforecastofficeid.NWSForecastOfficeID
    r"""Forecast office ID"""
    gridpoint: str
    r"""Forecast gridpoint pair(see https://weather-gov.github.io/api/gridpoints for more info)"""
    limit: NotRequired[int]
    r"""Limit"""
    cursor: NotRequired[str]
    r"""Pagination cursor"""


class GetGridpointObservationStationsRequest(BaseModel):
    wfo: Annotated[
        components_nwsforecastofficeid.NWSForecastOfficeID,
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Forecast office ID"""

    gridpoint: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Forecast gridpoint pair(see https://weather-gov.github.io/api/gridpoints for more info)"""

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 500
    r"""Limit"""

    cursor: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Pagination cursor"""


GetGridpointObservationStationsResponseResultTypedDict = TypeAliasType(
    "GetGridpointObservationStationsResponseResultTypedDict",
    Union[
        components_observationstationcollectionjsonld.ObservationStationCollectionJSONLdTypedDict,
        components_observationstationcollectiongeojson.ObservationStationCollectionGeoJSONTypedDict,
    ],
)


GetGridpointObservationStationsResponseResult = TypeAliasType(
    "GetGridpointObservationStationsResponseResult",
    Union[
        components_observationstationcollectionjsonld.ObservationStationCollectionJSONLd,
        components_observationstationcollectiongeojson.ObservationStationCollectionGeoJSON,
    ],
)


class GetGridpointObservationStationsResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: GetGridpointObservationStationsResponseResultTypedDict


class GetGridpointObservationStationsResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: GetGridpointObservationStationsResponseResult
