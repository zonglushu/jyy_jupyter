#!/usr/bin/env python
import nbformat
from nbconvert import HTMLExporter
import os
import re
import json
import argparse

# 创建命令行参数定义
parser = argparse.ArgumentParser(description='Export and operate on Jupyter Notebook as HTML')
parser.add_argument('notebook', type=str, help='Jupyter Notebook file to export and operate on')

# 解析命令行参数
args = parser.parse_args()
# 定义 Jupyter Notebook 文件名
notebook_file = args.notebook



# notebook_file ="./sides/test.ipynb"
# 获取原文件的文件夹路径
original_directory = os.path.dirname(notebook_file)
# 定义导出的 HTML 文件名
html_file = os.path.join(original_directory, 'output.html')

# 导出 Jupyter Notebook 为 HTML
def export_to_html():
    # 通过 nbconvert 将 Notebook 导出为 HTML
    exporter = HTMLExporter()
    with open(notebook_file, 'r', encoding='utf-8') as f:
        notebook_content = nbformat.read(f, as_version=4)
    (body, resources) = exporter.from_notebook_node(notebook_content)
    # print(body)
	# 查找 body 规则
    pattern = r'body\s*{[^}]*}'  # 正则表达式匹配 body 规则
    match = re.search(pattern, body)
    if match:
        body_rule = match.group()
        new_style = 'max-width: 720px;margin: 0 auto;'  # 新的样式
        modified_body_rule = f'{body_rule[:-1]}\n  {new_style}\n}}'  # 在 body 规则中添加新样式

        # 替换原始 body 规则为修改后的内容
        modified_html = re.sub(pattern, modified_body_rule, body)

        # 保存修改后的 HTML 文件
        with open(html_file, 'w', encoding='utf-8') as output_file:
            output_file.write(modified_html)
	    





if __name__ == '__main__':
    export_to_html()  # 导出 Jupyter Notebook 为 HTML

    print(f'Jupyter Notebook 已导出为 HTML 文件: {html_file}')
