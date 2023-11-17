
from IPython.display import HTML
import re
from bs4 import BeautifulSoup
import os
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from IPython.display import HTML
import ipywidgets as widgets
from ipywidgets.embed import embed_minimal_html, dependency_state

# 定义 `sideshow` 函数，接受一个参数 `page_number`，用于选择要嵌入的 HTML 文件
def sideshow(page_name,section_index):
    # 根据 `page_number` 选择要嵌入的 HTML 文件
    # 源幻灯片html的地址
    f
    sides_file_path=f"../html_src/{page_name}/dist/index.html"
    # 在Jupyter中展示的幻灯片的模版
    show_sides_path=f"../html_src/10.html"
    # 最后生成幻灯片的某个片段的路径
    gener_file_path=f"../html_src/{page_name}/dist/gener{section_index}.html"
    # 最后在Jupyter中展示的幻灯片代码的地址
    frame_side_path=f"../html_src/{page_name}/dist/frame_side{section_index}.html"
    
    if(os.path.exists(frame_side_path)):
        return HTML(frame_side_path)
    
    print(sides_file_path)
    with open(sides_file_path, 'r') as file:
        html_content = file.read()
    # 使用 `sideshow` 函数嵌入选择的 HTML 页面
     # 将用户指定的 HTML 内容替换到模板中的 <body> 部分
      # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    # 提取 <head> 部分的内容
    head_content = str(soup.head)
    # 查找 <script> 标签并插入到模板中
    script_tags = soup.body.find_all('script')
    script_content = ''.join([str(script) for script in script_tags])
    # 正则表达式用于匹配各种路径
    # 这个示例覆盖了相对路径、绝对路径和 ./ 开头的相对路径
    pattern = r'(\s(src|href)=")((?!https?://|/|data:|mailto:)[^"]+)"'
    # 基准 URL，可以根据需要修改
    base_url = '../html_src/ruankao/dist/'
    # 创建一个新的 HTML 模板并插入 <head> 部分
    template = f"""
    <!DOCTYPE html>
    <html>
    {head_content}
    <body class="d-flex flex-column h-100">
        <div class="reveal">
            <div class="slides">
                <!-- 此部分将由用户指定的 HTML 内容填充 -->
            </div>
        </div>
        {script_content}
    </body>
    </html>
    """
    # def fix_path(match):
    #     # 获取匹配的路径内容
    #     path = match.group(3)

    #     # 判断路径是否以 ./ 开头
    #     if path.startswith('./'):
    #         # 对于 ./ 开头的相对路径，拼接基准 URL 和路径内容
    #         return match.group(1) + base_url + path[2:] + '"'
    #     else:
    #         # 对于其他路径，直接拼接基准 URL 和路径内容
    #         return match.group(1) + base_url + path + '"'

    # 找到所有的section
    sides_div = soup.find('div', class_="slides")
    outermost_sections = sides_div.find_all('section', recursive=False)
    selected_section="没有找到对应的selection"
    if section_index >= 0 and section_index < len(outermost_sections):
        # 选择指定索引的 <section> 标签
        selected_section = outermost_sections[section_index]
    final_html = template.replace("<!-- 此部分将由用户指定的 HTML 内容填充 -->", str(selected_section))
    # 使用正则表达式和 fix_path 函数替换路径
    # fixed_html_content = re.sub(pattern, fix_path, final_html)

    with open(gener_file_path, "w") as f:
        f.write(final_html)
    

    with open(show_sides_path, 'r') as file:
        frame_html = file.read()
    frame_soup = BeautifulSoup(frame_html, 'html.parser')
    iframe = frame_soup.body.find('iframe')
    iframe['src'] = gener_file_path

    with open(frame_side_path, 'w') as file:
        file.write(str(frame_soup))
    # print(fixed_html_content)
    # 使用 `HTML` 对象将最终的 HTML 内容嵌入到 Jupyter Notebook 中
    
    return HTML(frame_side_path)


# 第一个参数是示例的名称，第二个是示例代码存放的路径，第三个是示例代码所依赖的库
# 第二个参数为一个文件夹时，把文件夹里的所有文件都展示出来，如果只是一个文件就把那个文件展示出来
# 我现在有点怀疑他那个是c盘，d盘的路径，
# 那我这里就不跟他的一样了，我就按相对路径来了
# 其实这里的libs就有点像依赖文件一样。
# 我觉得啊，这个libs就是自己写的一个类似于hutool包一样的工具包
# 可能以后某个文件写的时候用到了这个依赖包
# 那 demo里面就放描述就好了，然后去example里面把文件加载进来就好了
#  demo("pc-sem","c/peterson.c",libs=['thread.h', 'thread-sync.h'])

