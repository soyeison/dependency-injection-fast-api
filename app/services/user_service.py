from fastapi import Depends
from app.database.repositories.user_repository import UserRepository
from app.database.repositories.account_repository import AccountRepository
from app.exceptions.user_exception import UserAlreadyExistException

class UserService:
    def __init__(self, user_repository: UserRepository = Depends(UserRepository), account_repository: AccountRepository = Depends(AccountRepository)):
        print("Inicio el user service")
        self.user_repository = user_repository
        self.account_repository = account_repository

    def getAll(self, limit: int | None):
        print("limit:", limit)
        raise UserAlreadyExistException("El usuario no existe")
        print("Paso con el user service")
        print("Acocunt repository:",self.account_repository.getAll())
        print("User respository:",self.user_repository.getAll(limit=limit))
        return True