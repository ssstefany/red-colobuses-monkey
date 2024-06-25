from monkey import Monkey

class Troop:
    def __init__(self, iterations, monkeys, teams):
        self.max_iterations = iterations
        self.num_monkeys    = monkeys
        self.num_teams      = teams
        self.swarm          = []
        self.leader         = []
        self.best           = []
        self.worst          = []
        self.best_monkey    = Monkey()
        self.fitness_history = []

    def solve(self):
        self.initrand()
        self.evolve()
        print(f"Costo (Tiempo) : {self.best_monkey.fitness()}")
        print(f"Ruta (Destinos) : {self.show_route(self.best_monkey.position)}")

    def initrand(self):
        for i in range(self.num_teams):
            #print("team ",i)
            team = []
            for j in range(self.num_monkeys):
                while True:
                    m = Monkey()
                    if m.is_feasible():
                        break
                team.append(m)
                #print(f"team {i} mono {j} X: {m.position}")
            self.swarm.append(team)
            
    # obtener mejores y peores de cada grupo
            best_monkey = team[0]
            worst_monkey = team[0]
            for monkey in team:
                if monkey.is_better_than(best_monkey):
                    best_monkey = monkey
                if monkey.is_worse_than(worst_monkey):
                    worst_monkey = monkey
            self.best.append(best_monkey)
            self.worst.append(worst_monkey)

    #obtener el lider
            leader = max(team, key=lambda m: (m.combat_power_PA, m.body_power_PB))
            self.leader.append(leader)

    #obtener el mejor mono
        self.best_monkey = self.best[0]
        for monkey in self.best:
            if monkey.is_better_than(self.best_monkey):
                self.best_monkey = monkey

    def update_the_best_and_the_worst(self):
        for i in range(self.num_teams):
            self.best[i] = min(self.swarm[i], key=lambda m: m.fitness())
            self.worst[i] = max(self.swarm[i], key=lambda m: m.fitness())
            self.leader[i] = max(self.swarm[i], key=lambda m: (m.combat_power_PA, m.body_power_PB))
        self.best_monkey = min(self.best, key=lambda m: m.fitness())

    def evolve(self):
        t = 1
        while t <= self.max_iterations:
            self.change_worse_for_better_child()
            for i in range(self.num_teams):
                for j in range(self.num_monkeys):
                    m = Monkey()
                    while True:
                        m.copy(self.swarm[i][j])
                        m.move(self.leader[i].weight,self.best_monkey.position)
                        if m.is_feasible():
                            break
                    if m.is_better_than(self.swarm[i][j]):
                        self.swarm[i][j].copy(m)
            self.update_the_best_and_the_worst()
            self.fitness_history.append(self.best_monkey.fitness())
            #print(f"i:{t},{self.best_monkey}")
            t += 1

    def change_worse_for_better_child(self):
        best_child = self.best[self.num_teams-1]
        for i in range(self.num_teams-1):
            for j in range(self.num_monkeys):
                if self.swarm[i][j] == self.worst[i]:
                    self.swarm[i][j] = best_child

    def show_route(self,vector):
        route = []              #lista para ir generando la ruta
        next_position = 0       #inicio de la ruta en posición 0

        for i in range(len(vector)):
            # generar ruta 
            route.append(vector[next_position])
            next_position = vector[next_position]

        route_string = "0"
        for i in route:
            route_string += f"->{i}"

        return route_string