from abc import ABC, abstractmethod
from typing import List
from typing import Callable, Dict, List
import asyncio
class GameItem(ABC):
    def __init__(self, name, item_type, value, weight=1.0):
        self.name = name
        self.item_type = item_type
        self.value = value
        self.weight = weight

    @abstractmethod
    def use(self, character):
        """
        Использовать предмет на персонаже
        """
        pass

    def get_info(self):
        return f"{self.name} ({self.item_type}): стоимость {self.value}, вес {self.weight}"


class Weapon(GameItem):
    def __init__(self, name, value=100, weight=3.0, damage=10):
        super().__init__(name, "weapon", value, weight)
        self.damage = damage

    def use(self, character):
        if hasattr(character, 'attack_power'):
            character.attack_power += self.damage
            return f"{character.name} экипировал {self.name}, атака увеличена на {self.damage}"
        else:
            return f"{character.name} не может использовать {self.name} как оружие"


class Armor(GameItem):
    def __init__(self, name, value=150, weight=10.0, defense=5):
        super().__init__(name, "armor", value, weight)
        self.defense = defense

    def use(self, character):
        if hasattr(character, 'defense'):
            character.defense += self.defense
            return f"{character.name} экипировал {self.name}, защита увеличена на {self.defense}"
        else:
            return f"{character.name} не может использовать {self.name} как броню"


class Potion(GameItem):
    def __init__(self, name, value=25, weight=0.5, healing_power=30):
        super().__init__(name, "potion", value, weight)
        self.healing_power = healing_power

    def use(self, character):
        if hasattr(character, 'health') and hasattr(character, 'max_health'):
            old_health = character.health
            character.health = min(character.max_health, character.health + self.healing_power)
            healed = character.health - old_health
            return f"{character.name} использовал {self.name} и восстановил {healed} здоровья"
        else:
            return f"{character.name} не может использовать {self.name} как зелье"


class ItemFactory:
    @staticmethod
    def create_item(item_type, name, value=0, **kwargs):
        """
        Создать предмет по типу
        """
        if item_type.lower() == "weapon":
            damage = kwargs.get('damage', 10)
            return Weapon(name, value, kwargs.get('weight', 3.0), damage)
        elif item_type.lower() == "armor":
            defense = kwargs.get('defense', 5)
            return Armor(name, value, kwargs.get('weight', 10.0), defense)
        elif item_type.lower() == "potion":
            healing_power = kwargs.get('healing_power', 30)
            return Potion(name, value, kwargs.get('weight', 0.5), healing_power)
        else:
            raise ValueError(f"Неизвестный тип предмета: {item_type}")
        

class Monster(ABC):
    """
    Абстрактный класс монстра
    """
    def __init__(self, name, health, attack_power, monster_type="common"):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack_power = attack_power
        self.monster_type = monster_type
        self.is_alive = True

    @abstractmethod
    def special_attack(self):
        pass

    def get_info(self):
        status = "жив" if self.is_alive else "мертв"
        return f"{self.name} ({self.monster_type}, {status}): HP {self.health}/{self.max_health}, ATK {self.attack_power}"

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.is_alive = False

    def attack(self, target):
        if self.is_alive and target.is_alive:
            target.take_damage(self.attack_power)
            return f"{self.name} атакует {target.name} на {self.attack_power} урона"
        else:
            return f"{self.name} не может атаковать"


class Goblin(Monster):
    """
    Класс гоблина
    """
    def __init__(self, name, health=30, attack_power=8, monster_type="goblin"):
        super().__init__(name, health, attack_power, monster_type)
        self.speed = 8

    def special_attack(self):
        return f"{self.name} быстро наносит двойной удар!"


class Orc(Monster):
    """
    Класс орка
    """
    def __init__(self, name, health=70, attack_power=15, monster_type="orc"):
        super().__init__(name, health, attack_power, monster_type)
        self.armor = 5

    def special_attack(self):
        return f"{self.name} яростно атакует с дополнительным уроном!"


class Dragon(Monster):
    """
    Класс дракона
    """
    def __init__(self, name, health=200, attack_power=30, monster_type="dragon"):
        super().__init__(name, health, attack_power, monster_type)
        self.fire_damage = 15

    def special_attack(self):
        return f"{self.name} испускает огненное дыхание!"


