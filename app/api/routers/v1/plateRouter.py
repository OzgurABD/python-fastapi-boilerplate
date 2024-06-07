from typing import Any
from fastapi import APIRouter
from models.plate import ItemPlate, ItemsPlate, Message

# from app.business.plateBusiness import getPlateById

router = APIRouter()

# def read_items(
#     session: SessionDep, current_user: CurrentUser, skip: int = 0, limit: int = 100
# ) -> Any:


@router.get("/", response_model=ItemsPlate)
def read_items(skip: int = 0, limit: int = 100) -> Any:
    """
    Retrieve items.
    """
    return ItemsPlate(data=[], count=0)


@router.get("/{id}", response_model=ItemPlate)
def read_item(id: int) -> ItemPlate:
    """
    Get item by ID.
    """
    # return getPlateById(id)
    return ItemPlate(id=id, plateString="test")


@router.post("/", response_model=ItemPlate)
def create_item(*, item_in: ItemsPlate) -> Any:
    """
    Create new item.
    """
    return ItemPlate()


@router.put("/{id}", response_model=ItemPlate)
def update_item(*, id: int, item_in: ItemsPlate) -> Any:
    """
    Update an item.
    """
    return ItemPlate()


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
