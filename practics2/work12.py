# 1.1
# class GameItem:
#     def __init__(self, name, power, durability, weight=1.0):
#         self.name = name
#         self.power = power
#         self.durability = durability
#         self.weight = weight

#     def __add__(self, other):
#         # Проверяем, что складываем с другим GameItem
#         if isinstance(other, GameItem):
#             new_name = f"Объединенный {self.name}"
#             new_power = self.power + other.power
#             new_weight = self.weight + other.weight
#             # Усредняем прочность
#             new_durability = (self.durability + other.durability) / 2
#             return GameItem(new_name, new_power, new_durability, new_weight)
#         return NotImplemented

#     def __mul__(self, factor):
#         # Умножаем силу на числовой множитель
#         if isinstance(factor, (int, float)):
#             return GameItem(f"Усиленный {self.name}", self.power * factor, self.durability, self.weight)
#         return NotImplemented

#     def __truediv__(self, divisor):
#         # Разделяем силу и вес на части
#         if isinstance(divisor, (int, float)) and divisor != 0:
#             return GameItem(f"Осколок {self.name}", self.power / divisor, self.durability, self.weight / divisor)
#         return NotImplemented

#     def __str__(self):
#         return (f"'{self.name}' (Сила: {self.power:.1f}, "
#                 f"Прочность: {self.durability:.1f}, Вес: {self.weight:.1f})")

# # --- Тестирование ---
# sword1 = GameItem("Меч", 20, 100, 5.0)
# sword2 = GameItem("Меч", 15, 80, 4.0)

# # Проверка сложения
# combined = sword1 + sword2
# print(f"Результат сложения: {combined}")

# # Проверка умножения
# buffed = sword1 * 1.5
# print(f"Результат усиления: {buffed}")

# # Проверка деления
# shattered = sword1 / 2
# print(f"Результат разделения: {shattered}")

# 1.2
# class Player:
#     def __init__(self, name, level=1, experience=0, guild="None"):
#         self.name = name
#         self.level = level
#         self.experience = experience
#         self.guild = guild

#     def __str__(self):
#         # Краткое, дружелюбное представление
#         return f"{self.name} ({self.level} ур.)"

#     def __repr__(self):
#         # Формат для разработчика: позволяет воссоздать объект
#         return f"Player(name='{self.name}', level={self.level}, experience={self.experience}, guild='{self.guild}')"

#     def __format__(self, format_spec):
#         # Управление выводом через f-строки: f"{player:spec}"
#         if format_spec == "full":
#             return f"Игрок: {self.name} | Уровень: {self.level} | Опыт: {self.experience} | Гильдия: {self.guild}"
#         elif format_spec == "table":
#             return f"{self.name:<10} | {self.level:<5} | {self.guild:<15}"
#         # Если спецификатор не указан или по умолчанию
#         return str(self)

# # --- Тестирование ---
# player = Player("Артур", 5, 15000, "Рыцари Света")

# print(f"Краткий вид: {player}")                 # Вызов __str__
# print(f"Для отладки: {repr(player)}")           # Вызов __repr__
# print(f"Полный вид: {player:full}")             # Вызов __format__ со спецификатором 'full'
# print(f"Для таблицы: {player:table}")           # Вызов __format__ со спецификатором 'table'

# 2.1
# class Inventory:
#     def __init__(self, max_size=10):
#         self.items = []
#         self.max_size = max_size

#     def __getitem__(self, index):
#         # Позволяет получать предмет: item = inventory[0]
#         return self.items[index]

#     def __setitem__(self, index, item):
#         # Позволяет заменять предмет: inventory[0] = "Новый меч"
#         self.items[index] = item

#     def __delitem__(self, index):
#         # Позволяет удалять предмет: del inventory[0]
#         del self.items[index]

#     def __len__(self):
#         # Позволяет использовать len(inventory)
#         return len(self.items)