class MonsterFactory:
    """
    Фабрика для создания монстров
    """
    @staticmethod
    def create_monster(monster_type, name, health, attack_power):
        """
        Создать монстра по типу
        """
        if monster_type.lower() == "goblin":
            return Goblin(name, health, attack_power)
        elif monster_type.lower() == "orc":
            return Orc(name, health, attack_power)
        elif monster_type.lower() == "dragon":
            return Dragon(name, health, attack_power)
        else:
            raise ValueError(f"Неизвестный тип монстра: {monster_type}")
        
# Пример использования (после реализации)
weapon = ItemFactory.create_item("weapon", "Меч", 100)
armor = ItemFactory.create_item("armor", "Щит", 150)
potion = ItemFactory.create_item("potion", "Зелье", 25)
print(weapon.get_info())
print(armor.get_info())
print(potion.get_info())

goblin = MonsterFactory.create_monster("goblin", "Гоблин-воин", 30, 8)
orc = MonsterFactory.create_monster("orc", "Орк-берсерк", 70, 15)
dragon = MonsterFactory.create_monster("dragon", "Молодой дракон", 200, 30)
print(f"Монстр: {goblin.name}, здоровье: {goblin.health}, атака: {goblin.attack_power}")


class Observer(ABC):
    """
    Интерфейс наблюдателя для получения уведомлений об изменениях
    """
    @abstractmethod
    def update(self, event_type: str, data: dict = None):
        """
        Метод для получения уведомления об изменении
        """
        pass

class Subject(ABC):
    """
    Интерфейс субъекта, за которым могут наблюдать наблюдатели
    """
    def __init__(self):
        self._observers: List[Observer] = []

    def attach(self, observer: Observer):
        """Подписаться на уведомления"""
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer):
        """Отписаться от уведомлений"""
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, event_type: str, data: dict = None):
        """Уведомить всех наблюдателей об изменении"""
        for observer in self._observers:
            observer.update(event_type, data)


class Player(Subject):
    """
    Класс игрока, за которым могут наблюдать другие объекты
    """
    def __init__(self, name: str, health: int = 100):
        super().__init__()
        self.name = name
        self._health = health
        self._max_health = health
        self._level = 1
        self._experience = 0
        self.is_alive = True

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value: int):
        old_health = self._health
        self._health = max(0, min(self._max_health, value))
        if self._health <= 0:
            self._health = 0
            self.is_alive = False
            # Уведомляем наблюдателей о смерти игрока
            self.notify("player_died", {"player": self, "old_health": old_health, "new_health": self._health})
        elif old_health != self._health:
            # Уведомляем наблюдателей об изменении здоровья
            self.notify("player_health_changed", {"player": self, "old_health": old_health, "new_health": self._health})

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value: int):
        old_level = self._level
        self._level = value
        if self._level > old_level:
            # Уведомляем наблюдателей о повышении уровня
            self.notify("player_leveled_up", {"player": self, "old_level": old_level, "new_level": self._level})

    def take_damage(self, damage: int):
        """Получить урон"""
        self.health -= damage
        self.notify("player_damaged", {"player": self, "damage_amount": damage})

    def gain_experience(self, exp: int):
        """Получить опыт"""
        self._experience += exp
        self.notify("player_gained_experience", {"player": self, "exp_gained": exp, "total_exp": self._experience})
        # Проверяем, не пора ли повысить уровень
        required_exp = self._level * 100  # Упрощенная формула
        if self._experience >= required_exp:
            self.level_up()

    def level_up(self):
        """Повысить уровень игрока"""
        self._experience = 0  # Сбрасываем опыт при повышении уровня
        self._level += 1
        self._max_health += 20  # Увеличиваем максимальное здоровье
        self.health = self._max_health  # Полностью восстанавливаем здоровье
        self.level = self._level  # Вызываем сеттер для уведомления

    def get_info(self):
        return f"{self.name}: Lvl.{self._level}, HP {self._health}/{self._max_health}, EXP {self._experience}"


