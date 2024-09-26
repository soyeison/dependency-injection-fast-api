class BaseApiException(Exception):

    def __init__(self, message: str = "Service is unavailable", name: str = "MasCapital"):
        self.message = message
        self.name = name
        super().__init__(self.message, self.name)

class ServiceException(BaseApiException):
    pass