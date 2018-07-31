#process the data

def cleanTheData(sa):
    res=[]
    phone=""
    email=""
    if sa[len(sa)-1]=="$":
        for i in range(len(sa)):
            if i<=3:
                res.append(sa[i])
            elif i<len(sa)-1:
                phone=phone+sa[i]+","
            else:
                email=sa[len(sa)-1]
        phone=phone[:-1]
    elif '$' in sa:
        for i in range(len(sa)):
            if i<=3:
                res.append(sa[i])
            elif i==4:
                phone=sa[i]
            else:
                email=email+sa[i]+","
        email=email[:-1]
    else:
        flag=0
        for i in range(len(sa)):
            if i<=3:
                res.append(sa[i])
            elif flag==0:
                phone=phone+sa[i]+","
                flag=1 if sa[i+1].find("@")!=-1 else 0
            else:
                email=email+sa[i]+","

        phone=phone[:-1]
        email=email[:-1]
    res.append(phone)
    res.append(email)
    return res



def toNumericalAndCategory(s):
    if s=='$' or s=='-':
        return "$ ","$ "
    ind=s.find("万")
    num=""
    cat=""
    if ind==-1:
        for c in s:
            if c>='0' and c<='9':
                num=num+c
            else:
                cat=cat+c
    else:
        num=float(s[:ind])
        num*=10000
        num=str(num)
        cat=s[ind+1:]
    num+=" "
    cat+=" "
    return num,cat





def toNewFormat(s,f):
    if s=="":
        return
    sarr=s.split()
    sres=[]
    if len(sarr)!=6:
        sarr=cleanTheData(sarr)
    for i in range(6):
        word=""
        if i==2:
            num,word=toNumericalAndCategory(sarr[i])
            f.write(num)
        elif i==5:
            word=sarr[i]+"\n"
        else:
            word=sarr[i]+" "
        f.write(word)

    return




with open("./company_info","r",encoding="UTF-8") as f:
    fr=f.readline()
    with open("./company_info_processed","w",encoding="UTF-8") as ci:
        ci.write("公司名称"+" "+"公司法人"+" "+"注册资本"+" "+"货币类型"+" "+"注册时间"+" "+"联系电话"+" "+"邮箱\n")
        while fr!="":
            fr=f.readline()
            toNewFormat(fr,ci);