class HealthBarObserver(Observer):
    """
    Наблюдатель за изменением здоровья игрока
    """
    def update(self, event_type: str, data: dict = None):
        if event_type == "player_health_changed":
            player = data.get("player")
            if player:
                print(f"📊 Полоска здоровья {player.name}: {player.health}/{player._max_health}")


class LevelUpObserver(Observer):
    """
    Наблюдатель за повышением уровня игрока
    """
    def update(self, event_type: str, data: dict = None):
        if event_type == "player_leveled_up":
            player = data.get("player")
            if player:
                new_level = data.get("new_level", "N/A")
                print(f"📈 {player.name} достиг {new_level} уровня!")


class DeathObserver(Observer):
    """
    Наблюдатель за смертью игрока
    """
    def update(self, event_type: str, data: dict = None):
        if event_type == "player_died":
            player = data.get("player")
            old_health = data.get("old_health", 0)
            new_health = data.get("new_health", 0)
            
            if player:
                print(f"💀 {player.name} погибает! Было HP: {old_health}, стало HP: {new_health}")

death_observer = DeathObserver()
player = Player("Борис", health=50)
player.attach(death_observer)

print(f"Игрок: {player.get_info()}")
player.take_damage(60)
print(f"Игрок жив: {player.is_alive}")
class ExperienceObserver(Observer):
    """
    Наблюдатель за получением опыта
    """
    def update(self, event_type: str, data: dict = None):
        if event_type == "player_gained_experience":
            player = data.get("player")
            exp_gained = data.get("exp_gained", 0)
            total_exp = data.get("total_exp", 0)
            
            if player:
                print(f"⭐ {player.name} получил {exp_gained} опыта! Всего: {total_exp}")

# Пример использования (после реализации)
exp_observer = ExperienceObserver()
player = Player("Елена", health=100)
player.attach(exp_observer)

print(f"Игрок: {player.get_info()}")
player.gain_experience(75)
print(f"После получения опыта: {player.get_info()}")

class BattleStrategy(ABC):
    """
    Интерфейс боевой стратегии
    """
    @abstractmethod
    def execute_attack(self, attacker, target, environment=None):
        """
        Выполнить атаку с использованием данной стратегии
        """
        pass

    @abstractmethod
    def execute_defense(self, character, incoming_damage, environment=None):
        """
        Выполнить защиту с использованием данной стратегии
        """
        pass

class EventManager:
    """
    Менеджер событий для управления игровыми событиями
    """
    def __init__(self):
        self._event_handlers: Dict[str, List[Callable]] = {}

    def subscribe(self, event_type: str, handler: Callable):
        """Подписаться на событие определенного типа"""
        if event_type not in self._event_handlers:
            self._event_handlers[event_type] = []
        if handler not in self._event_handlers[event_type]:
            self._event_handlers[event_type].append(handler)

    def unsubscribe(self, event_type: str, handler: Callable):
        """Отписаться от события определенного типа"""
        if event_type in self._event_handlers:
            if handler in self._event_handlers[event_type]:
                self._event_handlers[event_type].remove(handler)
                if not self._event_handlers[event_type]:
                    del self._event_handlers[event_type]

    def trigger_event(self, event_type: str, data: dict = None):
        """Вызвать событие и уведомить всех подписчиков"""
        if event_type in self._event_handlers:
            handlers_copy = self._event_handlers[event_type].copy()
            for handler in handlers_copy:
                try:
                    handler(event_type, data)
                except Exception as e:
                    print(f"Ошибка при обработке события {event_type}: {e}")

    def get_subscribers_count(self, event_type: str) -> int:
        """Получить количество подписчиков на событие"""
        return len(self._event_handlers.get(event_type, []))


def player_damaged_handler(event_type: str, data: dict):
    """Обработчик события получения урона игроком"""
    if data and "player" in data and "damage_amount" in data:
        print(f" Игрок {data['player'].name} получил {data['damage_amount']} урона!")
        if hasattr(data['player'], 'health') and data['player'].health < data['player']._max_health * 0.3:
            print(f" {data['player'].name} находится в опасности!")

