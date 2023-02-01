import struct

class SCUnit():
    # sc unit helper class
    def __init__(self, data):
        self.class_instance, \
        self.x, self.y, \
        self.unit_id, self.link,\
        self.valid_flags, self.valid_props, \
        self.owner, self.hp, self.sp, self.energy, self.res, self.hangar, \
        self.flags, _, self.linked_class_instance = data
        
    def data(self):
        return struct.pack("<I6H4BIHHII", self.class_instance, self.x, self.y, self.unit_id, self.link,
                          self.valid_flags, self.valid_props, self.owner, self.hp, self.sp, self.energy,
                           self.res, self.hangar, self.flags, 0, self.linked_class_instance)
