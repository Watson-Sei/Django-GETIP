import socket
# ホスト名を取得、表示
host = socket.gethostname()
print(host)

# ipアドレスを取得、表示
ip = socket.gethostbyname(host)
print(ip) # 192.168.OOO.OOO
