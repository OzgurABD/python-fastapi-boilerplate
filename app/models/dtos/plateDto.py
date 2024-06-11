from pydantic import BaseModel


class CreatePlateDto(BaseModel):
    plateString: str
    fullName: str


class PlateDto(BaseModel):
    id: str
    plateString: str
    fullName: str
