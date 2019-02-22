from aip import AipSpeech
import io, playsound, os
def robot(name):
    App_Id = '14412190'
    App_Key = 'qGSUsRICVlSE9T9lY51EYM8E'
    App_Secret = 'QQqTMLul0NuMgqr3uUV4t7H10d8gXxSO'
    client = AipSpeech(App_Id, App_Key, App_Secret)
    with open('static/media/story/' + name + '.txt', 'r') as f:
        text = f.read()
    result = client.synthesis(text, 'zh', 1, {
        'vol': 5,
    })
    with open('static/music.mp3', 'wb') as f:
        f.write(result)

    playsound.playsound('static/music.mp3')
    return text