# 1.1
# class Animal:
#     def __init__(self, name, species, age, health=100):
#         # Атрибуты базового класса
#         self.name = name
#         self.species = species
#         self.age = age
#         self.health = health

#     def make_sound(self):
#         # Базовый метод звука
#         return f"{self.name} издает звук своего вида."

#     def eat(self):
#         # Повышаем здоровье при кормлении
#         self.health += 5
#         return f"{self.name} ест. Текущее здоровье: {self.health}"

#     def sleep(self):
#         # Метод сна
#         return f"{self.name} уснул. Zzz..."

# class Pet(Animal):
#     def __init__(self, name, species, age, owner, health=100):
#         # Вызов конструктора родительского класса Animal
#         super().__init__(name, species, age, health)
#         # Специфичные атрибуты питомца
#         self.owner = owner
#         self.happiness = 100

#     def make_sound(self):
#         # Переопределение метода для питомца
#         return f"{self.name} радостно ластится к хозяину по имени {self.owner}!"

#     def play_with_owner(self):
#         # Специфичный метод: игра повышает уровень счастья
#         self.happiness += 15
#         return f"{self.name} играет с {self.owner}. Счастье: {self.happiness}"

# # --- Тестирование ---
# my_pet = Pet("Барсик", "кот", 3, "Иван")

# print(my_pet.make_sound())      # Проверка переопределенного метода
# print(my_pet.eat())             # Проверка метода родителя
# print(my_pet.play_with_owner()) # Проверка уникального метода
# print(my_pet.sleep())           # Проверка метода сна

# 1.2
# class Vehicle:
#     def __init__(self, brand, model, year, max_speed):
#         # Инициализация общих атрибутов
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.max_speed = max_speed

#     def move(self):
#         # Базовый метод движения
#         return f"{self.brand} {self.model} начинает движение."

#     def get_info(self):
#         # Метод получения общей информации
#         return f"{self.year} {self.brand} {self.model} (Макс. скорость: {self.max_speed} км/ч)"

# class Car(Vehicle):
#     def __init__(self, brand, model, year, max_speed, fuel_capacity):
#         # Вызываем конструктор родителя и добавляем объем бака
#         super().__init__(brand, model, year, max_speed)
#         self.fuel_capacity = fuel_capacity

#     def move(self):
#         # Специфичное движение для машины
#         return f"Автомобиль {self.brand} {self.model} едет по дороге со скоростью до {self.max_speed} км/ч."

# class Airplane(Vehicle):
#     def __init__(self, brand, model, year, max_speed, max_altitude):
#         # Вызываем конструктор родителя и добавляем макс. высоту
#         super().__init__(brand, model, year, max_speed)
#         self.max_altitude = max_altitude

#     def move(self):
#         # Специфичное движение для самолета
#         return f"Самолет {self.brand} {self.model} взлетает и набирает высоту до {self.max_altitude} метров."

# # --- Тестирование ---
# my_car = Car("Toyota", "Camry", 2020, 180, 60)
# my_airplane = Airplane("Boeing", "737", 2019, 850, 12000)

# print(my_car.get_info())
# print(my_car.move())

# print("-" * 30)

# print(my_airplane.get_info())
# print(my_airplane.move())

# 2.1
# class Movable:
#     def __init__(self, speed=1.0, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.speed = speed
#         self.position = [0, 0]
    
#     def move(self, dx, dy):
#         self.position[0] += dx * self.speed
#         self.position[1] += dy * self.speed
#         print(f"Персонаж переместился на ({self.position[0]}, {self.position[1]})")

# class Attackable:
#     def __init__(self, attack_power=10, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.attack_power = attack_power
    
#     def attack(self, target):
#         if hasattr(target, 'health'):
#             target.health -= self.attack_power
#             print(f"Атака на {target.name} нанесла {self.attack_power} урона. Осталось HP: {target.health}")
#         else:
#             print("Цель нельзя атаковать")

# class MagicUser:
#     def __init__(self, mana=50, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.mana = mana
#         self.max_mana = mana
    
#     def cast_spell(self, spell_name, target=None):
#         if self.mana >= 10:
#             self.mana -= 10
#             print(f"Заклинание '{spell_name}' использовано! (Мана: {self.mana})")
#             if target and hasattr(target, 'health'):
#                 target.health -= 15
#         else:
#             print("Мана закончилась!")

# class HybridCharacter(Movable, Attackable, MagicUser):
#     def __init__(self, name, health=100, **kwargs):
#         # Инициализируем всю цепочку классов через именованные аргументы
#         super().__init__(**kwargs)
#         self.name = name
#         self.health = health
#         self.max_health = health

# # --- Тестирование ---
# # Создаем героя, передавая параметры для всех родительских классов
# hero = HybridCharacter("Арагорн", health=150, speed=2.0, attack_power=25, mana=100)

# # Создаем простого врага
# enemy = type('Enemy', (), {'name': 'Орк', 'health': 50})()

# hero.move(5, 3)             # Проверка Movable
# hero.attack(enemy)          # Проверка Attackable
# hero.cast_spell("Молния", enemy) # Проверка MagicUser

2.2
class Fighter:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack_power = attack_power
        self.is_alive = True

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.is_alive = False
        return damage

    def special_attack(self, target):
        # Мощный удар: наносит двойной урон
        damage = self.attack_power * 2
        actual_damage = target.take_damage(damage)
        return f"Воин {self.name} наносит сокрушительный удар по {target.name} на {actual_damage} урона!"

class Mage:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack_power = attack_power
        self.mana = 100
        self.is_alive = True

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.is_alive = False
        return damage

    def special_attack(self, target):
        # Магический взрыв: тратит ману, наносит урон игнорируя защиту (условно)
        if self.mana >= 30:
            self.mana -= 30
            damage = self.attack_power + 20
            actual_damage = target.take_damage(damage)
            return f"Маг {self.name} выпускает огненный шар в {target.name} на {actual_damage} урона! (Мана: {self.mana})"
        return f"У {self.name} недостаточно маны!"

class Archer:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack_power = attack_power
        self.arrows = 30
        self.is_alive = True

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.is_alive = False
        return damage

    def special_attack(self, target):
        # Град стрел: наносит три небольших удара
        if self.arrows >= 3:
            self.arrows -= 3
            damage = int(self.attack_power * 1.5)
            actual_damage = target.take_damage(damage)
            return f"Лучник {self.name} выпускает град стрел в {target.name}, нанося {actual_damage} урона!"
        return f"У {self.name} закончились стрелы!"

def battle_round(attacker, defender):
    """
    Функция демонстрирует полиморфизм: нам не важно, какой класс у attacker, 
    мы просто вызываем метод special_attack().
    """
    if attacker.is_alive and defender.is_alive:
        result = attacker.special_attack(defender)
        print(result)
        if not defender.is_alive:
            print(f"--- {defender.name} повержен! ---")
    else:
        print("Бой невозможен: один из участников не в состоянии сражаться.")

# --- Тестирование ---
warrior = Fighter("Конан", 120, 25)
mage = Mage("Гендальф", 80, 15)
archer = Archer("Робин", 90, 20)

battle_round(warrior, mage)  # Воин атакует мага
battle_round(mage, archer)   # Маг атакует лучника
battle_round(archer, warrior) # Лучник атакует воина
