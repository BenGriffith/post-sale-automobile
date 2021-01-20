import sys

# Receiving input from mapper and setting up structures for cleaning
standard_input = list(sys.stdin)
automobiles = [auto for auto in standard_input[:16]]
automobiles_clean = []
automobiles_dict = {auto.strip().split(" ")[0]: [auto.strip().split(" ")[1], "", ""] for auto in standard_input[16:]}

# Produce clean list of complete vehicle information
for auto in automobiles:
    line = auto.strip().strip("[]").split(",")
    line[0] = line[0].strip("''")
    for i in range(1, 8):
        line[i] = line[i].strip(" ''")
    
    automobiles_clean.append(line)

# Compare VIN in dictionary to VIN in clean list of vehicle information to retrieve make and year
for key in automobiles_dict:
    for auto in automobiles_clean:
        if key == auto[2]:
            if auto[3] != '' and auto[5] != '':
                automobiles_dict[key][1] = auto[3]
                automobiles_dict[key][2] = auto[5]

# Passing complete vehicle information to mapper
for auto in automobiles_clean:
    print(auto)

# Passing dictionary with make and year updated to mapper
for key, value in automobiles_dict.items():
    print(key, value)