# -*- coding: utf-8 -*-
from pprint import pprint
import time
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
############
def variables(date):
    for key, value in date.items():
        globals()[key] = value
#################
        
#################
# Указываем creds.json
CREDENTIALS_FILE = 'creds.json'
# Указываем ID гугл таблиц(https://docs.google.com/spreadsheets/d/ тут ID /edit#gid=1351249603)
pupils_spreadsheet_id = '11bQdaDpiSHQAlqa3r1iPHo1c6M4wkoHdgDJCVsArogQ'
teachers_spreadsheet_id = '1siKb0UjHmorKdws_RVxzy90j4Y06SRosbXX3zO3ss6g'
rooms_spreadsheet_id = '1PPhT_3HKA2bKuCVo_qGYp6WlD1OqbGtnyBjKhHQA5ME'

# Подключаем API
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)
'''
# Считываем данные
values = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id,
    range='A1:E10',
    majorDimension='COLUMNS'
).execute()
pprint(values)

# Вводим данные
values = service.spreadsheets().values().batchUpdate(
    spreadsheetId=spreadsheet_id,
    body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "B3:C4",
             "majorDimension": "ROWS",
             "values": [["This is B3", "This is C3"], ["This is B4", "This is C4"]]},
            {"range": "D5:E6",
             "majorDimension": "COLUMNS",
             "values": [["This is D5", "This is D6"], ["This is E5", "=5+5"]]}
        ]
    }
).execute()
'''
################
rut={}
################
#Вот тут наброски кода
class pupil: #создаем класс ученик
    def __init__(self, name, learningvar, dimention):
        name = name
        learningvar = learningvar
        dimention = dimention


class teacher: #создаем класс учитель
    def __init__(self, number, name, discipline, programs, programspriority, workgrafic, quartergrafic):
        
        number = number
        name = name
        discipline = discipline
        programs = programs
        programspriority = programspriority
        workgrafic = workgrafic
        quartergrafic = quartergrafic


class room:
    def __init__(self, name, space, purpose, config, priority, cando):

        name = name
        space = space
        purpose = purpose
        config = config
        priority = priority
        cando = cando

        
###############
t=2
m = 0
n = ''
p = ''
o = ''
while True: #Перебираем учеников
    global m
    m +=1
    name = str(service.spreadsheets().values().get( #Смотрим содержимое
            spreadsheetId=pupils_spreadsheet_id,
            range=str('B'+str(t)),
            ).execute())
    
    
    
    #Убираем лишнее
    name = list(name) # конвертируем в список
    l=0
    for i in range(1):
        while name[l] != '[':
                name[l] = ""
                l+=1
                if l==len(name):
                    break
        if l==len(name):
            break
        for i in range(3):
            name[l] = ""
            l=l+1
        while name[l] != ']':
            l=l+1
        name[l-1] = ""
        name[l] = ""
        for i in range(2):
            l+=1
            name[l] = ""
    name = "".join(name) # соединяем в строку
    print(name)
    global n 
    n = name
    if name == '': #Проверяем содержимое на наличие
        
        break
    
    
########################
    learningvar = str(service.spreadsheets().values().get( #Смотрим содержимое
            spreadsheetId=pupils_spreadsheet_id,
            range=str('E'+str(t)),
            ).execute())
    
    
    #Убираем лишнее
    learningvar = list(learningvar) # конвертируем в список
    l=0
    while learningvar[l] != '[':
            learningvar[l] = ""
            l=l+1
    for i in range(3):
        learningvar[l] = ""
        l=l+1
    while learningvar[l] != ']':
        l=l+1
    learningvar[l-1] = ""
    learningvar[l] = ""
    for i in range(2):
        l=l+1
        learningvar[l] = ""
    learningvar = "".join(learningvar) # соединяем в строку и возвращаем результат в место вызова
    
    print(learningvar)
    global o
    o = learningvar
    
    
############################
    dimention = str(service.spreadsheets().values().get(
            spreadsheetId=pupils_spreadsheet_id,
            range=str('F'+str(t)),
            ).execute())
    #Убираем лишнее
    dimention = list(dimention) # конвертируем в список
    l=0
    while dimention[l] != '[':
            dimention[l] = ""
            l+=1
    for i in range(3):
        dimention[l] = ""
        l+=1
    while dimention[l] != ']':
        l+=1
    dimention[l-1] = ""
    dimention[l] = ""
    for i in range(2):
        l+=1
        dimention[l] = ""
    dimention = "".join(dimention) # соединяем в строку и возвращ    аем результат в место вызова
    global p
    p = dimention
    print(dimention)
