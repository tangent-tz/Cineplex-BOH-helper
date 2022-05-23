import json

import requests
from bs4 import BeautifulSoup

def getTicketSoldStatus(url, ticketsold=False, totalseat=False):
    ticketsales = []
    for i in range(len(url)):
        test = requests.get(url[i])
        soup = BeautifulSoup(test.content, "html.parser")
        test = soup.find_all('script')
        test = str(test[17])
        test = test.replace("<script>", "")
        test = test.replace("</script>", "")
        test = test.replace("ko.applyBindings(seatMapViewModel);", "")
        test = test.replace("var seatMapViewModel = new SeatMapViewModel(seatMapViewModelInfo);", "")
        test = test.replace("   var seatMapViewModelInfo = ", "")
        test = test.replace("};", "}")
        test = test.replace("\n ", "")
        test = test.replace("     ", "")
        json_object = json.loads(test)
        with open('../dev.json', 'w') as fp:
            json.dump(json_object, fp)
        Totalseats = json_object["SeatMapData"]["AvailableSeatCount"] + json_object["SeatMapData"]["OccupiedSeatCount"]
        soldtickets = json_object["SeatMapData"]["OccupiedSeatCount"]
        if(ticketsold==True):
            ticketsales.append(soldtickets)
        if(totalseat==True):
            ticketsales.append(Totalseats)
    return ticketsales


