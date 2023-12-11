data = open("d1input")
f = data.readlines()


letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","y","x","z"]


i = 0
for x in f:
    current = x
    slop = []
    for y in current:
        if y in letters:
            pass
        else:
            slop.append(y)
    math = slop[0] + slop[-2]
    i+= int(math)
    print(i)
