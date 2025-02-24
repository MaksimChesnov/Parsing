import requests as req
import os
import fake_useragent as fu

#Подключение к сайту с музыкой

#Создаем заголовок будто это не парсинг, а реальный пользователь зашел на сайт
headers = {'UserAgent': fu.UserAgent().chrome}
url = 'https://rus.hitmotop.com'
res = req.request("GET", url, headers=headers)

print(res.status_code)

if res.status_code == 200:
    print('Подключение успешно, ', res.status_code)
    site_txt = res.text
    find_link = 'https://'
    find_mus_file = '.mp3'

    #Разбиваем полученный текст сайта на элементы списка
    spl_site_txt = site_txt.split()

    #Заполняем новый список элементами, которые содержат ссылку и музыкальный файл
    links = []
    for i in spl_site_txt:
        if find_link in i:
            if find_mus_file in i:
                links.append(i)

    print (links)

    #У нас есть список ссылок. Идем по ним и выкачиваем файлы
    ind = 0
    for i in links[0:10]:
        #Убираем href= из ссылки
        link = links[ind].replace('href=', '')
        #Убираем двойные кавычки
        link = link.replace('"', '')
        
        ind = ind + 1
        #Берем чистую ссылку
        req_link = req.get(link)
        dirname, filename = os.path.split(link)
        out = open(filename, 'wb')
        out.write(req_link.content)
        out.close()
        print (req_link.status_code, ',', link)
                
else:
    print('Не получилось подключиться, код ошибки = ', res.status_code) 
