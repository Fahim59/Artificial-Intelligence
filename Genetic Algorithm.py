import random
import math

def fitness(chromosome):
    count = 0
    idx = len(value)-1
    for i in chromosome:
        if(i==1):
            count += value[idx]
        idx -= 1
    x_value.append(count)
    fitness_value.append(count ** 2)


def probability(f_value):
    for i in f_value:
        prob.append(i/total_sum)

def selection(prob_cum_sum):
    for i in range(len(prob_cum_sum)):
        curr = []
        if i == 0:
            curr.append(0.00)
            curr.append(prob_cum_sum[i])
            bin.append(curr)
        else:
            curr.append(prob_cum_sum[i-1])
            curr.append(prob_cum_sum[i])
            bin.append(curr)

    for i in range(4):
        random_values = random.uniform(0,1)
        random_list.append(random_values)
        for j in range(len(bin)):
            curr1 = bin[j][0]
            curr2 = bin[j][1]
            if (random_values >= curr1 and random_values <= curr2):
                selected_strings_idx.add(j)
                select_freq.append(j)
                break
    print()
    freq_count = {}
    count = 0
    idx = 0
    for i in select_freq:
        freq_count[i] = select_freq.count(i)
    for i in freq_count:
        if freq_count[i] > count:
            idx = i
            count = freq_count[i]
    return idx

def crossover(chromosome1, chromosome2):
    if(len(selected_strings) > 1):
        ran_val = random.randint(1,3)
        print('Crossover Point: ', ran_val)
        string1 = []
        for i in range(ran_val):
            string1.append(strings[chromosome1][i])
        start = ran_val
        count = 0
        for j in range(len(strings[0])-start):
            string1.append(strings[chromosome2][start])
            start += 1
            count += 1
        Offsprings.append(string1)

        string2 = []
        for i in range(ran_val):
            string2.append(strings[chromosome2][i])
        start = ran_val
        count = 0
        for j in range(len(strings[0])-start):
            string2.append(strings[chromosome1][start])
            start += 1
            count += 1
        Offsprings.append(string2)

strings = [[0, 1, 1, 0, 1],
           [1, 1, 0, 0, 0],
           [0, 1, 0, 0, 0],
           [1, 0, 0, 1, 1]]

value = [1,2,4,8,16]
x_value = []
fitness_value = []
prob = []
bin = []
prob_cum_sum = []
selected_strings_idx = set()
select_freq = []
random_list = []
selected_strings = []
Offsprings = []

for i in range(len(strings)):
    fitness(strings[i])

total_sum = 0
maxi = 0
for i in fitness_value:
    total_sum += i
    if(i > maxi):
        maxi = i
avgerage = math.ceil(total_sum/len(fitness_value))

probability(fitness_value)

c_sum = 0
for i in range(len(prob)):
    c_sum += prob[i]
    prob_cum_sum.append(c_sum)

selected = selection(prob_cum_sum)

print(' => Phase 1:')
print('Fitness Value List:')
for i in fitness_value:
    print(i)

print('\nProbability List:')
for i in prob:
    print(i)

print('\nTotal Sum: ',total_sum)
print('Average: ',avgerage)
print('Max: ',maxi)

print('\nAssociated Bin List:')
for i in bin:
    print(i)

select_string = strings[selected]
selected_string_prob = prob[selected]
print('\nSelected chromosome: ',select_string)
print("Selected chromosome's probability: ", selected_string_prob)

print('\n => Phase 2:')

for i in selected_strings_idx:
    selected_strings.append(i)

for i in range(len(selected_strings)-1):
    crossover(selected_strings[i],selected_strings[i+1])

print('\nParent Strings: ')
for i in selected_strings:
    print(strings[i])

print('\nOffsprings: ')
for i in Offsprings:
    print(i)


print('\n => Phase 3:')
x_value.clear()
fitness_value.clear()
prob.clear()
bin.clear()
prob_cum_sum.clear()
selected_strings_idx.clear()
select_freq.clear()
random_list.clear()
selected_strings.clear()

for i in range(len(Offsprings)):
    fitness(Offsprings[i])

total_sum = 0
maxi = 0
for i in fitness_value:
    total_sum += i
    if(i > maxi):
        maxi = i
avgerage = math.ceil(total_sum/len(fitness_value))

probability(fitness_value)

c_sum = 0
for i in range(len(prob)):
    c_sum += prob[i]
    prob_cum_sum.append(c_sum)

print('Fitness Value List:')
for i in fitness_value:
    print(i)

print('\nProbability List:')
for i in prob:
    print(i)

print('\nTotal Sum: ',total_sum)
print('Average: ',avgerage)
print('Max: ',maxi)

selected = selection(prob_cum_sum)
select_string = Offsprings[selected]
selected_string_prob = prob[selected]
print('Selected chromosome: ',select_string)
print("Selected chromosome's probability: ", selected_string_prob)