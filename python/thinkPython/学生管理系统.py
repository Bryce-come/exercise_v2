import os

filename = 'student.txt'


def main():
    while True:
        menu()
        choice = int(input("请输入您的选择："))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input("您确定要退出程序吗？Y/N")
                if answer == 'Y' or answer == 'y':
                    print("感谢您的使用！！！")
                    break
                else:
                    continue
            elif choice == 1:
                insert()  # 录入学生信息
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()


def menu():
    print("===============学生信息管理系统====================")
    print('----------------功能菜单--------------------------')
    print('\t\t\t 1.录入学生信息')
    print('\t\t\t 2.查找学生信息')
    print('\t\t\t 3.删除学生信息')
    print('\t\t\t 4.修改学生信息')
    print('\t\t\t 5.学生信息排序')
    print('\t\t\t 6.统计学生总人数')
    print('\t\t\t 7.显示所有学生信息')
    print('\t\t\t 0.退出')
    print('------------------------------------------------')


def insert():
    student_list = []
    while True:
        try:  # 各种输入要规定好格式
            id = int(input("请输入ID（如1001）："))
            if not id:
                break
        except:
            print("无效输入，请输入数字ID")
            continue
        name = input("请输入学生姓名：")
        if not name:
            break
        try:
            english = int(input("请输入英语成绩："))
            python = int(input("请输入Python成绩："))
            java = int(input("请输入Java成绩："))

        except:
            print("输入无效，请重新输入！！！")
            continue

            # 接下来是将录入的信息保存到字典中
        student = {'id': id, 'name': name, 'english': english, 'python': python, 'java': java}
        # 再将学生信息添加到列表当中
        student_list.append(student)
        answer = input("是否继续添加？Y/N")
        if answer == 'Y' or answer == 'y':
            continue
        else:
            break

        # 调用save()函数用于存储
    save(student_list)
    print("学生信息录入完毕")


def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()


def search():
    student_query = []
    while True:
        id = ''
        name = ''
        if os.path.exists(filename):
            mode = input('按照ID查找请按1：，按照姓名查找请按2：')
            if mode == '1':
                try:
                    id = int(input('请输入学生ID'))
                except:
                    print("无效输入，请输入数字ID！")
                    continue
            elif mode == '2':
                name = input('请输入学生姓名')
            else:
                print('您的输入有误，请重新输入！')
                search()
            with open(filename, 'r', encoding='utf-8') as rfile:
                student = rfile.readlines()
                for item in student:
                    d = dict(eval(item))  # eval()函数就是实现list, dict,tuple 与str之间的转化
                    if id != '':
                        if d['id'] == id:
                            student_query.append(d)
                    elif name != '':
                        if d['name'] == name:
                            student_query.append(d)
            # 显示查询结果
            show_student(student_query)
            # 清空列表
            student_query.clear()
            answer = input('是否要继续查询？y/n \n')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break
        else:
            print('暂未保存数据')
            return


def show_student(lst):
    if len(lst) == 0:
        print('没有查到学生信息！')
        return
    # 定义标题显示格式
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('ID', '姓名', '英语成绩', 'Python成绩', 'Java成绩', '总成绩'))
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    for item in lst:
        print(format_data.format(item.get('id'),  # get()用于字典，返回其value
                                 item.get('name'),
                                 item.get('english'),
                                 item.get('python'),
                                 item.get('java'),
                                 int(item.get('english') + item.get('python') + item.get('java'))
                                 ))


def delete():
    while True:
        student_id = input("请输入您要删除的学生ID：")
        if student_id != '':
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()
            else:
                student_old = []
            flag = False  # 标记是否删除
            if student_old:
                with open(filename, 'w', encoding='utf-8') as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))
                        if d['id'] != student_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f"该学生{student_id}信息已被删除！")
                    else:
                        print(f'无id为{student_id}的学生！')
            else:
                print('无学生信息！')
                break
            show()
            answer = input("是否继续删除？y/n")
            if answer == 'Y' or answer == 'y':
                continue
            else:
                break


def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_old = rfile.readlines()

    else:
        return

    student_id = input("请输入您要修改的学生ID：")
    with open(filename, 'w', encoding='utf-8') as wfile:
        for item in student_old:
            d = dict(eval(item))
            if d['id'] == student_id:
                print('找到学生信息，可以进行修改！')
                while True:
                    try:
                        d['name'] = input('请输入学生姓名')
                        d['english'] = input('请输入学生英语成绩')
                        d['python'] = input('请输入学生Python成绩')
                        d['java'] = input('请输入学生Java成绩')
                    except:
                        print("您的输入有误，请重新输入！")
                    else:
                        break
                wfile.write(str(d) + '\n')
                print('修改成功')
            else:
                wfile.write(str(d) + '\n')

        answer = input('是否继续修改学生信息？y/n')
        if answer == 'y' or answer == 'Y':
            modify()


def sort():
    # 0 表示升序，1表示降序
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_list = rfile.readlines()
        student_new = []
        for item in student_list:
            d = dict(eval(item))
            student_new.append(d)
    else:
        return
    asc_or_desc = input('请选择升序还是降序！(0升，1降)')
    if asc_or_desc == '0':
        asc_or_desc_bool = False
    elif asc_or_desc == '1':
        asc_or_desc_bool = True
    else:
        print('您的输入有误，请重新输入')
        sort()
    mode = input('请选择排序方式(1.按英语成绩排序 2.按Python成绩排序 3.按Java成绩排序 4.按总成绩成绩排序：)')
    if mode == '1':
        student_new.sort(key=lambda student_new: int(student_new['english']), reverse=asc_or_desc_bool)
    elif mode == '2':
        student_new.sort(key=lambda student_new: int(student_new['python']), reverse=asc_or_desc_bool)
    elif mode == '3':
        student_new.sort(key=lambda student_new: int(student_new['java']), reverse=asc_or_desc_bool)
    elif mode == '4':
        student_new.sort(
            key=lambda student_new: int(student_new['english']) + int(student_new['python']) + int(student_new['java']),
            reverse=asc_or_desc_bool)
    else:
        print('您的输入有误，请重新输入')
        sort()
    show_student(student_new)


def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
            if students:
                print(f'一共有{len(students)}名学生')
            else:
                print('还没有录入学生信息')
    else:
        print('暂未保存数据...')


def show():
    student_lst = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student = rfile.readlines()
            for item in student:
                student_lst.append(eval(item))
            if student_lst:
                show_student(student_lst)


    else:
        print('暂未保存过数据!')


if __name__ == '__main__':
    main()
