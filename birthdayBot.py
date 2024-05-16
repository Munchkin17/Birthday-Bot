#get the current date
import datetime

#store the birthdates of my contacts
import json

from selenium import webdriver

#add a delay so that all elements of the webpage are loaded before processing
import time

#add emoji
import emoji

#global variable
eleNM = None

#this function is just to return a string of the message
def wish_birth(name):
    return "Happiest of Birthday's, may all your wishes and dreams come true. May you always be happy, healthy, wealthy, safe and surrounded by love" + print(emoji.emojize("smiling_face_with_3_hearts")) + name.spilt(" ")[0] + "!!";

#this function returns a list of values of some attributes based on the conditions on two attributes from the JSON file.
#use to return names of contacts having their birthday on the current date.
def getJsonData(file, atrr_ret, attr1, attr2, attr_val1, attr_val2):

    #load the file's data in 'data' variable
    data = json.load(file)
    retv = []
    
    #if the attributes value conditions are satisfied, append the name into the list to be returned.
    for i in data:
        if(i[attr1]== attr_val1 and i[attr2]== attr_val2):
            retv.append(i[atrr_ret])
    return retv

#opening the json file(birthdays.json) in read only mode
data_file = open("birthdays.json", "r")
namev =[]
print("Script Running")

#this will keep rerunning the part of the code from 'while True' to 'break'.
#use to keep waiting for the JSON function to return a non empty list.
#this function will keep rerunning at 11:59pm a day  before the birthday and break out at 12:00am.
while True:
    try:
        #get current date
        date = datetime.datetime.now()
        namev = getJsonData(data_file, "name", "birth_month", "birth_date", str(date.month), str(date.day))
        
    except json.decoder.JSONDecodeError:
        continue
    if(namev !=[]):
        break
    
#ChromeOptions allows us to use the userdata of chrome so that you don't have to sign in manually everytime
chropt = webdriver.ChromeOptions

#adding userdata argument to ChromeOptions object
chropt.add_argument("user-data-<LOCATION TO YOUR CHROME USER DATA>")

#creating a chrome webdriver object
driver = webdriver.Chrome(excutable_path="<c:\Users\Capaciti\Downloads\chromedriver_win32\chromedriver.exe>", options = chropt)
driver.get("https://web.whatsapp.com/")

#delay added to give time for all the elements to load
time.sleep(10)

print(namev)

#finds the chat of my contacts(as in the namev list)
for inp in namev:
    try:
        eleNM = driver.find_element_by_xpath('//span[@title ="{}"]'.format(inp))
    except Exception as ex:
            print(ex)
            continue
        
    #simulates a mouse click on the element
    eleNM.click()
    
    while(True):
        #finds the chat box element
        eleTF = driver.find_element_by_class_name("_13mgz")
        #writes the message - function to call wish_birth()
        eleTF.send_keys(wish_birth(inp))
        #finds the send button
        elseSND = driver.find_element_by_class("_3M-N-")
        #simulates a click on it
        elseSND.click()
        break
