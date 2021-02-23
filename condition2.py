def user_spendings(bank_balance, phone_balance):
    if phone_balance < 10:
        phone_balance += 10
        bank_balance -= 10
        return "phone balance: " + str(phone_balance) + " \nbank balance is: " + str(bank_balance)


print(user_spendings(104.39, 7.62))
