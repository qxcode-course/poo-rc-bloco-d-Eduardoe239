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

    def toogleFavorites(self):
        self.__favorited = not self.__favorited
    
    def __str__(self):
        favorited = "@" if self.__favorited else "-"
        list_fones = ", ".join(str(x) for x in self.__fones)
        return f"{favorited} {self.__name} [{list_fones}]"

def main():
    ctt = None

    while True:
        line = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(ctt)
        elif args[0] == "init":
            ctt = Contat(args[1])
        elif args[0] == "add":
            id = args[1]
            number = args[2]
            ctt.addFone(id, number)
        elif args[0] == "rm":
            rm = int(args[1])
            ctt.rmFone(rm)

        elif args[0] == "tfav":
            ctt.toogleFavorites()

        else:
            print("fail: comando invalido!")
main()

