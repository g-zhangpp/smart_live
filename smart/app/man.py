from aip import AipImageClassify

class Human:
    def __init__(self):
        """ 你的 APPID AK SK """
        self.APP_ID = '14896573'
        self.API_KEY = 'XkMmL6tPvtzMcudAgTy9eYgz'
        self.SECRET_KEY = 'gRRw18LdXn6jX8AbrUYHRGzfqdGImtWg '

    """ 读取图片 """
    def get_file_content(self, filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()
    def msg(self, filePath):
        image = self.get_file_content(filePath)
        client = AipImageClassify(self.APP_ID, self.API_KEY, self.SECRET_KEY)
        """ 如果有可选参数 """
        options = {}
        options["baike_num"] = 1
        """ 带参数调用菜品识别 """
        res = client.advancedGeneral(image, options)
        if res['result'][0]['baike_info']:
            return res['result'][0]['baike_info']['description']
        else:
            return  '我的能力也是有限的，没有识别到对应的公众人物！'