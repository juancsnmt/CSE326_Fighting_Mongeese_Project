import paths.paths

class rooms:
    def __init__(self, *args, **kwargs):
        if 'above' in kwargs:
            self.above = paths(kwargs.get('above'))
        if 'right' in kwargs:
            self.right = paths(kwargs.get('right'))
        if 'below' in kwargs: 
            self.below = paths(kwargs.get('below'))
        if 'left' in kwargs:
            self.left = paths(kwargs.get('left'))
 
