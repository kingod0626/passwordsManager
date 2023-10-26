import json
import os


def get_account_dic():
    with open("password.json", "r", encoding="utf-8") as f:
        account_str = f.read()
        if account_str == "":
            return {}
        else:
            return json.loads(account_str)


def add_account(name, account, password):
    file = "password.json"
    if os.path.isfile(file):
        if check_name(name):
            account_dic = get_account_dic()
            account_dic[name] = {
                "account": account,
                "password":password
            }
            with open("password.json","w", encoding="utf-8") as f:
                f.write(json.dumps(account_dic, indent=2))
            return True
        else:
            return False
    else:
        file = open('password.json', 'w')
        add_account(name, account, password)
        return True



def check_name(name):
    account_dic = get_account_dic()
    if name in account_dic.keys():
        return False
    else:
        return True


print("歡迎使用密碼管理")

while True:
    mode = input("選擇要使用的功能(r查詢 a新增 d刪除 q離開)")
    if mode == "q":
        break
    elif mode == "a":
        name = input("請輸入這組帳號的用途:")
        account = input("請輸入帳號:")
        password = input("請輸入密碼:")
        if add_account(name, account, password):
            print("新增成功")
        else:
            print("已有此帳號")
    elif mode =="r":
        name = input("請輸入帳號名稱:")
        if check_name(name):
            print("無此帳號")
        else:
            account_dic = get_account_dic()
            account = account_dic[name]["account"]
            password = account_dic[name]["password"]
            print(f"帳號:{account}, 密碼:{password}")
    elif mode =="d":
        name = input("請輸入要刪除的帳號")
        account_dic = get_account_dic()
        del account_dic[name]
        with open("password.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(account_dic, indent=2))
        print("帳號已刪除")
    else:
        print("請輸入代表功能的代號")


# password = {
#     "account":"123456789",
#     "password":"123"
# }
# with open("password1.json","w", encoding="utf-8") as f:#讀取(r) 覆寫(w) 再寫入(a)
#     f.write(json.dumps(password, indent=2))
# with open("password.json","r", encoding="utf-8") as f:#讀取(r) 覆寫(w) 再寫入(a)
#     x = json.loads(f.read())
#     print(x)
#     print(x["password"])

