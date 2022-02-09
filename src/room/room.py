import path.path

class room:
    def __init__(self, *args, **kwargs):
        self.path_no = 0
        if 'above' in kwargs:
            self.paths[self.path_no] = copy.deepcopy(kwargs.get('above'))
            self.path_no += 1
            self.above_index = self.path_no
        if 'right' in kwargs:
            self.paths[self.path_no] = copy.deepcopy(kwargs.get('above'))
            self.path_no += 1
            self.right_index = copy.deepcopy(kwargs.get('right'))
        if 'below' in kwargs: 
            self.paths[self.path_no] = copy.deepcopy(kwargs.get('above'))
            self.path_no += 1
            self.below_index = copy.deepcopypaths(kwargs.get('below'))
        if 'left' in kwargs:
            self.paths[self.path_no] = copy.deepcopy(kwargs.get('above'))
            self.path_no += 1            
            self.left_index = copy.deepcopypaths(kwargs.get('left'))
 
