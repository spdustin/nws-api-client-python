"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .nwscenterweatherserviceunitid import NWSCenterWeatherServiceUnitID
from datetime import datetime
from nws_api_client.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CenterWeatherAdvisoryTypedDict(TypedDict):
    cwsu: NotRequired[NWSCenterWeatherServiceUnitID]
    r"""Three-letter identifier for a Center Weather Service Unit (CWSU)."""
    end: NotRequired[datetime]
    id: NotRequired[str]
    issue_time: NotRequired[datetime]
    observed_property: NotRequired[str]
    sequence: NotRequired[int]
    start: NotRequired[datetime]
    text: NotRequired[str]


class CenterWeatherAdvisory(BaseModel):
    cwsu: Optional[NWSCenterWeatherServiceUnitID] = None
    r"""Three-letter identifier for a Center Weather Service Unit (CWSU)."""

    end: Optional[datetime] = None

    id: Optional[str] = None

    issue_time: Annotated[Optional[datetime], pydantic.Field(alias="issueTime")] = None

    observed_property: Annotated[
        Optional[str], pydantic.Field(alias="observedProperty")
    ] = None

    sequence: Optional[int] = None

    start: Optional[datetime] = None

    text: Optional[str] = None
