from colorama import Back
from datetime import datetime
from json import load, dump
playerStats = load(open("playerStats.json"))

#Construct Player Class
class Player:
    def __init__(self, id=len(playerStats), name=None, level=0, playTime=0, created=datetime.now()):
        self.id = id
        self.name = name
        self.level = level
        self.playTime = playTime
        if type(created) == str:
            self.created = datetime.strptime(created, "%m/%d/%Y, %H:%M:%S")
        else:
            self.created = created

    def __repr__(self):
        return(f"<Player#{self.id}>")

    def __iter__(self):
        yield "name", self.name,
        yield "level", self.level,
        yield "playTime", self.playTime,
        yield "created", self.created.strftime("%m/%d/%Y, %H:%M:%S")

    def fromDB(self, name):
        for k, v in playerStats.items():
            if v["name"] == name:
                self.__init__(k, **v)
                print(f"{Back.GREEN}Your data has been found...")
                break
        else:
            self.name = name
            print(f"{Back.RED}Couldn't find your data... Creating new player.")
        return self

    def save(self) -> str:
        try:
            with open("playerStats.json", "r") as file:
                playerStats = load(file)
                playerStats[str(self.id)] = dict(self)
            with open("playerStats.json", "w") as file:
                dump(playerStats, file, indent=4)
        except Exception as err:
            return(f"{Back.RED}Your stats couldn't be saved: `{err}`.")
        else:
            return(f"{Back.GREEN}Your stats were saved sucessfully.")