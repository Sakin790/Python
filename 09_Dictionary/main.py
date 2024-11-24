marks={
    "science":100,
    "Arts":19
}
print(marks["science"])
print(marks.get("Arts"))

student={
    "id":1,
    "name":"Mahid",
    "class":9,
    "Location":"BD",
    "age":19
}
print(student["name"])
print(student.get("class"))
print(student.get("Location"))
del student["Location"]
print(student.get("Location"))
print(len(student))