import requests

def weather():

    s_city = "Petrozavodsk,RU"
    city_id = 509820
    appid = "8a61dda3a2ef6afaf929cc1c4154f9ef"
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                            params={'q': s_city,
                                    'type': 'like',
                                    'units': 'metric',
                                    'APPID': appid
                            })
        data = res.json()
        print(data)
        print("температура",data['list'][0]['main']['temp'])
        print("ощущается",data['list'][0]['main']['feels_like'])
        print("давление",data['list'][0]['main']['pressure'])
        print("ощущается",data['list'][0]['main']['humidity'])
    except Exception as e:
                print("Исключение:", e)
                pass
