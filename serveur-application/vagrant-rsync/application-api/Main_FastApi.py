import uvicorn
from fastapi import FastAPI, HTTPException, status, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

# Import models app
from Machine import MachineFastApi
import Crud_FastApi

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "Error": "Name field is missing"}),
    )


@app.get("/")
async def root():
    return {"message": "Hello welcome to my app python"}


@app.get("/machines")
async def read_machines():
    return Crud_FastApi.get_machines()


@app.get("/machine/{hostname}", response_model=MachineFastApi)
async def read_machine(hostname: str):
    if Crud_FastApi.is_exists_machine(hostname):
        return Crud_FastApi.get_machine(hostname)
    else:
        http_exception(400, "Machine not exists", "My Error")


@app.post("/machine/")
async def create_machine(machine: MachineFastApi):
    if Crud_FastApi.is_exists_machine(machine.hostname):
        http_exception(400, "Machine already  exists", "My Error")
    else:
        if Crud_FastApi.is_valid_ipv4_address(machine.ip):
            Crud_FastApi.create_machine(machine)
            return machine
        else:
            http_exception(400, "Address IP not valid", "My Error")


@app.put("/machine/{hostname}", response_model=MachineFastApi)
async def update_machine(hostname: str, machine: MachineFastApi):
    if Crud_FastApi.is_exists_machine(hostname):
        if Crud_FastApi.is_valid_ipv4_address(machine.ip):
            Crud_FastApi.update_machine(hostname, machine)
            return machine
        else:
            http_exception(400, "Address IP not valid", "My Error")
    else:
        http_exception(400, "Machine not exists", "My Error")


@app.delete("/machine/{hostname}")
async def delete_machine(hostname: str):
    if Crud_FastApi.is_exists_machine(hostname):
        Crud_FastApi.delete_machine(hostname)
    else:
        http_exception(400, "Machine not exists", "My Error")


def http_exception(code: int, detail_code: str, headers_message: str):
    raise HTTPException(
        status_code=code,
        detail=detail_code,
        headers={str(code)+"-Error": headers_message},
    )


uvicorn.run(app)