def enemy_defeated_handler(event_type: str, data: dict):
    """Обработчик события уничтожения врага"""
    if data and "enemy" in data:
        print(f" Враг {data['enemy'].name} повержен!")

def level_up_handler(event_type: str, data: dict):
    """Обработчик события повышения уровня"""
    if data and "player" in data and "new_level" in data:
        print(f" {data['player'].name} достиг {data['new_level']} уровня!")

class Player(Subject):
    """
    Улучшенный класс игрока с дополнительными параметрами
    """
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
    def health(self):
        return self._health

    @health.setter
    def health(self, value: int):
        old_health = self._health
        self._health = max(0, min(self._max_health, value))
        if self._health <= 0:
            self._health = 0
            self.is_alive = False
           
            self.notify("player_died", {"player": self, "old_health": old_health, "new_health": self._health})
        elif old_health != self._health:
           
            self.notify("player_health_changed", {"player": self, "old_health": old_health, "new_health": self._health})

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, value: int):
        old_mana = self._mana
        self._mana = max(0, min(self._max_mana, value))
        if old_mana != self._mana:
          
            self.notify("player_mana_changed", {"player": self, "old_mana": old_mana, "new_mana": self._mana})

    @property
    def stamina(self):
        return self._stamina

    @stamina.setter
    def stamina(self, value: int):
        old_stamina = self._stamina
        self._stamina = max(0, min(self._max_stamina, value))
        if old_stamina != self._stamina:
          
            self.notify("player_stamina_changed", {"player": self, "old_stamina": old_stamina, "new_stamina": self._stamina})

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value: int):
        old_level = self._level
        self._level = value
        if self._level > old_level:
           
            self.notify("player_leveled_up", {"player": self, "old_level": old_level, "new_level": self._level})

    def take_damage(self, damage: int):
        """Получить урон"""
        
        actual_damage = max(1, damage - self._armor)
        self.health -= actual_damage
        self.notify("player_damaged", {"player": self, "damage_amount": actual_damage, "armor_reduced": self._armor})

    def gain_experience(self, exp: int):
        """Получить опыт"""
        self._experience += exp
        self.notify("player_gained_experience", {"player": self, "exp_gained": exp, "total_exp": self._experience})
        
        required_exp = self._level * 100  
        if self._experience >= required_exp:
            self.level_up()

    def level_up(self):
        """Повысить уровень игрока"""
        self._experience = 0  
        self._level += 1
        self._max_health += 20  
        self._max_mana += 15  
        self._max_stamina += 10 
        self.health = self._max_health  
        self.mana = self._max_mana    
        self.stamina = self._max_stamina 
        self._armor += 2 
        self.level = self._level

    def use_mana(self, amount: int):
        """Использовать ману"""
        if self._mana >= amount:
            old_mana = self._mana
            self._mana -= amount
            self.notify("player_mana_used", {"player": self, "mana_used": amount, "old_mana": old_mana, "new_mana": self._mana})
            return True
        else:
            self.notify("player_not_enough_mana", {"player": self, "required_mana": amount, "available_mana": self._mana})
            return False

    def use_stamina(self, amount: int):
        """Использовать выносливость"""
        if self._stamina >= amount:
            old_stamina = self._stamina
            self._stamina -= amount
            self.notify("player_stamina_used", {"player": self, "stamina_used": amount, "old_stamina": old_stamina, "new_stamina": self._stamina})
            return True
        else:
            self.notify("player_not_enough_stamina", {"player": self, "required_stamina": amount, "available_stamina": self._stamina})
            return False

    def get_info(self):
        return f"{self.name}: Lvl.{self._level}, HP {self._health}/{self._max_health}, MP {self._mana}/{self._max_mana}, STA {self._stamina}/{self._max_stamina}, EXP {self._experience}, ARMOR {self._armor}"
    


class AsyncObserver(ABC):
    """
    Асинхронный наблюдатель
    """
    @abstractmethod
    async def update_async(self, event_type: str, data: dict = None):
        """
        Асинхронное обновление при получении уведомления
        """
        pass


