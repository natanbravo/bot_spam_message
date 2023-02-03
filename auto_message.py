import time
import pyautogui as spam

message_limit = int(input("Enter max number of messages you want to send: "))
message_body = input("Enter the body of the message you want to send: ")

i = 0

time.sleep(2)

while i < int(message_limit):
    spam.typewrite(message_body)
    spam.press("Enter")
    i += 1