#######################
    time.sleep(5)
    t+=1
rut[m]=[name, learningvar, dimention]
t=2
##########################
print(rut)
while True: #Перебираем учителей
    number = str(service.spreadsheets().values().get( #Смотрим содержимое номера
            spreadsheetId=teachers_spreadsheet_id,
            range=str('A'+str(t)),
         ).execute())
    
    #Убираем лишнее
    number = list(number) # конвертируем в список
    l=0
    for i in range(1):
        while number[l] != '[':
                number[l] = ""
                l+=1
                if l==len(number):
                    break
        if l==len(number):
            break
        for i in range(3):
            number[l] = ""
            l=l+1
        while number[l] != ']':
            l=l+1
        number[l-1] = ""
        number[l] = ""
        for i in range(2):
            l+=1
            number[l] = ""
    number = "".join(number) # соединяем в строку
    print(number)
    
    if number == '': #Проверяем содержимое на наличие
        
        break
    ####################
    name = str(service.spreadsheets().values().get( #Смотрим содержимое имени
            spreadsheetId=teachers_spreadsheet_id,
            range=str('B'+str(t)),
            ).execute())
    
    #Убираем лишнее
    name = list(name) # конвертируем в список
    l=0
    while name[l] != '[':
            name[l] = ""
            l=l+1
    for i in range(3):
        name[l] = ""
        l=l+1
    while name[l] != ']':
        l=l+1
    name[l-1] = ""
    name[l] = ""
    for i in range(2):
        l=l+1
        name[l] = ""
    name = "".join(name) # соединяем в строку    

    print(name)    
    ##########################
    discipline = str(service.spreadsheets().values().get( #Смотрим содержимое
            spreadsheetId=teachers_spreadsheet_id,
            range=str('C'+str(t)),
            ).execute())
    
    
    #Убираем лишнее
    discipline = list(discipline) # конвертируем в список
    l=0
    while discipline[l] != '[':
            discipline[l] = ""
            l=l+1
    for i in range(3):
        discipline[l] = ""
        l=l+1
    while discipline[l] != ']':
        l=l+1
    discipline[l-1] = ""
    discipline[l] = ""
    for i in range(2):
        l=l+1
        discipline[l] = ""
    discipline = "".join(discipline) # соединяем в строку и возвращаем результат в место вызова
    
    print(discipline)
########################
    programs = str(service.spreadsheets().values().get(
            spreadsheetId=teachers_spreadsheet_id,
            range=str('D'+str(t)),
            ).execute())
    #Убираем лишнее
    programs = list(programs) # конвертируем в список
    l=0
    while programs[l] != '[':
            programs[l] = ""
            l=l+1
    for i in range(3):
        programs[l] = ""
        l=l+1
    while programs[l] != ']':
        l=l+1
    programs[l-1] = ""
    programs[l] = ""
    for i in range(2):
        l=l+1
        programs[l] = ""
    programs = "".join(programs) # соединяем в строку
    
    print(programs)
##############
    programspriority = str(service.spreadsheets().values().get(
            spreadsheetId=teachers_spreadsheet_id,
            range=str('E'+str(t)),
            ).execute())
    #Убираем лишнее
    programspriority = list(programspriority) # конвертируем в список
    l=0
    while programspriority[l] != '[':
            programspriority[l] = ""
            l=l+1
    for i in range(3):
        programspriority[l] = ""
        l=l+1
    while programspriority[l] != ']':
        l=l+1
    programspriority[l-1] = ""
    programspriority[l] = ""
    for i in range(2):
        l=l+1
        programspriority[l] = ""
    programspriority = "".join(programspriority) # соединяем в строку
    
    print(programspriority)
    ###############
    workgrafic = str(service.spreadsheets().values().get(
            spreadsheetId=teachers_spreadsheet_id,
            range=str('F'+str(t)),
            ).execute())
    #Убираем лишнее
    workgrafic = list(workgrafic) # конвертируем в список
    l=0
    while workgrafic[l] != '[':
            workgrafic[l] = ""
            l=l+1
    for i in range(3):
        workgrafic[l] = ""
        l=l+1
    while workgrafic[l] != ']':
        l=l+1
    workgrafic[l-1] = ""
    workgrafic[l] = ""
    for i in range(2):
        l=l+1
        workgrafic[l] = ""
    workgrafic = "".join(workgrafic) # соединяем в строку
    
    print(workgrafic)
