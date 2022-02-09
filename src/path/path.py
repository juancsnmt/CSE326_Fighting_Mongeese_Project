import room.room
import constants.position

class path:
    # Accepts \theta, r_{1}, r_{2} (|dist from origin|)
    def __init__(self, *args, **kwargs):
        self.children_no = 0
        if 'r1' in kwargs && 'r2' in kwargs:
            self.r1 = kwargs.get('r1')
            self.r2 = kwargs.get('r2')
        else:
            self.r1 = 0
            self.r2 = 1
        if 'theta' in kwargs:
            self.theta = kwargs.get('theta')
        else:
            self.theta = 90.0
        # meant to be array of rooms
        if 'rooms' in kwargs:
            self.rooms = rooms

    def get_r1(self):
        return self.r1
    def get_r2(self):
        return self.r2
    def get_length(self):
        return self.length
    def get_rooms(self):
        return self.rooms