class AsyncSubject:
    """
    Асинхронный субъект, за которым могут наблюдать
    """
    def __init__(self):
        self._async_observers: List[AsyncObserver] = []

    def attach_async(self, observer: AsyncObserver):
        """Подписаться на асинхронные уведомления"""
        if observer not in self._async_observers:
            self._async_observers.append(observer)

    def detach_async(self, observer: AsyncObserver):
        """Отписаться от асинхронных уведомлений"""
        if observer in self._async_observers:
            self._async_observers.remove(observer)

    async def notify_async(self, event_type: str, data: dict = None):
        """
        Асинхронно уведомить всех наблюдателей
        """
        tasks = []
        for observer in self._async_observers:
            task = asyncio.create_task(observer.update_async(event_type, data))
            tasks.append(task)
        
       
        if tasks:
            results = await asyncio.gather(*tasks, return_exceptions=True)
         
            for i, result in enumerate(results):
                if isinstance(result, Exception):
                    print(f"Ошибка в наблюдателе {i}: {result}")


class AsyncBattleLogger(AsyncObserver):
    """
    Асинхронный логгер боевых действий
    """
    def __init__(self, filename: str = "battle_log.txt"):
        self.filename = filename
        self.log_entries = []

    async def update_async(self, event_type: str, data: dict = None):
        """
        Обработать событие асинхронно и записать в лог
        """
        import time
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {event_type}: {data}"
        self.log_entries.append(log_entry)
        print(f"[ASYNC_LOGGER] Записано: {log_entry}")
        
    
        await asyncio.sleep(0.05)  


class AsyncAchievementNotifier(AsyncObserver):
    """
    Асинхронный обработчик достижений
    """
    def __init__(self):
        self.unlocked_achievements = []

    async def update_async(self, event_type: str, data: dict = None):
        """
        Обработать событие и проверить достижения
        """
       
        await asyncio.sleep(0.1)  
        
        if event_type == "player_damaged" and data and data.get("damage_amount", 0) >= 50:
            achievement = "Выносливость: Выдержал сильный удар"
            self.unlocked_achievements.append(achievement)
            print(f"[ASYNC_ACHIEVEMENT] Разблокировано достижение: {achievement}")
        elif event_type == "player_leveled_up" and data and data.get("new_level", 0) >= 10:
            achievement = "Опытный воин: Достиг 10 уровня"
            self.unlocked_achievements.append(achievement)
            print(f"[ASYNC_ACHIEVEMENT] Разблокировано достижение: {achievement}")



async def test_async_observer():
    subject = AsyncSubject()
    
    logger = AsyncBattleLogger()
    achievements = AsyncAchievementNotifier()
    
    subject.attach_async(logger)
    subject.attach_async(achievements)
    
    print("=== Асинхронная симуляция событий ===")
    
 
    await subject.notify_async("player_damaged", {"player": "Артур", "damage_amount": 25})
    await subject.notify_async("player_leveled_up", {"player": "Артур", "new_level": 10})
    await subject.notify_async("player_gained_experience", {"player": "Артур", "exp_gained": 150})
    
    print(f"\nЗаписи в логе: {len(logger.log_entries)}")
    print(f"Разблокированные достижения: {len(achievements.unlocked_achievements)}")
    for achievement in achievements.unlocked_achievements:
        print(f"  - {achievement}")

