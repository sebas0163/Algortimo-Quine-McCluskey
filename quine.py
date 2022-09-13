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
    table_0 = []
    table_1 = []
    table_2 = []
    table_3 = []
    table_4 = []
    table_5 = []
    table_6 = []
    x = len(table[0])-1
    for i in range(len(table)):
        if (table[i][x] == 0):
            table_0 += [table[i][:-1]]
        elif (table[i][x] == 1):
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
    return [table_0, table_1, table_2, table_3, table_4, table_5, table_6]
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
    [table_aux.append(x) for x in table if x not in table_aux]
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

def combine_minterms(table):
    table_aux = [remove_last(table)]
    x = len(table[0])-1
    for i in range(len(table)):
        minterms_aux = []
        for j in range(len(table[i][x])):
            minterms_aux += [table[i][x][j]]
        table_aux[0][i] += [(minterms_aux)]
    return table_aux

def sort_minterms(table):
    table_aux = []
    x = len(table[0][0])-1
    for i in range(len(table[0])):
        table[0][i][x].sort()
    return table

def get_minterms(table):
    minterms = []
    x = len(table[0])-1
    for i in range(len(table)):
        minterms += [table[i][x]]
    return minterms

def final_combine(minterms):
    minterms_aux = []
    for i in range(len(minterms)):
        for j in range(len(minterms[i])):
                minterms_aux += [minterms[i][j]]
    return minterms_aux

def remove_repeated_minterms(minterms):
    minterms_aux = []
    for i in minterms:
        count = 0
        for j in minterms:
            if i == j:
                count += 1
        if count == 1:
            minterms_aux += [i]
    return minterms_aux

def get_essentials(table, minterms):
    table_aux = []
    x = len(table[0])-1
    for i in range(len(table)):
        for j in range(len(table[i][x])):
            if table[i][x][j] in minterms:
                table_aux += [table[i]]
    return table_aux

def convert_to_output(table):
    string = ''
    print(table)
    for i in range(len(table)):
        first_term = True
        for j in range(len(table[i])):
    
            if table[i][j] != 'x' and first_term == False:
                string += '⋅'

            if j == 0:
                if table[i][j] == 1:
                    string += 'a'
                    first_term = False
                if table[i][j] == 0:
                    string += 'a\''
                    first_term = False
            elif j == 1:
                if table[i][j] == 1:
                    string += 'b'
                    first_term = False
                if table[i][j] == 0:
                    string += 'b\''
                    first_term = False
            elif j == 2:
                if table[i][j] == 1:
                    string += 'c'
                    first_term = False
                if table[i][j] == 0:
                    string += 'c\''
                    first_term = False
            elif j == 3:
                if table[i][j] == 1:
                    string += 'd'
                    first_term = False
                if table[i][j] == 0:
                    string += 'd\''
                    first_term = False
            elif j == 4:
                if table[i][j] == 1:
                    string += 'e'
                    first_term = False
                if table[i][j] == 0:
                    string += 'e\''
                    first_term = False
            elif j == 5:
                if table[i][j] == 1:
                    string += 'f'
                    first_term = False
                if table[i][j] == 0:
                    string += 'f\''
                    first_term = False

        if i != len(table)-1:
            string += ' + '
    return string

def remove_repeated_outputs(output):
    output_aux = ""
    listedOutput = output.split(" + ")
    listedOutput_aux = []
    [listedOutput_aux.append(x) for x in listedOutput if x not in listedOutput_aux]
    for i in range(len(listedOutput_aux)):
        output_aux += listedOutput_aux[i]
        if i != len(listedOutput_aux)-1:
            output_aux += " + "
    return output_aux
    

##____________
##__/ Main /__
def main(table):
    # Get number of variables [4,6]
    variables = len(table)
    variables = variables**(1/2)

    # First assigns minterms values
    table = add_minterm_element(table)

    # Filters to use only table with 1's
    table = reading_table(table)

    # Filters by minterms
    table = remove_one(table)

    ####################################
    
    #table = combine_groups(table)
    #table = combine_groups(table)
    #table = combine_groups(table)

    table_aux = []
    while(table != []):
        table_aux = table
        table = combine_groups(table)

    table = table_aux
    table = remove_last(table)

    table = combine_minterms(table)
    table = sort_minterms(table)
    table = remove_repeats(table[0])

    minterms = get_minterms(table)
    minterms = final_combine(minterms)
    minterms = remove_repeated_minterms(minterms)

    primeEssentials = get_essentials(table, minterms)
    table = remove_last(primeEssentials)
    
    output = convert_to_output(table)
    output = remove_repeated_outputs(output)

    #return table
    return output

