def getMovieTicketUrl(soup):
    id = soup.find_all('a', class_="showtime ng-binding ng-scope")
    for index, identities in enumerate(id):
        id[index] = id[index].get("id")
    url_data1_arr = []
    url_data2_arr = []
    url_data1 = ""
    url_data2 = ""
    url_arr = []
    for idd in range(len(id)):
        for index in range(9, 14):
            url_data1 = url_data1 + id[idd][index]
        url_data1_arr.append(url_data1)
        url_data1 = ""

    for idd in range(len(id)):
        for index in range(18, 27):
            url_data2 = url_data2 + id[idd][index]
        url_data2_arr.append(url_data2)
        url_data2 = ""
    for index in range(len(url_data1_arr)):
        url_arr.append(
            "https://onlineticketing.cineplex.com/SeatMap.aspx?locationId=1145&vistaSessionId=" + url_data1_arr[
                index] + "&VISTAHOAreaCategoryCode=" + url_data2_arr[index] + "&isExternal=True")
    return url_arr


def pretty_MovieTime(movie_time):
    target = []
    for index in range(len(movie_time)):
        temp = movie_time[index].split("|")
        temp.remove('')
        target.append(temp)
    return target


def movieSalesStatus(ticket_sales_status, seats):
    temp = [None] * len(ticket_sales_status)
    seatcounter = 0
    ticketcounter = 0
    while (ticketcounter < len(ticket_sales_status)):
        if (ticket_sales_status[ticketcounter] == '1'):
            temp[ticketcounter] = seats[seatcounter]
            seatcounter += 1
        else:
            temp[ticketcounter] = "Ticket Sales Closed"
        ticketcounter += 1
    return temp