class Character:
    """
    Класс игрового персонажа как контекст для боевых стратегий
    """
    def __init__(self, name: str, health: int = 100, attack_power: int = 20, defense: int = 5, character_class: str = "warrior"):
        self.name = name
        self._health = health
        self.max_health = health
        self.attack_power = attack_power
        self.defense = defense
        self.character_class = character_class
        self.level = 1
        self.is_alive = True
        self._battle_strategy: BattleStrategy = None

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value: int):
        self._health = max(0, min(self.max_health, value))
        if self._health <= 0:
            self._health = 0
            self.is_alive = False

    def set_battle_strategy(self, strategy: BattleStrategy):
        """Установить боевую стратегию"""
        self._battle_strategy = strategy

    def perform_attack(self, target, environment=None):
        """Выполнить атаку с использованием текущей стратегии"""
        if self._battle_strategy and self.is_alive and target.is_alive:
            return self._battle_strategy.execute_attack(self, target, environment)
        else:
            return f"{self.name} не может атаковать (мертв или нет цели)"

    def perform_defense(self, incoming_damage, environment=None):
        """Выполнить защиту с использованием текущей стратегии"""
        if self._battle_strategy and self.is_alive:
            return self._battle_strategy.execute_defense(self, incoming_damage, environment)
        else:
            self.health -= incoming_damage
            return f"{self.name} получает {incoming_damage} урона (без стратегии защиты)"

    def get_info(self):
        """Получить информацию о персонаже"""
        status = "жив" if self.is_alive else "мертв"
        return f"{self.name} ({self.character_class}, {status}): Lvl.{self.level}, HP {self.health}/{self.max_health}, ATK {self.attack_power}, DEF {self.defense}"

    def take_damage(self, damage: int):
        """Получить урон"""
        actual_damage = max(1, damage - self.defense)
        self.health -= actual_damage
        return actual_damage


class AggressiveStrategy(BattleStrategy):
    """
    Агрессивная боевая стратегия - наносит максимальный урон, но плохо защищается
    """
    def execute_attack(self, attacker, target, environment=None):
        enhanced_damage = int(attacker.attack_power * 1.2)
        actual_damage = target.take_damage(enhanced_damage)
        return f"{attacker.name} агрессивно атакует {target.name} на {actual_damage} урона!"

    def execute_defense(self, character, incoming_damage, environment=None):
        actual_damage = max(1, incoming_damage - character.defense * 0.5)
        character.health -= actual_damage
        return f"{character.name} получает {actual_damage} урона (агрессивная стратегия - минимальная защита)"


class DefensiveStrategy(BattleStrategy):
    """
    Защитная боевая стратегия - фокусируется на защите, наносит меньше урона
    """
    def execute_attack(self, attacker, target, environment=None):
        reduced_damage = int(attacker.attack_power * 0.8)
        actual_damage = target.take_damage(reduced_damage)
        return f"{attacker.name} осторожно атакует {target.name} на {actual_damage} урона!"

    def execute_defense(self, character, incoming_damage, environment=None):
        actual_damage = max(1, incoming_damage - character.defense * 1.5)
        character.health -= actual_damage
        return f"{character.name} защищается, получает {actual_damage} урона (защитная стратегия)"


class BalancedStrategy(BattleStrategy):
    """
    Сбалансированная боевая стратегия - средний урон и средняя защита
    """
    def execute_attack(self, attacker, target, environment=None):
        actual_damage = target.take_damage(attacker.attack_power)
        return f"{attacker.name} сбалансированно атакует {target.name} на {actual_damage} урона!"

    def execute_defense(self, character, incoming_damage, environment=None):
        actual_damage = max(1, incoming_damage - character.defense)
        character.health -= actual_damage
        return f"{character.name} защищается стандартно, получает {actual_damage} урона"


class BalancedStrategy(BattleStrategy):
    """
    Сбалансированная боевая стратегия - средний урон и средняя защита
    """
    def execute_attack(self, attacker, target, environment=None):
        actual_damage = target.take_damage(attacker.attack_power)
        return f"{attacker.name} сбалансированно атакует {target.name} на {actual_damage} урона!"

    def execute_defense(self, character, incoming_damage, environment=None):
        actual_damage = max(1, incoming_damage - character.defense)
        character.health -= actual_damage
        return f"{character.name} защищается стандартно, получает {actual_damage} урона"
        
balanced_strategy = BalancedStrategy()
player = Character("Баланс", health=100, attack_power=20, defense=5)
enemy = Character("Враг", health=100, attack_power=15, defense=3)

player.set_battle_strategy(balanced_strategy)

print(f"Игрок: {player.get_info()}")
print(f"Враг: {enemy.get_info()}")

result = player.perform_attack(enemy)
print(f"Результат атаки: {result}")

result = player.perform_defense(25)
print(f"Результат защиты: {result}")

print(f"\nПосле действий:")
print(f"Игрок: {player.get_info()}")
print(f"Враг: {enemy.get_info()}")

