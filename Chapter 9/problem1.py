poem = open("poem.txt")
content = poem.read()
print(content)
if("Twinkle" in content):
    print("twinkle is present")
else:
    print("twinkle is not present")
poem.close()
# The code opens a file named "poem.txt", reads its content, and prints it  