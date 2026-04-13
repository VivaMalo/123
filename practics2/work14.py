# 1.1
# from abc import ABC, abstractmethod

# class GameItem(ABC):
#     def __init__(self, name, item_type, value, weight=1.0):
#         # Добавляем атрибуты
#         self.name = name
#         self.item_type = item_type
#         self.value = value
#         self.weight = weight

#     @abstractmethod
#     def use(self, character):
#         """
#         Использовать предмет на персонаже
#         """
#         pass

#     def get_info(self):
#         return f"{self.name} ({self.item_type}): стоимость {self.value}, вес {self.weight}"


# class Weapon(GameItem):
#     def use(self, character):
#         return f"{character} экипирует {self.name}. Сила атаки возросла!"


# class Armor(GameItem):
#     def use(self, character):
#         return f"{character} надевает {self.name}. Защита увеличена!"


# class Potion(GameItem):
#     def use(self, character):
#         return f"{character} выпивает {self.name}. Здоровье восстановлено!"


# class ItemFactory:
#     @staticmethod
#     def create_item(item_type, name, value):
#         # Логика создания предметов в зависимости от типа
#         if item_type.lower() == "weapon":
#             return Weapon(name, "Оружие", value)
#         elif item_type.lower() == "armor":
#             return Armor(name, "Броня", value)
#         elif item_type.lower() == "potion":
#             return Potion(name, "Зелье", value)
#         else:
#             raise ValueError(f"Неизвестный тип предмета: {item_type}")


# # --- Тестирование ---
# weapon = ItemFactory.create_item("weapon", "Меч", 100)
# armor = ItemFactory.create_item("armor", "Щит", 150)
# potion = ItemFactory.create_item("potion", "Зелье", 25)

# print(weapon.get_info())
# print(armor.get_info())
# print(potion.get_info())

# # Проверка метода use
# print(weapon.use("Воин"))
# print(potion.use("Маг"))

# 1.2
# from abc import ABC, abstractmethod

# class Monster(ABC):
#     def __init__(self, name, health, attack_power):
#         self.name = name
#         self.health = health
#         self.attack_power = attack_power

#     @abstractmethod
#     def special_ability(self):
#         """Уникальная способность монстра"""
#         pass

# class Goblin(Monster):
#     def special_ability(self):
#         return f"{self.name} совершает быстрый коварный укол!"

# class Orc(Monster):
#     def special_ability(self):
#         return f"{self.name} впадает в ярость, увеличивая свою силу!"

# class Dragon(Monster):
#     def special_ability(self):
#         return f"{self.name} извергает поток пламени, сжигая всё вокруг!"

# class MonsterFactory:
#     @staticmethod
#     def create_monster(monster_type, name, health, attack_power):
#         """Создает экземпляр монстра на основе типа"""
#         target_class = monster_type.lower()
        
#         if target_class == "goblin":
#             return Goblin(name, health, attack_power)
#         elif target_class == "orc":
#             return Orc(name, health, attack_power)
#         elif target_class == "dragon":
#             return Dragon(name, health, attack_power)
#         else:
#             raise ValueError(f"Неизвестный тип монстра: {monster_type}")

# # --- Пример использования ---
# goblin = MonsterFactory.create_monster("goblin", "Гоблин-воин", 30, 8)
# orc = MonsterFactory.create_monster("orc", "Орк-берсерк", 70, 15)
# dragon = MonsterFactory.create_monster("dragon", "Молодой дракон", 200, 30)

# # Тестирование характеристик
# print(f"Монстр: {goblin.name}, здоровье: {goblin.health}, атака: {goblin.attack_power}")
# print(f"Монстр: {orc.name}, здоровье: {orc.health}, атака: {orc.attack_power}")

# # Тестирование способностей
# print(goblin.special_ability())
# print(dragon.special_ability())

# 2.1
# from abc import ABC, abstractmethod

# # --- Абстрактные продукты ---
# class Button(ABC):
#     def __init__(self, label, width, height):
#         self.label = label
#         self.width = width
#         self.height = height

#     @abstractmethod
#     def render(self):
#         pass

# class TextField(ABC):
#     def __init__(self, placeholder):
#         self.placeholder = placeholder

#     @abstractmethod
#     def render(self):
#         pass

# # --- Конкретные продукты: Fantasy ---
# class FantasyButton(Button):
#     def render(self):
#         return f"[Руническая кнопка: '{self.label}'] ({self.width}x{self.height}) — стиль: Дерево и Золото"

# class FantasyTextField(TextField):
#     def render(self):
#         return f"{{Магический свиток для ввода: '{self.placeholder}'}}"

