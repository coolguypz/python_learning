from datetime import datetime
from sqlite3 import Date
from xmlrpc.client import DateTime


journal = input("please enter your journal : ")
date = datetime.today().date()
print("your journal is : ", journal + "\nyour journal date is  : ", date )


