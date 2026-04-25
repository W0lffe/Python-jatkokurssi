import requests
import datetime

def train_departure(train, station, date):
    dateString = date.isoformat()

    url = f'https://rata.digitraffic.fi/api/v1/trains/{dateString}/{train}'

    ok=True
    try:
        response = requests.get(url)
    except Exception as e:
        print(e)
        ok=False

    if ok:
        data = response.json()
        if not data:
            raise Exception("Junaa ei löydy")
        
        
        timeTable = data[0]['timeTableRows']

        for row in timeTable:
            if(row['stationShortCode'] == station and row['type'] == 'DEPARTURE'):

                time = row.get('actualTime') or row.get('scheduledTime')
                dateTime = datetime.datetime.fromisoformat(time.replace("Z", ""))
                return dateTime.strftime('%Y-%m-%d %H:%M')
        




if __name__=='__main__':
    date=datetime.date(2021, 3, 21)
    departure = train_departure('56', 'OL', date)
    print(departure)
    