## // Case for 4
#print(main([[0,0,0,0,1],[0,0,0,1,1],[0,0,1,0,0],[0,0,1,1,1],
#            [0,1,0,0,0],[0,1,0,1,0],[0,1,1,0,1],[0,1,1,1,0],
#            [1,0,0,0,0],[1,0,0,1,1],[1,0,1,0,0],[1,0,1,1,0],
#            [1,1,0,0,1],[1,1,0,1,1],[1,1,1,0,0],[1,1,1,1,1]]))
## // Case for 5
#print(main([[0,0,0,0,0,1],[0,0,0,0,1,1],[0,0,0,1,0,0],[0,0,0,1,1,1],
#            [0,0,1,0,0,0],[0,0,1,0,1,0],[0,0,1,1,0,1],[0,0,1,1,1,0],
#            [0,1,0,0,0,0],[0,1,0,0,1,1],[0,1,0,1,0,0],[0,1,0,1,1,0],
#            [0,1,1,0,0,1],[0,1,1,0,1,1],[0,1,1,1,0,0],[0,1,1,1,1,1],
#            [1,0,0,0,0,1],[1,0,0,0,1,0],[1,0,0,1,0,1],[1,0,0,1,1,0],
#            [1,0,1,0,0,0],[1,0,1,0,1,0],[1,0,1,1,0,1],[1,0,1,1,1,0],
#            [1,1,0,0,0,0],[1,1,0,0,1,0],[1,1,0,1,0,0],[1,1,0,1,1,0],
#            [1,1,1,0,0,1],[1,1,1,0,1,0],[1,1,1,1,0,0],[1,1,1,1,1,1]]))
## // Case for 6
#print(main([[0,0,0,0,0,0,1], [0,0,0,0,0,1,1], [0,0,0,0,1,0,0], [0,0,0,0,1,1,1],
#                     [0,0,0,1,0,0,0], [0,0,0,1,0,1,0], [0,0,0,1,1,0,1], [0,0,0,1,1,1,0],
#                     [0,0,1,0,0,0,0], [0,0,1,0,0,1,1], [0,0,1,0,1,0,0], [0,0,1,0,1,1,0],
#                     [0,0,1,1,0,0,1], [0,0,1,1,0,1,1], [0,0,1,1,1,0,0], [0,0,1,1,1,1,1],
#                     [0,1,0,0,0,0,1], [0,1,0,0,0,1,0], [0,1,0,0,1,0,1], [0,1,0,0,1,1,0],
#                     [0,1,0,1,0,0,0], [0,1,0,1,0,1,0], [0,1,0,1,1,0,1], [0,1,0,1,1,1,0],
#                     [0,1,1,0,0,0,0], [0,1,1,0,0,1,0], [0,1,1,0,1,0,0], [0,1,1,0,1,1,0],
#                     [0,1,1,1,0,0,1], [0,1,1,1,0,1,0], [0,1,1,1,1,0,0], [0,1,1,1,1,1,1],
#                     [1,0,0,0,0,0,0], [1,0,0,0,0,1,1], [1,0,0,0,1,0,1], [1,0,0,0,1,1,1],
#                     [1,0,0,1,0,0,1], [1,0,0,1,0,1,0], [1,0,0,1,1,0,0], [1,0,0,1,1,1,1],
#                     [1,0,1,0,0,0,0], [1,0,1,0,0,1,0], [1,0,1,0,1,0,0], [1,0,1,0,1,1,0],
#                     [1,0,1,1,0,0,0], [1,0,1,1,0,1,1], [1,0,1,1,1,0,0], [1,0,1,1,1,1,0],
#                     [1,1,0,0,0,0,1], [1,1,0,0,0,1,1], [1,1,0,0,1,0,0], [1,1,0,0,1,1,1],
#                     [1,1,0,1,0,0,0], [1,1,0,1,0,1,1], [1,1,0,1,1,0,1], [1,1,0,1,1,1,0],
#                     [1,1,1,0,0,0,0], [1,1,1,0,0,1,1], [1,1,1,0,1,0,0], [1,1,1,0,1,1,0],
#                     [1,1,1,1,0,0,0], [1,1,1,1,0,1,0], [1,1,1,1,1,0,1], [1,1,1,1,1,1,0]]))
