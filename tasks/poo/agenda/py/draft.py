class Fone:
    def __init__(self, id, number):
        self._id = id
        self._number = number

    def isValid(self):
        return all(c.isdigit() for c in self._number)

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
            return
        self._fones.pop(index)

    def toggleFavorited(self):
        self._favorited = not self._favorited

    def isFavorited(self):
        return self._favorited

    def getFones(self):
        return self._fones

    def getName(self):
        return self._name

    def __str__(self):
        prefix = "@ " if self._favorited else "- "
        fones_str = ", ".join(str(f) for f in self._fones)
        return f"{prefix}{self._name} [{fones_str}]"


class Agenda:
    def __init__(self):
        self._contacts = []

    def findPosByName(self, name):
        for i, c in enumerate(self._contacts):
            if c.getName() == name:
                return i
        return -1

    def addContact(self, name, fones):
        pos = self.findPosByName(name)
        if pos != -1:
            cont = self._contacts[pos]
            for id_, num in fones:
                cont.addFone(id_, num)
        else:
            cont = Contact(name)
            for id_, num in fones:
                cont.addFone(id_, num)
            self._contacts.append(cont)
            self._contacts.sort(key=lambda c: c.getName())

    def getContact(self, name):
        pos = self.findPosByName(name)
        if pos == -1:
            return None
        return self._contacts[pos]

    def rmContact(self, name):
        pos = self.findPosByName(name)
        if pos != -1:
            self._contacts.pop(pos)

    def search(self, pattern):
        pat = pattern.lower()
        return [c for c in self._contacts if pat in str(c).lower()]

    def getFavorited(self):
        return [c for c in self._contacts if c.isFavorited()]

    def __str__(self):
        return "\n".join(str(c) for c in self._contacts)


def parse_fones(tokens):
    fones = []
    for t in tokens:
        if ":" in t:
            id_, num = t.split(":", 1)
            fones.append((id_, num))
    return fones


def main():
    agenda = Agenda()
    while True:
        try:
            line = input()
        except EOFError:
            break

        if not line:
            continue

        line = line.strip()
        if line == "":
            continue

        # imprime comando com $
        print(f"${line}")

        parts = line.split()

        if parts[0] == "add":
            name = parts[1]
            fones = parse_fones(parts[2:])
            agenda.addContact(name, fones)

        elif parts[0] == "show":
            print(agenda)

        elif parts[0] == "rmFone":
            if len(parts) != 3:
                print("fail: invalid command")
                continue
            name = parts[1]
            try:
                idx = int(parts[2])
            except:
                print("fail: invalid index")
                continue

            c = agenda.getContact(name)
            if c is None:
                print("fail: contact not found")
            else:
                c.rmFone(idx)

        elif parts[0] == "rm":
            if len(parts) == 2:
                agenda.rmContact(parts[1])

        elif parts[0] == "search":
            pad = line.split(" ", 1)[1]
            results = agenda.search(pad)
            for r in results:
                print(r)

        elif parts[0] == "tfav":
            name = parts[1]
            c = agenda.getContact(name)
            if c is None:
                print("fail: contact not found")
            else:
                c.toggleFavorited()

        elif parts[0] == "favs":
            for c in agenda.getFavorited():
                print(c)

        elif parts[0] == "end":
            break

main()