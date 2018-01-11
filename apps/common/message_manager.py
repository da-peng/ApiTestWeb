#encoding=utf-8
import random

# import requests
import time
import hashlib


class Message(object):


    def __init__(self,http_type,method,headers,cookies,base_url,path,certs=None,verify=None):
        self.http_type = http_type.lower()
        self.method = method.lower()
        self.headers = headers
        self.cookies = cookies
        self.base_url = base_url
        self.path = path
        self.certs = certs
        self.verify = verify

    def send_message(self,body_params):
        if self.method == 'get':
            self.__get(body_params)
        elif self.method == 'post':
            self.__post(body_params)

    def __md5(self,source):

        md5 = hashlib.md5()
        md5.update(source.encode(encoding="utf-8"))

        return md5.hexdigest()

    def __get_signature_time_identity(self,secret):

        time_stamp = time.time()
        time_format = str(int(time_stamp*1000))
        random_num = str(random.randint(100,999))

        identity = time_format + random_num

        signature = self.__md5(identity + ':' + secret + ':' +time_format)

        return signature,time_format,identity


    def __generation_body(self):

        body_params = {}

        return body_params



    def __get(self,params_dict):

        url = self.base_url + self.path

        if self.http_type == 'http':
            pass
            # response = requests.get(url,params=params_dict,
            #                         headers=self.headers,
            #                         cookies=self.cookies)

        elif self.http_type == 'https':
            pass
            # response = requests.get(url,params=params_dict,
            #                         headers=self.headers,
            #                         cookies=self.cookies,
            #                         verify=self.verify,
            #                         cert=self.certs)
        else:
            raise Exception('the parameters http_type is wrong ！,current value is: %s'%(self.http_type))

        # return response


    def __post(self,params_dict):

        url = self.base_url + self.path

        if self.http_type == 'http':
            pass
            # response = requests.post(url, params=params_dict,
            #                          headers=self.headers,
            #                          cookies=self.cookies)

        elif self.http_type == 'https':
            pass
            # response = requests.post(url, params=params_dict,
            #                          headers=self.headers,
            #                          cookies=self.cookies,
            #                          verify=self.verify,
            #                          cert=self.certs)
        else:
            raise Exception('the parameters http_type is wrong ！,current value is: %s'%(self.http_type))

        # return response


class  OperationFile(object):


    def __init__(self):
        pass


if __name__ =='__main__':
    pass