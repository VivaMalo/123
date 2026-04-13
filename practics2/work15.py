# 1.1
# from abc import ABC, abstractmethod

# # Интерфейс Наблюдателя
# class Observer(ABC):
#     @abstractmethod
#     def update(self, event_type, data):
#         pass

# # Конкретный наблюдатель за смертью
# class DeathObserver(Observer):
#     def update(self, event_type, data):
#         if event_type == "player_died":
#             name = data.get("name", "Неизвестный")
#             reason = data.get("reason", "неизвестные обстоятельства")
#             print(f"[УВЕДОМЛЕНИЕ] Персонаж {name} погиб! Причина: {reason}.")

# # Класс игрока (Субъект)
# class Player:
#     def __init__(self, name, health=100):
#         self.name = name
#         self.health = health
#         self.is_alive = True
#         self._observers = []

#     def attach(self, observer):
#         self._observers.append(observer)

#     def notify(self, event_type, data):
#         for observer in self._observers:
#             observer.update(event_type, data)

#     def take_damage(self, damage):
#         if not self.is_alive:
#             return
        
#         self.health -= damage
#         print(f"{self.name} получает {damage} урона. Осталось HP: {max(0, self.health)}")
        
#         if self.health <= 0:
#             self.is_alive = False
#             self.notify("player_died", {"name": self.name, "reason": "получение критического урона"})

#     def get_info(self):
#         return f"{self.name} (Здоровье: {self.health})"

# # --- Тестирование ---
# death_observer = DeathObserver()
# player = Player("Борис", health=50)

# # Подписываем наблюдателя на события игрока
# player.attach(death_observer)

# print(f"Игрок: {player.get_info()}")
# player.take_damage(60)  # Урон превышает здоровье, вызывая смерть

# print(f"Игрок жив: {player.is_alive}")

# 1.2
# from abc import ABC, abstractmethod

# # Базовый интерфейс наблюдателя
# class Observer(ABC):
#     @abstractmethod
#     def update(self, event_type, data):
#         pass

# # Конкретный наблюдатель за опытом
# class ExperienceObserver(Observer):
#     def update(self, event_type, data):
#         if event_type == "experience_gained":
#             amount = data.get("amount", 0)
#             total = data.get("total", 0)
#             print(f"[ОПЫТ] Получено +{amount} ед. опыта. Всего: {total}.")

# # Класс игрока для демонстрации работы
# class Player:
#     def __init__(self, name, health=100):
#         self.name = name
#         self.health = health
#         self.experience = 0
#         self._observers = []

#     def attach(self, observer):
#         self._observers.append(observer)

#     def notify(self, event_type, data):
#         for observer in self._observers:
#             observer.update(event_type, data)

#     def gain_experience(self, amount):
#         self.experience += amount
#         # Уведомляем наблюдателей о получении опыта
#         self.notify("experience_gained", {
#             "amount": amount, 
#             "total": self.experience
#         })

#     def get_info(self):
#         return f"{self.name} (HP: {self.health}, EXP: {self.experience})"

# # --- Тестирование ---
# exp_observer = ExperienceObserver()
# player = Player("Елена", health=100)

# # Подписываем наблюдателя
# player.attach(exp_observer)

# print(f"Игрок: {player.get_info()}")
# player.gain_experience(75)
# player.gain_experience(125)

# print(f"После получения опыта: {player.get_info()}")

# 2.1
# from typing import Callable, Dict, List

# class EventManager:
#     def __init__(self):
#         # Словарь, где ключ — тип события, значение — список функций-обработчиков
#         self._subscribers: Dict[str, List[Callable]] = {}

#     def subscribe(self, event_type: str, callback: Callable):
#         """Подписка на определенный тип события"""
#         if event_type not in self._subscribers:
#             self._subscribers[event_type] = []
#         self._subscribers[event_type].append(callback)
#         print(f"[Система] Обработчик зарегистрирован на событие: {event_type}")

#     def unsubscribe(self, event_type: str, callback: Callable):
#         """Отписка от события"""
#         if event_type in self._subscribers:
#             self._subscribers[event_type].remove(callback)

