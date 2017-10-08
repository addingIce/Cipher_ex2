  题目给出了利用PKCS#7 padding经过AES-CBC加密的一段密文（ challenge-ciphertext.txt），并给出能返回攻击者提交的密文是否符合填充规则
的服务器，提交的密文符合填充规则返回1，否则返回0。攻击者可以利用CBC加密模式的特性和PKCS#7的加密特性，通过Padding Oracle Attack来破解
密文。而在给出的密文中，前16字节是加密使用的初始IV。

Padding Oracle Attack的具体攻击原理见以下博客：
 http://www.cnblogs.com/LittleHann/p/3391393.html
（注意此博客中作者在讲到攻击者更新IV时有一处小错误）

本次实验利用了Padding Oracle Attack这一破解方法，这一方法是针对CBC模式的加密的，能够利用此方法的条件是：
1、攻击者能够获得密文（Ciphertext），以及附带在密文前面的IV（初始化向量）
2. 攻击者能够触发密文的解密过程，且能够知道密文的解密结果（解密是否正确，即padding是否正确）。
3. 需要注意的地方是，每一轮获得IV的一位后，需要更新IV的该位，之后的尝试中，已知的部分不变。

oracle.py 和 sample.py 用于向服务器提交密文并获得解密结果（padding是否正确）
