class shape:
    __init__(self, *args, **kwargs):
        if 'co_center' in kwargs:
            self.co_center = kwargs.get("co_center")
        else:
            self.co_center = 0
        if 'paths' in kwargs:
            self.paths = paths
        else:
            self.paths = []

