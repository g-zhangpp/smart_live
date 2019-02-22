import base64
from aip import AipFace

class Image:
    """这个模块主要用于调用摄像头以及生成图片"""
    def __init__(self):
        self.APP_ID = "14445494"
        self.API_KEY = "4fTrUzMZtsqqo1veoDXjSaWC"
        self.SECRECT_KEY = "i64MWSrUUu6V87h4FW7Z863pkIAiQRib"

    def token_access(self):
        """进行百度云用户身份验证"""
        client = AipFace(self.APP_ID, self.API_KEY, self.SECRECT_KEY)
        return client

    def face_detection(self, img):
        """颜值检测"""
        client = self.token_access()
        f = open(img, "rb")
        image = base64.b64encode(f.read())
        image = str(image, "utf-8")
        imageType = "BASE64"
        options = {}
        options["face_field"] = "age,faceshape,beauty,gender"
        res = client.detect(image, imageType, options)
        if res["result"] != None:
            sex = res["result"]["face_list"][0]["gender"]['type']
            age = res["result"]["face_list"][0]["age"]
            face_shape = res["result"]["face_list"][0]["face_shape"]['type']
            beauty = res["result"]["face_list"][0]["beauty"]
            return age, '{:.2f}'.format(beauty), sex, face_shape
        else:
            print("没有检测到人脸")
            return