def process_path(demo_code_path):
    if os.path.isfile(demo_code_path):
        # 如果是文件，读取并打印其内容
        with open(demo_code_path, 'r') as file:
            content = file.read()
            return content
    else:
        raise RuntimeError(f"{demo_code_path} is not a file")


def preter(code,lexer,formatter):
    highlighted_code=highlight(code,lexer,formatter)
    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(highlighted_code, 'html.parser')
    inline_style = "width:300px /* 其他样式 */"
    # 获取所有行号的 span
    lineno_spans = soup.select('.linenos')

    # 对每个行号的 span，将其到下一个行号之间的内容移动到新的 span 中
    for index, lineno_span in enumerate(lineno_spans, start=1):
        new_span = soup.new_tag("span", id=f"true-{index}",style=inline_style)
    
        lineno_span.insert_before(new_span)  # 将新 span 插入到当前行号之前
        next_lineno_span = lineno_spans[index] if index < len(lineno_spans) else None

        # 移动当前行号到下一个行号之间的所有内容到新的 span 中
        current_element = lineno_span
        while current_element != next_lineno_span:
            next_element = current_element.next_sibling
            new_span.append(current_element)
            current_element = next_element


    # 获取修改后的 HTML
    modified_html = str(soup)
    return modified_html
    
def demo(example_name, example_path, libs=[]):

    

    demo_desc_path=f"../demo/{example_name}/desc.md"
    demo_code_path=f"../code/{example_path}"
    code_type=example_path.split('/')[0]

    # 给定的 C 语言代码
    c_code = """
    #include <stdio.h>

    int main() {
        printf("Hello, World!\\n");
        return 0;
    }
    """
    demo_code_content=[]
    demo_code_titles=[]
    # 检查路径是否为文件
    if os.path.isfile(demo_code_path):
        demo_code_content.append(process_path(demo_code_path))
        demo_code_titles.append(os.path.basename(demo_code_path))
    # 检查路径是否为文件夹
    elif os.path.isdir(demo_code_path):
        code_pathes=[ os.path.join(demo_code_path, filename) for filename in os.listdir(demo_code_path)]
        demo_code_titles=[ filename for filename in os.listdir(demo_code_path)]
        demo_code_content=list(map(lambda x: process_path(x) , code_pathes))
    
    demo_lib_content=list(map(lambda x: process_path(f"../code/lib/{x}") , libs))
    
    # 将库函数添加到代码中
    demo_code_content.extend(demo_lib_content)

    demo_code_titles.extend(libs)

    # 指定代码语言为 C
    lexer = get_lexer_by_name(code_type, stripall=True)

    # 使用 HtmlFormatter 将代码转换为 HTML，并增加自定义 CSS 类
    formatter = HtmlFormatter(style="colorful", linenos="inline", linepad=3, cssclass='my-code')
    # 使用 BeautifulSoup 解析 HTML


    # 生成高亮的 HTML 代码
    highlighted_code_list=[preter(code,lexer,formatter) for code in demo_code_content]
    # 获取 Pygments 生成的样式
    pygments_style = f"<style>{formatter.get_style_defs('.my-code')}</style>"

    # 自定义 CSS 样式
    custom_style = """
    <style>
    .my-code .linenos {
        padding-right: 10px !important; /* 增加行号和代码之间的距离 */
        user-select: none; !important /* 防止行号被选择和复制 */
        color: #888; /* 设置行号的颜色 */
    }
    .my-code pre {
        
        background-color: #f7f7f7; /* 设置背景颜色 */
        border-radius: 5px; /* 设置边框圆角 */
    }
    .jp-OutputArea-output pre {
        line-height:125% !important; 
        font-family:'Fira Code', monospace !important;
    }
    </style>
    """

    # 将 Pygments 的样式和自定义样式结合
    full_style = pygments_style + custom_style
    display_code_html=[ full_style + highlighted_code for highlighted_code in highlighted_code_list]
    # 将 HTML 代码和样式结合显示在 Jupyter Notebook 中
    # display_code_html = full_style + highlighted_code
    # HTML(display_html)

    
    children = [widgets.HTML(value=display_html) for display_html in display_code_html ]
    # TODO 在列表前添加一个描述信息
    # children.insert(0, widgets.HTML(value=full_style))
    tab = widgets.Tab()
    tab.children = children
    tab.titles = [i for i in demo_code_titles]
    export_code_path=f"../demo/{example_name}/tab_code.html"
    embed_minimal_html(export_code_path, views=[tab])

    with open(export_code_path, "r") as f:
        html=f.read
    
    return HTML(export_code_path)

if(__name__=="__main__"):
    sideshow(1,0)
