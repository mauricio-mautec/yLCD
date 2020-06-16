def getSensorData ():
    maxTries = 3
    readOK   = 0
    humidity = -1
    temp     = -1

    while (not readOK and maxTries):
        humidity, temp = Adafruit_DHT.read_retry (Sensor, pinDHT)
        if (temp > 50 or temp < -10 or  humidity > 100 or humdity == 0):
            maxTries -= 1
            time.sleep(1)
            continue
        readOK = 1

    return [humidity, temp]
