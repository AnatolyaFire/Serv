from pydantic import BaseModel


class NewStation(BaseModel):
    namestaiton: str
    nhouse: int
    timeopen: int
    timeclose: int
    idstr: int

