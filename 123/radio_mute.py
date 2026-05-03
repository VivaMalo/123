import serial
import pyautogui
import time

# --- НАСТРОЙКИ ---
SERIAL_PORT = 'COM6'  # Проверь, совпадает ли номер порта!
BAUD_RATE = 9600

try:
    # Открываем порт
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    # Короткая пауза, чтобы Arduino успела перезагрузиться при подключении
    time.sleep(2) 
    print(f"Подключено к {SERIAL_PORT}. Жду нажатия кнопки...")

    while True:
        if ser.in_waiting > 0:
            # Читаем данные и очищаем от лишних символов
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            
            if line:
                print(f"Получено: {line}")
                
                # РЕАКЦИЯ НА СИГНАЛ:
                if line == "Signal_ON":
                    print(">>> Команда принята! Переключаю звук...")
                    pyautogui.press('volumemute') 

except serial.SerialException:
    print(f"ОШИБКА: Не могу открыть порт {SERIAL_PORT}. Проверь номер порта или закрой Монитор порта в Arduino IDE.")
except KeyboardInterrupt:
    print("\nПрограмма остановлена.")
finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
