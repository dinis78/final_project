import logging

logging.basicConfig(level=logging.INFO, filename='animal.log', filemode='w')
'''  Результат логирования будет записываться в файл 'animal.log', 
     который будет создан в рабочей директории программы.
'''
class Animal:
    def __init__(self, name):
        self.name = name

class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def wing_length(self):
        try:
            return self.wingspan / 2
        except ZeroDivisionError as e:
            logging.error("Error in wing_length(): " + str(e))

class Fish(Animal):
    def __init__(self, name, max_depth):
        super().__init__(name)
        self.max_depth = max_depth

    def depth(self):
        try:
            if self.max_depth < 10:
                return "Мелководная рыба"
            elif self.max_depth > 100:
                return "Глубоководная рыба"
            else:
                return "Средневодная рыба"
        except Exception as e:
            logging.error("Error in depth(): " + str(e))

class Mammal(Animal):
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight

    def category(self):
        try:
            if self.weight < 1:
                return "Малявка"
            elif self.weight > 200:
                return "Гигант"
            else:
                return "Обычный"
        except Exception as e:
            logging.error("Error in category(): " + str(e))

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, *args):
        try:
            if animal_type == "Bird":
                return Bird(*args)
            elif animal_type == "Fish":
                return Fish(*args)
            elif animal_type == "Mammal":
                return Mammal(*args)
            else:
                raise ValueError("Invalid animal type")
        except Exception as e:
            logging.error("Error in create_animal(): " + str(e))

if __name__ == "__main__":
    import sys

    try:
        animal_type = sys.argv[1]
        name = sys.argv[2]

        if animal_type == "Bird":
            wingspan = float(sys.argv[3])
            animal = Bird(name, wingspan)
        elif animal_type == "Fish":
            max_depth = int(sys.argv[3])
            animal = Fish(name, max_depth)
        elif animal_type == "Mammal":
            weight = float(sys.argv[3])
            animal = Mammal(name, weight)
        else:
            raise ValueError("Invalid animal type")

        print("Animal created successfully:", animal)
    except Exception as e:
        logging.error("Error in command line execution: " + str(e))

''' 
     запуск из командной строки с передачей параметров
'''

animal1 = AnimalFactory.create_animal('Bird', 'Орел', 200)
animal2 = AnimalFactory.create_animal('Fish', 'Лосось', 50)
animal3 = AnimalFactory.create_animal('Mammal', 'Слон', 5000)

print(animal1.wing_length())
print(animal2.depth())
print(animal3.category())