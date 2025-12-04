class Fone:
    def __init__(self, id: str, number: str):
        self.__id = id
        self.__number = number

    def isValid(self):
        valid = "0123456789()."
        return all(c in valid for c in self.__number)

    def __str__(self):
        return f"{self.__id}:{self.__number}"


class Contat:
    def __init__(self, name: str):
        self.__name = name
        self.__fones: list[Fone] = []
        self.__favorited = False

    def addFone(self, id: str, number: str):
        f = Fone(id, number)
        if not f.isValid():
            print("fail: invalid number")
            return
        self.__fones.append(f)

    def rmFone(self, index: int):
        if index < 0 or index >= len(self.__fones):
            print("fail: indice invalido")
            return
        self.__fones.pop(index)




