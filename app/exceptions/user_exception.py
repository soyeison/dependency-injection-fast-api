from app.exceptions.base_exception_class import BaseApiException

class UserAlreadyExistException(BaseApiException):
    """conflict detected, user already exist in database"""
    pass