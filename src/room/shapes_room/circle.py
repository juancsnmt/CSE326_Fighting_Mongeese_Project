import room.shapes_room.shape

class circle(shape):
    def __init__(self, *args, **kwargs):
        shape.__init__(self, args, kwargs)
        if 'radius' in kwargs:
            self.radius = kwargs.get("radius")
        else:
            self.radius = 1
