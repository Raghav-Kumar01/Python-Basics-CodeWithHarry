words = ["bad"  , "Donkey" , "nice"]
with open("donkey_prb4.txt") as f:
     content = f.read()
for word in words:
    content = content.replace(word , "#"*len(word))    
with open("donkey_prb4.txt" , "w") as f:
     f.write(content)
