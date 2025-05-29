class Battalion:
    def __init__(self, level=1, name="Battalion", health=1, isRuler=False):
        self.level = level
        self.name = name
        self.health = health
        self.isRuler = isRuler
        self.lastTurnTheyMoved = 0

    def display_health(self):
        result = ""
        for _ in range(self.health):
            result += "💗"
        return result
    
    def decrease_health(self):
        self.health -= 1
        return (self.health <= 0) 