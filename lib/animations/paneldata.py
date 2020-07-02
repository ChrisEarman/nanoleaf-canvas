from lib.animations.colordata import ColorData


class PanelData(object):
    """
    Collection of frame data in the form of a set of ColorData objects for a given panel
    """
    def __init__(self, panel_id: int, frames: [ColorData] = None):
        self.frames = frames if frames else []  # type: [ColorData]
        self.panel_id = panel_id  # type: int

    def __str__(self):
        frames = " ".join(map(str, self.frames))
        return "{panel_id} {frame_count} {frames}".format(panel_id=self.panel_id,
                                                          frame_count=str(len(self.frames)),
                                                          frames=frames)

    def add_frame(self, frame: ColorData, pos: int = -1):
        """
        adds a frame to this panels animation
        :param frame: ColorData value for the frame
        :param pos: position to add the frame, if -1 adds to the end
        :return: this PanelData object
        """
        self.frames.insert(pos, frame)
        return self