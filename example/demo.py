import random
import time

from lib.animations.animdata import AnimData
from lib.animations.colordata import RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, WHITE, ColorData
from lib.animations.customanimation import CustomAnimation, EffectType
from lib.animations.paneldata import PanelData
from lib.layoutdetector import Layout
from lib.nanoclient import NanoLeafClient

colors = [
    # RED,
    GREEN,
    BLUE,
    # YELLOW,
    # ORANGE,
    PURPLE,
    # WHITE
]


def rand_color() -> ColorData:
    return random.choice(colors)


if __name__ == "__main__":
    nc = NanoLeafClient(auth_path='/Users/cearman/repos/nanoleaf-canvas/.auth',
                        address='10.0.0.129')
    layout = Layout(nanoclient=nc)
    layout.print_layout()

    animation_data = AnimData()
    for i in range(len(layout.tile_map.items())):
        panel_data = PanelData(panel_id=int(layout.translate(str(i))))

        for j in range(random.randint(1, 5)):
            panel_data.add_frame(rand_color())

        animation_data.add_panel(panel_data)

    animation = CustomAnimation(anim_data=animation_data, loop=True,
                                anim_type=EffectType.CUSTOM)
    print(animation.payload())
    print(nc.write_effect(effect_payload=animation.payload()))
    # time.sleep(1)

    # print(nc.get_effect())
