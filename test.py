import requests
from bs4 import BeautifulSoup

r = requests.get("https://isu.ugatu.su/api/new_schedule_api", params={
    'schedule_semestr_id': '222', 'WhatShow': '1', 'student_group_id': '1531'})
bs = BeautifulSoup(r.text, "lxml")
days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']
times = ['08:00-09:35', '09:45-11:20', '12:10-13:45',
         '13:55-15:30', '16:10-17:45', '17:55-19:30']
pos = []
Pon = []
Vtor = []
Sr = []
Chet = []
Pyt = []
Syb = []
PonTable = []
VtorTable = []
SrTable = []
ChetTable = []
PytTable = []
SybTable = []
table = []
week = '23'
PonTable = []
f = bs.findAll('tr')
for i in f:
    e = i.findAll('p')
    for _ in e:
        table.append(_.text)
table = table[8:]
for _ in range(len(table)):
    if table[_] == days[0]:
        pos.append(_)
    if table[_] == days[1]:
        pos.append(_)
    if table[_] == days[2]:
        pos.append(_)
    if table[_] == days[3]:
        pos.append(_)
    if table[_] == days[4]:
        pos.append(_)
    if table[_] == days[5]:
        pos.append(_)
for _ in range(pos[0]+1, pos[1]):
    Pon.append(table[_])
for _ in range(pos[1]+1, pos[2]):
    Vtor.append(table[_])
for _ in range(pos[2]+1, pos[3]):
    Sr.append(table[_])
for _ in range(pos[3]+1, pos[4]):
    Chet.append(table[_])
for _ in range(pos[4]+1, pos[5]):
    Pyt.append(table[_])
for _ in range(pos[5]+1, len(table)):
    Syb.append(table[_])

for _ in range(len(Pon)):
    if Pon[_] in times and Pon[_+1] != 'Нет информации':
        if week in Pon[_+1]:
            PonTable.append(Pon[_])
            PonTable.append(Pon[_+2])
for _ in range(len(Vtor)):
    if Vtor[_] in times and Vtor[_+1] != 'Нет информации':
        if week in Vtor[_+1]:
            VtorTable.append(Vtor[_])
            VtorTable.append(Vtor[_+2])
for _ in range(len(Sr)):
    if Sr[_] in times and Sr[_+1] != 'Нет информации':
        if week in Sr[_+1]:
            SrTable.append(Sr[_])
            SrTable.append(Sr[_+2])
for _ in range(len(Chet)):
    if Chet[_] in times and Chet[_+1] != 'Нет информации':
        if week in Chet[_+1]:
            ChetTable.append(Chet[_])
            ChetTable.append(Chet[_+2])
for _ in range(len(Pyt)):
    if Pyt[_] in times and Pyt[_+1] != 'Нет информации':
        if week in Pyt[_+1]:
            PytTable.append(Pyt[_])
            PytTable.append(Pyt[_+2])
for _ in range(len(Syb)):
    if Syb[_] in times and Syb[_+1] != 'Нет информации':
        if week in Syb[_+1]:
            SybTable.append(Syb[_])
            SybTable.append(Syb[_+2])

print(PonTable, VtorTable, SrTable, ChetTable, PytTable, SybTable)
