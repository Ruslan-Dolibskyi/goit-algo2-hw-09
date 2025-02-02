import random
import math

# Визначення функції Сфери
def sphere_function(x):
    return sum(xi ** 2 for xi in x)

# Hill Climbing
def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    # Ініціалізація випадкової точки
    current_solution = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current_solution)

    for _ in range(iterations):
        # Генерація сусідньої точки
        neighbor = [xi + random.uniform(-0.1, 0.1) for xi in current_solution]
        neighbor = [max(min(neighbor[i], bounds[i][1]), bounds[i][0]) for i in range(len(bounds))]  # Обмеження в межах bounds
        neighbor_value = func(neighbor)

        # Якщо сусід кращий, приймаємо його
        if neighbor_value < current_value:
            current_solution, current_value = neighbor, neighbor_value

        # Умова зупинки
        if abs(current_value - neighbor_value) < epsilon:
            break

    return current_solution, current_value

# Random Local Search
def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    # Випадковий початковий розв'язок
    best_solution = [random.uniform(b[0], b[1]) for b in bounds]
    best_value = func(best_solution)

    for _ in range(iterations):
        candidate = [random.uniform(b[0], b[1]) for b in bounds]
        candidate_value = func(candidate)

        if candidate_value < best_value:
            best_solution, best_value = candidate, candidate_value

        # Умова зупинки
        if abs(best_value - candidate_value) < epsilon:
            break

    return best_solution, best_value

# Simulated Annealing
def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6):
    # Випадковий початковий розв'язок
    current_solution = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current_solution)
    best_solution, best_value = current_solution, current_value

    for _ in range(iterations):
        temp *= cooling_rate  # Зменшення температури
        if temp < epsilon:
            break  # Якщо температура стала надто малою, завершити

        # Генеруємо нову сусідню точку
        neighbor = [xi + random.uniform(-0.5, 0.5) for xi in current_solution]
        neighbor = [max(min(neighbor[i], bounds[i][1]), bounds[i][0]) for i in range(len(bounds))]
        neighbor_value = func(neighbor)

        # Якщо сусід кращий або приймаємо гірший з певною ймовірністю
        if neighbor_value < current_value or random.uniform(0, 1) < math.exp((current_value - neighbor_value) / temp):
            current_solution, current_value = neighbor, neighbor_value

        if current_value < best_value:
            best_solution, best_value = current_solution, current_value

    return best_solution, best_value

# Межі для функції
bounds = [(-5, 5), (-5, 5)]

# Виконання алгоритмів
hc_solution, hc_value = hill_climbing(sphere_function, bounds)
rls_solution, rls_value = random_local_search(sphere_function, bounds)
sa_solution, sa_value = simulated_annealing(sphere_function, bounds)

# Виведення результатів
print("Hill Climbing:")
print("Розв'язок:", hc_solution, "Значення:", hc_value)

print("\nRandom Local Search:")
print("Розв'язок:", rls_solution, "Значення:", rls_value)

print("\nSimulated Annealing:")
print("Розв'язок:", sa_solution, "Значення:", sa_value)
