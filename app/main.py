from fastapi import FastAPI, status
from app.controllers.user_controller import UserController
from app.exceptions.create_handler_exception import create_handler_exception
from app.exceptions.base_exception_class import ServiceException
from app.exceptions.user_exception import UserAlreadyExistException

app = FastAPI()

user_controller = UserController()

app.include_router(user_controller.router, prefix="/user", tags=["User"])

app.add_exception_handler(
    exc_class_or_status_code=UserAlreadyExistException,
    handler=create_handler_exception(
        status.HTTP_404_NOT_FOUND, "User don't exist"
    )
)

app.add_exception_handler(
    exc_class_or_status_code=ServiceException,
    handler=create_handler_exception(
        status.HTTP_500_INTERNAL_SERVER_ERROR, "A service seems to be down, try again later."
    )
)