class Monster:
    def __init__(self, name, health, attack_power, monster_type="common"):
        # Добавляем атрибуты
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.monster_type = monster_type

    def get_info(self):
        # Возвращаем строку с информацией о монстре
        return f'"{self.name}" — тип: {self.monster_type} (здоровье: {self.health}, атака: {self.attack_power})'

# Создание экземпляра и проверка
goblin = Monster("Гоблин", 30, 8, "обычный")
print(goblin.get_info());

class GameItem:
    def __init__(self, name, item_type, value=0):
        # Добавляем атрибуты
        self.name = name
        self.item_type = item_type
        self.value = value

    def use_on(self, character):
        # Использование предмета на персонаже
        return f"Предмет '{self.name}' использован на персонаже {character}. Эффект активирован!"

    def get_description(self):
        # Получение описания предмета
        return f"Предмет: {self.name} | Тип: {self.item_type} | Стоимость: {self.value} золота"

# --- Тестирование ---
health_potion = GameItem("Зелье здоровья", "зелье", 25)

# Проверка описания
print(health_potion.get_description()) 

# Проверка использования (передаем имя персонажа строкой)
print(health_potion.use_on("Воин Артур"));

