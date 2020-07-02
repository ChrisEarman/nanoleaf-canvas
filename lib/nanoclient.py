import json
import requests

from lib.httpclient import HttpClient


class NanoLeafClient(HttpClient):
    def __init__(self, auth_path, address, port=16021, scheme='http'):
        super(NanoLeafClient, self).__init__(address, port, scheme=scheme)
        with open(auth_path, 'r') as f:
            self.auth = json.load(f)['auth_token']

    def _v1_get(self, uri: str, params=None, **kwargs) -> requests.Response:
        """
        Wrapper for the V1 GET requests against the NanoLeafCanvas
        :param uri:             extension string for the v1 apis
        :param params:          forwarded to HttpClient.get
        :param kwargs:          forwarded to HttpClient.get
        :return:                request.Response Object
        """
        return self.get("/api/v1/{auth}{uri}".format(auth=self.auth,
                                                     uri=uri),
                        params=params,
                        **kwargs)

    def _v1_put(self, uri: str, data: str = None, **kwargs) -> requests.Response:
        """
        Wrapper for the V1 PUT requests against the NanoLeafCanvas
        :param uri:             extension string for the v1 apis
        :param data:            forwarded to HttpClient.put
        :param kwargs:          forwarded to HttpClient.put
        :return:                request.Response Object
        """
        return self.put("/api/v1/{auth}{uri}".format(auth=self.auth,
                                                     uri=uri),
                        data=data,
                        **kwargs)

    def _v1_post(self, uri: str, data: str = None, **kwargs) -> requests.Response:
        """
        Wrapper for the V1 POST requests against the NanoLeafCanvas
        :param uri:             extension string for the v1 apis
        :param data:            forwarded to HttpClient.post
        :param kwargs:          forwarded to HttpClient.post
        :return:                request.Response Object
        """
        return self.post("/api/v1/{auth}{uri}".format(auth=self.auth,
                                                     uri=uri),
                         data=data,
                         **kwargs)

    def get_info(self) -> dict:
        """
        Get the info json blob for the NanoLeaf
        :return:        json blob
        """
        return self._v1_get('/').json()

    def get_state(self) -> dict:
        """
        Get the on/off state of the NanoLeaf
        :return:        json blob -> { "value": true }
        """
        return self._v1_get('/state/on').json()

    def get_brightness(self) -> dict:
        """
        Get the brightness state of the NanoLeaf
        :return:            json blob -> { "value": 100, "max": 100, "min": 0 }
        """
        return self._v1_get('/state/brightness').json()

    def get_hue(self) -> dict:
        """
        Get the hue state of the NanoLeaf
        :return:            json blob -> { "value": 0, "max": 360, "min": 0 }
        """
        return self._v1_get('/state/hue').json()

    def get_ct(self) -> dict:
        """
        Get the color temperature state of the NanoLeaf
        :return:            json blob -> { "value": 4000, "max": 6500, "min": 1200 }
        """
        return self._v1_get('/state/ct').json()

    def get_effect(self) -> str:
        """
        Get the current active effect
        :return:            str -> "Fireworks"
        """
        return self._v1_get('/effects/select').text

    def get_effects(self) -> [str]:
        """
        Get the registered list of effects
        :return:            [str] -> ["Color Burst", "Fireworks"]
        """
        return self._v1_get('/effects/effectsList').json()

    def _put_state(self, data: str = None, **kwargs) -> requests.Response:
        """
        Helper method for the various state altering put calls
        :param data:            data for state change
        :param kwargs:          forwarded to HttpClient.put
        :return:                requests.Response -> <Response [204]>
        """
        return self._v1_put('/state', data=data, **kwargs)

    def put_state(self, b: bool) -> requests.Response:
        """
        Change on/off state of lights
        :param b:           True to turn the lights on, False to turn them off
        :return:            requests.Response -> <Response [204]>
        """
        payload = {'on': {'value': b}}
        return self._put_state(data=json.dumps(payload))

    def put_brightness(self, value: int, duration: int = None) -> requests.Response:
        """
        Change the brightness
        :param value:           brightness level [0, 100]
        :param duration:        time in seconds over which to change the brightness
        :return:
        """
        payload = {'brightness': {'value': value}}
        if duration is not None:
            payload['brightness']['duration'] = duration
        return self._put_state(data=json.dumps(payload))

    def put_hue(self, value: int) -> requests.Response:
        """
        Change the hue
        :param value:           hue value [0, 360]
        :return:
        """
        payload = {'hue': {'value': value}}
        return self._put_state(data=json.dumps(payload))

    def put_ct(self, value: int) -> requests.Response:
        """
        Change the ct
        :param value:           hue value [1200, 6500]
        :return:
        """
        payload = {'ct': {'value': value}}
        return self._put_state(data=json.dumps(payload))

    def select_effect(self, effect_name: str) -> requests.Response:
        """
        Set an effect on the NanoLeaf
        :param effect_name:     string effect name
        :return:
        """
        payload = {'select': effect_name}
        return self._v1_put('/effects', data=json.dumps(payload))

    def delete_effect(self, effect_name: str) -> requests.Response:
        """
        delete an effect on the NanoLeaf
        :param effect_name:     string effect name
        :return:
        """
        payload = {'write': {'command': 'delete',
                             'animName': effect_name}}
        return self._v1_put('/effects', data=json.dumps(payload))

    def write_effect(self, effect_payload: dict) -> requests.Response:
        """
        Write an effect to the NanoLeaf
        :param effect_payload:      effect payload
        :return:
        """
        payload = {'write': effect_payload}
        return self._v1_put('/effects', data=json.dumps(payload))


if __name__ == '__main__':
    nc = NanoLeafClient(auth_path='/Users/cearman/repos/nanoleaf-canvas/.auth',
                        address='10.0.0.127')  # 02:55:DA:08:44:CC
    # print(json.dumps(nc.get_info(), indent=2))
    # from datetime import datetime
    # print(datetime.now().strftime("%H:%M:%S"))
    # state = nc.get_state()
    # print(json.dumps(state, indent=2))
    # print(datetime.now().strftime("%H:%M:%S"))
    # print(nc.put_state(not state['value']))
    # print(datetime.now().strftime("%H:%M:%S"))
    # print(json.dumps(nc.get_state(), indent=2))
    # print(json.dumps(nc.get_hue()))
    # from random import randint
    # hue = randint(0, 360)
    # sat = randint(0, 100)
    # ct = randint(1200, 6500)
    # print(nc._put_state(json.dumps({
    #     # "hue": {"value": hue},
    #     "sat": {"value": 100},
    #     "ct": {"value": ct}
    # })))
    # print(hue, sat, ct)
    # for i in range(0, 360, 10):
    #     print(nc._put_state(json.dumps({"hue": {"value": i}})))
    # for i in range(1200, 6500, 100):
    #     print(nc._put_state(json.dumps({"ct": {"value": i}})))
    print(nc.get_effects())
    # print(nc.delete_effect(''))
    print(nc.select_effect("Sea Flame"))
    # print(nc.select_effect("Sea Flame"))
    # nc.put_state(False)
