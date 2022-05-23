def totalShows(movie_time_refined, seats):
    temp = 0
    for i in range(len(movie_time_refined)):
        for j in range(len(movie_time_refined[i])):
            temp = temp + 1
    return temp


def ticketSalesStopped(movie_time_refined, seats):
    temp = totalShows(movie_time_refined, seats)
    return (temp - len(seats))


def copyconstructor(tocopy):
    temp = []
    for i in range(len(tocopy)):
        temp.append(tocopy[i])
    return temp


def printer(movie_name, show_type_per_movie, showtypes, movie_time_refined, Guestlist):
    iter = 0
    iter1 = 0
    thisdict = {}

    for i, names in enumerate(show_type_per_movie):
        thisdict2 = {"Name": [], "Screen Type": [], "Time": [], "SeatsOccupied": []}
        thisdict2["Name"] = movie_name[i]
        # print(movie_name[i])
        for j in range(show_type_per_movie[i]):
            thisdict2["Screen Type"].append(showtypes[iter])
            thisdict2["Time"].append(movie_time_refined[iter])
            thisdict2["SeatsOccupied"].append(Guestlist[iter])
            # print(showtypes[iter])
            # print(movie_time_refined[iter])
            # print(Guestlist[iter])
            iter += 1
        thisdict[i] = thisdict2
        iter1 += 1
        # print(thisdict)
    return thisdict


def getTicketSales(soup):
    test = soup.find_all(class_="showtime-wrap clearfix ng-scope")
    temp = []
    for i in range(len(test)):
        if (test[i].find(class_="seatMapDisabled seatMapLink ng-scope") != None):
            temp.append("0")
        else:
            temp.append("1")
    return temp
