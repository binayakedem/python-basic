print("\n Please fill up for for registration or login\n")

user_name=input("Please enter user name:")
user_email=input("Please enter email :")
user_password=input("Please enter password:")

my_disctionary={
    "name":{user_name},
    "email":{user_email},
    "password":{user_password}
}
dictionary_list=list(my_disctionary)
for key, value in my_disctionary.items():
    print(f"{key}: {value}")
