def sensorStub():
    return {
        'temperatureInC': 50,
        'precipitation': 70,
        'humidity': 26,
        'windSpeedKMPH': 52
    }


def rainyStub():
    return {
        'temperatureInC': 30,
        'precipitation': 70,  
        'humidity': 60,
        'windSpeedKMPH': 40  
    }

def report(sensorReader):
    readings = sensorReader()
    weather = "Sunny Day"

    if (readings['temperatureInC'] > 25):
        if readings['precipitation'] >= 20 and readings['precipitation'] < 60:
            weather = "Partly Cloudy"
        elif readings['windSpeedKMPH'] > 50:
            weather = "Alert, Stormy with heavy rain"
    return weather


def testRainy():
    weather = report(rainyStub)
    print("TestRainy:", weather)
    assert("rain" in weather.lower())  


def testHighPrecipitation():
    weather = report(rainyStub)
    print("TestHighPrecipitation:", weather)
    assert(weather == "Alert, Stormy with heavy rain")  


if __name__ == '__main__':
    testRainy()
    testHighPrecipitation()
    print("All is well (maybe!)")
