"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from nws_api_client.types import BaseModel
from typing import Dict, Optional
from typing_extensions import NotRequired, TypedDict


class AlertsActiveCountTypedDict(TypedDict):
    r"""A data structure showing the counts of active alerts broken down by various categories"""

    areas: NotRequired[Dict[str, int]]
    r"""Active alerts by area (state/territory)"""
    land: NotRequired[int]
    r"""The total number of active alerts affecting land zones"""
    marine: NotRequired[int]
    r"""The total number of active alerts affecting marine zones"""
    regions: NotRequired[Dict[str, int]]
    r"""Active alerts by marine region"""
    total: NotRequired[int]
    r"""The total number of active alerts"""
    zones: NotRequired[Dict[str, int]]
    r"""Active alerts by NWS public zone or county code"""


class AlertsActiveCount(BaseModel):
    r"""A data structure showing the counts of active alerts broken down by various categories"""

    areas: Optional[Dict[str, int]] = None
    r"""Active alerts by area (state/territory)"""

    land: Optional[int] = None
    r"""The total number of active alerts affecting land zones"""

    marine: Optional[int] = None
    r"""The total number of active alerts affecting marine zones"""

    regions: Optional[Dict[str, int]] = None
    r"""Active alerts by marine region"""

    total: Optional[int] = None
    r"""The total number of active alerts"""

    zones: Optional[Dict[str, int]] = None
    r"""Active alerts by NWS public zone or county code"""
