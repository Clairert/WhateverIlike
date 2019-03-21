# Decorator Pattern Example
#
# Suppose your tracking service has a Tracker object that you either
# wish to get stats on, or are trying to debug in a production environment.
# A decorator can let you log to one or more files, in whichever order you want.
#

class Tracker():
    def get_packet(self):
        print("receiving packet from service")

    def decode_packet(self):
        print("pulling out location elements from packet")


class TrackerLoggingToInfo(Tracker):
    def __init__(self, t):
        # The big trick: store a reference to the thing you want to decorate...
        self.my_tracker = t

    def get_packet(self):
        print("logging some start state to info file")
        # ...then call the method of the parent object.  Now you can call the
        # wrappers in an order that is independent of the class hierarchy.
        self.my_tracker.get_packet()
        print("logging some end state to info file")

    def decode_packet(self):
        """
        It's important to provide a version of this method in the decorator.
        If you rely on inheritance, you'll get the instance method of the Decorator,
        rather than the object it's trying to decorate.
        """
        self.my_tracker.decode_packet()

class TrackerLoggingToError(Tracker):
    def __init__(self, t):
        self.my_tracker = t

    def get_packet(self):
        print("logging some start state to error file")
        self.my_tracker.get_packet()
        print("logging some end state to error file")

    def decode_packet(self):
        self.my_tracker.decode_packet()


if __name__ == "__main__":
    t = Tracker()
    ti = TrackerLoggingToInfo(t)
    te = TrackerLoggingToError(t)
    tei = TrackerLoggingToError(TrackerLoggingToInfo(t))
    t.get_packet()
    print()
    ti.get_packet()
    print()
    te.get_packet()
    print()
    tei.get_packet()
    tei.decode_packet()