#     def __contains__(self, item_name):
#         # Проверка через оператор 'in' (по имени предмета или объекту)
#         return any(item_name in str(item) for item in self.items)

#     def __iter__(self):
#         # Позволяет использовать в цикле: for item in inventory:
#         return iter(self.items)

#     def __bool__(self):
#         # True если не пуст, False если пуст. Используется в if inventory:
#         return len(self.items) > 0

#     def add_item(self, item):
#         if len(self.items) < self.max_size:
#             self.items.append(item)
#             return True
#         print("Инвентарь переполнен!")
#         return False

# # --- Тестирование ---
# inventory = Inventory(max_size=5)

# # Добавляем данные (для теста используем строки или объекты)
# inventory.add_item("Меч")
# inventory.add_item("Щит")
# inventory.add_item("Зелье")

# print(f"Количество предметов: {len(inventory)}") # __len__
# print(f"Пуст ли инвентарь: {not bool(inventory)}") # __bool__

# if "Меч" in inventory: # __contains__
#     print("Меч найден!")

# print("Список предметов:")
# for item in inventory: # __iter__
#     print(f"- {item}")

# inventory[1] = "Улучшенный Щит" # __setitem__
# print(f"Второй слот теперь: {inventory[1]}") # __getitem__

# del inventory[0] # __delitem__
# print(f"После удаления первого предмета осталось: {len(inventory)}")

2.2
class Skill:
    def __init__(self, name, power, skill_type="combat", cooldown=2):
        self.name = name
        self.power = power
        self.skill_type = skill_type
        self.max_cooldown = cooldown
        self.current_cooldown = 0

    def __call__(self, target, user=None):
        # Проверка кулдауна
        if self.current_cooldown > 0:
            print(f"Навык '{self.name}' еще не восстановился (осталось {self.current_cooldown} ходов).")
            return False

        # Применение навыка в зависимости от типа
        print(f"Использование навыка '{self.name}' на {getattr(target, 'name', 'цель')}...")
        
        if self.skill_type == "combat":
            damage = self.power + (user.attack_power if user else 0)
            target.health -= damage
            print(f"  Нанесено {damage} урона!")
            
        elif self.skill_type == "support":
            target.health += self.power
            print(f"  Восстановлено {self.power} здоровья!")
            
        elif self.skill_type == "magic":
            # Условная логика для магии
            target.health -= self.power * 1.5
            print(f"  Магический взрыв нанес {self.power * 1.5} урона!")

        # Установка кулдауна после успешного применения
        self.current_cooldown = self.max_cooldown
        return True

    def reduce_cooldown(self):
        if self.current_cooldown > 0:
            self.current_cooldown -= 1

    def __str__(self):
        status = "Готов" if self.current_cooldown == 0 else f"Кулдаун: {self.current_cooldown}"
        return f"Навык '{self.name}' [{self.skill_type}] (Сила: {self.power}, {status})"

    def __repr__(self):
        return f"Skill(name='{self.name}', power={self.power}, type='{self.skill_type}', cd={self.current_cooldown})"

# --- Пример тестирования ---
# Создаем простую заглушку персонажа
class SimpleChar:
    def __init__(self, name, health, attack_power=0):
        self.name = name
        self.health = health
        self.attack_power = attack_power

hero = SimpleChar("Рыцарь", 100, 10)
enemy = SimpleChar("Гоблин", 50)

# Создаем навыки
slash = Skill("Рубящий удар", 15, "combat", cooldown=2)
heal = Skill("Лечение", 20, "support", cooldown=3)

# Использование
slash(enemy, hero)  # Вызов через __call__
print(f"Здоровье гоблина: {enemy.health}")
print(slash)

# Попытка повторного использования (сработает проверка кулдауна)
slash(enemy, hero)

# Перемотка времени
slash.reduce_cooldown()
slash.reduce_cooldown()
print(f"Состояние после отдыха: {slash}")
