class Telemetry:
    def __init__(self):
        self.humidity = 0
        self.temperature = 0
        self.pressure = 0
        self.luminosity = 0.0
        self.lamps = 0
        self.airfan = 0
        self.heater = 0
        self.timestamp = 0

    def set(self, humidity, temperature, pressure, luminosity, lamps, airfan, heater, timestamp):
        self.humidity = humidity
        self.temperature = temperature
        self.pressure = pressure
        self.luminosity = luminosity
        self.lamps = lamps
        self.airfan = airfan
        self.heater = heater
        self.timestamp = timestamp

    def serialize(self):
        JSONed = {
            'humidity': self.humidity,
            'temperature': self.temperature,
            'pressure': self.pressure,
            'luminosity': self.luminosity,
            'lamps': self.lamps,
            'airfans': self.airfan,
            'heaters': self.heater,
            'timestamp': str(self.timestamp)
        }
        return JSONed
