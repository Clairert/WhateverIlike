class Publisher():
    def __init__(self):
        self.subscribers = []

    def register(self, subscriber):
        self.subscribers.append(subscriber)

    def deregister(self, subscriber):
        pass  # TODO later

    def notify_all(self):
        for s in self.subscribers:
            s.notify(self)


class EnvDataCollector(Publisher):

    def __init__(self):
        super().__init__()
        self.latest_temperature = 0
        self.latest_humidity = 0

    def set_temperature(self, temperature):
        self.latest_temperature = temperature
        self.notify_all("temp")

    def set_humidity(self, humidity):
        self.latest_humidity = humidity
        self.notify_all()

    def get_latest_temperature(self):
        return self.latest_temperature

    def get_latest_humidity(self):
        return self.latest_humidity


class CurrentWeatherDisplay():
    def notify(self, dataCollector):
        print("Current temperature: %f, current humidity: %d%%" % (dataCollector.get_latest_temperature(), dataCollector.get_latest_humidity()))


class AverageWeatherDisplay():
    def __init__(self):
        self.humidity_count = self.humidity_sum = 0
        self.temperature_count = self.temperature_sum = 0

    def notify(self, dataCollector):
        self.temperature_sum += dataCollector.get_latest_temperature()
        self.humidity_sum += dataCollector.get_latest_humidity()
        self.temperature_count += 1
        self.humidity_count += 1
        print("Avg temperature: %f, avg humidity: %d%%" % (self.temperature_sum / self.temperature_count, self.humidity_sum / self.humidity_count))


if __name__ == "__main__":
    collector = EnvDataCollector()

    display = CurrentWeatherDisplay()
    collector.register(display)
    collector.register(AverageWeatherDisplay())

    # simulate temperature readings
    collector.set_temperature(21)
    collector.set_humidity(55)
    collector.set_temperature(21.1)
    collector.set_temperature(21.3)
