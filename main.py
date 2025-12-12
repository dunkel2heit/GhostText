from cryptography.fernet import Fernet


def print_fading_cipher():
    print("\n" + "=" * 60)
    print("👻 G H O S T T E X T 👻")
    print("=" * 60)

    line1 = ".  / / ( ) \\ \\   / / [ ] \\ \\   : : { } : :   \\ \\ < > / /   ."
    line2 = ".  -- -- -- --  .  -- -- -- --  .  -- -- -- --  .  -- -- -- --  ."
    line3 = ".                                                                ."
    line_name = ".          G  H  O  S  T  T  E  X  T          ."
    line5 = ".    ( ( ( ( ( . ) ) ) ) )    ( ( ( . ) ) )    ( . )            ."
    line6 = ".  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / ."

    top_border = "." * 65

    print(top_border)
    print(line1)
    print(line2)
    print(line3)
    print(line_name)
    print(line3)
    print(line5)
    print(line6)
    print(line6.replace('/', '\\'))  # Flipped slashes for symmetry
    print(line2)
    print(line1.replace('/', '#').replace('\\', '/').replace('#', '\\'))  # Flipped slashes/backslashes
    print(top_border)
print_fading_cipher()
n_or_c = input("(N)ew or (C)ustom key?\n")
if n_or_c.lower() == "n":
    key = Fernet.generate_key()
    f = Fernet(key)
    print(key)
elif n_or_c.lower() == "c":
    print("Sorry this feature isn't accessible for you right now.\nwe will just generate a new password for you right now :) ")
    key = Fernet.generate_key()
    print(key)
    f = Fernet(key)
else:
    print("You have entered an invalid action. Try again!")
    exit()

def write():
    message = input("Enter your message:\n")
    message_bytes = message.encode()
    encrypted_message = f.encrypt(message_bytes)
    print(encrypted_message.decode())
def read():
    message = input("Enter the message to decrypt:\n")
    message_bytes = message.encode()
    decrypted_message = f.decrypt(message_bytes)
    print(decrypted_message.decode())


while True:
    main = input("Wich action do you want to perform: (R)ead or (W)rite or (Q)uit? ")
    main = main.lower()
    if main == "r":
        read()
    elif main == "w":
        write()
    elif main == "q":
        break
    else:
        print("You have entered an invalid action.")

