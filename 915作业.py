import random


list=["老鼠","耗牛","华南虎","玉兔","祥龙","眼镜蛇","汗血宝马","绵羊","金丝猴","大公鸡","小金毛","老母猪"]
dz=["仰卧起坐","蹲起","俯卧撑","蛙跳","后空翻","高抬腿"]
peo = int(input("请输入你要处罚的编号"))-1
if peo <= 12 and peo > -12:
    fsk=random.randint(0,len(dz)-1)
    ran=random.randint(100,500)
    print(list[peo],"处罚了",ran,"遍",dz[fsk])
else:
    print("只有十二个别整多了")