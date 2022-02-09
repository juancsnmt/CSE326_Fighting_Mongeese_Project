import rooms.rooms
import constants.positions

class paths:
    def __init__(self, *args, **kwargs):
        if 'position' in kwargs:
            self.position = kwargs.get('position')
            if self.position == positions.VERT:
                self.name = "|"
            elif self.position == positions.HORZ:
                self.name = "-"

    def get_position(self):
        return self.position

    def get_name(self):
        return self.name
