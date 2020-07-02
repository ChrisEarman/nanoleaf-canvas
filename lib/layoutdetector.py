from lib.nanoclient import NanoLeafClient


class Layout(object):
    def __init__(self, nanoclient: NanoLeafClient):
        self.nanoclient = nanoclient
        self._raw_positional_data = None
        self.tile_map = {}  # type: dict
        self._detect()

    def _names(self):
        """
        internal generator for names, can be overwritten to suit different needs
        :return:
        """
        return [str(x) for x in range(len(self._raw_positional_data))]

    def _detect(self):
        self._raw_positional_data = self.nanoclient.get_info()["panelLayout"]["layout"]["positionData"]

        names = self._names()
        for tile in sorted(self._raw_positional_data, key=lambda t: (t['x'], t['y'])):
            self.tile_map[names.pop()] = tile

    def get_tile(self, name):
        if name in self.tile_map:
            return self.tile_map[name]
        raise Exception("({name}) not present in the tile_mapping".format(name=name))

    def translate(self, name) -> str:
        """
        translates a local tile name to its ID
        :param name:    canonical local tile name
        :return:
        """
        return self.get_tile(name)['panelId']

    def print_layout(self):
        """
        positional data is provided in increments of 50, and placements are allowed at an offset, thus we can display
        each tile as a collection of 4 characters in a square.

        Currently assumes ['panelLayout']['globalOrientation']['value'] == 0
        :return:
        """
        grid = [[" " for x in range(len(self._raw_positional_data)*2)] for x in range(len(self._raw_positional_data)*2)]
        for name, tile in self.tile_map.items():
            pos = [tile['y']//50, tile['x']//50]
            grid[pos[0]][pos[1]] = name
            grid[pos[0]+1][pos[1]] = name
            grid[pos[0]][pos[1]+1] = name
            grid[pos[0]+1][pos[1]+1] = name

        grid.reverse()
        for row in grid:
            # row.reverse()
            if len(set(row)) > 1:  # skip blank lines
                print(*row)


if __name__ == "__main__":
    nc = NanoLeafClient(auth_path='/Users/cearman/repos/nanoleaf-canvas/.auth',
                        address='10.0.0.129')
    ld = Layout(nc)
    ld.print_layout()
    print(ld.translate('1'))
