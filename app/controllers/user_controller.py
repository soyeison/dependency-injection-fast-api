from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from app.services.user_service import UserService
from app.exceptions.base_exception_class import ServiceException
from app.exceptions.user_exception import UserAlreadyExistException

class UserController:
    def __init__(self, ):
        self.router = APIRouter()
        self._add_routes()

    def _add_routes(self):
        self.router.get("/")(self.get_all)

    def get_all(self, limit: int | None = None, user_service: UserService = Depends(UserService)):
        try:
            print("limit:", limit)
            raise UserAlreadyExistException("El usuario no existe")
            users = user_service.getAll(limit=limit)
            # encriptar datos
            return JSONResponse(content={"message": "Todos los usuarios"}, status_code=200)
        except Exception as e:
            raise ServiceException(str(e))