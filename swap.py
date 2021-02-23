
#normal ways of switching values in a variable without creating extra variable
# a = 4;
# b = 6;

# a = a+b;
# b = a - b;
# a = a - b;

# print(b);

#python way of doing it
a = 4;
b = 6;

a,b = b,a;
print(b);