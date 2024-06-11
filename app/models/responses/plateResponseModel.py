from pydantic import BaseModel


class PlateResponseModel(BaseModel):
    id: str
    plateString: str
    fullName: str | None = None


class PlatesResponseModel(BaseModel):
    data: list[PlateResponseModel]
    count: int
