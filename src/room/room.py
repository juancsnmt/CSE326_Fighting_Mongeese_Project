import room.shapes_room.shape

class room:
    def __init__(self, *args, **kwargs):
        if 'shape' in kwargs:
            self.shape = copy.deepcopy(kwargs.get('shape'))
        if 'children' in kwargs:
            self.children = children
