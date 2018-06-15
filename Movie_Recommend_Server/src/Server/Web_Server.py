import socket
from src import Recommend

HOST = 'localhost'
PORT = 5001
ADDR = (HOST,PORT)
BUFSIZE = 4096
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    #TCP

serv.bind(ADDR)
serv.listen(5)
client=None

while True:
    if client is None:
        print('waiting for conn...')
        client, addr = serv.accept()
        print('client connected ... ', addr)
    else:
        print('waiting for response...')
        data=client.recv(65535)
        data_str=str(data,"UTF-8")
        print('받은 데이터: ',data_str)
        if data_str=='exit()':
            break
        recomendMovie= Recommend.getRecommendMovie(data_str)
        recomendMovie_str=""
        for ele in recomendMovie:
            recomendMovie_str+=(str(ele)+'/')
        print(recomendMovie_str)
        print(type(recomendMovie_str))
        client.send((recomendMovie_str+"\n").encode('UTF-8'))
        client.close()
        client = None

if client is not None:
    client.close()
serv.close()