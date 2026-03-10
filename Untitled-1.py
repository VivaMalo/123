import json
from datetime import datetime
from pathlib import Path



class PlayerProgressManager:
    def __init__(self, saves_directory="saves"):
        self.saves_directory = Path(saves_directory)
        self.saves_directory.mkdir(exist_ok=True)

    def save_player_progress(self, player, save_name):
        save_path = self.saves_directory / f"{save_name}.json"
        player_data = player.to_dict()
        player_data['save_date'] = datetime.now().isoformat()
        with open(save_path, 'w', encoding='utf-8') as f:
            json.dump(player_data, f, indent=2, ensure_ascii=False)

    def load_player_progress(self, save_name):
        save_path = self.saves_directory / f"{save_name}.json"
        if not save_path.exists(): 
            return None
        try:
            with open(save_path, 'r', encoding='utf-8') as f:
                player_data = json.load(f)
            
                return Player.from_dict(player_data)
        except json.JSONDecodeError:
            print(f"Ошибка чтения сохранения: {save_path}")
            return None

    def list_saves(self):
        save_files = list(self.saves_directory.glob("*.json"))
        save_names = [f.stem for f in save_files]
        return sorted(save_names, reverse=True)



class Player:


    def to_dict(self):
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
        creation_date = datetime.fromisoformat(data['creation_date'])
        last_played = datetime.fromisoformat(data['last_played'])

        player = cls(
            name=data['name'],
            level=data['level'],
            health=data['health'],
            position=tuple(data['position'])
        )
        player.max_health = data.get('max_health', 100)
        player.inventory = data.get('inventory', [])
        player.stats = data.get('stats', {'strength': 10, 'agility': 10, 'intelligence': 10})
        player.play_time = data.get('play_time', 0)
        player.creation_date = creation_date
        player.last_played = last_played

        return player