student = {
    # key: value
    "name": "Bob",
    18: True,
    "music": ["rock", "classic"],
    "email": {"home": "bob@home.com", "work": "bob@work.com"}
}

# Get the name and music taste from the dictionary
print(student["name"])
print(student["music"])
print(student[18])
print(student["email"]["work"])

# Loop over dictionaries
for key, value in student.items():
    print(f"The key is {key} and the value is {value}")

# Check if something is in a dictionary
if "adress" in student:  # Check if the key is in the dictionary
    print(student["adress"])  # If it is, print the value
else:
    student["adress"] = ""  # If it is not, add the key and value to the dictionary

print(student)
