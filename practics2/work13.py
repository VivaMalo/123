# 1.1
# class ResourceManager:
#     _instance = None  # Приватный атрибут для хранения единственного экземпляра

#     def __new__(cls, *args, **kwargs):
#         # Если экземпляр еще не создан, создаем его
#         if cls._instance is None:
#             cls._instance = super(ResourceManager, cls).__new__(cls)
#             # Инициализируем словарь ресурсов только один раз
#             cls._instance.resources = {}
#         return cls._instance

#     def load_resource(self, resource_name, resource_path):
#         """Имитация загрузки ресурса"""
#         self.resources[resource_name] = f"Data from {resource_path}"
#         print(f"Ресурс '{resource_name}' загружен.")

#     def get_resource(self, resource_name):
#         """Получение ресурса из кэша"""
#         resource = self.resources.get(resource_name)
#         if resource:
#             return resource
#         print(f"Ресурс '{resource_name}' не найден.")
#         return None

#     def unload_resource(self, resource_name):
#         """Удаление ресурса из памяти"""
#         if resource_name in self.resources:
#             del self.resources[resource_name]
#             print(f"Ресурс '{resource_name}' выгружен.")
#         else:
#             print(f"Ошибка: Ресурс '{resource_name}' не существует.")

# # --- Тестирование ---
# rm1 = ResourceManager()
# rm2 = ResourceManager()

# print(f"Одинаковые экземпляры: {rm1 is rm2}")  # Должно вывести True

# rm1.load_resource("background", "/assets/background.png")

# # Пытаемся получить ресурс через другой объект (rm2)
# resource = rm2.get_resource("background")
# print(f"Ресурс получен через rm2: {resource is not None}")

# rm2.unload_resource("background")
# print(f"Проверка после выгрузки: {rm1.get_resource('background')}")

# 1.2
# class GameLogger:
#     _instance = None  # Ссылка на единственный экземпляр

#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super(GameLogger, cls).__new__(cls)
#             # Инициализируем список для хранения логов один раз
#             cls._instance.history = []
#         return cls._instance

#     def log(self, message, level="INFO"):
#         """Записывает сообщение с указанным уровнем важности"""
#         entry = {"message": message, "level": level.upper()}
#         self.history.append(entry)
#         print(f"[{entry['level']}] {entry['message']}")

#     def get_logs(self, level_filter=None):
#         """Возвращает список логов, опционально фильтруя по уровню"""
#         if level_filter:
#             level_filter = level_filter.upper()
#             return [entry for entry in self.history if entry["level"] == level_filter]
#         return self.history

#     def clear_logs(self):
#         """Очищает всю историю сообщений"""
#         self.history.clear()
#         print("История логов очищена.")

# # --- Тестирование ---
# logger1 = GameLogger()
# logger2 = GameLogger()

# print(f"Одинаковые экземпляры: {logger1 is logger2}")  # True

# logger1.log("Игра запущена", "INFO")
# logger2.log("Низкий уровень здоровья!", "WARNING")
# logger2.log("Ошибка загрузки уровня", "ERROR")

# print("\nВсе логи через logger1:")
# for entry in logger1.get_logs():
#     print(f" - {entry}")

# print("\nТолько ошибки через logger2:")
# print(logger2.get_logs(level_filter="ERROR"))

# logger1.clear_logs()
# print(f"Количество логов после очистки: {len(logger2.get_logs())}")

# 2.1
# import threading

# class ThreadSafeResourceManager:
#     _instance = None
#     _lock = threading.Lock()  # Глобальная блокировка для создания экземпляра

#     def __new__(cls, *args, **kwargs):
#         # Первая проверка (без блокировки для скорости)
#         if cls._instance is None:
#             with cls._lock:
#                 # Вторая проверка (под блокировкой)
#                 if cls._instance is None:
#                     cls._instance = super(ThreadSafeResourceManager, cls).__new__(cls)
#                     cls._instance.resources = {}
#                     cls._instance.res_lock = threading.Lock() # Локальная блокировка для данных
#         return cls._instance

#     def load_resource(self, resource_name, resource_path):
#         # Блокировка при записи, чтобы избежать гонки данных
#         with self.res_lock:
#             self.resources[resource_name] = f"Data({resource_path})"
#             print(f"Загружен: {resource_name}")

#     def get_resource(self, resource_name):
#         # Блокировка при чтении
#         with self.res_lock:
#             return self.resources.get(resource_name)

#     def get_loaded_resources_count(self):
#         with self.res_lock:
#             return len(self.resources)

# def create_resource_manager(results, idx):
#     """Функция для создания экземпляра в отдельном потоке"""
#     manager = ThreadSafeResourceManager()
#     results[idx] = manager

# # --- Тестирование ---
# threads = []
# results = [None] * 10  # Увеличим количество потоков для надежности теста

# for i in range(10):
#     t = threading.Thread(target=create_resource_manager, args=(results, i))
#     threads.append(t)

# for t in threads:
#     t.start()

# for t in threads:
#     t.join()

# # Проверка результатов
# ids = [id(r) for r in results]
# print(f"ID всех экземпляров: {ids}")
# print(f"Все ID одинаковы: {len(set(ids)) == 1}")

# # Проверка работы методов
# rm = ThreadSafeResourceManager()
# rm.load_resource("map_01", "/assets/map.tmx")
# print(f"Всего ресурсов: {rm.get_loaded_resources_count()}")

2.2
import threading

class SingletonMeta(type):
    """Метакласс для создания потокобезопасного Singleton."""
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        # Двойная проверка блокировки для эффективности
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    # Создаем экземпляр, если его еще нет
                    instance = super().__call__(*args, **kwargs)
                    cls._instances[cls] = instance
        return cls._instances[cls]

class GameSettings(metaclass=SingletonMeta):
    def __init__(self):
        # Инициализируем настройки по умолчанию
        self._settings = {
            "volume": 50,
            "resolution": (1280, 720),
            "fullscreen": False,
            "quality": "Medium"
        }
        self._lock = threading.Lock() # Блокировка для безопасного изменения настроек

    def set_volume(self, volume):
        with self._lock:
            self._settings["volume"] = max(0, min(100, volume))
            print(f"Громкость установлена на {self._settings['volume']}")

    def set_resolution(self, width, height):
        with self._lock:
            self._settings["resolution"] = (width, height)
            print(f"Разрешение изменено на {width}x{height}")

    def toggle_fullscreen(self):
        with self._lock:
            self._settings["fullscreen"] = not self._settings["fullscreen"]
            mode = "Вкл" if self._settings["fullscreen"] else "Выкл"
            print(f"Полноэкранный режим: {mode}")

    def get_settings_summary(self):
        with self._lock:
            s = self._settings
            return (f"--- Настройки игры ---\n"
                    f"Громкость: {s['volume']}%\n"
                    f"Разрешение: {s['resolution'][0]}x{s['resolution'][1]}\n"
                    f"Полноэкранный режим: {s['fullscreen']}")

# --- Тестирование ---
settings1 = GameSettings()
settings2 = GameSettings()

print(f"Одинаковые экземпляры: {settings1 is settings2}")  # True

settings1.set_volume(80)
settings2.set_resolution(1920, 1080)
settings1.toggle_fullscreen()

print(settings1.get_settings_summary())
