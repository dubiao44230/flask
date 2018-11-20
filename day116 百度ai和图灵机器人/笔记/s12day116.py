# # 2018年10月16日
# # 上节回顾：
# # 	websocket；握手
# # 		浏览器 - 链接 - 服务器
# # 		浏览器 - 发送 - 字符串(求情头) - Sec-Websocket-Key - 服务器
# #
# # 		服务器 - 获取Sec-Websocket-Key的值+magic_string - sha1 - base64 - 拼接一个响应头 - Sec-WebSocket-Accept值就是
# # 		服务器 - 拼接好的响应头 - 浏览器
# # 		浏览器 - Sec-WebSocket-Accept 解密得到 Sec-Websocket-Key - 握手成功与否
# #
# #
# # 今日内容：
# # 	websocket 加解密
# # 		解密：
# # 			b_str = b'\x81\xfe\x01G\xa0`~dE\xe5\xf6\x81\x18\xfd\x9b\xec;\x84\xc6\xfeF\xfc\xd4\x81-\xea\x96\xe4,\x84\xc6\xc9I\xe1\xed\x81\x14\xc9\x98\xca"\x8f\xc2\xe8D\xdb\xf4\x81\x04\xc9\x9a\xdc+\x84\xc6\xedE\xe8\xf8\x8b\x1c\xec\x99\xff*\x85\xc9\xfaG\xf6\xcc\x81\x1c\xea\x91\xd8,\x86\xd3\xc0H\xcf\xe4\x81-\xd1\x98\xe4\x05\x85\xd3\xfcD\xda\xdf\x80\x19\xeb\x99\xc3+\x84\xc7\xfbC\xe0\xfc\x83$\xd6\x9a\xda-\x85\xf3\xcfD\xd9\xf5\x8c\'\xc3\x9a\xdc-\x86\xf9\xecD\xda\xf0\x81&\xe5\x91\xd8,\x85\xc1\xc4E\xdf\xe9\x80\x19\xeb\x9b\xc7\x0b\x85\xc1\xfcH\xda\xd5\x80\x1a\xee\x9b\xc06\x88\xfe\xe1O\xdc\xf2\x83;\xf6\x96\xdb\x1d\x85\xfb\xecE\xd8\xe3\x80\x19\xeb\x98\xca*\x89\xff\xe3O\xdc\xf2\x82\x0c\xd2\x98\xee\x05\x84\xc7\xefD\xda\xf0\x8d9\xfb\x9a\xdc+\x84\xc7\xfbC\xe0\xfc\x8c\x0f\xfa\x9b\xca<\x85\xc2\xe4E\xdc\xde\x81<\xc3\x9b\xf4\x0c\x8f\xc2\xe8D\xdb\xdb\x81%\xe9\x9b\xe1(\x85\xc6\xf9I\xe1\xe9\x81\x1e\xd7\x91\xd8,\x86\xff\xc6E\xdc\xe6\x81\x1f\xf7\x9b\xc7\x0b\x84\xc7\xefF\xd0\xea\x8b\x1c\xec\x9a\xdc-\x85\xd0\xf8E\xc6\xfa\x8c\'\xca\x96\xeb\x12\x88\xe8\xe0O\xdc\xf2\x81\x1c\xf5\x9b\xf2\x1b\x85\xda\xd5D\xd9\xf7\x8b\x1c\xec\x9a\xdf\x05\x85\xdf\xfaE\xdf\xde\x8c\x10\xef\x9a\xdd+\x88\xc9\xcbD\xd9\xe1'
# c_str = b'\x81\xfe\x02d\xbe@<\x07'
# s1 = c_str[0]
# print(bin(s1))
# # 			# 123 \x81
# # 			#[\x81,\x83,\xc8,\xbd,\xa6,\x9c,\xf9,\x8f,\x95]
# # 			# 1000011
# # 			# 0111111
# # 			# 0000011
# # 			#--------
# # 			# 1111110
# # 			# 0111111 127
# # 			# 0111110 126
# #
# #
# # 			data_lenth = b_str[1] & 127
# # 			# print(data_lenth)
# #
# # 			# data_lenth == 127 之后的多少位为数据长度3-10字节代表数据长度 11-14为mask_key
# # 			if data_lenth == 127:
# # 				extend_payload_len = b_str[2:10]
# # 				mask = b_str[10:14]
# # 				data = b_str[14:]
# #
# # 			# data_lenth == 126 之后的多少位为数据长度3-4字节代表数据长度 65535 5-8为mask_key
# # 			if data_lenth == 126:
# # 				extend_payload_len = b_str[2:4]
# # 				mask = b_str[4:8]
# # 				data = b_str[8:]
# #
# # 			# data_lenth <= 125 当前的 data_lenth 就是数据的长度 125      3-6为mask_key
# # 			if data_lenth <= 125:
# # 				extend_payload_len = b_str[1]
# # 				mask = b_str[2:6]
# # 				data = b_str[6:]
# #
# #
# # 			str_byte = bytearray()
# #
# # 			for i in range(len(data)):
# # 				byte = data[i] ^ mask[i % 4]  # 0123
# # 				str_byte.append(byte)
# #
# # 			print(str_byte.decode("utf8"))#
# #
# # 		加密：
# # 			import struct
# # 			msg_bytes = "先帝创业未半而中道崩殂，今天下三分，益州疲弊，此诚危急存亡之秋也。然侍卫之臣不懈于内，忠志之士忘身于外者，盖追先帝之殊遇，欲报之于陛下也。诚宜开张圣听，以光先帝遗德，恢弘志士之气，不宜妄自菲薄，引喻失义，以塞忠谏之路也".encode("utf8")
# # 			token = b"\x81"
# # 			length = len(msg_bytes)
# #
# # 			if length < 126:
# # 				token += struct.pack("B", length)
# # 			elif length == 126:
# # 				token += struct.pack("!BH", 126, length)
# # 			else:
# # 				token += struct.pack("!BQ", 127, length)
# #
# # 			msg = token + msg_bytes
# #
# # 			print(msg)
# #
# # 	1.语音合成
# # 		"""
# # 		给他一个字符串
# # 		输出音频(二进制流)
# # 		"""
# #
# # 		from aip import AipSpeech
# #
# # 		APP_ID = '14446007'
# # 		API_KEY = 'QrQWLLg5a8qld7Qty7avqCGC'
# # 		SECRET_KEY = 'O5mE31LSl17hm8NRYyf9PwlE5Byqm0nr'
# #
# # 		client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
# #
# # 		res = client.synthesis("日照香炉生紫烟，遥看瀑布挂前川，清明上河图，完全搞不懂，平方差公式",options={
# # 			"vol":8,
# # 			"pit":8,
# # 			"spd":5,
# # 			"per":4
# # 		})
# # 		print(res)
# # 		with open("audio.mp3","wb") as f:
# # 			f.write(res)
# #
# # 	2.语音识别
# # 		from aip import AipSpeech
# # 		import os
# #
# # 		APP_ID = '14446007'
# # 		API_KEY = 'QrQWLLg5a8qld7Qty7avqCGC'
# # 		SECRET_KEY = 'O5mE31LSl17hm8NRYyf9PwlE5Byqm0nr'
# #
# # 		client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
# #
# # 		def get_file_content(filePath):
# # 			cmd_str = f"ffmpeg -y -i {filePath} -acodec pcm_s16le -f s16le -ac 1 -ar 16000 {filePath}.pcm"
# # 			os.system(cmd_str)
# # 			with open(f"{filePath}.pcm", 'rb') as fp:
# # 				return fp.read()
# #
# # 		res = client.asr(speech=get_file_content("audio.mp3"),options={
# # 			"dev_pid":1536,
# # 		})
# #
# #
# #
# # 今日作业：
# # 	1.语音合成基于百度ai
# # 	2.语音识别基于百度ai
# # 	3.学说话 回答简单问题
# # 	4.websocket版本录音
# #
# # 今日内容汇个总：
# # 	1.百度ai
# # 	2.基于百度ai实现了语音合成
# # 	3.基于百度ai实现了语音识别
# # 		FFmpeg 转换PCM音频格式
# # 	4.基于百度ai NLP技术中的Simnet 实现 短文本相似度
# # 	5.简单问答 + Tuling机器人
# # 	6.web录音知道里面是干什么的，Audio标签 src音频地址 autoplay当src加载完成时自动播放 controls 显示或关闭播放器
# # 	7.基于websocket传输语音
# # 	8.return send_file(file_name)
# #
#
#
#
# hashstr = b'\x81\x83\xceH\xb6\x85\xffz\x85'
# # b'\x81    \x83    \xceH\xb6\x85\xffz\x85'
#
# # 将第二个字节也就是 \x83 第9-16位 进行与127进行位运算
# payload = hashstr[1] & 127
# print(payload)
# if payload == 127:
#      extend_payload_len = hashstr[2:10]
#      mask = hashstr[10:14]
#      decoded = hashstr[14:]
#  # 当位运算结果等于127时,则第3-10个字节为数据长度
#  # 第11-14字节为mask 解密所需字符串
#  # 则数据为第15字节至结尾
#
# if payload == 126:
#      extend_payload_len = hashstr[2:4]
#      mask = hashstr[4:8]
#      decoded = hashstr[8:]
#  # 当位运算结果等于126时,则第3-4个字节为数据长度
#  # 第5-8字节为mask 解密所需字符串
#  # 则数据为第9字节至结尾
#
#
# if payload <= 125:
#      extend_payload_len = None
#      mask = hashstr[2:6]
#      decoded = hashstr[6:]
#
#  # 当位运算结果小于等于125时,则这个数字就是数据的长度
#  # 第3-6字节为mask 解密所需字符串
#  # 则数据为第7字节至结尾
#
#  str_byte = bytearray()
#
# for i in range(len(decoded)):
#      byte = decoded[i] ^ mask[i % 4]
#      str_byte.append(byte)
#
# print(str_byte.decode("utf8"))