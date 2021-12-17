from typing import Generic, TypeVar, Optional, List

from pydantic import Field
from pydantic.generics import GenericModel


T = TypeVar("T")


class Response(GenericModel, Generic[T]):
    code: int = Field(0, example=0)
    message: str = Field('', example='')
    data: Optional[T]


class PageData(GenericModel, Generic[T]):
    skip: int = Field(0, example=0)
    limit: int = Field(0, example=10)
    total: int = Field(0, example=10)
    has_more: bool = Field(False, example=False)
    data: List[T] = Field([])
