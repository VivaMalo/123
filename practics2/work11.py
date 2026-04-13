# 1.1
# from abc import ABC, abstractmethod

# class Attackable(ABC):
#     @abstractmethod
#     def take_damage(self, damage):
#         pass

#     @abstractmethod
#     def deal_damage(self, target):
#         pass

# class Warrior(Attackable):
#     def __init__(self, name, health, attack_power, defense=5):
#         # Инициализация атрибутов
#         self.name = name
#         self.health = health
#         self.max_health = health
#         self.attack_power = attack_power
#         self.defense = defense
#         self.is_alive = True

#     def take_damage(self, damage):
#         # Расчет чистого урона с учетом защиты (минимум 1 единица)
#         pure_damage = max(1, damage - self.defense)
#         self.health -= pure_damage
        
#         if self.health <= 0:
#             self.health = 0
#             self.is_alive = False
            
#         return pure_damage

#     def deal_damage(self, target):
#         # Нанесение урона цели через её метод take_damage
#         if self.is_alive:
#             actual_damage = target.take_damage(self.attack_power)
#             return f"{self.name} наносит {actual_damage} урона цели {target.name}."
#         return f"{self.name} не может атаковать, так как он мертв."

#     def get_combat_info(self):
#         # Боевая информация о персонаже
#         status = "Жив" if self.is_alive else "Мертв"
#         return (f"Воин: {self.name} | Статус: {status} | "
#                 f"HP: {self.health}/{self.max_health} | "
#                 f"Атака: {self.attack_power} | Защита: {self.defense}")

# # --- Тестирование ---
# warrior1 = Warrior("Конан", 120, 25, 10)
# warrior2 = Warrior("Рангнарок", 100, 20, 5)

# print(warrior1.get_combat_info())
# print(warrior1.deal_damage(warrior2)) # Конан бьет Рангнарока
# print(warrior2.get_combat_info())     # Проверяем остаток здоровья

# 1.2
# from abc import ABC, abstractmethod

# # Базовый абстрактный класс
# class InventoryItem(ABC):
#     def __init__(self, name, item_type, weight=1.0, value=0):
#         self.name = name
#         self.item_type = item_type
#         self.weight = weight
#         self.value = value

#     @abstractmethod
#     def use(self, character):
#         pass

# # Класс-наследник (Зелье здоровья)
# class HealthPotion(InventoryItem):
#     def __init__(self, name="Зелье здоровья", healing_power=50, weight=0.5, value=25):
#         # Вызываем конструктор родителя, передавая необходимые параметры
#         super().__init__(name, "potion", weight, value)
#         self.healing_power = healing_power

#     def use(self, character):
#         # Реализация восстановления здоровья
#         # Предполагаем, что у character есть атрибут health
#         character.health += self.healing_power
#         print(f"Предмет {self.name} использован. Восстановлено {self.healing_power} HP.")

# # --- Тестирование ---
# # Создаем простейший объект-заглушку вместо полноценного класса персонажа
# class Hero:
#     def __init__(self):
#         self.health = 50

# my_hero = Hero()
# health_potion = HealthPotion("Малое зелье здоровья", 30)

# print(f"Здоровье до: {my_hero.health}")
# health_potion.use(my_hero)
# print(f"Здоровье после: {my_hero.health}")

from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name, health, attack_power, level=1):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack_power = attack_power
        self.level = level
        self.experience = 0
        self.is_alive = True

    @abstractmethod
    def use_special_ability(self):
        pass

    @abstractmethod
    def level_up(self):
        pass

    def rest(self):
        self.health = self.max_health
        return f"{self.name} отдохнул и полностью восстановил здоровье."

class Knight(Character):
    def __init__(self, name, health=150, attack_power=20, level=1, armor=10):
        super().__init__(name, health, attack_power, level)
        self.armor = armor

    def use_special_ability(self):
        return f"Рыцарь {self.name} использует 'Щит веры', увеличивая защиту на {self.armor}."

    def level_up(self):
        self.level += 1
        self.max_health += 30
        self.attack_power += 5
        return f"Рыцарь {self.name} поднял уровень до {self.level}!"

class Wizard(Character):
    def __init__(self, name, health=90, attack_power=15, level=1, mana=100):
        super().__init__(name, health, attack_power, level)
        self.mana = mana

    def use_special_ability(self):
        self.mana -= 20
        return f"Волшебник {self.name} произносит 'Огненный шар'. Осталось маны: {self.mana}."

    def level_up(self):
        self.level += 1
        self.mana += 50
        self.attack_power += 10
        return f"Волшебник {self.name} изучил новые заклинания! Уровень: {self.level}."

class Ranger(Character):
    def __init__(self, name, health=110, attack_power=18, level=1, arrows=30):
        super().__init__(name, health, attack_power, level)
        self.arrows = arrows

    def use_special_ability(self):
        if self.arrows > 0:
            self.arrows -= 1
            return f"Рейнджер {self.name} выпускает меткую стрелу. Осталось стрел: {self.arrows}."
        return f"У {self.name} закончились стрелы!"

    def level_up(self):
        self.level += 1
        self.attack_power += 7
        self.max_health += 15
        return f"Рейнджер {self.name} стал опытнее! Уровень: {self.level}."

# --- Тестирование ---
knight = Knight("Ланселот")
wizard = Wizard("Гендальф")
ranger = Ranger("Леголас")

# Тест отдыха
knight.health = 50
print(f"Здоровье Ланселота до отдыха: {knight.health}")
knight.rest()
print(f"Здоровье Ланселота после отдыха: {knight.health}")

# Тест способностей
print(wizard.use_special_ability())
print(ranger.use_special_ability())

# Тест повышения уровня
print(knight.level_up())


# 2.2
# from abc import ABC, abstractmethod

# # Расширенный абстрактный класс
# class GameEntity(ABC):
#     def __init__(self, name):
#         self.name = name

#     @abstractmethod
#     def interact_with_environment(self, environment_object):
#         """Абстрактный метод для взаимодействия с объектами окружения"""
#         pass

#     @abstractmethod
#     def respond_to_event(self, event):
#         """Абстрактный метод для реакции на игровые события"""
#         pass

# # Класс Игрока
# class PlayerCharacter(GameEntity):
#     def interact_with_environment(self, environment_object):
#         return f"Игрок {self.name} активно использует {environment_object}: обыскивает или активирует."

#     def respond_to_event(self, event):
#         return f"Игрок {self.name} получил уведомление о событии '{event}' и готов к действиям."

# # Класс NPC (Неигровой персонаж)
# class NonPlayerCharacter(GameEntity):
#     def interact_with_environment(self, environment_object):
#         return f"NPC {self.name} просто стоит рядом с {environment_object}, проигрывая фоновую анимацию."

#     def respond_to_event(self, event):
#         return f"NPC {self.name} реагирует на событие '{event}' заранее прописанной фразой или испугом."

# # --- Пример тестирования ---
# player = PlayerCharacter("Алекс")
# npc = NonPlayerCharacter("Торговец")

# print(player.interact_with_environment("Сундук"))
# print(npc.interact_with_environment("Сундук"))

# print(player.respond_to_event("Начало шторма"))
# print(npc.respond_to_event("Начало шторма"))
