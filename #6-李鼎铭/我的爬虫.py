import requests,json,time


def get(pagenum):
    url='https://club.jd.com/comment/productPageComments.action?productId=100019125569&score=0&sortType=5'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54'}
    param={
        "page":pagenum,
        "pageSize":"10",
        "isShadowSku":"0",
        "fold":"1"
    }
    content = requests.get(url=url,headers=headers,params=param)
    response = content.text
    a=json.loads(response)
    b=a['comments']
    return b
if __name__=="__main__":
    for i in range(0,51):
        b=get(i)
        for j in b:
            nickname=j['nickname']
            creationTime=j['creationTime']
            content=j['content']
            print(nickname,creationTime,content,)
            print("=================================================")
            fp = open("E:\Pythoncharm\爬虫jiaotang\success.txt", "a", encoding='utf-8')
            fp.write(str(i)+"   ")
            fp.write(nickname+"\t")
            fp.write(creationTime+"\n")
            fp.write(content+"\n")
            time.sleep(0.4)
            fp.close()