#############
    quartergrafic = str(service.spreadsheets().values().get(
            spreadsheetId=teachers_spreadsheet_id,
            range=str('G'+str(t)),
            ).execute())
    #Убираем лишнее
    quartergrafic = list(quartergrafic) # конвертируем в список
    l=0
    while quartergrafic[l] != '[':
            quartergrafic[l] = ""
            l=l+1
    for i in range(3):
        quartergrafic[l] = ""
        l=l+1
    while quartergrafic[l] != ']':
        l=l+1
    quartergrafic[l-1] = ""
    quartergrafic[l] = ""
    for i in range(2):
        l=l+1
        quartergrafic[l] = ""
    quartergrafic = "".join(quartergrafic) # соединяем в строку
    
    print(quartergrafic)
##############
    time.sleep(5)
    t+=1
t=2
###########
while True:#перебираем комнаты
    name = str(service.spreadsheets().values().get( #Смотрим содержимое номера
            spreadsheetId=rooms_spreadsheet_id,
            range=str('A'+str(t)),
         ).execute())
    
    #Убираем лишнее
    name = list(name) # конвертируем в список
    l=0
    for i in range(1):
        while name[l] != '[':
                name[l] = ""
                l+=1
                if l==len(name):
                    break
        if l==len(name):
            break
        for i in range(3):
            name[l] = ""
            l=l+1
        while name[l] != ']':
            l=l+1
        name[l-1] = ""
        name[l] = ""
        for i in range(2):
            l+=1
            name[l] = ""
    name = "".join(name) # соединяем в строку
    print(name)
    if name == '': #Проверяем содержимое на наличие
        
        break
    ##############
    space = str(service.spreadsheets().values().get(
            spreadsheetId=rooms_spreadsheet_id,
            range=str('B'+str(t)),
            ).execute())
    #Убираем лишнее
    space = list(space) # конвертируем в список
    l=0
    while space[l] != '[':
            space[l] = ""
            l=l+1
    for i in range(3):
        space[l] = ""
        l=l+1
    while space[l] != ']':
        l=l+1
    space[l-1] = ""
    space[l] = ""
    for i in range(2):
        l=l+1
        space[l] = ""
    space = "".join(space) # соединяем в строку
    
    print(space)
##############
    purpose = str(service.spreadsheets().values().get(
            spreadsheetId=rooms_spreadsheet_id,
            range=str('C'+str(t)),
            ).execute())
    #Убираем лишнее
    purpose = list(purpose) # конвертируем в список
    l=0
    while purpose[l] != '[':
            purpose[l] = ""
            l=l+1
    for i in range(3):
        purpose[l] = ""
        l=l+1
    while purpose[l] != ']':
        l=l+1
    purpose[l-1] = ""
    purpose[l] = ""
    for i in range(2):
        l=l+1
        purpose[l] = ""
    purpose = "".join(purpose) # соединяем в строку
    
    print(purpose)
##############
    config = str(service.spreadsheets().values().get(
            spreadsheetId=rooms_spreadsheet_id,
            range=str('D'+str(t)),
            ).execute())
    #Убираем лишнее
    config = list(config) # конвертируем в список
    l=0
    while config[l] != '[':
            config[l] = ""
            l=l+1
    for i in range(3):
        config[l] = ""
        l=l+1
    while config[l] != ']':
        l=l+1
    config[l-1] = ""
    config[l] = ""
    for i in range(2):
        l=l+1
        config[l] = ""
    config = "".join(config) # соединяем в строку
    
    print(config)
##############
    priority = str(service.spreadsheets().values().get(
            spreadsheetId=rooms_spreadsheet_id,
            range=str('E'+str(t)),
            ).execute())
    #Убираем лишнее
    priority = list(priority) # конвертируем в список
    l=0
    while priority[l] != '[':
            priority[l] = ""
            l=l+1
    for i in range(3):
        priority[l] = ""
        l=l+1
    while priority[l] != ']':
        l=l+1
    priority[l-1] = ""
    priority[l] = ""
    for i in range(2):
        l=l+1
        priority[l] = ""
    priority = "".join(priority) # соединяем в строку
    
    print(priority)
##############
    cando = str(service.spreadsheets().values().get(
            spreadsheetId=rooms_spreadsheet_id,
            range=str('F'+str(t)),
            ).execute())
    #Убираем лишнее
    cando = list(cando) # конвертируем в список
    l=0
    while cando[l] != '[':
            cando[l] = ""
            l=l+1
    for i in range(3):
        cando[l] = ""
        l=l+1
    while cando[l] != ']':
        l=l+1
    cando[l-1] = ""
    cando[l] = ""
    for i in range(2):
        l=l+1
        cando[l] = ""
    cando = "".join(cando) # соединяем в строку
    
    print(cando)
    #################
    t+=1
t = 2
