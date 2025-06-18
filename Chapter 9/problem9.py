with open("this1.txt") as f:
    content1 = f.read()

with open("this2.txt") as f:
    content2 = f.read()
if(content1 == content2):
    print("Yes these files are idnitical")
else:
    print("NOT IDENTICAL")