"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .jsonldcontext_union import JSONLdContextUnion, JSONLdContextUnionTypedDict
from nws_api_client.types import BaseModel, Nullable
import pydantic
from typing import Dict, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class TextProductLocationCollectionTypedDict(TypedDict):
    at_context: NotRequired[JSONLdContextUnionTypedDict]
    locations: NotRequired[Dict[str, Nullable[str]]]


class TextProductLocationCollection(BaseModel):
    at_context: Annotated[
        Optional[JSONLdContextUnion], pydantic.Field(alias="@context")
    ] = None

    locations: Optional[Dict[str, Nullable[str]]] = None
