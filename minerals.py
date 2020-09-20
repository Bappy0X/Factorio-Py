from json import load
minerals = load(open("minerals.json", "r"))

class Mineral:
    def __init__(self, name: str):
        self.name = name
        data = minerals.get(name)
        if not data:
            raise Exception("Couldn't find that mineral!")
        self.value = data["value"]
        self.price = data["price"]
        self.level = data["level"]
        self.progress = 0