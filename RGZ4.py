import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Задание параметров для имитационного моделирования
n_requests = 100000  # количество заявок
time_horizon = 10000  # временной горизонт

# Генерация входного потока заявок
interarrival_times = np.random.uniform(0, 1, n_requests) ** 3
arrival_times = np.cumsum(interarrival_times)

# Генерация периода обслуживания для первого канала
service_times_channel_1 = np.abs(
    np.random.f(dfnum=3, dfden=3, size=n_requests) - np.random.f(dfnum=5, dfden=5, size=n_requests))

# Генерация периода обслуживания для второго канала
service_times_channel_2 = 1 / (1 + np.random.uniform(0, 1, n_requests))

# Инициализация переменных для моделирования
time_channel_1 = 0
time_channel_2 = 0
served_requests = 0
busy_time_channel_1 = 0
busy_time_channel_2 = 0

# Моделирование процесса обслуживания заявок
for arrival_time, service_time_1, service_time_2 in zip(arrival_times, service_times_channel_1,
                                                        service_times_channel_2):
    if arrival_time > time_horizon:
        break

    if time_channel_1 <= arrival_time and time_channel_2 <= arrival_time:
        # Оба канала свободны, выбираем канал с минимальным ожидаемым периодом обслуживания
        if service_time_1 < service_time_2:
            time_channel_1 = arrival_time + service_time_1
            busy_time_channel_1 += service_time_1
        else:
            time_channel_2 = arrival_time + service_time_2
            busy_time_channel_2 += service_time_2
    elif time_channel_1 <= arrival_time:
        # Свободен только первый канал
        time_channel_1 = arrival_time + service_time_1
        busy_time_channel_1 += service_time_1
    elif time_channel_2 <= arrival_time:
        # Свободен только второй канал
        time_channel_2 = arrival_time + service_time_2
        busy_time_channel_2 += service_time_2

    if time_channel_1 > arrival_time or time_channel_2 > arrival_time:
        served_requests += 1

# Оценка параметров системы
total_requests = len(arrival_times)
relative_throughput = served_requests / total_requests
load_channel_1 = busy_time_channel_1 / time_horizon
load_channel_2 = busy_time_channel_2 / time_horizon
overall_load = (busy_time_channel_1 + busy_time_channel_2) / time_horizon

# Вывод результатов
print(f'Относительная пропускная способность системы: {relative_throughput:.4f}')
print(f'Загруженность первого канала: {load_channel_1:.4f}')
print(f'Загруженность второго канала: {load_channel_2:.4f}')
print(f'Общая загруженность системы: {overall_load:.4f}')
