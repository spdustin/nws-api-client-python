"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from nws_api_client.models.components import glossary as components_glossary
from nws_api_client.types import BaseModel
from typing import Dict, List
from typing_extensions import TypedDict


class GetGlossaryTermsResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: components_glossary.GlossaryTypedDict


class GetGlossaryTermsResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: components_glossary.Glossary
