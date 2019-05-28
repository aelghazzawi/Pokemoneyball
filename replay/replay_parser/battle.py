class Pokemon:
    def __init__(self, species, health=100, switches=0):
        self.__species = species
        self.__health = health
        self.__switches = switches

    def __lt__(self, other):
        return self.__species < other.__species

    @property
    def species(self):
        return self.__species

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, new_health):
        if new_health > 100:
            self.__health = 100
        elif new_health < 0:
            self.__health = 0
        else:
            self.__health = new_health


class Switch:
    def __init__(self, player, pokemon):
        self.__player = player
        self.__pokemon = pokemon

    @property
    def player(self):
        return self.__player

    @property
    def pokemon(self):
        return self.__pokemon


class Move:
    def __init__(self, player, pokemon, damage=0):
        self.__player = player
        self.__pokemon = pokemon
        self.__damage = damage

    @property
    def player(self):
        return self.__player

    @property
    def pokemon(self):
        return self.__pokemon

    @property
    def damage(self):
        return self.__damage


class Turn:
    def __init__(self, number, switches, moves):
        self.__number = number
        self.__switches = switches
        self.moves = moves

    @property
    def number(self):
        return self.__number

    @property
    def switches(self):
        return self.__switches
