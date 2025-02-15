# Nodes Dictionary which takes a key of node number and a value of also a dictionary with keys that are the nodes connected to the prior node and value of the weight of the line
nodes = {
    # Node Number : {Node Number : Node Weight}
    "1" : {
    3 : 10,
    2 : 12,
    7 : 12
},
    "2" : {
    3 : 8,
    1 : 12,
    4 : 12
},
    "3" : {
    5 : 3,
    2 : 8,
    7 : 9,
    1 : 10,
    4 : 11
},
    "4" : {
    6 : 10, 
    5: 11,
    3 : 11, 
    2 : 12
},
    "5" : {
    3 : 3,
    6 : 6,
    7 : 7,
    4 : 11
},
    "6" : {
    5 : 6, 
    7 : 9,
    4 : 10
},
    "7" : {
    5 : 7, 
    6 : 9,
    3 : 9, 
    1 : 12
}
}
combinations = [] # A container for the possible routes / combinations of nodes
total_weight = [] # Corresponding weight of the routes that will be stored on the combination list

starting_index = input("Enter the starting node (1-7): ")
# Nested Loops that takes consideration of every possible routes
for key1 in nodes[starting_index]: 
    current_node_list = [int(starting_index), key1] # Container for the nodes that are already passed on
    for key2 in nodes[str(key1)]:
        if key2 not in current_node_list: # To handle nodes going back to their predecessor
            for key3 in nodes[str(key2)]:
                current_node_list = [int(starting_index), key1,key2]
                if key3 not in current_node_list:
                    for key4 in nodes[str(key3)]:
                        current_node_list = [int(starting_index), key1,key2,key3]
                        if key4 not in current_node_list:
                            key = f"{starting_index}-{key1}-{key2}-{key3}-{key4}"
                            value = sum([nodes[starting_index][key1], nodes[str(key1)][key2], nodes[str(key2)][key3], nodes[str(key3)][key4]])
                            combinations.append(key)
                            total_weight.append(value)

smallest_weight = total_weight[0] # Starting value
smallest_weight_index = 0  # Starting index
for i in range(1, len(total_weight)): # Checks for both the lowest number and its index among the weights
    if total_weight[i] < smallest_weight:
        smallest_weight = total_weight[i]
        smallest_weight_index = i

print(f"The Shortest Path to Reach 5 Cities Are: {combinations[smallest_weight_index]}")
