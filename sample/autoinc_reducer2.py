import sys

# Receiving input from mapper and setting up structures for cleaning
standard_input = list(sys.stdin)
automobiles_data = []
automobiles_dict = {}
make_year = set()
make_year_dict = {}

# Setup dictionary data to be cleaned
for auto in standard_input:
    automobiles_data.append([auto[:18].strip(), auto[18:].strip()])

# Clean dictionary data
for auto in automobiles_data:
    auto[1] = auto[1].strip("[]").split(",")
    auto[1][0] = auto[1][0].strip("''")
    auto[1][1] = auto[1][1].strip(" ''")
    auto[1][2] = auto[1][2].strip(" ''")
    auto[1][3] = auto[1][3].strip(" ''")

# Setup dictionary after data cleaned
for auto in automobiles_data:
    automobiles_dict[auto[0]] = auto[1]

# Retrieve make year from dictionary
for key, value in automobiles_dict.items():
    make_year.add((value[1], value[2]))

# Sum accidents by make and year
for value in automobiles_dict.values():
    if int(value[3]) > 0:
        for make in make_year:
            make_year_name = '{} {}'.format(str(make[0]), str(make[1]))
            if value[1] == make[0] and value[2] == make[1]:
                if make_year_name in make_year_dict:
                    make_year_dict[make_year_name] += 1
                else:
                    make_year_dict[make_year_name] = 1
            
# Output make and year accident counts
for key, value in make_year_dict.items():
    print(key, value)