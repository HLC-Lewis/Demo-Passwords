import requests

#https://github.com/danielmiessler/SecLists
SECLIST_GIT = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Leaked-Databases/"

list_of_leaked_databases = {
    "000webhost","Ashley-Madison","Lizard-Squad","NordVPN","adobe100","alleged-gmail-passwords","bible-withcount",
    "bible","carders.cc","elitehacker-withcount","elitehacker","faithwriters-withcount","faithwriters","fortinet-2021",
    "hak5-withcount","hak5","honeynet-withcount","honeynet","honeynet2","hotmail","izmy","md5decryptor-uk","muslimMatch-withcount",
    "muslimMatch","myspace-withcount","myspace","phpbb-cleaned-up","phpbb-withcount","phpbb","porn-unknown-withcount",
    "porn-unknown","rockyou-05","rockyou-10","rockyou-15","rockyou-20","rockyou-25","rockyou-30","rockyou-35","rockyou-40",
    "rockyou-45","rockyou-50","rockyou-55","rockyou-60","rockyou-65","rockyou-70",    "rockyou-75","rockyou-withcount.tar.gz",
    "rockyou.tar.gz","singles.org-withcount","singles.org","tuscl","youporn2012-raw","youporn2012",
}

set_of_passwords = set()
for each in list_of_leaked_databases:
    url = f'{SECLIST_GIT}{each}.txt'
    print(f'[Password Checker] Compiling: `{each}` into the password set')

    list_of_passwords = requests.get(url)

    for password in list_of_passwords.iter_lines():
        utf8_password = password.decode('UTF-8')
        if password: set_of_passwords.add(utf8_password.lower())

print(f'[Password Checker] Compiled password set')

while True:
    enter_password = input("⎯"*30+"\nEnter the password to check\n> ")
    if enter_password.lower() in set_of_passwords:
        print("[Password Checker] The password entered was found in a leaked password database.\nWe recommend changing your password.")
