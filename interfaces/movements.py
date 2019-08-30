
# NOTE: "I" is just a naming convention to remind us that twwe are using these as interfaces
class ISwimming:

    def __init__(self):
        self.swim_speed = 0
        self.maximum_depth = 0

    def swim(self):
        print("Glug glug, I'm swimming!")

class IFlying:

    def __init__(self, wing_count=2):
        self.flight_speed = 0
        self.wing_count = wing_count

    def fly(self):
        print("Flap flap, I'm flying!")

class IWalking:

    def __init__(self, leg_count=2):
        self.leg_count = leg_count
        self.move_speed = 0
