from models.exception_not_found_model import NotFound
from fastapi.requests import Request
from fastapi.responses import JSONResponse

async def not_found_exception_handler(request: Request, exc: NotFound):
    return JSONResponse(
        status_code=404,
        content={"message": f"Oops! {exc.nome} não foi encontrado(a)..."},
    )