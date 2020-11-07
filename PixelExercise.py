picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
    ]

for item in picture :
    for item_star in item :
        if item_star == 1 :
            print('*',end = "")
        else : print(' ',end = "")
    print(end="\n")
