"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from nws_api_client.types import BaseModel
from typing import Any, List, Union
from typing_extensions import TypeAliasType, TypedDict


class JSONLdContextTypedDict(TypedDict):
    pass


class JSONLdContext(BaseModel):
    pass


JSONLdContextUnionTypedDict = TypeAliasType(
    "JSONLdContextUnionTypedDict", Union[JSONLdContextTypedDict, List[Any]]
)


JSONLdContextUnion = TypeAliasType(
    "JSONLdContextUnion", Union[JSONLdContext, List[Any]]
)
