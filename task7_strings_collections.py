text = "Python Data Analytics"
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Replace:", text.replace("Python", "Basic Python"))
print("Find 'Data':", text.find("Data"))

numbers = [30, 10, 20]
numbers.append(40)
numbers.remove(10)
numbers.sort()
print("List:", numbers)

student_tuple = ("Ananya", 20, "CSE")
print("Tuple:", student_tuple)
print("Tuple item at index 0:", student_tuple[0])

student = {"name": "Ananya", "age": 20, "branch": "CSE"}
print("Student dictionary:", student)

skills = {"Python", "Excel"}
skills.add("SQL")
skills.remove("Excel")
print("Set:", skills)
