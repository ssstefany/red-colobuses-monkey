from troop import Troop
import numpy as np
import time
import pandas as pd
import matplotlib.pyplot as plt
import datetime

if __name__ == "__main__":

    # troop = Troop(1000,20,3)
    # troop.solve()

    iterations = [200]
    num_monkeys = [50]
    num_teams = [4]
    data = []
    all_fitness_evolutions = []
    iterations_to_reach_54 = []

    for i in iterations:
        for m in num_monkeys:
            for t in num_teams:
                #for more_data in range(5):
                values = []
                inicio = time.perf_counter()

                for test in range(30):
                    inicio = time.perf_counter()
                    troop = Troop(i,m,t)
                    troop.solve()
                    fin = time.perf_counter()
                    tiempo_ejecucion = fin - inicio
                    data.append([i, m, t, m*t , troop.best_monkey.fitness() ,tiempo_ejecucion])
                    #print(f"{i};{m};{t};{troop.best_monkey.fitness()};{tiempo_ejecucion}")
                    all_fitness_evolutions.append(troop.fitness_history.copy())

                    for idx, fitness in enumerate(troop.fitness_history):
                        if fitness <= 54:
                            iterations_to_reach_54.append((test, idx + 1))
                            break
                    else:
                        # Si no se alcanza el fitness 54, poner un número mayor a max_iterations
                        iterations_to_reach_54.append((test, i + 1))


    columns = ["iterations", "num_monkeys", "num_teams", "total_monkeys", "fitness_value", "execution_time"]
    df = pd.DataFrame(data, columns=columns)

    fitness_stats = {
        "min": df["fitness_value"].min(),
        "max": df["fitness_value"].max(),
        "median": df["fitness_value"].median(),
        "mean": df["fitness_value"].mean(),
        "std_dev": df["fitness_value"].std(),
        "iqr": df["fitness_value"].quantile(0.75) - df["fitness_value"].quantile(0.25)
    }

    # Mostrar los resultados
    for stat, value in fitness_stats.items():
        print(f"{stat}: {value}")

    # Guardar los resultados en un archivo Excel
    df.to_excel(f'metaheuristica_resultados_{(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))}.xlsx', index=False)

    # Crear gráfico de línea de la evolución del valor fitness para cada ejecución
    plt.figure(figsize=(10, 6))
    for fitness_evolution in all_fitness_evolutions:
        plt.plot(range(1, len(fitness_evolution) + 1), fitness_evolution, linestyle='-', alpha=0.5)

    plt.title('Evolución del Valor Fitness por Iteración para cada Ejecución')
    plt.xlabel('Número de Iteración')
    plt.ylabel('Valor Fitness')
    plt.grid(True)
    plt.savefig(f'fitness_evolucion_{(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))}.png')
    plt.show()

    fastest_execution = min(iterations_to_reach_54, key=lambda x: x[1])[0]

    # Crear gráfico de línea de la evolución del valor fitness para cada ejecución
    plt.figure(figsize=(10, 6))
    for idx, fitness_evolution in enumerate(all_fitness_evolutions):
        if idx == fastest_execution:
            plt.plot(range(1, len(fitness_evolution) + 1), fitness_evolution, linestyle='-', alpha=0.9, linewidth=2, color='red', label='Solución más rapida')
        else:
            plt.plot(range(1, len(fitness_evolution) + 1), fitness_evolution, linestyle='-', color='grey', alpha=0.5)

    plt.title('Evolución del Valor Fitness por Iteración para cada Ejecución')
    plt.xlabel('Número de Iteración')
    plt.ylabel('Valor Fitness')
    plt.grid(True)
    plt.legend()
    plt.savefig(f'fitness_evolucion_{(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))}.png')
    plt.show()
