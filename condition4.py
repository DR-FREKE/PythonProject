def Age_limit(age):
    free_to_age = 4;
    child_up_to = 18;
    senior_from = 65;

    adult_price = 2.25;
    not_adult_price = 1.25;

    if age <= free_to_age:
        price_ticket = 0;
    elif age > free_to_age and age <= child_up_to:
        price_ticket = not_adult_price;
    elif age >= senior_from:
        price_ticket = not_adult_price;
    else:
        price_ticket = adult_price;
    message = "Someone who is {} years old will pay ${} to ride the bus".format(age, price_ticket);
    return message;
print(Age_limit(18));