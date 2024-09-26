class UserRepository:
    def __init__(self):
        print("Inicio el user repository")
        self.users = [
            {
                "id": 1,
                "name": "Antonio",
                "age": 22
            },
            {
                "id": 2,
                "name": "Alfredo",
                "age": 25
            }
        ]

    def getAll(self, limit):
        print("Paso por el user repository")
        if limit is None:
            return self.users[:2]
        elif limit == 1:
            return self.users[0]
        else:
            return self.users[:limit]