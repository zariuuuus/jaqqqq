# time_utils.py

import time
import sys

def countdown_timer(seconds):
    """Функция обратного отсчета."""
    for i in range(seconds, 0, -1):
        sys.stdout.write(f'\rОсталось времени: {i} секунд')
        sys.stdout.flush()
        time.sleep(1)
    print("\nВремя вышло!")

def animated_sleep(seconds):
    """Функция задержки с анимацией (показывает точки во время ожидания)."""
    for i in range(seconds):
        time.sleep(1)
        sys.stdout.write('.')
        sys.stdout.flush()
    print("\nЗадержка завершена!")

def format_time(seconds):
    """Форматирует время в часы, минуты и секунды."""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours} ч : {minutes} мин : {seconds} сек"

def measure_execution_time(func, *args, **kwargs):
    """Измеряет время выполнения функции."""
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time