import sys
    
# 0 is incident_id
# 1 is incident_type
# 2 is vin_number
# 3 is make
# 4 is model
# 5 is year
# 6 is incident_date
# 7 is description

# List from standard input
automobiles = [line.strip().split(",") for line in sys.stdin]

# Passing standard input to reducer
for automobile in automobiles:
    print(automobile)

# Dictionary containing vin_number, incident_type, make, year
automobiles_dict = {auto[2]: auto[1] + auto[3] + auto[5] for auto in automobiles}

# Passing dictionary to reducer
for key, value in automobiles_dict.items():
    print(key, value)