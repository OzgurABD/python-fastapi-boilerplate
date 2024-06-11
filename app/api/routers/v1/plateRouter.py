from typing import Any
from fastapi import APIRouter, Depends
from business.plateBusiness import PlateBusiness
from models.responses.plateResponseModel import PlateResponseModel, PlatesResponseModel
from models.requests.insertPlateRequestModel import InsertPlateRequestModel
from models.baseModel import Message
from mappers.mapToDto.plateDtoMapper import *


router = APIRouter()

# def read_items(
#     session: SessionDep, current_user: CurrentUser, skip: int = 0, limit: int = 100
# ) -> Any:


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@router.get("/check")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons


@router.get("/", response_model=list[PlatesResponseModel])
async def read_items(skip: int = 0, limit: int = 100) -> PlatesResponseModel:
    """
    Retrieve items.
    """
    return PlatesResponseModel(data=[], count=0)


@router.get("/{id}", response_model=PlateResponseModel)
async def read_item(id: str) -> PlateResponseModel:
    """
    Get item by ID.
    """
    return PlateBusiness.getPlateById(id)


@router.post("/", response_model=PlateResponseModel)
async def create_item(model: InsertPlateRequestModel) -> PlateResponseModel:
    """
    Create new item.
    """
    # TODO MapToCreateDtoExt alternatives to MapToCreateDto, The method (MapToCreateDto) is located in the class it depends on.
    # return PlateBusiness.postPlate(model.MapToCreateDtoExt())
    return PlateBusiness.postPlate(model.MapToCreateDto())


@router.put("/{id}", response_model=PlateResponseModel)
async def update_item(*, id: int, model: PlateResponseModel) -> Any:
    """
    Update an item.
    """
    return PlateResponseModel()


@router.delete("/{id}")
async def delete_item(id: int) -> Message:
    """
    Delete an item.
    """
    return Message(message="Item deleted successfully")
