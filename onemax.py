# one max problem è un problema di optimizzazione che, data una popolazione di individui (array di 0 e 1),
# sia in grado di ottenere un individuo, dato dall'accoppiamento dei precedenti nella popolazione,
# la cui costituzione prevede un incrocio tra i dna dei genitori, tale che esso abbia il massimo numero di 1.



# importo le librerie random (per generare valori randomici)
import random
# e creator, base, tools, algorithms da deap
from deap import creator, base, tools, algorithms

# Creo una classe di nome FitnessMax che estende la classe base.Fitness e con attributo weights = (1.0,)
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
# Creo un individuo che è semplicemente una lista e che ha come parametro l'oggetto FitnessMax
creator.create("Individual", list, fitness=creator.FitnessMax)

# creo un insieme di tool per effettuare le operazioni di comparazione per l'evoluzione
toolbox = base.Toolbox()

# creo 3 funzioni "alias" che mi fanno ottenere rispettivamente un valore booleano,
toolbox.register("attr_bool", random.randint, 0, 1)
# una che mi fa inserire in un individuo il risultato del lancio di 25 volte la funzione attr_bool
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=25)
# una che mi fa riempire una lista di nuovi individui
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# definisco una funzione che mi somma gli individui
def evalOneMax(individual):
    return sum(individual),

# creiamo degli alias per le funzioni che usiamo
toolbox.register("evaluate", evalOneMax)
toolbox.register("mate", tools.cxTwoPoint) # faccio un incrocio tra i due individui selezionati
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05) # funzione per mutare i bit con probabilità indpb = 0.05
toolbox.register("select", tools.selTournament, tournsize=4) # seleziona il migliore individuo nel torneo di dimensione tournsize = 4

# creo una popolazione di n = 100 individui
population = toolbox.population(n=100)

# ipotizzo di avere 10 generazioni
NGEN=10
# per ognuna delle quali...
for gen in range(NGEN):
    # si crea una prole data dall'incrocio e dalla mutazione degli individui, con possibilità di incrocio di cxpb = 0.5
    # e possibilità mutare individui indipendenti mutpb = 0.1
    offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)
    # mappo la prole con la valutazione degli individui (?)
    fits = toolbox.map(toolbox.evaluate, offspring)
    # per ogni elemento della mappa e ogni indice della prole...
    for fit, ind in zip(fits, offspring):
        # la qualità della soluzione dell'indice della prole prende il valore della entry nella mappa
        ind.fitness.values = fit
    # effettua una selezione tra la prole per la lunghezza della popolazione, raggruppandoli a 4 a 4
    population = toolbox.select(offspring, k=len(population))
# prendo i 3 migliori elementi della popolazione
#top3 = tools.selBest(population, k=20)

print("------------------------------------TUTTI GLI ELEMENTI------------------------------------")
n0 = 0
for element in population:
    print(element)
    if (0 in element):
        n0 += 1

print("\n\n\n\n\n\n\n------------------------------------MIGLIORI ELEMENTI------------------------------------")
nMigliori = 0
for element in population:
    if (0 not in element):
        nMigliori += 1
        print(element)


print("\n\n\n\n\n\n\nNumero elementi con almeno uno 0: ", n0, "\nNumero elementi migliori: ", nMigliori)
