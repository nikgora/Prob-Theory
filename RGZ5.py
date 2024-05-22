import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def is_inside_body(x, y, z, bodies):
    for body in bodies:
        (xi, yi, zi, Ai, Bi, Ci, rid) = body
        num = ((abs(x - xi) ** rid )/ Ai) + ((abs(y - yi) ** rid) / Bi) +((abs(z - zi) ** rid) / Ci)
        if num.real < 1 or (num.real == 1 and num.imag == 0):
            return True
    return False


def monte_carlo_volume(bodies, N):
    # Определяем границы параллелепипеда
    x_min = min(body[0] - max(0, body[3] ** (1 / body[6])) for body in bodies)
    x_max = max(body[0] + max(0, body[3] ** (1 / body[6])) for body in bodies)
    y_min = min(body[1] - max(0, body[4] ** (1 / body[6])) for body in bodies)
    y_max = max(body[1] + max(0, body[4] ** (1 / body[6])) for body in bodies)
    z_min = min(body[2] - max(0, body[5] ** (1 / body[6])) for body in bodies)
    z_max = max(body[2] + max(0, body[5] ** (1 / body[6])) for body in bodies)

    # Объем параллелепипеда
    V0 = (x_max - x_min) * (y_max - y_min) * (z_max - z_min)

    # Генерация случайных точек и подсчет количества попавших внутрь тела
    count_inside = 0
    for _ in range(N):
        x_rand = np.random.uniform(x_min, x_max)
        y_rand = np.random.uniform(y_min, y_max)
        z_rand = np.random.uniform(z_min, z_max)

        if is_inside_body(x_rand, y_rand, z_rand, bodies):
            count_inside += 1

    # Оценка объема тела
    V = V0 * count_inside / N
    return V


def calculate_volumes_and_errors(bodies, N_values):
    volumes = []
    errors = []
    confidence_intervals = []
    for N in N_values:
        volume_estimates = [monte_carlo_volume(bodies, N) for _ in range(10)]
        volume_mean = np.mean(volume_estimates)
        volume_std = np.std(volume_estimates)
        volumes.append(volume_mean)
        errors.append(np.std(volume_estimates))

        # 95% confidence interval
        z_score = norm.ppf(0.975)  # Z-score for 95% confidence
        margin_of_error = z_score * volume_std / np.sqrt(len(volume_estimates))
        confidence_intervals.append((volume_mean - margin_of_error, volume_mean + margin_of_error))

    return volumes, errors, confidence_intervals


def plot_results(N_values, volumes, errors, confidence_intervals):
    print("N, V, P")
    for i in range(len(N_values)):
        print(N_values[i], volumes[i], errors[i], sep=", ")

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.plot(N_values, volumes, 'o-', label='Оцененный объем')
    plt.fill_between(N_values, [ci[0] for ci in confidence_intervals], [ci[1] for ci in confidence_intervals], color='b', alpha=0.2, label='95% доверительный интервал')
    plt.xlabel('Размер выборки (N)')
    plt.ylabel('Объем')
    plt.title('Зависимость вычисленного объема от размера выборки')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(N_values, errors, 'o-', label='Погрешность')
    plt.xlabel('Размер выборки (N)')
    plt.ylabel('Погрешность')
    plt.title('Зависимость погрешности от размера выборки')
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # bodies = [
    #     (1.7, -2.5, 0, 10, 12, 8, 1.9),
    #     (0, 1.7, -2.5, 10, 8, 12, 2.5),
    #     (0, -2.5, 1.7, 10, 10, 12, 3.7)
    # ]
    bodies = [
        (1.7, -2.5, 2.5, 12, 6, 12, 2.5),
        (-2.5, 0, 0, 10, 10, 12, 1.9),
        (1.7, 1.7, 1.7, 6, 12, 12, 1.4)
    ]
    N_values = [100, 300, 500, 1000, 2000, 3000, 5000, 8000, 10000, 12000, 15000, 20000, 25000, 30000, 45000, 50000, 55000, 60000, 65000]
    volumes, errors, confidence_intervals = calculate_volumes_and_errors(bodies, N_values)

    plot_results(N_values, volumes, errors, confidence_intervals)