# # --- Конкретные продукты: Sci-Fi ---
# class SciFiButton(Button):
#     def render(self):
#         return f"<Голографическая кнопка: '{self.label}'> ({self.width}x{self.height}) — стиль: Неон"

# class SciFiTextField(TextField):
#     def render(self):
#         return f"|Лазерное поле ввода: '{self.placeholder}'|"

# # --- Конкретные продукты: Medieval ---
# class MedievalButton(Button):
#     def render(self):
#         return f"[[Кованая кнопка: '{self.label}']] ({self.width}x{self.height}) — стиль: Железо"

# class MedievalTextField(TextField):
#     def render(self):
#         return f"((Пергамент для текста: '{self.placeholder}'))"

# # --- Абстрактная фабрика ---
# class UIElementFactory(ABC):
#     @abstractmethod
#     def create_button(self, label, width, height) -> Button:
#         pass

#     @abstractmethod
#     def create_text_field(self, placeholder) -> TextField:
#         pass

#     @staticmethod
#     def create_factory(style):
#         factories = {
#             "fantasy": FantasyUIFactory,
#             "scifi": SciFiUIFactory,
#             "medieval": MedievalUIFactory
#         }
#         factory_class = factories.get(style.lower())
#         if factory_class:
#             return factory_class()
#         raise ValueError(f"Неизвестный стиль интерфейса: {style}")

# # --- Конкретные фабрики ---
# class FantasyUIFactory(UIElementFactory):
#     def create_button(self, label, width, height):
#         return FantasyButton(label, width, height)
    
#     def create_text_field(self, placeholder):
#         return FantasyTextField(placeholder)

# class SciFiUIFactory(UIElementFactory):
#     def create_button(self, label, width, height):
#         return SciFiButton(label, width, height)
    
#     def create_text_field(self, placeholder):
#         return SciFiTextField(placeholder)

# class MedievalUIFactory(UIElementFactory):
#     def create_button(self, label, width, height):
#         return MedievalButton(label, width, height)
    
#     def create_text_field(self, placeholder):
#         return MedievalTextField(placeholder)

# # --- Тестирование ---
# fantasy_factory = UIElementFactory.create_factory("fantasy")
# scifi_factory = UIElementFactory.create_factory("scifi")

# fantasy_button = fantasy_factory.create_button("Начать игру", 150, 40)
# scifi_button = scifi_factory.create_button("Активировать", 120, 35)
# scifi_text = scifi_factory.create_text_field("Введите координаты")

# print(fantasy_button.render())
# print(scifi_button.render())
# print(scifi_text.render())

2.2
class CharacterFactory:
    # Словарь для хранения соответствия типа (строки) и класса
    _character_types = {}

    @classmethod
    def register_character_type(cls, character_type, character_class):
        """Регистрирует новый тип персонажа в фабрике"""
        cls._character_types[character_type.lower()] = character_class
        print(f"Тип персонажа '{character_type}' успешно зарегистрирован.")

    @classmethod
    def create_character(cls, character_type, name, **kwargs):
        """Создает персонажа зарегистрированного типа с произвольными параметрами"""
        char_class = cls._character_types.get(character_type.lower())
        
        if not char_class:
            raise ValueError(f"Тип персонажа '{character_type}' не зарегистрирован!")
        
        # Создаем экземпляр класса, передавая имя и все дополнительные аргументы
        return char_class(name, **kwargs)

# --- Пример реализации классов персонажей для теста ---
class Warrior:
    def __init__(self, name, health=100, attack=15):
        self.name = name
        self.health = health
        self.attack = attack
    
    def get_info(self):
        return f"Воин {self.name}: Здоровье {self.health}, Атака {self.attack}"

class Mage:
    def __init__(self, name, health=70, mana=100):
        self.name = name
        self.health = health
        self.mana = mana
    
    def get_info(self):
        return f"Маг {self.name}: Здоровье {self.health}, Мана {self.mana}"

# --- Тестирование ---
# 1. Регистрация типов
CharacterFactory.register_character_type("warrior", Warrior)
CharacterFactory.register_character_type("mage", Mage)

# 2. Создание с параметрами по умолчанию
warrior_default = CharacterFactory.create_character("warrior", "Артур")

# 3. Создание с измененными параметрами через **kwargs
warrior_strong = CharacterFactory.create_character("warrior", "Конан", health=130, attack=25)
mage_custom = CharacterFactory.create_character("mage", "Гендальф", mana=200)

print(warrior_default.get_info())
print(warrior_strong.get_info())
print(mage_custom.get_info())
