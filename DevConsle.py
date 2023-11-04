from colorama import init, Fore, Back, Style
import os

init(convert=True)

# when tool running will put you in tools directory where it will show you tools for hacking etc...
def tool():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        tools = input(Fore.GREEN + "-/tools $ ")

        if tools == "ls":
            # here will be github tools
            print(Fore.RED + "1. https://github.com/evildevill/EmptyPhish")
            print(Fore.RED + "2. https://github.com/tvvnp2/info-ip")
            print(Fore.RED + "3. https://github.com/tvvnp2/The-bat")

        if tools == "exit":
            # this command will clear the terminal and exit the directory
            os.system('cls' if os.name == 'nt' else 'clear')
            break

# this command will clear the terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# if the user gets correct pass and user he will enter the terminal
print("======= login =======")
user = input("username: ")
password = input("password: ")

if user == "error" and password == "AEC":
    print(Fore.YELLOW + "Welcome Owner!")
elif user == "hecker_01" and password == "Nopassword.1234":
    print(Fore.BLUE + "Welcome Moderator!")
else:
    # if the password wrong it will exit the program
    print(Fore.RED + "Wrong!")
    exit()

print("=====================")

print(Fore.YELLOW + "[!] use --help for commands")

while True:
    # user will use command with this input
    command = input(Fore.GREEN + '- $ ')
    print("")

    if command.lower() == "info":
        print(Fore.YELLOW + "This project, created by Error Code, showcases a collection of valuable online tools that I've discovered. Due to my school commitments, I was unable to dedicate more time to this project. However, if you're interested in seeing more projects like this in the future, please don't hesitate to reach out and let me know. Your feedback and support will inspire me to continue sharing useful resources and projects.")
        print("")




    if command.lower() == "--help":
        print(Fore.YELLOW + "--tools: this command is for entering tools directory")
        print(Fore.YELLOW + "cls or clear: this command is used for clearing the terminal")

    if command.lower() == "--tools":
        tool()

    if command.lower() == "cls" or command.lower() == "clear":
        clear_terminal()
