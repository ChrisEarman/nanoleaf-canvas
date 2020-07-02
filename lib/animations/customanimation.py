"""
{
  "command": "display/add",
  "animType": "static",
  "animData": "3 82 1 255 0 255 0 20 60 1 0 255 255 0 20 118 1 0 0 0 0 20",
  "loop": false
}
"""
from enum import Enum

from lib.animations.animdata import AnimData


class CommandType(Enum):
    DISPLAY = 'display'
    ADD = 'add'


class EffectType(Enum):
    STATIC = 'static'
    DYNAMIC = 'dynamic'
    SOLID = 'solid'
    CUSTOM = 'custom'


class CustomAnimation(object):
    def __init__(self,
                 anim_data: AnimData,
                 command: CommandType = CommandType.DISPLAY,
                 anim_type: EffectType = EffectType.STATIC,
                 loop: bool = False):
        self.anim_data = anim_data
        self.command = command
        self.anim_type = anim_type
        self.loop = loop

    def payload(self):
        return {
            "command": self.command.value,
            "animType": self.anim_type.value,
            "animData": str(self.anim_data),
            "loop": self.loop
        }
