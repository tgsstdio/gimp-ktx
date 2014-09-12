#!/usr/bin/python3

# UInt32 glType = 0
# UInt32 glTypeSize = 1
# UInt32 glFormat = 0
# UInt32 glInternalFormat = GL_ETC1_RGB8_OES
# UInt32 glBaseInternalFormat = GL_RGB
# UInt32 pixelWidth = 32
# UInt32 pixelHeight = 32
# UInt32 pixelDepth = 0
# UInt32 numberOfArrayElements = 0
# UInt32 numberOfFaces = 1
# UInt32 numberOfMipmapLevels = 1
# UInt32 bytesOfKeyValueData = 16

# METADATA
# UInt32 keyAndValueByteSize = 10
# UTF8 key:   'api\0'
# UTF8 v: 'gles2\0'
# Byte[2] valuePadding (2 bytes)
# TEXTURE DATA
# UInt32 imageSize = 512 bytes
# Byte[512] ETC compressed texture data

import struct

def load(filename):
	right_file_id = bytes([0xAB, 0x4B, 0x54, 0x58, 0x20, 0x31, 0x31, 0xBB, 0x0D, 0x0A, 0x1A, 0x0A])
	big_endians = bytes([0x04,0x03,0x02,0x01])
	little_endians = bytes([0x01,0x02,0x03,0x04])
	c_end = '>' 
	info = {'glType' : 0,
				'glTypeSize' : 1,
				'glFormat' : 2,
				'glInternalFormat' : 3,
				'glBaseInternalFormat' : 4,
				'pixelWidth' : 5,
				'pixelHeight' : 6,
				'pixelDepth' : 7,
				'numberOfArrayElements' : 8,
				'numberOfFaces' : 9,
				'numberOfMipmapLevels' : 10,
				'bytesOfKeyValueData' : 11}
	with open(filename, 'rb') as f:
		file_id = f.read(12)
		if file_id == right_file_id:
			print('Is\'s KTX')
		else : print('It\'s don\'t KTX')
		endians = f.read(4)
		if endians == little_endians:
			c_end = '<'
		else :
			c_end = '>'
		info_b = f.read(len(info)*4)
		info_f = '';
		for i in range(len(info)):
			info_f += 'I'
		info_plain = struct.unpack(c_end + info_f,info_b)
		for key,value in info.items():
			print(key + ':' + str(info_plain[value]))
			info[key] = info_plain[value]
		# TODO Add support of metadata
		#m_byte_size = struct.unpack(c_end+'I',f.read(4))
		#metadata_p = f.read(m_byte_size)
		#valuePadding = struct.unpack('',f.read(2))
		f.read(info['bytesOfKeyValueData'])
		print(f.tell())
		imageSize = struct.unpack(c_end + 'I',f.read(4))
		print('imageSize:' + str(imageSize[0]))
		imageData = f.read(imageSize[0])


# TEST rgba
load('../images/rgba.ktx')
