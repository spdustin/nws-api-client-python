"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from nws_api_client.models.components import (
    alertcertainty as components_alertcertainty,
    alertcollectiongeojson as components_alertcollectiongeojson,
    alertcollectionjsonld as components_alertcollectionjsonld,
    alertmessagetype_parameter as components_alertmessagetype_parameter,
    alertregiontype as components_alertregiontype,
    alertseverity as components_alertseverity,
    alertstatus_parameter as components_alertstatus_parameter,
    alerturgency as components_alerturgency,
    areacode as components_areacode,
    marineregioncode as components_marineregioncode,
)
from nws_api_client.types import BaseModel
from nws_api_client.utils import FieldMetadata, QueryParamMetadata
from typing import Dict, List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class GetActiveAlertsRequestTypedDict(TypedDict):
    status: NotRequired[List[components_alertstatus_parameter.AlertStatusParameter]]
    r"""Status (actual, exercise, system, test, draft)"""
    message_type: NotRequired[
        List[components_alertmessagetype_parameter.AlertMessageTypeParameter]
    ]
    r"""Message type (alert, update, cancel)"""
    event: NotRequired[List[str]]
    r"""Event name"""
    code: NotRequired[List[str]]
    r"""Event code"""
    area: NotRequired[List[components_areacode.AreaCode]]
    r"""State/territory code or marine area code This parameter is incompatible with the following parameters: point, region, region_type, zone"""
    point: NotRequired[str]
    r"""Point (latitude,longitude) This parameter is incompatible with the following parameters: area, region, region_type, zone"""
    region: NotRequired[List[components_marineregioncode.MarineRegionCode]]
    r"""Marine region code This parameter is incompatible with the following parameters: area, point, region_type, zone"""
    region_type: NotRequired[components_alertregiontype.AlertRegionType]
    r"""Region type (land or marine) This parameter is incompatible with the following parameters: area, point, region, zone"""
    zone: NotRequired[List[str]]
    r"""Zone ID (forecast or county) This parameter is incompatible with the following parameters: area, point, region, region_type"""
    urgency: NotRequired[List[components_alerturgency.AlertUrgency]]
    r"""Urgency (immediate, expected, future, past, unknown)"""
    severity: NotRequired[List[components_alertseverity.AlertSeverity]]
    r"""Severity (extreme, severe, moderate, minor, unknown)"""
    certainty: NotRequired[List[components_alertcertainty.AlertCertainty]]
    r"""Certainty (observed, likely, possible, unlikely, unknown)"""
    limit: NotRequired[int]
    r"""Limit"""


class GetActiveAlertsRequest(BaseModel):
    status: Annotated[
        Optional[List[components_alertstatus_parameter.AlertStatusParameter]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""Status (actual, exercise, system, test, draft)"""

    message_type: Annotated[
        Optional[List[components_alertmessagetype_parameter.AlertMessageTypeParameter]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""Message type (alert, update, cancel)"""

    event: Annotated[
        Optional[List[str]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""Event name"""

    code: Annotated[
        Optional[List[str]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""Event code"""

    area: Annotated[
        Optional[List[components_areacode.AreaCode]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""State/territory code or marine area code This parameter is incompatible with the following parameters: point, region, region_type, zone"""

    point: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Point (latitude,longitude) This parameter is incompatible with the following parameters: area, region, region_type, zone"""

    region: Annotated[
        Optional[List[components_marineregioncode.MarineRegionCode]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""Marine region code This parameter is incompatible with the following parameters: area, point, region_type, zone"""

    region_type: Annotated[
        Optional[components_alertregiontype.AlertRegionType],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Region type (land or marine) This parameter is incompatible with the following parameters: area, point, region, zone"""

    zone: Annotated[
        Optional[List[str]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""Zone ID (forecast or county) This parameter is incompatible with the following parameters: area, point, region, region_type"""

    urgency: Annotated[
        Optional[List[components_alerturgency.AlertUrgency]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""Urgency (immediate, expected, future, past, unknown)"""

    severity: Annotated[
        Optional[List[components_alertseverity.AlertSeverity]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""Severity (extreme, severe, moderate, minor, unknown)"""

    certainty: Annotated[
        Optional[List[components_alertcertainty.AlertCertainty]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""Certainty (observed, likely, possible, unlikely, unknown)"""

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 500
    r"""Limit"""


GetActiveAlertsResponseResultTypedDict = TypeAliasType(
    "GetActiveAlertsResponseResultTypedDict",
    Union[
        components_alertcollectionjsonld.AlertCollectionJSONLdTypedDict,
        components_alertcollectiongeojson.AlertCollectionGeoJSONTypedDict,
    ],
)


GetActiveAlertsResponseResult = TypeAliasType(
    "GetActiveAlertsResponseResult",
    Union[
        components_alertcollectionjsonld.AlertCollectionJSONLd,
        components_alertcollectiongeojson.AlertCollectionGeoJSON,
    ],
)


class GetActiveAlertsResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: GetActiveAlertsResponseResultTypedDict


class GetActiveAlertsResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: GetActiveAlertsResponseResult
