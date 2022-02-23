"""Demonstration of dictionary capabilities."""


# Declaring the type of dictionary
schools: dict[str, int]

# Initialize to an empty dictionary
schools = dict()

# Set a key-value pairing in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26510

print(f"UNC has {schools['UNC']} students")

# remove s key-value pair from dict. by its key
schools.pop("Duke")

# Test for existence of a key
if "Duke" in schools:
    print("Found the key 'Duke' in schools.")
else:
    print("No key 'Duke' in schools")

# Update / Resassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200

print(schools)

# Demonstration of dictionary literals 

# Empty dictionary literal
schools = {}  # same as dict()

# Alternatively, initilize key-value pairs
schools = {
    "UNC": 19400, 
    "Duke": 6717, 
    "NCSU": 26510}
print(schools)
for school in schools:
    print