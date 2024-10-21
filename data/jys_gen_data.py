import json
def escape_special_characters(text):
    # 转义文本中的特殊字符
    escaped_text = json.dumps(text, ensure_ascii=False)  # 利用json.dumps自动处理转义
    return escaped_text

# 输入文件，进行转义后输出文件
def escape_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read()
        escaped_text = escape_special_characters(text)
        with open(f'{file_name}_escaped.txt', 'w', encoding='utf-8') as f:
            f.write(escaped_text)

# 输入文本内容，输出转义后的文本内容
def escape_text(text):
    escaped_text = escape_special_characters(text)
    return escaped_text

text = """
"    肝脏大小未见异常，外形规则，表面光滑，肝实质内未见异常密度影；肝内、外胆管未见扩张，胆囊缺如。胰腺大小、形态未见异常，密度均匀，主胰管未见扩张，胰周间隙清晰。脾脏不大，密度均匀。胃壁厚较均匀，未见局限性增厚及软组织肿块。双肾、双肾上腺未见异常。上腹腔及腹膜后未见积液及肿大淋巴结。所示双侧肺底纹理增多增粗，肺气肿征。腰椎侧弯，腰椎椎体边缘骨质增生，腰4椎体右侧移位约0.8cm，腰4/5椎间隙狭窄。
"	"1、胆囊缺如。
2、肝、胆、胰、脾、胃、双肾及双肾上腺CT平扫未见明确异常。
3、扫及双侧肺底纹理增多增粗，肺气肿征。
4、腰椎侧弯，腰椎骨质增生退变，腰4椎体侧移滑脱。
"
"""
if __name__ == '__main__':
    # escape_file('jys_instruction.txt')
    print(escape_text(text))




