import json
from pathlib import Path
from datetime import datetime
import xml.etree.ElementTree as ET

class GameConfig:
    """
    Система конфигурации игры через JSON-файл
    """
    def __init__(self, config_file="config.json"):
        self.config_file = Path(config_file)
        self.default_config = {
            "resolution": {
                "width": 1920,
                "height": 1080
            },
            "graphics": {
                "quality": "high",
                "vsync": True,
                "anti_aliasing": "4x"
            },
            "audio": {
                "master_volume": 0.8,
                "music_volume": 0.7,
                "sfx_volume": 1.0
            },
            "controls": {
                "mouse_sensitivity": 5.0,
                "key_bindings": {
                    "move_forward": "W",
                    "move_backward": "S",
                    "move_left": "A",
                    "move_right": "D",
                    "jump": "SPACE",
                    "inventory": "TAB"
                }
            },
            "gameplay": {
                "difficulty": "normal",
                "language": "en",
                "subtitles": True
            }
        }
        self.config = self.load_config()
    
    def load_config(self):
        """
        Загружает конфигурацию из файла
        
        Returns:
            dict: Словарь конфигурации
        """
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    loaded_config = json.load(f)
                merged_config = self.merge_configs(self.default_config, loaded_config)
                return merged_config
            except json.JSONDecodeError:
                print(f"Ошибка чтения конфигурации из {self.config_file}, используется значение по умолчанию")
                return self.default_config
        else:
            self.save_config()
            return self.default_config
    
    def save_config(self):
        """
        Сохраняет текущую конфигурацию в файл
        """
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=2, ensure_ascii=False)
    
    def get_setting(self, *keys):
        """
        Возвращает значение настройки по цепочке ключей
        
        Args:
            *keys: Ключи для доступа к настройке
            
        Returns:
            значение: Значение настройки
        """
        value = self.config
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return None
        return value
    
    def set_setting(self, value, *keys):
        """
        Устанавливает значение настройки по цепочке ключей
        
        Args:
            value: Значение для установки
            *keys: Ключи для доступа к настройке
        """
        config_ref = self.config
        for key in keys[:-1]:
            if key not in config_ref or not isinstance(config_ref[key], dict):
                config_ref[key] = {}
            config_ref = config_ref[key]
        
        config_ref[keys[-1]] = value
    
    def merge_configs(self, default, override):
        """
        Объединяет конфигурации, заполняя отсутствующие поля значениями по умолчанию
        
        Args:
            default (dict): Конфигурация по умолчанию
            override (dict): Переопределяющая конфигурация
            
        Returns:
            dict: Объединенная конфигурация
        """
        result = default.copy()
        
        for key, value in override.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = self.merge_configs(result[key], value)
            else:
                result[key] = value
        
        return result
    

class PlayerProgressManager:
    """
    Система управления сохранением и загрузкой прогресса игрока
    """
    def __init__(self, saves_directory="saves"):
        self.saves_directory = Path(saves_directory)
        self.saves_directory.mkdir(exist_ok=True)
    
    def save_player_progress(self, player, save_name):
        """
        Сохраняет прогресс игрока в JSON-файл
        
        Args:
            player (object): Объект игрока
            save_name (str): Имя сохранения
        """
        save_path = self.saves_directory / f"{save_name}.json"
        
        player_data = player.to_dict()
        player_data['save_date'] = datetime.now().isoformat()
        
        with open(save_path, 'w', encoding='utf-8') as f:
            json.dump(player_data, f, indent=2, ensure_ascii=False)
    
    def load_player_progress(self, save_name):
        """
        Загружает прогресс игрока из JSON-файла
        
        Args:
            save_name (str): Имя сохранения для загрузки
            
        Returns:
            object: Загруженный объект игрока
        """
        save_path = self.saves_directory / f"{save_name}.json"
        
        if not save_path.exists():
            return None
        
        try:
            with open(save_path, 'r', encoding='utf-8') as f:
                player_data = json.load(f)
            player_data['last_played'] = datetime.now()
            
            return Player.from_dict(player_data)
        except json.JSONDecodeError:
            print(f"Ошибка чтения сохранения: {save_path}")
            return None
    
    def list_saves(self):
        """
        Возвращает список доступных сохранений
        
        Returns:
            list: Список имен файлов сохранений
        """
        save_files = list(self.saves_directory.glob("*.json"))
        save_names = [f.stem for f in save_files]
        return sorted(save_names, reverse=True)
    
    def delete_save(self, save_name):
        """
        Удаляет файл сохранения
        
        Args:
            save_name (str): Имя сохранения для удаления
        """
        save_path = self.saves_directory / f"{save_name}.json"
        if save_path.exists():
            save_path.unlink()
            return True
        return False

