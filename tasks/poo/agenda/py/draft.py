class Fone:
    def __init__(self, id, number):
        self._id = id
        self._number = number

    def isValid(self):
        valid_chars = "0123456789"
        for c in self._number:
            if c not in valid_chars:
                return False
        return True

    def getId(self):
        return self._id

    def getNumber(self):
        return self._number

    def __str__(self):
        return f"{self._id}:{self._number}"


class Contact:
    def __init__(self, name):
        self._name = name
        self._fones = []
        self._favorited = False

    def addFone(self, id, number):
        f = Fone(id, number)
        if f.isValid():
            self._fones.append(f)
        else:
            print("fail: invalid number")

    def rmFone(self, index):
        if index < 0 or index >= len(self._fones):
            print("fail: invalid index")
        else:
            new_fones = []
            for i in range(len(self._fones)):
                if i != index:
                    new_fones.append(self._fones[i])
            self._fones = new_fones
