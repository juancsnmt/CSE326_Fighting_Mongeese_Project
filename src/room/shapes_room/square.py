import shape

class square(shape):
    def __init__(self, *args, **kwargs):
        shape.__init__(self, args, kwargs)
        if 'height' in kwargs:
            self.height = kwargs.get("height")
        else:
            self.height = 1
        if 'width' in kwargs:
            self.width = kwargs.get("width")
        else:
            self.width = 1
