import requests


class HttpClient(object):
    def __init__(self, address, port, scheme='http'):
        self.address = address
        self.port = port
        self.scheme = scheme

    def get(self, uri, params=None, **kwargs) -> requests.Response:
        """
        Base level GET request for the HttpClient
        :param uri:         api path string
        :param params:      forwards to requests.get
        :param kwargs:      forwards to requests.get
        :return:
        """
        url = "{scheme}://{address}:{port}{uri}".format(scheme=self.scheme,
                                                        address=self.address,
                                                        port=self.port,
                                                        uri=uri)
        return requests.get(url,
                            params=params,
                            **kwargs)

    def put(self, uri: str, data: str = None, **kwargs) -> requests.Response:
        """
        Base level PUT request for the HttpClient
        :param uri:         api path string
        :param data:        forwards to requests.put
        :param kwargs:      forwards to requests.put
        :return:
        """
        url = "{scheme}://{address}:{port}{uri}".format(scheme=self.scheme,
                                                        address=self.address,
                                                        port=self.port,
                                                        uri=uri)
        return requests.put(url,
                            data=data,
                            **kwargs)

    def post(self, uri: str, data: str = None, **kwargs) -> requests.Response:
        """
        Base level POST request for the HttpClient
        :param uri:         api path string
        :param data:        forwards to requests.put
        :param kwargs:      forwards to requests.put
        :return:
        """
        url = "{scheme}://{address}:{port}{uri}".format(scheme=self.scheme,
                                                        address=self.address,
                                                        port=self.port,
                                                        uri=uri)
        return requests.post(url,
                             data=data,
                             **kwargs)
