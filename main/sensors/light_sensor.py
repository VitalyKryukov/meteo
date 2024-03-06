class LightSensor:
    i = 0

    def __init__(self):
        pass

    def light(self):
        self.i = self.i + 1
        return self.i

    def proximity(self):
        return self.i
