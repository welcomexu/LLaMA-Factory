# 读取excel文件
import pandas as pd
import os
import json

txt_6_50 = """放射检查号：WH00000041
姓名：CT 胸部
性别：男
年龄：64岁
申请科室：
住院号：
门诊号：
检查项目：胸部平扫
送检医师要求：
临床诊断：
检查方法：
"""

txt_51_74 = """放射检查号：WH24051300000001
姓名：检查号合并
性别：女
年龄：25岁
申请科室：
住院号：
体检号：
检查项目：头颅正侧位
送检医师要求：
检查方法：
"""

txt_75_106 = """放射检查号：WH00000023
姓 名：CT 颅部
性 别：男
年 龄：50岁
申请科室：
住院号：
体 检 号：
检查项目：颅部血管成像平扫+增强
送检医师要求：
检查方法：
"""

txt_200 = """放射检查报告
放射检查号： 姓名：
性别： 年龄：
申请科室： 住院号：
体检号： 检查项目：
送检医师要求： 检查方法：
"""

write_path = "C:\\Users\\WS\\Downloads\\jys2"
file_path = "D:\\xyh\\mygitfiles\\info_records\\data-full.xlsx"
data = pd.read_excel(file_path, dtype=str, na_values="")
# data = data[:10]
for item in data.iterrows():
    row = item[0]
    info = item[1].to_dict()
    if pd.notna(info['txt']):
        # 以下针对一种类型的情况
        # info_num = int(info['txt'])
        # text = ""
        # if info_num >= 6 and info_num <= 50:
        #     text = txt_6_50
        # elif info_num >= 51 and info_num <= 74:
        #     text = txt_51_74
        # # else info_num >= 75 and info_num <= 106:
        # else:
        #     text = txt_75_106
        # filename = str(info['txt'])
        # desc = "放射学表现：\n" + info['影像所见'].replace("\n", "    ")
        # diags = "放射学诊断：\n" + info['影像诊断'].replace("\n", "")
        # text = text + desc + "\n" + diags
        # # 将text写入txt文件
        # with open(os.path.join(write_path, filename + ".txt"), "w", encoding="utf-8") as f:
        #     f.write(text)

        if pd.notna(info['txt']):
            info_num = int(info['txt'])
            text = ""
            if info_num >= 250:
                text = txt_200
                filename = str(info['txt'])
                desc = "放射学表现：\n" + info['影像所见']
                diags = "放射学诊断：\n" + info['影像诊断']
                text = text + desc + "\n" + diags
                # 将text写入txt文件
                with open(os.path.join(write_path, filename + ".txt"), "w", encoding="utf-8") as f:
                    f.write(text)
