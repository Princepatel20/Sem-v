def fractional_knapsack(value, weight, capacity):
index = list(range(len(value)))
ratio = [v/w for v, w in zip(value, weight)]
index.sort(key=lambda i:ratio[i], reverse=True)
max_value = 0
fractions = [0]*len(value)
for i in index:
if weight[i] <= capacity:
fractions[i] = 1
max_value += value[i]
capacity -= weight[i]
else:
fractions[i] = capacity/weight[i]
max_value += value[i]*capacity/weight[i]
break
return max_value, fractions
weight = [10,20,30]
value= [60,100,150]
capacity = 50
max_value, fractions = fractional_knapsack(value, weight, capacity)
print("Maximum value:", max_value)
print("Fractions:", fractions)
