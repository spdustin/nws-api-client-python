"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from nws_api_client.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
import pydantic
from pydantic import model_serializer
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class QualityControl(str, Enum):
    r"""For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml"""

    Z = "Z"
    C = "C"
    S = "S"
    V = "V"
    X = "X"
    Q = "Q"
    G = "G"
    B = "B"
    T = "T"


class QuantitativeValueTypedDict(TypedDict):
    r"""A structured value representing a measurement and its unit of measure. This object is a slighly modified version of the schema.org definition at https://schema.org/QuantitativeValue"""

    max_value: NotRequired[float]
    r"""The maximum value of a range of measured values"""
    min_value: NotRequired[float]
    r"""The minimum value of a range of measured values"""
    quality_control: NotRequired[QualityControl]
    r"""For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml"""
    unit_code: NotRequired[str]
    r"""A string denoting a unit of measure, expressed in the format \"{unit}\" or \"{namespace}:{unit}\". Units with the namespace \"wmo\" or \"wmoUnit\" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace \"nwsUnit\" are currently custom and do not align to any standard. Units with no namespace or the namespace \"uc\" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future.

    """
    value: NotRequired[Nullable[float]]
    r"""A measured value"""


class QuantitativeValue(BaseModel):
    r"""A structured value representing a measurement and its unit of measure. This object is a slighly modified version of the schema.org definition at https://schema.org/QuantitativeValue"""

    max_value: Annotated[Optional[float], pydantic.Field(alias="maxValue")] = None
    r"""The maximum value of a range of measured values"""

    min_value: Annotated[Optional[float], pydantic.Field(alias="minValue")] = None
    r"""The minimum value of a range of measured values"""

    quality_control: Annotated[
        Optional[QualityControl], pydantic.Field(alias="qualityControl")
    ] = None
    r"""For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml"""

    unit_code: Annotated[Optional[str], pydantic.Field(alias="unitCode")] = None
    r"""A string denoting a unit of measure, expressed in the format \"{unit}\" or \"{namespace}:{unit}\". Units with the namespace \"wmo\" or \"wmoUnit\" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace \"nwsUnit\" are currently custom and do not align to any standard. Units with no namespace or the namespace \"uc\" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future.

    """

    value: OptionalNullable[float] = UNSET
    r"""A measured value"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "maxValue",
            "minValue",
            "qualityControl",
            "unitCode",
            "value",
        ]
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
