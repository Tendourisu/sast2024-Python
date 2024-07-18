import json
import sys

def load_data(filepath):
    # 加载JSON文件数据
    if filepath.endswith('.jsonl'):
        try:
            with open(filepath, 'r') as file:
                return [json.loads(line) for line in file]
        except FileNotFoundError:
            print(f"文件 {filepath} 未找到。")
            sys.exit(2)
        except json.JSONDecodeError:
            print(f"文件 {filepath} 格式不正确。")
            sys.exit(3)
    elif filepath.endswith('.json'):
        try:
            with open(filepath, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"文件 {filepath} 未找到。")
            sys.exit(2)
        except json.JSONDecodeError:
            print(f"文件 {filepath} 格式不正确。")
            sys.exit(3)
    else:
        print(f"不支持的文件格式: {filepath}")
        sys.exit(4)

def select_course(student, courses):
    # 实现选课逻辑
    print("可选的课程：")
    for i, course in enumerate(courses, start=1):
        print(f"{i}. {course['name']}")
    choice = int(input("请选择课程编号："))
    selected_course = courses[choice - 1]
    student.setdefault('courses', [])
    student['courses'].append(selected_course)
    print(f"已选课程：{selected_course['name']}")

def view_selected_courses(student):
    # 查看已选课程
    selected_courses = student.get('courses', [])
    for course in selected_courses:
        print(course['name'])
            

def save_data(filepath, data):
    # 保存数据到JSON文件
    try:
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError:
        print(f"无法保存到文件 {filepath}。")

def print_menu():
    print("\n选课系统菜单：")
    print("1. 选课")
    print("2. 查看已选课程")
    print("3. 退出")

def main(student_file, courses_file):
    students = load_data(student_file)
    courses = load_data(courses_file)
    
    while True:
        print_menu()
        choice = input("请选择一个操作（1-3）：")
        if choice == '1':
            # 示例：选课操作
            select_course(students, courses)
            pass
        elif choice == '2':
            # 示例：查看已选课程
            view_selected_courses(students)
            pass
        elif choice == '3':
            print("退出系统。")
            break
        else:
            print("无效的输入，请重新选择。")
    
    # 保存学生数据
    save_data(student_file, students)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <student_filepath> <courses_filepath>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])