# 1.1
# from abc import ABC, abstractmethod

# # Базовый абстрактный класс стратегии
# class BattleStrategy(ABC):
#     @abstractmethod
#     def execute_attack(self, attacker, target):
#         pass

#     @abstractmethod
#     def execute_defense(self, character, incoming_damage):
#         pass

# # Конкретная реализация: Сбалансированная стратегия
# class BalancedStrategy(BattleStrategy):
#     def execute_attack(self, attacker, target):
#         # Сбалансированный урон: 100% от силы атаки
#         damage = attacker.attack_power
#         target.health -= damage
#         return f"{attacker.name} наносит {damage} урона (Сбалансированная атака)"

#     def execute_defense(self, character, incoming_damage):
#         # Сбалансированная защита: поглощает 50% урона + базовый показатель защиты
#         blocked = int(incoming_damage * 0.5) + character.defense
#         final_damage = max(0, incoming_damage - blocked)
#         character.health -= final_damage
#         return f"{character.name} блокирует {blocked} урона. Получено чистого урона: {final_damage}"

# # Класс персонажа, использующий стратегию
# class Character:
#     def __init__(self, name, health, attack_power, defense):
#         self.name = name
#         self.health = health
#         self.attack_power = attack_power
#         self.defense = defense
#         self.strategy = None

#     def set_battle_strategy(self, strategy: BattleStrategy):
#         self.strategy = strategy

#     def perform_attack(self, target):
#         if self.strategy:
#             return self.strategy.execute_attack(self, target)
#         return "Стратегия не установлена"

#     def perform_defense(self, damage):
#         if self.strategy:
#             return self.strategy.execute_defense(self, damage)
#         return "Стратегия не установлена"

#     def get_info(self):
#         return f"{self.name} (HP: {self.health}, ATK: {self.attack_power}, DEF: {self.defense})"

# # --- Тестирование ---
# balanced_strategy = BalancedStrategy()
# player = Character("Баланс", health=100, attack_power=20, defense=5)
# enemy = Character("Враг", health=100, attack_power=15, defense=3)

# # Устанавливаем стратегию
# player.set_battle_strategy(balanced_strategy)

# print(f"Игрок: {player.get_info()}")
# print(f"Враг: {enemy.get_info()}")

# # Выполняем атаку
# print(f"\nДействие: {player.perform_attack(enemy)}")

# # Выполняем защиту (враг наносит 25 урона)
# print(f"Действие: {player.perform_defense(25)}")

# print(f"\nПосле действий:")
# print(f"Игрок: {player.get_info()}")
# print(f"Враг: {enemy.get_info()}")

# 1.2
# from abc import ABC, abstractmethod

# # Базовый абстрактный класс стратегии (для корректной работы кода)
# class BattleStrategy(ABC):
#     @abstractmethod
#     def execute_attack(self, attacker, target):
#         pass

#     @abstractmethod
#     def execute_defense(self, character, incoming_damage):
#         pass

# # Конкретная реализация: Стратегия лечения
# class HealingStrategy(BattleStrategy):
#     def execute_attack(self, attacker, target):
#         # Вместо нанесения урона цели, персонаж лечит себя
#         # Сила лечения зависит от силы атаки (например, 1.5x)
#         heal_amount = int(attacker.attack_power * 1.5)
#         attacker.health += heal_amount
        
#         # Ограничение здоровья (если бы у нас был атрибут max_health)
#         if hasattr(attacker, 'max_health'):
#             attacker.health = min(attacker.health, attacker.max_health)
            
#         return f"{attacker.name} выбирает медитацию вместо атаки и восстанавливает {heal_amount} HP!"

#     def execute_defense(self, character, incoming_damage):
#         # В режиме лечения персонаж максимально закрывается
#         # Блокирует 80% урона, но не может контратаковать
#         blocked = int(incoming_damage * 0.8) + character.defense
#         final_damage = max(0, incoming_damage - blocked)
#         character.health -= final_damage
#         return f"{character.name} уходит в глухую оборону, поглощая {blocked} урона."

# # Класс персонажа для тестирования
# class Character:
#     def __init__(self, name, health, attack_power, defense):
#         self.name = name
#         self.health = health
#         self.max_health = 100 # Для корректности лечения
#         self.attack_power = attack_power
#         self.defense = defense
#         self.strategy = None

#     def set_battle_strategy(self, strategy: BattleStrategy):
#         self.strategy = strategy

#     def perform_attack(self, target):
#         return self.strategy.execute_attack(self, target)

#     def get_info(self):
#         return f"{self.name} (HP: {self.health}, ATK: {self.attack_power})"

# # --- Тестирование ---
# healing_strategy = HealingStrategy()
# healer = Character("Лекарь", health=40, attack_power=10, defense=3)
# enemy = Character("Враг", health=100, attack_power=20, defense=2)

# healer.set_battle_strategy(healing_strategy)

# print(f"Лекарь до действия: {healer.get_info()}")

# # Выполняем "атаку" (на самом деле лечение)
# result = healer.perform_attack(enemy)
# print(f"Результат: {result}")

# print(f"Лекарь после действия: {healer.get_info()}")
# print(f"Враг (не пострадал): {enemy.get_info()}")

# 2.1
# from abc import ABC, abstractmethod
# import random

# # Базовый класс для персонажей
# class Character:
#     def __init__(self, name, health, attack_power, defense, character_class="common"):
#         self.name = name
#         self.health = health
#         self.max_health = health
#         self.attack_power = attack_power
#         self.defense = defense
#         self.character_class = character_class
#         self.is_alive = True

