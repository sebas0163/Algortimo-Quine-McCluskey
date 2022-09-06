## Step 1: Truncs rows if they finish in 1
def reading_table(table):
    x = len(table[0])-2
    table_aux = []
    for i in range(len(table)):
        if (table[i][x] == 1):
            table_aux += [table[i]]
    return table_aux
## Finish step 1

## Step 2: Defines how many 1's per row and sorts it
def trunc(table):
    x = len(table[0])-1
    for i in range(len(table)):
        count = 0
        for j in range(len(table[i])-1):
            if (table[i][j] == 1):
                count += 1
        table[i] += [count]
    return sorted(table, key=lambda tab: tab[x+1]) #Sorts by how many 1's
## Finish step 2

## Step 3: Combines by quantity of 1's
def combine_by_number(table):
    table = trunc(table)
    table_1 = []
    table_2 = []
    table_3 = []
    table_4 = []
    table_5 = []
    table_6 = []
    x = len(table[0])-1
    for i in range(len(table)):
        if (table[i][x] == 1):
            table_1 += [table[i][:-1]]
        elif (table[i][x] == 2):
            table_2 += [table[i][:-1]]
        elif (table[i][x] == 3):
            table_3 += [table[i][:-1]]
        elif (table[i][x] == 4):
            table_4 += [table[i][:-1]]
        elif (table[i][x] == 5):
            table_5 += [table[i][:-1]]
        elif (table[i][x] == 6):
            table_6 += [table[i][:-1]]
    return [table_1, table_2, table_3, table_4, table_5, table_6]
# Finish step 3

# Step 4: Identify changes and creates "Don't cares"
def identify_changes(tuple1, tuple2):
    differences = 0
    tuple_aux = []
    for i in range(len(tuple1)):
        if (tuple1[i] != tuple2[i]):
            differences += 1
            tuple_aux += ["x"]
        else:
            tuple_aux += [tuple1[i]]  
    if differences > 1:
        return -1
    else: ##unnecessary
        return tuple_aux


def combine_groups(table):
    table = combine_by_number(table)
    table_aux = []
    for i in range(len(table)):
        for j in range(len(table[i])):
            for k in range(len(table[i+1])):
                #print(table[i][j], table[i+1][k])
                first_minterm = table[i][j][-1]
                second_minterm = table[i+1][k][-1]
                x = identify_changes(table[i][j][:-1], table[i+1][k][:-1])
                if (x != -1):
                    table_aux += [x + [(first_minterm, second_minterm)]]
    return table_aux
                        


#print(combine_groups([[[0, 0, 0, 1], [0, 1, 0, 0]], [[0, 0, 1, 1], [0, 1, 0, 1], [1, 0, 0, 1], [1, 1, 0, 0]], [[1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]], [[1, 1, 1, 1]], [], []]))
## Finish step 4

## Step 0: Add last item to every list in table
def add_minterm_element(table):
    for i in range(len(table)):
        table[i] += [i]
    return table
## Finish step 0

def get_minterms(table):
    minterms = []
    x = len(table[0])-1
    for i in range(len(table)):
        minterms += [table[i][x]]
    return minterms

def remove_repeats(table):
    table_aux = []
    for x in table:
        if x not in table_aux:
            table_aux.append(x)
    return table_aux

def remove_one(table):
    table_aux = []
    for i in range(len(table)):
        minterm = table[i][-1]
        table_aux += [table[i][:-2] + [minterm]]
    return table_aux

def remove_last(table):
    table_aux = []
    for i in range(len(table)):
        table_aux += [table[i][:-1]]
    return table_aux

#print(remove_repeats([['x', 0, 'x', 1], ['x', 'x', 0, 1], ['x', 0, 'x', 1], ['x', 'x', 0, 1], ['x', 1, 0, 'x'], ['x', 1, 0, 'x'], [1, 'x', 'x', 1], [1, 'x', 'x', 1], [1, 1, 'x', 'x'], [1, 1, 'x', 'x']]))
## Finish step 6


def main(table):
    # First assigns minterms values
    table = add_minterm_element(table)

    # Filters to use only table with 1's
    table = reading_table(table)

    # Filters by minterms
    table = remove_one(table)

    ####################################

    table_aux = []
    while(table != []):
        table_aux = table
        table = combine_groups(table)

    table = table_aux
    table = remove_last(table)

    table = remove_repeats(table)

    #print("-------")
    #print(getLen(table))
    #x = getLen(table)
    #print("-------")

    #print(table)

    #print("-------")
    #print(simplify(table, x))
    #print("-------")

    #table = combine_groups(combine_by_number(trunc(table)))
    #table = combine_groups(combine_by_number(trunc(table)))
    #table = combine_groups(combine_by_number(trunc(table)))


    #table = trunc(table)
    #table = combine_by_number(table)
    #table = combine_groups(table)

    #table = trunc(table)
    #table = combine_by_number(table)
    #table = combine_groups(table)

    #table = trunc(table)
    #table = combine_by_number(table)
    #table = combine_groups(table)


    #table = remove_repeats(table)


    ######
    # Se debe de hacer recursivo hasta obtener todos los primos implicantes


    # Se obtienen los primos implicantes esenciales
    # -> Codigo

    
    return table

print(main([[0,0,0,0,0],[0,0,0,1,1],[0,0,1,0,0],[0,0,1,1,1],[0,1,0,0,1],[0,1,0,1,1],[0,1,1,0,0],[0,1,1,1,0],[1,0,0,0,0],[1,0,0,1,1],[1,0,1,0,0],[1,0,1,1,1],[1,1,0,0,1],[1,1,0,1,1],[1,1,1,0,1],[1,1,1,1,1]]))

