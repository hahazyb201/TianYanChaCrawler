# TianYanChaCrawler
<p>
数据爬虫部分：<br>
~/crawler/ 下<br>
1.<br>
运行 python3 ./test.py  ,可以自动按照 company_before.csv 上的企业名录去天眼查中爬取企业信息，并保存到company_info中<br>
运行 python3 ./process.py   可以将company_info中的数据格式转换为更易于存储在dgraph中的格式，保存在company_info_processed中<br>
2.<br>
运行 python3 orgCode.py   可以随机产生组织机构代码。<br>
3.<br>
运行 python3 ./findControler.py  可以分析所输入公司的实际控制人，并输入构建dgraph所需的关系到share<br>
4.<br>
exchange.py : 来自网络的汇率转化程序<br>
<br>
dgraph部分:<br>
~/KnowledgeGraph/ 下：<br>
build_Dgraph 中的指令用于构建dgraph<br>
其他dgraph介绍见ppt<br>


</p>
