from typing import Generic, Optional
from annotated_types import T
from pydantic import BaseModel


class ServiceResult(BaseModel, Generic[T]):
    isSuccess: bool
    data: Optional[T] | None = None


class ServicePaginationResult(ServiceResult):
    total: int | None = None
    pages: int | None = None
    page: int | None = None
    size: int | None = None
