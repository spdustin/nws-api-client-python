"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from nws_api_client.types import BaseModel, Nullable, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GridpointQuantitativeValueLayerValueTypedDict(TypedDict):
    valid_time: str
    r"""A time interval in ISO 8601 format. This can be one of:
    1. Start and end time
    2. Start time and duration
    3. Duration and end time
    The string \"NOW\" can also be used in place of a start/end time.

    """
    value: Nullable[float]


class GridpointQuantitativeValueLayerValue(BaseModel):
    valid_time: Annotated[str, pydantic.Field(alias="validTime")]
    r"""A time interval in ISO 8601 format. This can be one of:
    1. Start and end time
    2. Start time and duration
    3. Duration and end time
    The string \"NOW\" can also be used in place of a start/end time.

    """

    value: Nullable[float]

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["value"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


class GridpointQuantitativeValueLayerTypedDict(TypedDict):
    r"""A gridpoint layer consisting of quantitative values (numeric values with associated units of measure)."""

    values: List[GridpointQuantitativeValueLayerValueTypedDict]
    uom: NotRequired[str]
    r"""A string denoting a unit of measure, expressed in the format \"{unit}\" or \"{namespace}:{unit}\". Units with the namespace \"wmo\" or \"wmoUnit\" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace \"nwsUnit\" are currently custom and do not align to any standard. Units with no namespace or the namespace \"uc\" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future.

    """


class GridpointQuantitativeValueLayer(BaseModel):
    r"""A gridpoint layer consisting of quantitative values (numeric values with associated units of measure)."""

    values: List[GridpointQuantitativeValueLayerValue]

    uom: Optional[str] = None
    r"""A string denoting a unit of measure, expressed in the format \"{unit}\" or \"{namespace}:{unit}\". Units with the namespace \"wmo\" or \"wmoUnit\" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace \"nwsUnit\" are currently custom and do not align to any standard. Units with no namespace or the namespace \"uc\" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future.

    """
