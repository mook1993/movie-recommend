# 안드로이드 앱 서버
# : 앱에서 사용자 값 전달받고 그 결과값(추천 영화)을 돌려준다

import socket
from src import Recommend

HOST = '192.168.0.12'
PORT = 5001
ADDR = (HOST,PORT)
BUFSIZE = 4096
serv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP

serv.bind(ADDR)
client=None

while True:
    if client is None:
        print('waiting for conn...')
        data, addr = serv.recvfrom(65535)
        print('server received %r from %r' % (data, addr))
        data_str=str(data,"UTF-8")
        print('받은 데이터: ',data_str)

        recomendMovie= Recommend.getRecommendMovie(data_str)
        recomendMovie_str=""
        for ele in recomendMovie:
            recomendMovie_str+=(str(ele)+'/')
        print(recomendMovie_str)
        serv.sendto((recomendMovie_str+"\n").encode('UTF-8'),addr)

if client is not None:
    client.close()
serv.close()