from flask import Flask, jsonify, make_response
import flask_cors
from flask_restful import Api, Resource, reqparse
import requests
from bs4 import BeautifulSoup


days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']
times = ['08:00-09:35', '09:45-11:20', '12:10-13:45',
         '13:55-15:30', '16:10-17:45', '17:55-19:30']
pos = []
week = 23
PonTable = []
VtorTable = []
SrTable = []
ChetTable = []
PytTable = []
SybTable = []
r = requests.Response
bs = BeautifulSoup()
app = Flask(__name__)
api = Api(app)
flask_cors.CORS(app)


with app.app_context():
    def getweek():
        global week, r, bs
        r = requests.get("https://isu.ugatu.su/api/new_schedule_api", params={
            'schedule_semestr_id': '222', 'WhatShow': '1', 'weeks': '0', 'student_group_id': '1531'})
        bs = BeautifulSoup(r.text, "lxml")
        weekk = bs.find('p')
        week = weekk.text[-2:]

    def gettable():
        table = []
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
                    PonTable.append({'time': Pon[_], 'pred': Pon[_+2]})
        for _ in range(len(Vtor)):
            if Vtor[_] in times and Vtor[_+1] != 'Нет информации':
                if week in Vtor[_+1]:
                    VtorTable.append({'time': Vtor[_], 'pred': Vtor[_+2]})
        for _ in range(len(Sr)):
            if Sr[_] in times and Sr[_+1] != 'Нет информации':
                if week in Sr[_+1]:
                    SrTable.append({'time': Sr[_], 'pred': Sr[_+2]})
        for _ in range(len(Chet)):
            if Chet[_] in times and Chet[_+1] != 'Нет информации':
                if week in Chet[_+1]:
                    ChetTable.append({'time': Chet[_], 'pred': Chet[_+2]})
        for _ in range(len(Pyt)):
            if Pyt[_] in times and Pyt[_+1] != 'Нет информации':
                if week in Pyt[_+1]:
                    PytTable.append({'time': Pyt[_], 'pred': Pyt[_+2]})
        for _ in range(len(Syb)):
            if Syb[_] in times and Syb[_+1] != 'Нет информации':
                if week in Syb[_+1]:
                    SybTable.append({'time': Syb[_], 'pred': Syb[_+2]})
        return PonTable, VtorTable, SrTable, ChetTable, PytTable, SybTable


class Table(Resource):
    def get(self):
        PonTable, VtorTable, SrTable, ChetTable, PytTable, SybTable = gettable()
        tablezz = [
            {'id': 1, 'days': days[0], 'table': PonTable},
            {'id': 2, 'days': days[1], 'table': VtorTable},
            {'id': 3, 'days': days[2], 'table': SrTable},
            {'id': 4, 'days': days[3], 'table': ChetTable},
            {'id': 5, 'days': days[4], 'table': PytTable},
            {'id': 6, 'days': days[5], 'table': SybTable},
            #{'id': 7, 'days': 'Воскресение', 'table': []},
        ]
        return jsonify(tablezz)
    # Enable Access-Control-Allow-Origin


class Weeks(Resource):
    def get(self):
        getweek()
        return jsonify({'week': week})


api.add_resource(Table, "/table", "/table/", "/table/<int:week>")
api.add_resource(Weeks, "/week", "/week/")
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
