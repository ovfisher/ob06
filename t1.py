class   Hero:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    def attack(self,Hero):
        if Hero.health >= self.attack_power :
            Hero.health = Hero.health - self.attack_power
        else: print('Game over')
    def is_alive(self):
        alive = self.health > 0
        if alive:
            print(f'{self.name} - still alive benzin - {self.health}, continue')
        else: print(f'{self.name} - dead, game over')
        return alive
#Класс `Game`:- Атрибуты:
#- Игрок (`player`), экземпляр класса `Hero`
#- Компьютер (`computer`), экземпляр класса `Hero`
#- Методы:
#- `start()`:начинает игру, чередует ходы игрока и компьютера,
# пока один из героев не умрет. Выводит информацию о каждом ходе
# (кто атаковал и сколько здоровья осталось у противника) и объявляет победителя.
class   Game(player,comp):
    def __init__(self,player,comp):
        self.player = Hero
        self.comp = Hero
    def start(self):
        while self.comp.is_alive() and self.player.is_alive():
            self.player.attack(self.comp)
            self.comp.attack(self.player)

p1 = Hero('Hercules',100,20)

p2 = Hero('Comp',400,20)
p1.attack(p2)
if p2.is_alive():
    print(f'{p2.name} - xxxxxx ')

gm = Game(p1,p2)
if p1.health > 0:
    print(f'{p1.name},{p1.health} - winner')
elif  p2.health > 0:
    print(f'{p2.name},{p2.health} - winner')
else: print('game is over - draw')

print(f'{p1.name},{p1.health} - winner')
print(f'{p2.name},{p2.health} - winner')