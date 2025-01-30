import requests as req 
import selenium as sel
import fake_useragent as fu
#from requests import *

url = 'https://proza.ru/login/'
print(url)
login = input('Введите логин: ')
password = input('Введите пароль: ')
log_pass ={'login': login, 'password': password}
files=[]
headers = {'UserAgent': fu.UserAgent().chrome}
print (headers)

response = req.request("POST", url, headers=headers, data=log_pass, files=files)
print(response.status_code)

url2 = 'https://proza.ru/avtor/macson'
res = req.request("GET", url2, headers=headers)
print (res.text)