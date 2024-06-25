
class Problem:
    def __init__(self):
        # 0 al 4 fitness 80
        # self.dimension = 5
        # self.costs = [
        #     [0, 10, 20, 15, 30],
        #     [10, 0, 25, 20, 10],
        #     [20, 25, 0, 30, 15],
        #     [15, 20, 30, 0, 18],
        #     [30, 10, 15, 18, 0]
        #     ]
        
        # 0 al 10 fitness 54
        self.dimension = 11
        self.costs = [
            #  0    1   2   3   4   5   6   7   8   9   10  
            [ 0,    5,  10, 15, 7,  12, 20, 8,  14, 10, 9],
            [ 5,    0,  6,  9,  5,  8,  14, 4,  7,  5,  6],
            [10,    6,  0,  8,  4,  6,  13, 7,  5,  8,  9],
            [15,    9,  8,  0,  7,  4,  10, 5,  3,  6,  12],
            [ 7,    5,  4,  7,  0,  3,  9,  6,  4,  5,  8],
            [12,    8,  6,  4,  3,  0,  7,  3,  5,  6,  9],
            [20,    14, 13, 10, 9,  7,  0,  6,  5,  8, 10],
            [ 8,    4,  7,  5,  6,  3,  6,  0,  2,  5,  7],
            [14,    7,  5,  3,  4,  5,  5,  2,  0,  3,  8],
            [10,    5,  8,  6,  5,  6,  8,  5,  3,  0,  4],
            [ 9,    6,  9, 12,  8,  9, 10,  7,  8,  4,  0]
            ]

        #12 CLIENTES
        # self.dimension = 13
        # self.costs = [
        #     [0, 5, 10, 15, 7, 12, 20, 8, 14, 10, 9, 6, 11],
        #     [5, 0, 6, 9, 5, 8, 14, 4, 7, 5, 6, 3, 8],
        #     [10, 6, 0, 8, 4, 6, 13, 7, 5, 8, 9, 5, 7],
        #     [15, 9, 8, 0, 7, 4, 10, 5, 3, 6, 12, 9, 4],
        #     [7, 5, 4, 7, 0, 3, 9, 6, 4, 5, 8, 7, 5],
        #     [12, 8, 6, 4, 3, 0, 7, 3, 5, 6, 9, 4, 6],
        #     [20, 14, 13, 10, 9, 7, 0, 6, 5, 8, 10, 9, 7],
        #     [8, 4, 7, 5, 6, 3, 6, 0, 2, 5, 7, 4, 6],
        #     [14, 7, 5, 3, 4, 5, 5, 2, 0, 3, 8, 5, 4],
        #     [10, 5, 8, 6, 5, 6, 8, 5, 3, 0, 4, 6, 5],
        #     [9, 6, 9, 12, 8, 9, 10, 7, 8, 4, 0, 7, 6],
        #     [6, 3, 5, 9, 7, 4, 9, 4, 5, 6, 7, 0, 5],
        #     [11, 8, 7, 4, 5, 6, 7, 6, 4, 5, 6, 5, 0]
        # ]

        # 14 CLIENTES
        # self.dimension = 15
        # self.costs = [
        #     [0, 5, 10, 15, 7, 12, 20, 8, 14, 10, 9, 6, 11, 13, 7],
        #     [5, 0, 6, 9, 5, 8, 14, 4, 7, 5, 6, 3, 8, 10, 4],
        #     [10, 6, 0, 8, 4, 6, 13, 7, 5, 8, 9, 5, 7, 9, 6],
        #     [15, 9, 8, 0, 7, 4, 10, 5, 3, 6, 12, 9, 4, 11, 5],
        #     [7, 5, 4, 7, 0, 3, 9, 6, 4, 5, 8, 7, 5, 8, 3],
        #     [12, 8, 6, 4, 3, 0, 7, 3, 5, 6, 9, 4, 6, 9, 4],
        #     [20, 14, 13, 10, 9, 7, 0, 6, 5, 8, 10, 9, 7, 12, 6],
        #     [8, 4, 7, 5, 6, 3, 6, 0, 2, 5, 7, 4, 6, 8, 5],
        #     [14, 7, 5, 3, 4, 5, 5, 2, 0, 3, 8, 5, 4, 7, 4],
        #     [10, 5, 8, 6, 5, 6, 8, 5, 3, 0, 4, 6, 5, 8, 5],
        #     [9, 6, 9, 12, 8, 9, 10, 7, 8, 4, 0, 7, 6, 9, 6],
        #     [6, 3, 5, 9, 7, 4, 9, 4, 5, 6, 7, 0, 5, 8, 3],
        #     [11, 8, 7, 4, 5, 6, 7, 6, 4, 5, 6, 5, 0, 7, 4],
        #     [13, 10, 9, 11, 8, 9, 12, 8, 7, 8, 9, 8, 7, 0, 9],
        #     [7, 4, 6, 5, 3, 4, 6, 5, 4, 5, 6, 3, 4, 9, 0]
        # ]

    def check(self, solution):
        # Verificar si todos los elementos son únicos
        if (len(solution)) != (len(set(solution))):
           #print("no unicos")
            return False
        
        # Verificar que estén todos los destinos
        if (set(solution) != set(range(len(solution)))):
            #print("no del 0 a la dim-1")
            return False

        # Verificar que la salida no es el mismo destino
        for i in solution:
            if i == solution.index(i):
                #print("mismo indice")
                return False
            
        # Verificar si hay ciclos
        if self.has_cycle(solution):
            #print("tiene ciclo", solution)
            return False
        return True

    def has_cycle(self, vector):
        route = []              #lista para ir generando la ruta
        next_position = 0       #inicio de la ruta en posición 0

        for i in range(len(vector)):
            # generar ruta 
            route.append(vector[next_position])
            next_position = vector[next_position]
            # si no es el ultimo destino y el vector está en la ruta
            if (i != self.dimension-1) and (vector[next_position] in route):
                return True

        return False

    def fit(self, solution):
        return sum(self.costs[salida][destino] for salida, destino in enumerate(solution))

