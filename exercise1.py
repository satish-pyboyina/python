def generate_evens():
    num = list(range(1,50) )
    evens = []
    # print(num)
    for x in num:
        # print(x)
        if(x%2 == 0):
            evens.append(x)
    print(evens)

generate_evens()

def generate_evens2():
    evens = []
    x=1
    while x < 50:
        if x%2 == 0:
            evens.append(x)
            x+=1
        x+=1
    print(evens)
generate_evens2()