#     def trigger_event(self, event_type: str, data: dict):
#         """Вызов всех подписанных обработчиков для данного события"""
#         if event_type in self._subscribers:
#             for callback in self._subscribers[event_type]:
#                 callback(event_type, data)

# # --- Примеры обработчиков событий ---

# def player_damaged_handler(event_type: str, data: dict):
#     player_name = data.get("name", "Игрок")
#     damage = data.get("damage_amount", 0)
#     print(f"[LOG] {player_name} получил {damage} урона. Проверка состояния...")

# def enemy_defeated_handler(event_type: str, data: dict):
#     enemy_type = data.get("enemy_type", "Монстр")
#     print(f"[LOG] {enemy_type} повержен! Раздача трофеев...")

# def level_up_handler(event_type: str, data: dict):
#     new_level = data.get("level", 1)
#     print(f"[LOG] ПОЗДРАВЛЯЕМ! Достигнут уровень {new_level}!")

# # --- Тестирование ---

# event_manager = EventManager()

# # Подписываем обработчики
# event_manager.subscribe("player_damaged", player_damaged_handler)
# event_manager.subscribe("enemy_died", enemy_defeated_handler)
# event_manager.subscribe("player_leveled_up", level_up_handler)

# # Имитация игровых событий
# print("\n--- Процесс игры ---")
# event_manager.trigger_event("player_damaged", {"name": "Артур", "damage_amount": 25})
# event_manager.trigger_event("enemy_died", {"enemy_type": "Гоблин"})
# event_manager.trigger_event("player_leveled_up", {"level": 2})

2.2
from abc import ABC, abstractmethod

# Базовые классы для работы паттерна
class Observer(ABC):
    @abstractmethod
    def update(self, event_type: str, data: dict = None):
        pass

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self, event_type: str, data: dict = None):
        for observer in self._observers:
            observer.update(event_type, data)

# Улучшенный класс игрока
class Player(Subject):
    def __init__(self, name: str, health: int = 100, mana: int = 50, stamina: int = 100):
        super().__init__()
        self.name = name
        self._health = health
        self._max_health = health
        self._mana = mana
        self._max_mana = mana
        self._stamina = stamina
        self._max_stamina = stamina
        self._level = 1
        self._experience = 0
        self._armor = 5
        self.is_alive = True

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, value):
        old_mana = self._mana
        # Ограничиваем значение от 0 до максимума
        self._mana = max(0, min(value, self._max_mana))
        if old_mana != self._mana:
            self.notify("player_mana_changed", {
                "player": self,
                "old_mana": old_mana,
                "new_mana": self._mana
            })

    @property
    def stamina(self):
        return self._stamina

    @stamina.setter
    def stamina(self, value):
        old_stamina = self._stamina
        self._stamina = max(0, min(value, self._max_stamina))
        if old_stamina != self._stamina:
            self.notify("player_stamina_changed", {
                "player": self,
                "old_stamina": old_stamina,
                "new_stamina": self._stamina
            })

    def use_mana(self, amount: int):
        if self.mana >= amount:
            print(f"✨ {self.name} читает заклинание...")
            self.mana -= amount
        else:
            print(f"❌ Недостаточно маны!")

    def use_stamina(self, amount: int):
        if self.stamina >= amount:
            print(f"⚔️ {self.name} совершает рывок...")
            self.stamina -= amount
        else:
            print(f"❌ Слишком устал для рывка!")

    def get_info(self):
        return f"{self.name} (HP: {self._health}, MP: {self.mana}, SP: {self.stamina})"

# --- Тестирование ---
class ManaObserver(Observer):
    def update(self, event_type: str, data: dict = None):
        if event_type == "player_mana_changed":
            player = data.get("player")
            old_mana = data.get("old_mana", 0)
            new_mana = data.get("new_mana", 0)
            print(f"🔵 {player.name} изменил ману: {old_mana} -> {new_mana}")

player = Player("Маг", health=80, mana=100, stamina=80)
mana_observer = ManaObserver()
player.attach(mana_observer)

print(f"Игрок: {player.get_info()}")
player.use_mana(30)
player.use_mana(80) # Попытка использовать больше, чем есть
