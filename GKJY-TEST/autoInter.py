#!/usr/bin/env python3

import requests


class lhl:
    
    def __init__(self):
        pass

    def respondGet(self, url, header={}, param={}):
        """
        请求时需要3个参数，完整url，请求header,请求参数
        函数返回一个字典{'body': , 'respondTime':, 'code':}
        """
        s = requests.session()
        res = s.get(url, headers=header, params=param)
        print(res.text,res.elapsed.total_seconds(),res.status_code)
        result = {'body': res.text, 'respondTime':res.elapsed.total_seconds(), 'code':res.status_code}
        return result
   
    def respondPost(self, url, header={}, data={}):
        """
        请求时需要3个参数，完整url，请求header,请求参数
        函数返回一个字典{'body': , 'respondTime':, 'code':}
        """
        s = requests.session()
        res = s.post(url, headers=header, data=data)
        print(res.text,res.elapsed.total_seconds(),res.status_code)
        result = {'body': res.text, 'respondTime':res.elapsed.total_seconds(), 'code':res.status_code}
        return result

if __name__ == "__main__":
    pass
