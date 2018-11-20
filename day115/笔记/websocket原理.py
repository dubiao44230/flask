import socket, base64, hashlib

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('127.0.0.1', 9527))
sock.listen(5)
# 获取客户端socket对象
conn, address = sock.accept()
# 获取客户端的【握手】信息
data = conn.recv(1024)
print(data)


def get_headers(data):
    header_dict = {}
    header_str = data.decode("utf8")
    for i in header_str.split("\r\n"):
        if str(i).startswith("Sec-WebSocket-Key"):
            header_dict["Sec-WebSocket-Key"] = i.split(":")[1].strip()

    return header_dict

ws_key = get_headers(data).get("Sec-WebSocket-Key")

# # magic string为：258EAFA5-E914-47DA-95CA-C5AB0DC85B11
magic_string = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
socket_str = ws_key + magic_string
socket_str_sha1 = hashlib.sha1(socket_str.encode("utf8")).digest()
socket_str_base64 = base64.b64encode(socket_str_sha1)

response_tpl = "HTTP/1.1 101 Switching Protocols\r\n" \
               "Upgrade:websocket\r\n" \
               "Connection: Upgrade\r\n" \
               "Sec-WebSocket-Accept: %s\r\n" \
               "WebSocket-Location: ws://127.0.0.1:9527\r\n\r\n" %(socket_str_base64.decode("utf8"))

conn.send(response_tpl.encode("utf8"))
while 1:
    msg = conn.recv(8096)
    print(msg)

"""
b'GET / HTTP/1.1\r\n
Host: 127.0.0.1:9527\r\n
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0\r\n
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2\r\n
Accept-Encoding: gzip, deflate\r\n
Sec-WebSocket-Version: 13\r\n
Origin: http://localhost:63342\r\n
Sec-WebSocket-Extensions: permessage-deflate\r\n
Sec-WebSocket-Key: x/BjPHeWzOqqLxVuZq/bfw==\r\n
Cookie: session=fe2f4896-0309-4801-b8cd-9a719b26fb8d\r\n
Connection: keep-alive, Upgrade\r\n
Pragma: no-cache\r\n
Cache-Control: no-cache\r\n
Upgrade: websocket\r\n\r\n'
"""

# # magic string为：258EAFA5-E914-47DA-95CA-C5AB0DC85B11
# magic_string = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
#
#
# def get_headers(data):
#     header_dict = {}
#     header_str = data.decode("utf8")
#     for i in header_str.split("\r\n"):
#         if str(i).startswith("Sec-WebSocket-Key"):
#             header_dict["Sec-WebSocket-Key"] = i.split(":")[1].strip()
#
#     return header_dict
#
#
# def get_header(data):
#     """
#      将请求头格式化成字典
#      :param data:
#      :return:
#      """
#     header_dict = {}
#     data = str(data, encoding='utf-8')
#
#     header, body = data.split('\r\n\r\n', 1)
#     header_list = header.split('\r\n')
#     for i in range(0, len(header_list)):
#         if i == 0:
#             if len(header_list[i].split(' ')) == 3:
#                 header_dict['method'], header_dict['url'], header_dict['protocol'] = header_list[i].split(' ')
#         else:
#             k, v = header_list[i].split(':', 1)
#             header_dict[k] = v.strip()
#     return header_dict
#
#
# headers = get_headers(data)  # 提取请求头信息
# # 对请求头中的sec-websocket-key进行加密
# response_tpl = "HTTP/1.1 101 Switching Protocols\r\n" \
#                "Upgrade:websocket\r\n" \
#                "Connection: Upgrade\r\n" \
#                "Sec-WebSocket-Accept: %s\r\n" \
#                "WebSocket-Location: ws://127.0.0.1:9527\r\n\r\n"

# value = headers['Sec-WebSocket-Key'] + magic_string
# print(value)
# ac = base64.b64encode(hashlib.sha1(value.encode('utf-8')).digest())
# response_str = response_tpl % (ac.decode('utf-8'))
# # 响应【握手】信息
# conn.send(response_str.encode("utf8"))
#
# while True:
#     msg = conn.recv(8096)
#     print(msg)
