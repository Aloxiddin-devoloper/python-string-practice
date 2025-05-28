import random

name1 = input("isminggizni kiriting:")
name2 = input("Familyanggizni kiriting:")

b = random.randint(1, 100)

a = f"{name1}.{name2}\n {name2}_{name1}\n {name2[0]}{name1}{b}\n {name1}{name2[0]}"

print(a)
