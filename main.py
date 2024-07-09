import uvicorn
from typing import Optional
from fastapi import FastAPI, Request
from database.city import CityDatabase
from database.models import NewStation
from database.street import StreetDatabase
from database.station import StationDatabase
from fastapi.responses import JSONResponse

app = FastAPI(
    title="STO",
    description="STO",
    version="1.0.0"
)

@app.exception_handler(Exception)
async def validation_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=400,
        content={
            "message": (
                f"Failed method {request.method} at URL {request.url}."
                f" Exception message is {exc!r}."
            )
        },
    )

cityDB = CityDatabase()
streetDB = StreetDatabase()
stationDB = StationDatabase()


@app.get("/city")       #получение всех городов из базы
async def root():
    return {'data': cityDB.select()}


@app.get("/city/street/{city_id}")      #получение всех улиц города по city_id
async def street(city_id: int):
    return {'data': streetDB.select(city_id)}


@app.post("/shop")      #создание магазина
async def add_shop(data: NewStation):
    return {'data': stationDB.insert(data)}


@app.get("/shop/")      #получение списка магазина по параметрам
async def shop(
        street: Optional[str] = None,
        city: Optional[str] = None,
        open: Optional[int] = None
):
    data = {'namestr': street, 'namecity': city, 'is_open': open }
    return {'data': stationDB.select(data)}



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001, log_level="info")
