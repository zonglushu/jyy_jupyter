import subprocess
import docx
import re
# 要执行的Mac命令
# 将用户输入的参数与命令一起构建
# user_input = "你是谁"



def lab_to_gpt(*user_input):
    i=0
    lab_problem=list(user_input)
    while True:
        # print(f"要执行第{i}个")
        command = f"run_myscript.sh --input {lab_problem[i]}" # 以"ls -l"命令为例
        # 使用subprocess运行命令
        print(command)
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # 获取命令的标准输出和标准错误输出
        # 检查命令的返回码
        if result.returncode == 0:
            a=result.stdout
            # 命令成功执行
            # print("命令执行成功")
            # print("命令输出：")
            # print(f"内部的输出\n{result.stdout}")
            yield a
        else:
            # 命令执行失败
            # print("命令执行失败")
            # print("错误信息：")
            yield result.stderr
        i+=1
    

# 打开Word文档
doc = docx.Document("sides/实验3-实验报告.docx")

# # 遍历文档中的段落，查找表格
# for table in doc.tables:
#     # 遍历表格中的行
#     for row in table.rows:
#         # 遍历行中的单元格
#         for cell in row.cells:
#             # 检查单元格中的文本是否包含特定内容
#             if "你好" in cell.text:

#                 # 如果找到匹配的内容，打印整行的文本
#                 row_text = cell.text

#                 source_codes=row_text.split("列出测试数据和实验结果截图：")
#                 labs=[ i for i in source_codes]
                
#                 problems=[(lambda x :x.replace(" ","").replace("\n","").replace(" ","").replace("\n","").replace(" ","").replace("\n","").replace(" ",""))(lab) for lab in labs]
#                 print(len(labs))
#                 print(problems)
#                 lab_generator=lab_to_gpt(*problems)
#                 for i in range( len(labs)):
#                     lab_result=next(lab_generator)
#                     # print(lab_result)
#                     labs[i]+=lab_result
#                     labs[i]+="\n列出测试数据和实验结果截图：\n"

#                 with open("os.txt", "w") as f:
#                     f.write("".join(labs))

                # with open("result.txt", "r") as f:
                #     cell.text=f.read()
                # doc.save("sides/实验报告（实验6）.docx")
                # break

# with open("sides/实验报告（实验6）.docx", "rb") as f:
#     f.write("".join(source_codes).encode("utf-8"))
if __name__=="__main__":
    # 好友管理系统

    friends = []  # 存储好友列表

    # 添加好友
    def add_friend():
        print("请输入要添加的好友：")
        name = input()
        friends.append(name)
        print("好友添加成功")

    # 删除好友
    def delete_friend():
        print("请输入删除好友姓名：")
        name = input()
        if name in friends:
            friends.remove(name)
            print("删除成功")
        else:
            print("好友不存在")

    # 备注好友
    def edit_friend():
        print("请输入要修改的好友姓名：")
        old_name = input()
        if old_name in friends:
            print("请输入修改后的好友姓名：")
            new_name = input()
            index = friends.index(old_name)
            friends[index] = new_name
            print("备注成功")
        else:
            print("好友不存在")

    # 展示好友
    def show_friends():
        if not friends:
            print("好友列表为空")
        else:
            print("好友列表:")
            for friend in friends:
                print(friend)

    # 主程序
    while True:
        print("\n好友管理系统")
        print("1. 添加好友")
        print("2. 删除好友")
        print("3. 备注好友")
        print("4. 展示好友")
        print("5. 退出")
        choice = input("请输入您的选项：")

        if choice == "1":
            add_friend()
        elif choice == "2":
            delete_friend()
        elif choice == "3":
            edit_friend()
        elif choice == "4":
            show_friends()
        elif choice == "5":
            print("关闭好友系统，再见！")
            break
        else:
            print("无效的选项，请重新输入")
