from typing import Callable
from fastapi import Request
from fastapi.responses import JSONResponse
from app.exceptions.base_exception_class import BaseApiException

def create_handler_exception(
        status_code: str, initial_detail: str
) -> Callable[[Request, BaseApiException], JSONResponse]:
    detail = {"message": initial_detail}

    async def excpetion_handler(_: Request, exc: BaseApiException) -> JSONResponse:
        if exc.message:
            detail["message"] = exc.message

        if exc.name:
            detail["message"] = f"{detail['message']} [{exc.name}]"

        return JSONResponse(content={"detail": detail["message"]}, status_code=status_code)
    
    return excpetion_handler