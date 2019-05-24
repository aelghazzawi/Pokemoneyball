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


class Turn:
    def __init__(self, number, standby_phase, attack_phase, end_phase):
        self.number = number
        self.standby_phase = standby_phase
        self.attack_phase = attack_phase
        self.end_phase = end_phase