class HealingStrategy(BattleStrategy):

    """
    Стратегия лечения - персонаж восстанавливает здоровье вместо атаки
    """
    def execute_attack(self, attacker, target, environment=None):
        heal_amount = min(20, attacker.max_health - attacker.health)
        old_health = attacker.health
        attacker.health += heal_amount
        healed = attacker.health - old_health
        return f"{attacker.name} использует лечение и восстанавливает {healed} здоровья!"

    def execute_defense(self, character, incoming_damage, environment=None):
        actual_damage = max(1, incoming_damage - character.defense)
        character.health -= actual_damage
        if character.health < character.max_health:
            heal_amount = min(5, character.max_health - character.health)
            character.health += heal_amount
            return f"{character.name} защищается и восстанавливает {heal_amount} здоровья, получает {actual_damage} урона"
        else:
            return f"{character.name} защищается, получает {actual_damage} урона"

healing_strategy = HealingStrategy()
healer = Character("Лекарь", health=80, attack_power=10, defense=3)
enemy = Character("Враг", health=100, attack_power=20, defense=2)

healer.set_battle_strategy(healing_strategy)

print(f"Лекарь: {healer.get_info()}")
print(f"Враг: {enemy.get_info()}")

result = healer.perform_attack(enemy)
print(f"Результат: {result}")

print(f"\nПосле действия:")
print(f"Лекарь: {healer.get_info()}")
print(f"Враг: {enemy.get_info()}")

class BalancedStrategy(BattleStrategy):
    """
    Сбалансированная боевая стратегия - средний урон и средняя защита
    """
    def execute_attack(self, attacker, target, environment=None):
        
        actual_damage = target.take_damage(attacker.attack_power)
        return f"{attacker.name} сбалансированно атакует {target.name} на {actual_damage} урона!"

    def execute_defense(self, character, incoming_damage, environment=None):
       
        actual_damage = max(1, incoming_damage - character.defense)
        character.health -= actual_damage
        return f"{character.name} защищается стандартно, получает {actual_damage} урона"
   # balanced_strategy = BalancedStrategy()
player = Character("Баланс", health=100, attack_power=20, defense=5)
enemy = Character("Враг", health=100, attack_power=15, defense=3)

player.set_battle_strategy(balanced_strategy)

print(f"Игрок: {player.get_info()}")
print(f"Враг: {enemy.get_info()}")

# Выполняем атаку
result = player.perform_attack(enemy)
print(f"Результат атаки: {result}")

# Выполняем защиту
result = player.perform_defense(25)
print(f"Результат защиты: {result}")

print(f"\nПосле действий:")
print(f"Игрок: {player.get_info()}")
print(f"Враг: {enemy.get_info()}") 
class HealingStrategy(BattleStrategy):

    """
    Стратегия лечения - персонаж восстанавливает здоровье вместо атаки
    """
    def execute_attack(self, attacker, target, environment=None):
        heal_amount = min(20, attacker.max_health - attacker.health)
        old_health = attacker.health
        attacker.health += heal_amount
        healed = attacker.health - old_health
        return f"{attacker.name} использует лечение и восстанавливает {healed} здоровья!"

    def execute_defense(self, character, incoming_damage, environment=None):
        actual_damage = max(1, incoming_damage - character.defense)
        character.health -= actual_damage
        
        if character.health < character.max_health:
            heal_amount = min(5, character.max_health - character.health)
            character.health += heal_amount
            return f"{character.name} защищается и восстанавливает {heal_amount} здоровья, получает {actual_damage} урона"
        else:
            return f"{character.name} защищается, получает {actual_damage} урона"
healing_strategy = HealingStrategy()
healer = Character("Лекарь", health=80, attack_power=10, defense=3)
enemy = Character("Враг", health=100, attack_power=20, defense=2)

healer.set_battle_strategy(healing_strategy)

print(f"Лекарь: {healer.get_info()}")
print(f"Враг: {enemy.get_info()}")

# Выполняем "атаку" (на самом деле лечение)
result = healer.perform_attack(enemy)
print(f"Результат: {result}")

print(f"\nПосле действия:")
print(f"Лекарь: {healer.get_info()}")
print(f"Враг: {enemy.get_info()}")