d = {} #empty dictonary

marks = {
    "harry":100,
    "raghav":32,
    "rohan":54,
    0:"harry"
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"harry":99,"renuka":44})
print(marks)

print(marks.get("harry")) #prints NONE
print(marks["harry"])     #returns an error 