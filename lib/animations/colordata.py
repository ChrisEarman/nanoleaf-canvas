class ColorData(object):
    """
    R; G; B; W; T;
    red, green, blue, (W is ignored), T for transition time.
    """
    def __init__(self, r: int, g: int, b: int, t: int = 0):
        """
        Constructor for color data ommits W value as it is ignored by the controller, always set to 0
        :param r:       red value in an RGB format
        :param g:       green value in an RGB format
        :param b:       blue value in an RGB format
        :param t:       transition time, t=1 means 100ms, -1 will have the frame start at that value (not recommended)
        """
        self.r, self.g, self.b , self.w, self.t = r, g, b, 0, t

    def __str__(self):
        return "{r} {g} {b} {w} {t}".format(r=self.r, g=self.g, b=self.b, w=self.w, t=self.t)


RED = ColorData(255, 0, 0, 10)
ORANGE = ColorData(255, 255, 0, 10)
GREEN = ColorData(0, 255, 0, 10)
YELLOW = ColorData(0, 255, 255, 10)
BLUE = ColorData(0, 0, 255, 10)
PURPLE = ColorData(255, 0, 255, 10)
WHITE = ColorData(255, 255, 255, 10)
