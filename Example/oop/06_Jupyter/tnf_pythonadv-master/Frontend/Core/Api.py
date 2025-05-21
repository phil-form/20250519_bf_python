import json
from urllib import request, parse

class API(object):
    def __init__(self, url=None) -> None:
        super().__init__()
        self.__authToken = ""
        self.__baseUrl = url
        self.__data = ""

    def sendRequest(self, url=None, data=None, method='GET'):
        try:
            if self.__baseUrl is not None and url is not None:
                if data is not None:
                    data = parse.urlencode(data).encode()
                # __baseUrl = http://localhost:8000/api/
                # url = composer/
                req = request.Request(url=self.__baseUrl + url, data=data, method=method)

                if self.__authToken != "":
                    req.add_header('Authorization', 'Bearer %s' % self.__authToken)

                response = request.urlopen(req)
                encoding = response.headers.get_content_charset()

                if encoding is None:
                    encoding = "utf-8"

                self.__data = json.loads(response.read().decode(encoding))
        except:
            print("Error while executing request!")

        return self.__data

    def login(self, data):
        try:
            tokens = self.sendRequest('auth/token/', data, method='POST')
            print(tokens)
            self.__authToken = tokens['access']
            return True
        except:
            print("wrong username and/or password!")
            return False

WebApi = API("http://localhost:8000/api/")