name = input("Enter your name:")
date = input("Enter date:")
print(f''' Dear {name}
You are selected!
      {date}''')

letter = '''Dear name
you are selected
date'''
print(letter.replace("name","raghav").replace("date","23 sept 2050").capitalize())