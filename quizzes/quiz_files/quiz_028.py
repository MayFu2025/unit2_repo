def sort_dict(in_dict:dict)-> dict:
    x = in_dict.values()
    y = in_dict.keys()
    for i in range(len(x)):
        for n in range(i+1, len(x)):
            if x[i] > x[n]:
                x[i],x[n] = x[n],x[i]
                y[i],y[n] = y[n],y[x]
    z = {}


    # low cost