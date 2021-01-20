import sys

# Receiving input from reducer and setting up structures for cleaning
standard_input = list(sys.stdin)
automobiles = [auto.strip() for auto in standard_input[:16]]
automobiles_clean = []
automobiles_dict_clean = []
automobiles_dict = {}

# Produce clean list of complete vehicle information
for auto in automobiles:
    line = auto.strip().strip("[]").split(",")
    line[0] = line[0].strip("''")
    for i in range(1, 8):
        line[i] = line[i].strip(" ''")

    automobiles_clean.append(line)

# Setup dictionary data to be cleaned
for auto in standard_input[16:]:
    automobiles_dict_clean.append([auto[:18].strip(), auto[18:].strip()])

# Clean dictionary data
for auto in automobiles_dict_clean:
    auto[1] = auto[1].strip("[]").split(",")
    auto[1][0] = auto[1][0].strip("''")
    auto[1][1] = auto[1][1].strip(" ''")
    auto[1][2] = auto[1][2].strip(" ''")

# Setup dictionary after data cleaned
for auto in automobiles_dict_clean:
    automobiles_dict[auto[0]] = auto[1]

# Check for accident
def is_accident(vin, alist):
    accident_count = 0
    for i in alist:
        if vin == i[2] and i[1] == "A":
            accident_count += 1
    
    return accident_count

# Update dictionary with accident information
for key in automobiles_dict:
    automobiles_dict[key] += str(is_accident(key, automobiles_clean))

# Passing dictionary to reducer
for key, value in automobiles_dict.items():
    print(key, value)