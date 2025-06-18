word = "Donkey"
with open("donkey_prb4.txt") as f:
     content = f.read()

contentNew = content.replace(word , "#####")    
with open("donkey_prb4.txt" , "w") as f:
     f.write(contentNew)
