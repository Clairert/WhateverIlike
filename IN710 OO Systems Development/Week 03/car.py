import time


def timed(func):
    def time_on_call(*args, **kwargs):
        start = time.time()
        retVal = func(*args, **kwargs)
        end = time.time()
        print("Warning, %s took %3fs" % (func.__name__, end-start))
        return retVal
    return time_on_call


class Car():
    @timed
    def drive(self):
        time.sleep(0.5)
        return "driving"

    def stop(self):
        return "stopping..."


class Boat():
    def drive(self):
        return "driving"

    def stop(self):
        return "stopping..."


class LoudExhaust():
    def __init__(self, car):
        self._car = car

    def drive(self):
        return self._car.drive() + " and making a lot of noise"

    def stop(self):
        return self._car.stop()

    def skid(self):
        return self._car.skid()


if __name__ == "__main__":
    c = Car()
    c = LoudExhaust(c)
    print(c.drive())
    print(c.stop())

    b = LoudExhaust(Boat())
    print(b.drive())

