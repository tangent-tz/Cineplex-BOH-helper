from bs4 import BeautifulSoup
import Main
import requests
import json


def test(url):
    ticketsales=[]

    for i in range(len(url)):
        test=requests.get(url[i])
        soup=BeautifulSoup(test.content, "html.parser")
        test=soup.find_all('script')
        test=str(test[17])
        test=test.replace("<script>", "")
        test=test.replace("</script>", "")
        test=test.replace("ko.applyBindings(seatMapViewModel);", "")
        test=test.replace("var seatMapViewModel = new SeatMapViewModel(seatMapViewModelInfo);", "")
        test=test.replace("   var seatMapViewModelInfo = ", "")
        test=test.replace("};", "}")
        test=test.replace("\n ", "")
        test=test.replace("     ", "")
        json_object=json.loads(test)
        with open('dev.json', 'w') as fp:
            json.dump(json_object, fp)
        Totalseats=json_object["SeatMapData"]["AvailableSeatCount"]+ json_object["SeatMapData"]["OccupiedSeatCount"]
        soldtickets= json_object["SeatMapData"]["OccupiedSeatCount"]
        temp = []
        temp.append(soldtickets)
        temp.append(Totalseats)
        ticketsales.append(temp)
    return (ticketsales)
