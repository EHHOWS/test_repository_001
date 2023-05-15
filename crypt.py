import random
import time

CODE_LEN = 8

class Encode():
    def __init__(self):
        self.main()
    
    def randomizer(self, key:int):
        random.seed(key)
        lists = [[] for _ in range(10)]
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=~';:/?.]"
        for char in random.sample(chars, len(chars)):
            index = random.randint(0, 9)
            lists[index].append(char)
        return lists
        
    def encrypting(self, txt:str, lists:list):
        new_txt = str()
        random.seed()
        for c in txt:
            if c == "0": temp = lists[0][random.randint(0, len(lists[0])-1)]
            elif c == "1": temp = lists[1][random.randint(0, len(lists[1])-1)]
            elif c == "2": temp = lists[2][random.randint(0, len(lists[2])-1)]
            elif c == "3": temp = lists[3][random.randint(0, len(lists[3])-1)]
            elif c == "4": temp = lists[4][random.randint(0, len(lists[4])-1)]
            elif c == "5": temp = lists[5][random.randint(0, len(lists[5])-1)]
            elif c == "6": temp = lists[6][random.randint(0, len(lists[6])-1)]
            elif c == "7": temp = lists[7][random.randint(0, len(lists[7])-1)]
            elif c == "8": temp = lists[8][random.randint(0, len(lists[8])-1)]
            elif c == "9": temp = lists[9][random.randint(0, len(lists[9])-1)]
            new_txt += temp
        return new_txt

    def decrypting(self, txt:str, lists:list):
        new_txt = str()
        for c in txt:
            if c in lists[0]: temp = 0
            elif c in lists[1]: temp = 1
            elif c in lists[2]: temp = 2
            elif c in lists[3]: temp = 3
            elif c in lists[4]: temp = 4
            elif c in lists[5]: temp = 5
            elif c in lists[6]: temp = 6
            elif c in lists[7]: temp = 7
            elif c in lists[8]: temp = 8
            elif c in lists[9]: temp = 9
            new_txt += str(temp)
        return new_txt
        
    def to_base_length(self, text:str, length=CODE_LEN):
        text = str(text)
        while len(text) < length:
            text = "0" + text
        return text
        
    def encode(self, text:str, key):
        code = str()
        for c in text:
            encrypted_char = ord(c)
            code += self.to_base_length(encrypted_char, CODE_LEN)
        return (self.encrypting(code, self.randomizer(key)), key)
    
    def decode(self, code:str, key):
        decoded_text = str()
        decrypted_code = self.decrypting(code, self.randomizer(key))
        for i in range(int(len(decrypted_code)/CODE_LEN)):
            start = int(CODE_LEN * i)
            end = int(CODE_LEN + start)
            decoded_char = int(decrypted_code[start:end])
            decoded_text += chr(decoded_char)
        return decoded_text
    

    def main(self):
        while True:
            print()
            act = input("Command Here> ")
            print()
            try:
                if act.upper() == "ENCODE" or act == "0":
                    text = input("Text Here: ")
                    key = random.randint(1, 909999)
                    result = self.encode(text, key)
                    print(f"your code | {result[0]}\nyour key | {result[1]}")

                elif act.upper() == "DECODE" or act =="1":
                    code = input("Code Here: ")
                    key = int(input("Key Here: "))
                    result = self.decode(code, key)
                    print(f"original text | {result}")

                elif act.upper() == "ENCODEWITHKEY" or act =="2":
                    text = input("Text Here: ")
                    key = int(input("Key Here: "))
                    result = self.encode(text, key)
                    print(f"your code | {result[0]}\nyour key | {result[1]}")

                elif act.upper() == "EXIT" or act.upper() =="QUIT":
                    break

                elif act.upper() == "HELP" or act =="?":
                    print("""ENCODE or 0 -> get text and make code and key
DECODE or 1 -> get code and key to make plaintext
ENCODEWITHKEY or 2 -> get text and key to make code
EXIT or QUIT -> break this program
HELP or ? -> show this list""")

                else:
                    print(f"{act} is not a correct command.\ntry 'help' or '?' to get an information of commands")
            
            except:
                print("UNEXPECTED ERROR OCCURED\nPLESE RETRY")
Encode()