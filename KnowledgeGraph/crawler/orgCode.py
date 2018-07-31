import random

def OrgCode():
     factorList = [3, 7, 9, 10, 5, 8, 4, 2]#加权因子列表
     OrgCode = []#用于存放生成的组织机构代码
     sum = 0
     for i in range(8):#随机取前8位数字
         OrgCode.append(random.randint(0, 35))#随机取1位数字
         sum = sum +OrgCode[i]*factorList[i]#用orgCode*加权因子
         # print(dd)
     for i in range(len(OrgCode)):
         if OrgCode[i]>=0 and OrgCode[i]<=9:
             OrgCode[i] = str(OrgCode[i])#将orgCode（int）变成str
         else:
             OrgCode[i]=chr(OrgCode[i]+55)
     C9 = 11-sum % 11 #C9代表校验码。用已经生成的前8位加权后与11取余，然后用11减
     # print(C9)
     if C9 == 10:#当C9的值为10时，校验码应用大写的拉丁字母X表示；当C9的值为11时校验码用0表示;除此之外就是C9本身
          C9 = 'X'
     else:
          if C9 == 11:
               C9 = '0'
          else:
               C9 = str(C9)
     OrgCode.append('-' + C9)
     return "".join(OrgCode)#拼接最终生成的组织代码

for i in range(2):
     print(OrgCode())