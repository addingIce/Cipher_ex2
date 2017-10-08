from oracle import *

data = '813EC9D944A5C8347A7CA69AA34D8DC0'       #第一组密文
ctext1 = []
for i in range(0,16):
    ctext1.append(0)                            #假设IV为16字节的0

ctext2 = [(int(data[i:i+2],16)) for i in range(0, len(data), 2)]

Oracle_Connect()
q = 0
InVector = []                                   #InVector为明文经过AES加密后的值（与IV异或之前），待破解
for k in range(0,16):
    for p in range(q,0,-1):
        ctext1[16-p] = (q+1)^InVector[q-p]      #，每一轮得到IV的一位，之后需要更新猜测的IV
    for i in range(0,256):
        ctext1[15-q] = in                       #遍历0~255直到padding正确
        ctext = ctext1+ctext2
        rc = Oracle_Send(ctext, 2)

        if rc == 1:
            InVector = [(i^(k+1))] + InVector   #每一轮得到InVector的一位，从最后一位开始往前
#            print InVector
            q = q+1
            break

Oracle_Disconnect()

print InVector                                   #得到这一分组的InVector
