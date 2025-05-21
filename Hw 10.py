# 1
class Animal:
    def speak(self):
        return "издает звук"


class MixinSwim:
    def swim(self):
        return "плавает"


class MixinFly:
    def fly(self):
        return "летает"


class Duck(Animal, MixinSwim, MixinFly):
    def speak(self):
        return "кря-кря"


class Penguin(Animal, MixinSwim):
    def speak(self):
        return "буль-буль"


birds = [Duck(), Penguin()]

for bird in birds:
    print(f"{bird.__class__.__name__}:")
    print(f"- Говорит: {bird.speak()}")
    print(f"- Плавает: {bird.swim()}")
    
    if isinstance(bird, MixinFly):
        print(f"- Летает: {bird.fly()}")
    else:
        print("- Не умеет летать")


# 2
class Writer:
    def write(self):
        return "пишет текст"


class Painter:
    def draw(self):
        return "рисует картину"


class CreativePerson(Writer, Painter):
    def write(self):
        return "творчески пишет стихотворение"
    
    def draw(self):
        return "выразительно рисует пейзаж"

creatives = [Writer(), Painter(), CreativePerson()]

for person in creatives:
    print(f"{person.__class__.__name__}:")
    
    if hasattr(person, 'write'):
        print(f"- {person.write()}")
    
    if hasattr(person, 'draw'):
        print(f"- {person.draw()}")
