# Alexander Diana
# 3/3/2014  LGPLv3+
from winreg import *
from itertools import *
B=print;Q=QueryInfoKey;r=range

def C(A,M):
	try:H=OpenKey(M,A)
	except FileNotFoundError:return
	for I in r(Q(H)[1]):B(EnumValue(H,I)[1])
	for I in r(Q(H)[0]):C(A+"\\"+EnumKey(H,I),M)
	H.Close()

H=[HKEY_LOCAL_MACHINE,HKEY_CURRENT_USER]
P="SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\"
E=["Run","RunOnce","RunOnceEx","RunServices","RunServicesOnce"]
for J,I in product(H,E):C(P+I,J)
