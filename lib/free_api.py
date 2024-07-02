import json
from json import JSONDecodeError

import requests
from requests import Response


class api_free:
    def get_url(self, url, **kwargs):
        add_url = self.joint_url(url=url, **kwargs)
        res = requests.get(url=add_url)
        res_json = self.convert_json(res=res)
        return res_json

    def joint_url(self, url, **kwargs):
        first = True
        for key, value in kwargs.items():
            if first:
                url += f"?{key}={value}"
                first = False
            else:
                url += f"&{key}={value}"
        return url

    def convert_json(self, res: Response):
        content = res.text.strip()
        content_json = json.loads(content)
        return content_json


api = api_free()

if __name__ == '__main__':
    res = api.get_url(url='https://cn.apihz.cn/api/xinwen/baidu.php', id='88888888', key='88888888')
    # response_text = res.text.replace('\n', '')
    response_text = res.text.strip()
    # try:
    res_json = json.loads(response_text)
    # except JSONDecodeError:
    #     erro_context = res.text[max(0,6176-5):6176+10]
    #     print('报错部分：',erro_context)
    print('这是接口响应码：', res_json['code'])
    print('这是接口msg信息：', res_json['msg'])
    print(res_json)
    print('data信息条数：', len(res_json['data']['content']))
