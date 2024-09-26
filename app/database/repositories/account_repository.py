class AccountRepository:
    def __init__(self) -> None:
        print("Inicio el account repository")
        self.accounts = []

    def getAll(self):
        print("Paso por el account repository")
        return self.accounts