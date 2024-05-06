import configparser
import os


def update_config(option, new_value):
    # 创建一个配置文件解析器对象
    config = configparser.ConfigParser()

    # 读取配置文件
    config.read('config.ini')

    # 根据用户选择修改配置项
    if option == '1':
        config.set('Network', 'IP', new_value)
    elif option == '2':
        config.set('Network', 'V', new_value)
    elif option == '3':
        config.set('Cookies', 'JSESSIONID', new_value)
    elif option == '5':
        config.set('User', 'username', new_value)
    elif option == '6':
        config.set('User', 'password', new_value)
    else:
        print("无效的选项")

    # 保存修改后的配置文件
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    os.system('cls')
    print("配置已更新:", new_value)


def read_config():
    # 创建一个配置文件解析器对象
    config = configparser.ConfigParser()

    # 读取配置文件
    config.read('config.ini')

    # 读取配置文件中的值
    ip = config.get('Network', 'IP')
    v = config.get('Network', 'V')
    jsessionid = config.get('Cookies', 'JSESSIONID')
    username = config.get('User', 'username')
    password = config.get('User', 'password')

    return ip, v, jsessionid, username, password


def main():
    print("1. 修改IP")
    print("2. 修改V")
    print("3. 修改JSESSIONID")
    print("4. 读取配置文件")
    print("5. 修改用户名")
    print("6. 修改密码")
    print("====================")

    # 用户选择要执行的操作
    option = input("请输入选项 (1/2/3/4/5/6): \n")
    if option not in ['1', '2', '3', '4', '5', '6']:
        print("无效的选项")
        return

    if option == '4':
        os.system('cls')
        # 读取配置文件并显示配置项的值
        ip, v, jsessionid, username, password = read_config()
        print(f"IP: {ip}")
        print(f"V: {v}")
        print(f"JSESSIONID: {jsessionid}")
        print(f"Username: {username}")
        print(f"password: {password}")

    else:
        new_value = input("请输入新的值: \n")
        # 调用函数来更新或写入配置
        update_config(option, new_value)


if __name__ == "__main__":
    main()
