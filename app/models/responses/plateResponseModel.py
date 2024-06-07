from pydantic import BaseModel


class PlateResponseModel(BaseModel):
    id: str
    plateString: str
