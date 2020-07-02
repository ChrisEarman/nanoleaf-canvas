"""
https://forum.nanoleaf.me/docs/openapi

Section 3.2.6.1

 numPanels; panelId0; numFrames0; RGBWT01; RGBWT02; ... RGBWT0n(0);
      panelId1; numFrames1; RGBWT11; RGBWT12; ... RGBWT1n(1); ... ... panelIdN;
      numFramesN; RGBWTN1; RGBWTN2; ... RGBWTNn(N);

Examples
Temporary static display

Copy{
  "command": "display/add",
  "animType": "static",
  "animData": "3 82 1 255 0 255 0 20 60 1 0 255 255 0 20 118 1 0 0 0 0 20",
  "loop": false
}

2
53349 2
255 255 0 0 0
0 255 255 0 0
21918 2
255 255 255 0 0
255 255 255 0 0

Copy<nPanels> = 3
<numFrames> = 1
Panel 1:
PanelId: 82, R:255, G:0, B:255, W:0, TransitionTime:20*0.1s
Panel 2:
PanelId: 60, R:0, G:255, B:255, W:0, TransitionTime:20*0.1s
Panel 3:
PanelId:118, R:0, G:0, B:0, W:0, TransitionTime:20*0.1s
"""
from lib.animations.colordata import ColorData, RED, BLUE
from lib.animations.paneldata import PanelData


class AnimData(object):
    """
    Collection of Panel data
    """
    def __init__(self, panels: [PanelData] = None):
        self.panels = panels if panels else []

    def __str__(self):
        panels = " ".join(map(str, self.panels))
        return "{panel_count} {panels}".format(panel_count=str(len(self.panels)),
                                               panels=panels)

    def add_panel(self, panel: PanelData):
        """
        adds a PanelData to the animation data object
        :param panel:   PanelData
        :return: this AnimData object
        """
        self.panels.append(panel)
        return self


if __name__ == "__main__":
    pd = PanelData(panel_id=12200, frames=[ColorData(10, 20, 30, 5),
                                           ColorData(11, 22, 33, 5)])
    pd2 = AnimData().add_panel(
        PanelData(12200)
        .add_frame(RED)
        .add_frame(BLUE)
    )
    print(str(pd))
    print(str(pd2))
