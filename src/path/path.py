import room.room
import constants.position

class path:
    def __init__(self, *args, **kwargs):
        if 'position' in kwargs:
            self.position = kwargs.get('position')
            if self.position == position.VERT:
                self.name = "|"
            elif self.position == position.HORZ:
                self.name = "-"

    def get_position(self):
        return self.position

    def get_name(self):
        return self.name
