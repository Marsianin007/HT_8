import json
import time

def help_func(banknotes):
    with open("banknotes.data", "w") as banknotes_file:
        json.dump(banknotes, banknotes_file)
    change_quantity()


def change_quantity(banknotes):

    nominal = input("Введіть номінал купюру, кількість якої треба змінити: ")
    quantity = input("Введіть потрібну кількість: ")


    with open("banknotes.data", "w") as banknotes_file:
        if nominal in banknotes.keys():
            banknotes[nominal] = quantity
            print("Якщо хочете змінити к-сть інших купюр, введіть '1'\n Інакше введіть будь-який символ для виходу")
            action = input("Ваш вибір: ")
            if action == "1":
                change_quantity(banknotes)

        else:
            print("Такого номіналу не існує, спробуйте знову")
            change_quantity()
        json.dump(banknotes, banknotes_file)


def admin_menu():
    banknotes_list = ["10", "20", "50", "100", "200", "500", "1000"]
    print("")
    print("Выберіть дію\n1. Переглянути наявні купюри\n2. Змінити кількість купюр")
    num = input("Ваш вибір: ")
    if num.isdigit() == False:
        print("Невірне значення")
        admin_menu()
    num = int(num)
    if num == 1:
        with open("banknotes.data", "r") as banknotes_file:
            banknotes = json.load(banknotes_file)
            for i in banknotes_list:
                print(i + " - " + str(banknotes[i]))
        admin_menu()
    if num == 2:
        with open("banknotes.data", "r") as banknotes_file:
            banknotes = json.load(banknotes_file)
        change_quantity(banknotes)


'''def add_new_user():
    with open("users.data", "r") as users_file:
        users = json.load(users_file)
        username = input("Введіть логін: ")
        password = input("Введіть ваш пароль:")
        for i in users:
            if username in i.keys():
                print("Такий логін вже існує")
                add_new_user()

        with open("users.data", "r") as users_file:
            users_list = json.load(users_file)
            pair_name_pass = {username : password}
            users_list.append(pair_name_pass)

        with open("users.data", "w") as users_file:
            json.dump(users_list, users_file)

        with open("{}_balance.data".format(username), "w") as balance_file:
            balance_file.write("0")

        with open("{}_transactions.data".format(username), "w") as transactions_file:
            time_local = time.localtime()
            time_string = time.strftime("%m/%d/%Y, %H:%M:%S", time_local)
            transactions_file.write(r"{} Date of create\n".format(time_string))
            
    print("Реєстрація успішна")
    login_menu()
    
'''

def write_time_and_action(action, username):
    with open("{}_transactions.data".format(username), "a") as transactions_file:
        time_local = time.localtime()
        time_string = time.strftime("%m/%d/%Y, %H:%M:%S", time_local)
        transactions_file.write(r"{0} {1}\n".format(time_string, action))