#     def get_info(self):
#         return f"{self.name} ({self.character_class}): HP {self.health}, ATK {self.attack_power}, DEF {self.defense}"

# class AIStrategy(ABC):
#     @abstractmethod
#     def decide_action(self, enemy, player, environment=None):
#         pass

#     @abstractmethod
#     def evaluate_threat(self, enemy, player, environment=None):
#         pass

# class Enemy(Character):
#     def __init__(self, name: str, health: int, attack_power: int, defense: int, enemy_type: str = "common"):
#         super().__init__(name, health, attack_power, defense, character_class=enemy_type)
#         self.enemy_type = enemy_type
#         self._ai_strategy: AIStrategy = None

#     def set_ai_strategy(self, strategy: AIStrategy):
#         self._ai_strategy = strategy

#     def take_turn(self, player, environment=None):
#         if self._ai_strategy and self.is_alive and player.is_alive:
#             return self._ai_strategy.decide_action(self, player, environment)
#         return f"{self.name} не может действовать."

#     def evaluate_player_threat(self, player, environment=None):
#         if self._ai_strategy:
#             return self._ai_strategy.evaluate_threat(self, player, environment)
#         return "неизвестно"

# class AggressiveAI(AIStrategy):
#     def decide_action(self, enemy, player, environment=None):
#         damage = max(1, enemy.attack_power - player.defense)
#         player.health -= damage
#         return f"{enemy.name} яростно атакует {player.name}, нанося {damage} урона!"

#     def evaluate_threat(self, enemy, player, environment=None):
#         return f"{enemy.name} видит в {player.name} достойную жертву. Угроза: ВЫСОКАЯ."

# class DefensiveAI(AIStrategy):
#     def decide_action(self, enemy, player, environment=None):
#         heal = int(enemy.max_health * 0.2)
#         enemy.health = min(enemy.max_health, enemy.health + heal)
#         return f"{enemy.name} уходит в глухую оборону и восстанавливает {heal} HP."

#     def evaluate_threat(self, enemy, player, environment=None):
#         return f"{enemy.name} опасается мощи {player.name}. Угроза: КРИТИЧЕСКАЯ."

# class RandomAI(AIStrategy):
#     def decide_action(self, enemy, player, environment=None):
#         action = random.choice(["attack", "defend", "wait"])
#         if action == "attack":
#             return f"{enemy.name} проводит случайную атаку!"
#         elif action == "defend":
#             return f"{enemy.name} неуклюже пытается закрыться щитом."
#         else:
#             return f"{enemy.name} отвлекся на пролетающую мимо птицу."

#     def evaluate_threat(self, enemy, player, environment=None):
#         return f"{enemy.name} не понимает, насколько опасен {player.name}. Угроза: НЕОПРЕДЕЛЕНА."

# # --- Тестирование ---
# player = Character("Герой", health=150, attack_power=25, defense=10)

# aggressive_goblin = Enemy("Агрессивный гоблин", 50, 15, 2, "goblin")
# defensive_orc = Enemy("Оборонительный орк", 80, 12, 8, "orc")
# random_skeleton = Enemy("Случайный скелет", 40, 10, 3, "skeleton")

# aggressive_goblin.set_ai_strategy(AggressiveAI())
# defensive_orc.set_ai_strategy(DefensiveAI())
# random_skeleton.set_ai_strategy(RandomAI())

# enemies = [aggressive_goblin, defensive_orc, random_skeleton]

# print("Оценка угрозы:")
# for enemy in enemies:
#     print(f"  {enemy.evaluate_player_threat(player)}")

# print("\nХоды врагов:")
# for enemy in enemies:
#     print(f"  {enemy.take_turn(player)}")

2.2
from abc import ABC, abstractmethod

# 1. Сначала объявляем базовый интерфейс (обязательно!)
class AIStrategy(ABC):
    @abstractmethod
    def decide_action(self, enemy, player, environment=None):
        pass

    @abstractmethod
    def evaluate_threat(self, enemy, player, environment=None):
        pass

# 2. Теперь реализуем тактический ИИ
class TacticalAI(AIStrategy):
    def __init__(self, aggression_level=0.5, caution_level=0.5):
        self.aggression_level = aggression_level
        self.caution_level = caution_level

    def decide_action(self, enemy, player, environment=None):
        # Простая проверка на наличие атрибутов, чтобы код не падал
        max_hp = getattr(enemy, 'max_health', 100)
        health_ratio = enemy.health / max_hp
        distance = environment.get("distance_to_player", 5) if environment else 5

        # Логика: лечимся, если мало HP и мы осторожны
        if health_ratio < 0.3 and self.caution_level > 0.4:
            enemy.health += 20
            return f"{enemy.name} отступает и лечится. HP теперь: {enemy.health}"

        # Логика: атакуем, если мы агрессивны и игрок близко
        if distance <= 2 and self.aggression_level > 0.5:
            damage = enemy.attack_power
            player.health -= damage
            return f"{enemy.name} тактически атакует {player.name} на {damage} урона!"

        return f"{enemy.name} выжидает подходящий момент."

    def evaluate_threat(self, enemy, player, environment=None):
        if player.attack_power > enemy.health:
            return "ВЫСОКАЯ"
        return "НИЗКАЯ"

# --- Мини-тест для проверки ---
class MockUnit: # Заглушка для теста
    def __init__(self, name, hp, atk):
        self.name, self.health, self.max_health, self.attack_power = name, hp, hp, atk

hero = MockUnit("Герой", 100, 20)
dragon = MockUnit("Дракон", 50, 30)

ai = TacticalAI(aggression_level=0.8)
print(ai.decide_action(dragon, hero, {"distance_to_player": 1}))
