from typing import Any
from fastapi import APIRouter
from business.plateBusiness import PlateBusiness
from models.responses.plateResponseModel import PlateResponseModel, PlatesResponseModel
from models.requests.insertPlateRequestModel import InsertPlateRequestModel
from models.baseModel import Message
from mappers.mapToDto.plateDtoMapper import *


router = APIRouter()

# def read_items(
#     session: SessionDep, current_user: CurrentUser, skip: int = 0, limit: int = 100
# ) -> Any:


@router.get("/", response_model=list[PlatesResponseModel])
def read_items(skip: int = 0, limit: int = 100) -> PlatesResponseModel:
    """
    Retrieve items.
    """
    return PlatesResponseModel(data=[], count=0)


@router.get("/{id}", response_model=PlateResponseModel)
def read_item(id: str) -> PlateResponseModel:
    """
    Get item by ID.
    """
    return PlateBusiness.getPlateById(id)


@router.post("/", response_model=PlateResponseModel)
def create_item(model: InsertPlateRequestModel) -> PlateResponseModel:
    """
    Create new item.
    """
    # return PlateBusiness.postPlate(model.MapToCreateDtoExt())
    return PlateBusiness.postPlate(model.MapToCreateDto())


@router.put("/{id}", response_model=PlateResponseModel)
def update_item(*, id: int, model: PlateResponseModel) -> Any:
    """
    Update an item.
    """
    return PlateResponseModel()


@router.delete("/{id}")
def delete_item(id: int) -> Message:
    """
    Delete an item.
    """
    return Message(message="Item deleted successfully")


# items = {"foo": "The Foo Wrestlers"}


# @app.get("/items/{item_id}")
# async def read_item(item_id: str):
#     if item_id not in items:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return {"item": items[item_id]}


# @app.get("/items-header/{item_id}")
# async def read_item_header(item_id: str):
#     if item_id not in items:
#         raise HTTPException(
#             status_code=404,
#             detail="Item not found",
#             headers={"X-Error": "There goes my error"},
#         )
#     return {"item": items[item_id]}
