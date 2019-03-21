class Canvas():
    def draw(self, bitmap):
        pass

class HorizontalScrollbar():
    def __init__(self, canvas):
        self._canvas = canvas

    def draw(self, bitmap):
        # TODO
        self._canvas.draw(bitmap)

class VerticalScrollbar():
    def __init__(self, canvas):
        self._canvas = canvas

    def draw(self, bitmap):
        self._canvas.draw(bitmap)
        # TODO


c = VerticalScrollbar(HorizontalScrollbar(Canvas()))

c2 = VerticalScrollbar(Canvas())
