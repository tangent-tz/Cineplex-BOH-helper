
def guestnumber(movie_per_show_type, temp):
    x=0
    A=[]
    B=[]
    for temped in enumerate(movie_per_show_type):
        for i in range(temped[1]):
            A.append(temp[x])
            x+=1
        B.append(A)
        A=[]
    return B