# examples.py

from time_utils import countdown_timer, animated_sleep, format_time, measure_execution_time

# Пример использования таймера обратного отсчета
print("Запуск таймера обратного отсчета на 5 секунд:")
countdown_timer(5)

# Пример использования задержки с анимацией
print("Запуск задержки с анимацией на 3 секунды:")
animated_sleep(3)

# Пример использования форматирования времени
seconds = 3665  # Пример: 1 час, 1 минута и 5 секунд
formatted_time = format_time(seconds)
print(f"Отформатированное время: {formatted_time}")

# Пример измерения времени выполнения функции
def sample_function(n):
    """Пример функции, которая будет выполняться для измерения времени."""
    total = 0
    for i in range(n):
        total += i
    return total

result, exec_time = measure_execution_time(sample_function, 1000000)
print(f"Результат функции: {result}, Время выполнения: {exec_time} секунд")