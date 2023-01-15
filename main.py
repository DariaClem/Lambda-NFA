def drum(stare, cuvant):
    global gasit, drumParcurs
    # We treat the case for lambda separately
    if cuvant == '#':
        if stariFinale[stare]:  # if we have reached a final state
            drumParcurs.append(stare)
            gasit = 1
        elif '#' in automat[stare]:
            for index4 in automat[stare]['#']:
                drumParcurs.append(stare)
                drum(index4, cuvant)
                if gasit:
                    return
                drumParcurs.pop()
        else:
            return
    # If we found a path that validates the word or if we ended up with the empty word,
    # but without being on a final state, we return None
    if gasit or (cuvant == "" and stariFinale[stare] == 0):
        return
    # We found a (correct) path of states that validates the word.
    if stariFinale[stare] == 1 and cuvant == "":
        drumParcurs.append(stare)
        gasit = 1
        return
    else:
        # If we reached a state from which we can no longer leave, we return to the previous state
        if stare not in automat:
            return
        if cuvant[0] in automat[stare]:
            # We go through the states related to the character
            for stareViitoare in automat[stare][cuvant[0]]:
                cuvantNou = cuvant[1:]
                drumParcurs.append(stare)
                drum(stareViitoare, cuvantNou)
                # If we found a path, we no longer delete states from the list. Otherwise, we must
                # remove the invalid state
                if gasit:
                    return
                drumParcurs.pop()
        if '#' in automat[stare]:
            # We traverse the states we can reach with lambda.
            for stareViitoare in automat[stare]['#']:
                drumParcurs.append(stare)
                drum(stareViitoare, cuvant)
                # If we found a path, we no longer delete states from the list. Otherwise, we must
                # remove the invalid state
                if gasit:
                    return
                drumParcurs.pop()
    return


fisier = open("date.in", "r")
continutFisier = fisier.read().split("\n")

# Determine the values of n and m
valori = continutFisier[0].split()
n = int(valori[0])
m = int(valori[1])

# We create a distionary like this
# automata = {state: {character: [states in which it is possible to go through the respective transition]}}
automat = {}

for index1 in range(1, m + 1):
    valori = continutFisier[index1].split()
    if int(valori[0]) in automat:  # check if the current state exists in the automata
        if valori[2] in automat[int(valori[0])]:  # check if the transition exists for the current state
            automat[int(valori[0])][valori[2]].append(int(valori[1]))
        else:
            automat[int(valori[0])][valori[2]] = [int(valori[1])]
    else:
        automat[int(valori[0])] = {valori[2]: [int(valori[1])]}

# Initial state index
stareInitiala = int(continutFisier[m + 1])

valori = [int(element) for element in continutFisier[m + 2].split()]
# Memorize the number of final states
nrStariFinale = valori[0]
# Building a list in which we will record the existence of end states
stariFinale = [0 for index2 in range(n + 1)]
for element in valori[1:]:
    stariFinale[element] = 1

# Memorize the words that will be tested
cuvinte = list()
numarCuvinte = int(continutFisier[m + 3])
for index3 in range(m + 4, m + 4 + numarCuvinte):
    cuvinte.append(continutFisier[index3])

fisier.close()

# We go through the list of words and check the validity
for cuv in cuvinte:
    drumParcurs = list()  # The list stores the states through which a word is validated
    gasit = 0  # the variable records the finding of a way to validate a word
    drum(stareInitiala, cuv)
    if drumParcurs:
        print("YES")
        print("Route:", *drumParcurs)
    else:
        print("NO")
    print('_________________________')
