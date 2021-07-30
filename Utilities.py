def totalShows(movie_time_refined, seats):
    temp=0
    for i in range(len(movie_time_refined)):
        for j in range(len(movie_time_refined[i])):
            temp=temp+1
    return temp
    
def ticketSalesStopped(movie_time_refined, seats):
    temp=totalShows(movie_time_refined, seats)
    return (temp-len(seats))