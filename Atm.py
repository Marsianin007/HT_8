import json
import time
from admin import admin_menu, write_time_and_action



def check_balance(username):
    with open("{}_balance.data".format(username), "r") as balance_file:
        balance = json.load(balance_file)
        print("Ваш баланс: " + str(balance) +" uah")
        start_menu(username)
    write_time_and_action("check_balance", username)



def up_balance(username):
    sum_to_put = input("Введіть сумму, на яку хочете поповнити картку: ")

    if sum_to_put.isdigit():
        sum_to_put = int(sum_to_put)
        with open("{}_balance.data".format(username), "r") as balance_file:
            old_balance = int(json.load(balance_file))

        with open("{}_balance.data".format(username), "w") as balance_file:
            new_balance  = old_balance + sum_to_put
            new_balance = str(new_balance)
            balance_file.write(new_balance)
            print("Поповнення успішне")
        start_menu(username)
    else:
        print("Введіть будь-ласка додатнє число\n")
        up_balance(username)

    write_time_and_action("up_balance", username)

def exit_from_func(sum_to_get, nominal, variable, username):
    with open("banknotes.data", "r") as banknotes_file:
        banknotes_dict = json.load(banknotes_file)
        list = [10, 20, 50, 100, 200, 500, 1000]
        check = True
        for i in list:
            if sum_to_get % i == 0 and int(banknotes_dict[str(i)]) > 0:
                check = False
        if check:
            #print(nominal)
            #print(variable)
            sum_to_get += nominal * variable
            #print("check = True")
            #print(sum_to_get)
            #banknotes_to_get(sum_to_get, username)
            #return nominal

            return sum_to_get, 0
        else:
            return sum_to_get, variable

def banknotes_to_get(sum_to_get, username):

    with open("banknotes.data", "r") as banknotes_file:
        banknotes_dict = json.load(banknotes_file)
        uah_10 = uah_20 = uah_50 = uah_100 = uah_200 = uah_500 = uah_1000 = 0
        print(sum_to_get)

        while sum_to_get >= 1000 and int(banknotes_dict["1000"]) > 0:
            uah_1000 += 1
            banknotes_dict["1000"] = int(banknotes_dict["1000"]) - 1
            sum_to_get -= 1000
        sum_to_get, uah_1000 = exit_from_func(sum_to_get, 1000, uah_1000, username)

        while sum_to_get >= 500 and int(banknotes_dict["500"]) > 0:
            uah_500 += 1
            banknotes_dict["500"] = int(banknotes_dict["500"]) - 1
            sum_to_get -= 500
        sum_to_get, uah_500 = exit_from_func(sum_to_get, 500, uah_500, username)

        while sum_to_get >= 200 and int(banknotes_dict["200"]) > 0:
            uah_200 += 1
            banknotes_dict["200"] = int(banknotes_dict["200"]) - 1
            sum_to_get -= 200
        sum_to_get, uah_200 = exit_from_func(sum_to_get, 200, uah_200, username)

        while sum_to_get >= 100 and int(banknotes_dict["100"]) > 0:
            uah_100 += 1
            banknotes_dict["100"] = int(banknotes_dict["100"]) - 1
            sum_to_get -= 100
        sum_to_get, uah_100 = exit_from_func(sum_to_get, 100, uah_100, username)

        while sum_to_get >= 50 and int(banknotes_dict["50"]) > 0:
            uah_50 += 1
            banknotes_dict["50"] = int(banknotes_dict["50"]) - 1
            sum_to_get -= 50
        sum_to_get, uah_50 = exit_from_func(sum_to_get, 50, uah_50, username)



        while sum_to_get >= 20 and int(banknotes_dict["20"]) > 0:
            uah_20 += 1
            banknotes_dict["20"] = int(banknotes_dict["20"]) - 1
            sum_to_get -= 20
        sum_to_get, uah_20 = exit_from_func(sum_to_get, 20, uah_20, username)

        while sum_to_get >= 10 and int(banknotes_dict["10"]) > 0:
            uah_10 += 1
            banknotes_dict["10"] = int(banknotes_dict["10"]) - 1
            sum_to_get -= 10
        sum_to_get, uah_10 = exit_from_func(sum_to_get, 10, uah_10, username)

        if sum_to_get != 0:
            print("Нажаль банкомат не може видасти потрібну сумму, спробуйте змінити сумму\n")
            get_money(username)

    with open("banknotes.data", "w") as banknotes_file:
        json.dump(banknotes_dict, banknotes_file)

    #print(banknotes_dict)
    if uah_1000 != 0: print("1000 - " + str(uah_1000))
    if uah_500 != 0: print("500 - " + str(uah_500))
    if uah_200 != 0: print("200 - " + str(uah_200))
    if uah_100 != 0: print("100 - " + str(uah_100))
    if uah_50 != 0: print("50 - " + str(uah_50))
    if uah_20 != 0: print("20 - " + str(uah_20))
    if uah_10 != 0: print("10 - " + str(uah_10))

    start_menu(username)


