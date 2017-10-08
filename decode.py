
IV = '9F0B13944841A832B2421B9EAF6D9836'       #密文头部自带的初始IV
IV2 = '813EC9D944A5C8347A7CA69AA34D8DC0'	  #第一组密文作为第二组的IV	
InVector = [198, 106, 106, 181, 104, 24, 199, 71, 146, 37, 126, 234, 143, 12, 246, 22]
#第一组明文AES加密后的值（与IV异或之前）
InVector2 = [192, 16, 233, 228, 109, 174, 195, 63, 113, 119, 173, 145, 168, 70, 134, 203]
#第二组明文AES加密后的值（与IV2异或之前）
iv =[]
iv2 =[]
plain =''

for i in range(0,32,2):
    iv.append(IV[i:i+2])
for i in range(0,16):
    plain = plain + chr(InVector[i]^int(iv[i],16)) 		#iv 与 InVector 异或即得明文

for i in range(0,32,2):
    iv2.append(IV2[i:i+2])
for i in range(0,16):
    plain = plain + chr(InVector2[i]^int(iv2[i],16))

print plain

