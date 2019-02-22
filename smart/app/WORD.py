from aip import AipOcr
def img_word(filePath):
    """ 你的 APPID AK SK """
    APP_ID = '14448660'
    API_KEY = '1Hmzv7SCVG08USGIF9DU6KYz'
    SECRET_KEY = 'FzYVl3HBvssvuimequVEfN0OflAlluaE'

    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    """ 读取图片 """
    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    image = get_file_content(filePath)
    """ 调用通用文字识别, 图片参数为本地图片 """
    reses = client.basicGeneral(image)
    message = ''
    for res in reses['words_result']:
        message += res['words']
    return message