def get_money(username):
    print("Введіть сумму кратну '10', яку потрібно зняти\n Мінімальна сумма 10")
    sum_to_get = input("Ваша сумма: ")
    if sum_to_get.isdigit() == False:
        #sum_to_get = 0
        print("Введіть коректну сумму\n")
        get_money(username)
    sum_to_get = int(sum_to_get)
    if sum_to_get < 10 or sum_to_get % 10 != 0:
        print("Введіть коректну сумму:\n")
        get_money(username)
    with open("{}_balance.data".format(username), "r") as username_balance:
        user_balance = json.load(username_balance)
        if sum_to_get > int(user_balance):
            print("Недостятньо коштів...")
            start_menu(username)
    with open("{}_balance.data".format(username), "w") as username_balance:
        new_balance = int(user_balance) - sum_to_get
        username_balance.write(str(new_balance))
    write_time_and_action("get_money", username)
    banknotes_to_get(sum_to_get, username)



def login_menu():

    username = input("Введіть Ваш логін: ")
    password = input("Введіть ваш пароль: ")

    if username == "admin" and password == "admin":
        admin_menu()
    else:
        entrance_flag = False
        with open("users.data", "r") as users_file:
            users =  json.load(users_file)
            for i in users:
                if username in i and i[username] == password:
                    entrance_flag = True
                    print("Вітаємо {}".format(username))
                    start_menu(username)
            if entrance_flag == False:
                print("Перевірте логін та пароль\nАбо якщо бажаєто зареєструватись, натисніть '1', інакше будь-який символ\n")
                num = input("Ваш вибір:")
                if num == "1":
                    add_new_user()
                else:
                    login_menu()






def start_menu(username):
    print("")
    print("Введіть дію:\n1. Продивитись баланс\n2. Поповнити баланс\n3. Зняти кошти\n4. Вихід")
    number_from_user = input("Ваша дія: ")
    print("")
    if number_from_user.isdigit():
        number_from_user = int(number_from_user)
        if number_from_user == 1:
            check_balance(username)
        if number_from_user == 2:
            up_balance(username)
        if number_from_user == 3:
            get_money(username)
        if number_from_user == 4:
            print("До зустрічі {}!".format(username))
            write_time_and_action("exit", username)
        if number_from_user < 1 or number_from_user > 4:
            print("Дії з таким номером не існує")
            start_menu(username)
    else:
        print("Введіть буль-ласка число")
        start_menu(username)


def add_new_user():
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
            pair_name_pass = {username: password}
            users_list.append(pair_name_pass)

        with open("users.data", "w") as users_file:
            json.dump(users_list, users_file)

        with open("{}_balance.data".format(username), "w") as balance_file:
            balance_file.write("0")

        with open("{}_transactions.data".format(username), "w") as transactions_file:
            time_local = time.localtime()
            time_string = time.strftime("%m/%d/%Y, %H:%M:%S", time_local)
            transactions_file.write(r"{} Date of create\n".format(time_string))

    print("Реєстрація успішна\n")
    login_menu()



login_menu()





