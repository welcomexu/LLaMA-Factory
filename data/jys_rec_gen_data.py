
# user_content = "<image>识别图片中检查报告中的文字"

def gen_user_content():
    user_contents = [
        "识别图片中检查报告中的文字",
        "识别图片中的文字",
        "识别图片中检查报告中的文字内容",
        "提取图片中的文字",
        "OCR识别图片中检查报告中的文字",
        "OCR识别图片中的文字内容",
        "OCR识别图片中检查报告中的文字信息",
        "提取图片中的文字内容",
        "识别图片中检查报告中的文本",
        "提取图片中的文本",
        "你是一个OCR专家，帮我识别一下图片中检查报告中的文字",
        "你能帮我识别一下图片中的文字吗",
        "你能帮我提取一下图片中检查报告中的文字吗",
        "你能帮我提取一下图片中的文字内容吗",
        "你能帮我提取一下图片中的文字信息吗",
        "你是一个OCR专家，你的任务是识别图片中检查报告中的文字",
        "你是一个OCR专家，你的任务是提取图片中的文字",
        "你是一个OCR专家，你的任务是提取图片中检查报告中的文字内容",
        "你是一个OCR专家，你的任务是提取图片中的文字信息",
        "你是一个OCR专家，你的任务是识别图片中检查报告中的文字内容",
        "作为一个OCR专家，你的任务是识别图片中的文字",
        "作为一个OCR专家，你的任务是提取图片中检查报告中的文字",
        "作为一个OCR专家，你的任务是提取图片中检查报告中的文字内容",
        "作为一个OCR专家，你的任务是提取图片中的文字信息",
        "作为一个OCR专家，你的任务是识别图片中检查报告中的文字内容",
        "作为一个OCR专家，你的任务是提取图片中的文本",
        "作为一个OCR专家，你的任务是提取图片中检查报告中的文本内容",
        "作为一个OCR专家，你的任务是提取图片中的文本信息",
        "作为一个OCR专家，你的任务是识别图片中检查报告中的文本",
        "作为一个OCR专家，你的任务是提取图片中的文本内容"
    ]
    return random.choice(user_contents)

file_path = "C:\\Users\\WS\\Downloads\\jys"

# 读取文件夹中所有txt文件
import os
import re
import json
import random
json_ret = []

for root, dirs, files in os.walk(file_path):
    for file in files:
        if file.endswith(".txt"):
            print(os.path.join(root, file))
            with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                content = f.read()
                response_content = repr(content)
            # 获取file文件名，不要后缀
            file_name = os.path.splitext(file)[0]
            imgs_name_prefix = file_name + "."
            # 读取以imgs_name_prefix开头的所有图片文件并随机选择一张图片
            imgs = []
            for img_file in files:
                if img_file.startswith(imgs_name_prefix) and not img_file.endswith(".txt"):
                    imgs.append(img_file)
            # print(imgs)
            if len(imgs) > 0:
                img_file = random.choice(imgs)
                img_file_path = os.path.join(root, img_file)
                response_img_file_path = img_file_path
                # print(response_img_file_path)
            json_ret.append({
                "messages": [
                    {
                        "content": "<image>" + gen_user_content(),
                        "role": "user"
                    },
                    {
                        "content": response_content,
                        "role": "assistant"
                    }
                ],
                "images": [
                    response_img_file_path
                ]
            })

print(json.dumps(json_ret, ensure_ascii=False, indent=4))
# 写入.json文件
with open("C:\\Users\\WS\\Downloads\\jys\\jys.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(json_ret, ensure_ascii=False, indent=4))





