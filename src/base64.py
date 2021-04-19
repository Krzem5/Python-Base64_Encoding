__all__=["encode","decode","BASE64_ALPHABET"]



BASE64_ALPHABET=b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"



def encode(dt):
	if (len(dt)==0):
		return b""
	o=[]
	i=0
	while (i<len(dt)-2):
		o.append(BASE64_ALPHABET[dt[i]>>2])
		o.append(BASE64_ALPHABET[((dt[i]<<4)&0x3f)|(dt[i+1]>>4)])
		o.append(BASE64_ALPHABET[((dt[i+1]<<2)&0x3f)|(dt[i+2]>>6)])
		o.append(BASE64_ALPHABET[dt[i+2]&0x3f])
		i+=3
	if (i==len(dt)-2):
		o.append(BASE64_ALPHABET[dt[i]>>2])
		o.append(BASE64_ALPHABET[((dt[i]<<4)&0x3f)|(dt[i+1]>>4)])
		o.append(BASE64_ALPHABET[(dt[i+1]<<2)&0x3f])
		o.append(0x3d)
	elif (i==len(dt)-1):
		o.append(BASE64_ALPHABET[dt[i]>>2])
		o.append(BASE64_ALPHABET[(dt[i]<<4)&0x3f])
		o.append(0x3d)
		o.append(0x3d)
	return bytes(o)



def decode(dt):
	dt=dt.strip(b"=")
	if (len(dt)==0):
		return b""
	o=[]
	i=0
	while (i<(len(dt)>>2)<<2):
		idx1=BASE64_ALPHABET.index(dt[i+1])
		idx2=BASE64_ALPHABET.index(dt[i+2])
		o.append((BASE64_ALPHABET.index(dt[i])<<2)|(idx1>>4))
		o.append(((idx1&0xf)<<4)|(idx2>>2))
		o.append(((idx2&0x3)<<6)|(BASE64_ALPHABET.index(dt[i+3])))
		i+=4
	if ((len(dt)&3)==3):
		idx1=BASE64_ALPHABET.index(dt[i+1])
		o.append((BASE64_ALPHABET.index(dt[i])<<2)|(idx1>>4))
		o.append(((idx1&0xf)<<4)|(BASE64_ALPHABET.index(dt[i+2])>>2))
	elif ((len(dt)&3)==2):
		idx1=BASE64_ALPHABET.index(dt[i+1])
		o.append((BASE64_ALPHABET.index(dt[i])<<2)|(BASE64_ALPHABET.index(dt[i+1])>>4))
	return bytes(o)
