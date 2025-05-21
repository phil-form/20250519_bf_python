import json
import urllib.request
import urllib.parse

class Server(object):
    def __init__(self, url=None) -> None:
        super().__init__()
        self.__authToken = ""
        self.__refreshToken = ""
        self.__baseUrl = url
        self.data = ""
    
    # __baseUrl = "http://localhost:8000/api/"
    # url composer/1     
    def getData(self, url=None, data=None, method='GET'):
        try:
            if self.__baseUrl is not None and url is not None:
                if data is not None:
                    data = urllib.parse.urlencode(data).encode()
                print(data)
                request = urllib.request.Request(url=self.__baseUrl + url, data=data, method=method)
                if(self.__authToken != ""):
                    request.add_header('Authorization', 'Bearer %s' % self.__authToken)
                response = urllib.request.urlopen(request)
                encoding = response.headers.get_content_charset()
                if encoding is None:
                    encoding = 'utf-8'
                self.data = json.loads(response.read().decode(encoding))
        except:
            print("Error while executing request!")
            
        return self.data
    
    def login(self, url, data):
        try:
            tokens = self.getData(url, data, method='POST')
            self.__authToken = tokens['access']
            self.__refreshToken = tokens['refresh']
            return True
        except:
            print('Wrong username or password')
            return False
    
webApi = Server(url="http://localhost:8000/api/")