class Player:
    def __init__(self, name, level=1, health=100, position=(0, 0)):
        self.name = name
        self.level = level
        self.health = health
        self.max_health = 100
        self.position = position
        self.inventory = []
        self.stats = {
            'strength': 10,
            'agility': 10,
            'intelligence': 10
        }
        self.play_time = 0
        self.creation_date = datetime.now()
        self.last_played = datetime.now()
    
    def to_dict(self):
        """
        Преобразует игрока в словарь для сохранения в JSON
        """
        return {
            'name': self.name,
            'level': self.level,
            'health': self.health,
            'max_health': self.max_health,
            'position': self.position,
            'inventory': self.inventory,
            'stats': self.stats,
            'play_time': self.play_time,
            'creation_date': self.creation_date.isoformat(),
            'last_played': self.last_played.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        Создает игрока из словаря
        
        Args:
            data (dict): Словарь с данными игрока
        """
        creation_date = datetime.fromisoformat(data['creation_date'])
        last_played = datetime.fromisoformat(data['last_played'])
        
        player = cls(
            name=data['name'],
            level=data['level'],
            health=data['health'],
            position=tuple(data['position'])
        )
        
        player.max_health = data['max_health']
        player.inventory = data['inventory']
        player.stats = data['stats']
        player.play_time = data['play_time']
        player.creation_date = creation_date
        player.last_played = last_played
        
        return player
    



class GameConfig:
    """
    Система конфигурации игры через XML-файл
    """
    def __init__(self, config_file="config.xml"):
        self.config_file = Path(config_file)
        self.default_config = {
            "resolution": {
                "width": 1920,
                "height": 1080
            },
            "graphics": {
                "quality": "high",
                "vsync": True,
                "anti_aliasing": "4x"
            },
            "audio": {
                "master_volume": 0.8,
                "music_volume": 0.7,
                "sfx_volume": 1.0
            },
            "controls": {
                "mouse_sensitivity": 5.0,
                "key_bindings": {
                    "move_forward": "W",
                    "move_backward": "S",
                    "move_left": "A",
                    "move_right": "D",
                    "jump": "SPACE",
                    "inventory": "TAB"
                }
            },
            "gameplay": {
                "difficulty": "normal",
                "language": "en",
                "subtitles": True
            }
        }
        self.root = self.load_config()
    
    def load_config(self):
        """
        Загружает конфигурацию из XML-файла
        
        Returns:
            Element: Корневой элемент XML-документа
        """
        if self.config_file.exists():
            try:
                tree = ET.parse(self.config_file)
                root = tree.getroot()
                return root
            except ET.ParseError:
                print(f"Ошибка чтения конфигурации из {self.config_file}, используется значение по умолчанию")
                return self.create_default_config()
        else:
            root = self.create_default_config()
            self.save_config()
            return root
    
    def create_default_config(self):
        """
        Создает XML-дерево с конфигурацией по умолчанию
        
        Returns:
            Element: Корневой элемент XML-документа
        """
        root = ET.Element("config")
        
        self.add_config_section(root, self.default_config)
        
        return root
    
    def add_config_section(self, parent, config_dict):
        """
        Рекурсивно добавляет разделы конфигурации в XML
        
        Args:
            parent: Родительский элемент
            config_dict: Словарь конфигурации
        """
        for key, value in config_dict.items():
            if isinstance(value, dict):
                section = ET.SubElement(parent, key)
                self.add_config_section(section, value)
            else:
                element = ET.SubElement(parent, key)
                element.text = str(value)
    
    def save_config(self):
        """
        Сохраняет текущую конфигурацию в XML-файл
        """
        tree = ET.ElementTree(self.root)
        tree.write(self.config_file, encoding="utf-8", xml_declaration=True)
    
    def get_setting(self, *keys):
        """
        Возвращает значение настройки по цепочке ключей
        
        Args:
            *keys: Ключи для доступа к настройке
            
        Returns:
            значение: Значение настройки
        """
        current = self.root
        for key in keys:
            current = current.find(key)
            if current is None:
                return None
        
        if current.text is not None:
            text = current.text.strip()
            if text.lower() in ['true', 'false']:
                return text.lower() == 'true'
            elif text.isdigit():
                return int(text)
            else:
                try:
                    return float(text)
                except ValueError:
                    return text
        else:
            if len(current) > 0:
                return current
            else:
                return None
    
    def set_setting(self, value, *keys):
        """
        Устанавливает значение настройки по цепочке ключей
        
        Args:
            value: Значение для установки
            *keys: Ключи для доступа к настройке
        """
        current = self.root
        for key in keys[:-1]:
            child = current.find(key)
            if child is None:
                child = ET.SubElement(current, key)
            current = child
        
        last_key = keys[-1]
        target_element = current.find(last_key)
        if target_element is None:
            target_element = ET.SubElement(current, last_key)
        
        target_element.text = str(value)


class PlayerProgressManager:
    """
    Система управления сохранением и загрузкой прогресса игрока
    """
    def __init__(self, saves_directory="saves"):
        self.saves_directory = Path(saves_directory)
        self.saves_directory.mkdir(exist_ok=True)
    
    def save_player_progress(self, player, save_name):
        """
        Сохраняет прогресс игрока в XML-файл
        
        Args:
            player (object): Объект игрока
            save_name (str): Имя сохранения
        """
        save_path = self.saves_directory / f"{save_name}.xml"
        
        root = player.to_xml()
        
        save_date_elem = ET.SubElement(root, "save_date")
        save_date_elem.text = datetime.now().isoformat()
        
        tree = ET.ElementTree(root)
        tree.write(save_path, encoding="utf-8", xml_declaration=True)
    
    def load_player_progress(self, save_name):
        """
        Загружает прогресс игрока из XML-файла
        
        Args:
            save_name (str): Имя сохранения для загрузки
            
        Returns:
            object: Загруженный объект игрока
        """
        save_path = self.saves_directory / f"{save_name}.xml"
        
        if not save_path.exists():
            return None
        
        try:
            tree = ET.parse(save_path)
            root = tree.getroot()
            
            player = Player.from_xml(root)
            player.last_played = datetime.now()
            
            return player
        except ET.ParseError:
            print(f"Ошибка чтения сохранения: {save_path}")
            return None
    
    def list_saves(self):
        """
        Возвращает список доступных сохранений
        
        Returns:
            list: Список имен файлов сохранений
        """
        save_files = list(self.saves_directory.glob("*.xml"))
        save_names = [f.stem for f in save_files]
        return sorted(save_names, reverse=True)
    
    def delete_save(self, save_name):
        """
        Удаляет файл сохранения
        
        Args:
            save_name (str): Имя сохранения для удаления
        """
        save_path = self.saves_directory / f"{save_name}.xml"
        if save_path.exists():
            save_path.unlink()
            return True
        return False

class Player:
    def __init__(self, name, level=1, health=100, position_x=0, position_y=0):
        self.name = name
        self.level = level
        self.health = health
        self.max_health = 100
        self.position_x = position_x
        self.position_y = position_y
        self.inventory = []
        self.stats = {
            'strength': 10,
            'agility': 10,
            'intelligence': 10
        }
        self.play_time = 0
        self.creation_date = datetime.now()
        self.last_played = datetime.now()
    
    def to_xml(self):
        """
        Преобразует игрока в XML-элемент
        """
        player_elem = ET.Element("player")
        
        name_elem = ET.SubElement(player_elem, "name")
        name_elem.text = self.name
        
        level_elem = ET.SubElement(player_elem, "level")
        level_elem.text = str(self.level)
        
        health_elem = ET.SubElement(player_elem, "health")
        health_elem.text = str(self.health)
        
        max_health_elem = ET.SubElement(player_elem, "max_health")
        max_health_elem.text = str(self.max_health)
        
        pos_x_elem = ET.SubElement(player_elem, "position_x")
        pos_x_elem.text = str(self.position_x)
        
        pos_y_elem = ET.SubElement(player_elem, "position_y")
        pos_y_elem.text = str(self.position_y)
        
        play_time_elem = ET.SubElement(player_elem, "play_time")
        play_time_elem.text = str(self.play_time)
        
        creation_date_elem = ET.SubElement(player_elem, "creation_date")
        creation_date_elem.text = self.creation_date.isoformat()
        
        last_played_elem = ET.SubElement(player_elem, "last_played")
        last_played_elem.text = self.last_played.isoformat()
        
        inventory_elem = ET.SubElement(player_elem, "inventory")
        for item in self.inventory:
            item_elem = ET.SubElement(inventory_elem, "item")
            item_elem.text = str(item)
        
        stats_elem = ET.SubElement(player_elem, "stats")
        for stat_name, stat_value in self.stats.items():
            stat_elem = ET.SubElement(stats_elem, stat_name)
            stat_elem.text = str(stat_value)
        
        return player_elem
    
    @classmethod
    def from_xml(cls, xml_element):
        """
        Создает игрока из XML-элемента
        
        Args:
            xml_element: XML-элемент игрока
        """
        name = xml_element.find("name").text
        level = int(xml_element.find("level").text)
        health = int(xml_element.find("health").text)
        max_health = int(xml_element.find("max_health").text)
        position_x = float(xml_element.find("position_x").text)
        position_y = float(xml_element.find("position_y").text)
        play_time = float(xml_element.find("play_time").text)

        player = cls(name, level, health, position_x, position_y)
        player.max_health = max_health
        player.play_time = play_time
        
        creation_date_str = xml_element.find("creation_date").text
        last_played_str = xml_element.find("last_played").text
        player.creation_date = datetime.fromisoformat(creation_date_str)
        player.last_played = datetime.fromisoformat(last_played_str)
        
        inventory_elem = xml_element.find("inventory")
        if inventory_elem is not None:
            player.inventory = [item.text for item in inventory_elem.findall("item")]
        
        stats_elem = xml_element.find("stats")
        if stats_elem is not None:
            for stat_elem in stats_elem:
                player.stats[stat_elem.tag] = int(stat_elem.text)
        
        return player