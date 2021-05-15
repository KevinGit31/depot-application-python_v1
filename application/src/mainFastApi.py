import uvicorn
from fastapi import FastAPI, HTTPException, status, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

# Import app
from Machine import MachineFastApi
import crudFastApi

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
    """
        API qui va permettre d'afficher la liste des machines du parc informatique
    :return: liste de machines
    """
    return crudFastApi.get_machines()


@app.get("/machine/{hostname}", response_model=MachineFastApi)
async def read_machine(hostname: str):
    """
        API qui va permettre d'afficher une machine par son hostname
     :param hostname: on récupère l'hostname saisi par l'utilisateur
    :return: machine
    """
    if crudFastApi.is_exists_machine(hostname):
        return crudFastApi.get_machine(hostname)
    else:
        http_exception(400, "Machine not exists", "My Error")


@app.post("/machine/")
async def create_machine(machine: MachineFastApi):
    """
        API permettant de créer une nouvelle
     :param machine: on récupère la machine saisie par l'utilisateur
    :return: machine
    """
    if crudFastApi.is_exists_machine(machine.hostname):
        http_exception(400, "Machine already exists", "My Error")
    else:
        if crudFastApi.is_valid_ipv4_address(machine.ip):
            crudFastApi.create_machine(machine)
            return machine
        else:
            http_exception(400, "Address IP not valid", "My Error")


@app.put("/machine/{hostname}", response_model=MachineFastApi)
async def update_machine(hostname: str, machine: MachineFastApi):
    """
        API permettant la mise à jour d'une machine existante à l'aide de son hostname
    :param hostname: nom de la machine sur laquelle on va faire les modifications
    :param machine: nouvelle machine
    :return:
    """
    if crudFastApi.is_exists_machine(hostname):
        if crudFastApi.is_valid_ipv4_address(machine.ip):
            crudFastApi.update_machine(hostname, machine)
            return machine
        else:
            http_exception(400, "Address IP not valid", "My Error")
    else:
        http_exception(400, "Machine not exists", "My Error")


@app.delete("/machine/{hostname}")
async def delete_machine(hostname: str):
    """
        API permettant la suppression d'une machine à l'aide de son hostname
    :param hostname: nom de la machine
    :return:
    """
    if crudFastApi.is_exists_machine(hostname):
        crudFastApi.delete_machine(hostname)
    else:
        http_exception(400, "Machine not exists", "My Error")


def http_exception(code: int, detail_code: str, headers_message: str):
    """
        Méthode permettant d'afficher les exceptions HTTP
    :param code: code d'erreur
    :param detail_code: detail code
    :param headers_message: headers message
    :return:
    """
    raise HTTPException(
        status_code=code,
        detail=detail_code,
        headers={str(code)+"-Error": headers_message},
    )


"""
    Démarrage de l'application
"""
uvicorn.run(app)
