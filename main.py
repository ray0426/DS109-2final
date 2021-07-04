from directGraph import DirectedGraph
from utilities import *
from utilities2 import *
from utilities1415 import *
import json
import pickle


def read(graph, filename='data.json'):
    with open(filename, 'r') as obj:
        data = json.load(obj)
    add_people(graph, data)

def read_relation(graph,filename ='relationship.json'):
    with open(filename, 'r') as obj:
        datas = json.load(obj)
    for data in datas:
        add_relation(graph, data['people'], {'distance': 0})
        if data['type'] != 'home':
            for key in data['people']:
                graph.set_vertex_specific_value(key, 'job', data['type'])
    print("read relation data complete!")

def show_personal_status(graph):
    print("please input people to show")
    print("format: [0, 2, 3, 5, 6]")
    keys = eval(input(""))
    print("print people status: ")
    fields = ['id', 'age', 'job', 'infected-time', 'infectable',"isolated-start","isolated-end"]
    for key in keys:
        print("name: " + str(graph._vertices_list[key].value['name']), end='')
        for f in fields:
            tmp = str(graph._vertices_list[key].value[f])
            tmp = tmp if len(tmp) != 0 else 'empty'
            print(", " + str(f) + ": " + \
                    tmp, end='')
        print()
    print("show personal status complete")

def show_who_infected(graph):
    print("print people who get infected: ")
    tmp = show_infected(graph,None)
    tmp = None if len(tmp) == 0 else tmp
    print(tmp)
    
def add_single_relation(graph):
    print("please input single relation")
    print("format: [3, 6, 7, 8], 0")
    relation = input("")
    add_relation(graph, eval(relation)[0], {'distance': eval(relation)[1]})
    print("add single relation complete!")

def add_infected(graph):
    print("please input infected people")
    print("format: [3, 5, 6, 7]")
    people = eval(input(""))
    print("please input infected time")
    print("format: 2021/6/7")
    infeced_time = input("")
    try:
        r = time.strptime(infeced_time,'%Y/%m/%d')
        infeced_time = time.strftime('%Y/%m/%d',r)
    except:
        print('Unsuccessful: wrong in time format!')
        int('wrong in key')
    insert_infected(graph, people, infeced_time)
    ans = []
    for x in people:
        while True:
            t = input('please input infectable time for {} (e g. 2021/6/6) = '.format(x)).lower().strip()
            try:
                r = time.strptime(t,'%Y/%m/%d')
                t = time.strftime('%Y/%m/%d',r)
                ans.append(t)
                break
            except:
                print('wrong in format {} you input for {}'.format(t,x))
    set_infectable(graph, people, ans)
    print("add infected people complete")

def add_tmp_relation_main(graph):
    print("please input relative people")
    print("format: [0, 2, 3, 5, 6]")
    relations = eval(input(""))
    print("please input relation time")
    print("format: 2021/6/7-15:30")
    relations_time = input("")
    add_tmp_relation(graph, relations, relations_time)
    print("add tmp relation complete")

def find_contacted_main(graph):
    print("please input people concerned")
    print("format: [0, 2, 3, 5, 6]")
    people = eval(input(""))
    print(find_contacted(graph, people))
    print("find contacted complete")

def find_by(graph):
    sss ='please input find by (name = n, job = j, age = a, gender = g, infected-time = i, infectable = o, isolated-start = s, isolated-end = e) = '
    c = input(sss).lower().strip()[0]
    d = {'n':'name','j':'job','a':'age','g':'gender','i':'infected-time','o':'infectable','s':'isolated-start','e':'isolated-end'}
    try:
        d[c]
    except:
        return
    try:
        value = input('input a value using to search data {} = '.format(d[c])).lower().strip()
        if c in ['s','e','o','i']:
            v = time.strptime(value,'%Y/%m/%d')
            value = time.strftime('%Y/%m/%d',v)
        print(graph.get_search_list(d[c],value))
    except:
        print('find nothing')

def save_data(graph):
    try:
        file = open(b"fileGraph.p","wb")
        pickle.dump(graph,file)
        print('save data successful!')
    except:
        print('save data -> exit(): unsuccessful')
def load_data():
    try:
        file = open("fileGraph.p",'rb')
        print('load data successful!')
        return pickle.load(file)
    except:
        print('load data -> exit(): unsuccessful')

def add_isolated_start_end():
    print("please input people you wanna change their isolated start or end")
    print("format: [3, 5, 6, 7]")
    people = eval(input(""))
    ans = {}
    print('time format you should type like this below')
    print("time format1: 2021/6/8-2021/6/19")
    print("time format2: 2021/6/8-?")
    for x in people:
        while True:
            print("please input time format for {}".format(x))
            times = input('')
            try:
                if len(times)- len(times.replace('-','')) != 1:
                    int('WroNg')
                else:
                    tmp = [x.strip() for x in times.split('-')]
                    r1 = time.strptime(tmp[0],'%Y/%m/%d')
                    t1 = time.strftime('%Y/%m/%d',r1)
                    try:
                        ans[t1][0].append(x)
                    except:
                        ans[t1] = [[x],[]]
                    if tmp[1].find('?') == -1:
                        r2 = time.strptime(tmp[1],'%Y/%m/%d')
                        t2 = time.strftime('%Y/%m/%d',r2)
                        try:
                            ans[t2][1].append(x)
                        except:
                            ans[t2] = [[],[x]]
                    break
            except:
                print('time format wrong for {} your input is {}'.format(x,times))        
    for x in ans:
        isolation(graph,ans[x][0],ans[x][1],x)
    print("add isolated time complete")


if __name__ == '__main__':
    print("start program")
    graph = DirectedGraph()
    while True:
        command = input("please input command: ").lower().strip()
        command = command.split(' ')
        tmp = []
        for x in command:
            if len(x) != 0:
                tmp.append(x)
        command = ' '.join(tmp)
        if command == 'exit' or command == 'r0':
            print("stop program")
            break
        print("command you input: " + command)
        if command == 'read by default' or  command == 'r1':
            read(graph)
            print("read people data complete!")
            read_relation(graph)
            continue
        if command == 'save' or  command == 'r+':
            save_data(graph)
            continue
        if command == 'load' or  command == 'r-':
            graph = load_data()
            continue
        elif command == 'read people'or  command == 'r2':
            try:
                filename = input("please input people file name: ")
                read(graph, filename)
                print("read people data complete!")
            except:
                print('read people -> exit(): wrong file name')
            continue
        elif command == 'read relation' or  command == 'r3':
            try:
                filename = input("please input people file name: ")
                read_relation(graph,filename)
            except:
                print('read relation -> exit(): wrong file name')
            continue
        elif command == 'show status' or  command == 'r4':
            show_vertex_status(graph, 0, 10000, False)
            continue
        elif command == 'show personal status' or  command == 'r5':
            try:
                show_personal_status(graph)
            except:
                print('show personal status -> exit() : wrong in key')
            continue
        elif command == 'show who infected' or  command == 'r6' :
            show_who_infected(graph)
            continue
        elif command == 'add single relation' or  command == 'r7' :
            try:
                add_single_relation(graph)
            except:
                print('add single relation -> exit()')
            continue
        elif command == 'add infected' or  command == 'r8':
            try:
                add_infected(graph)
            except:
                print('add infected -> exit()')            
            continue
        elif command == 'add isolated time' or  command == 'r9':
            try:
                add_isolated_start_end()
            except:
                print('add isolated time -> exit()')            
            continue
        elif command == 'add tmp relation' or  command == 'r10':
            try:
                add_tmp_relation_main(graph)
            except:
                print('add tmp relation -> exit()')
            continue
        elif command == 'find contacted' or  command == 'r11':
            try:
                find_contacted_main(graph)
            except:
                print('find contacted -> exit()')
            continue
        elif command == 'find people by' or  command == 'r12':
            try:
                find_by(graph)
            except:
                print('find people by -> exit()')
            continue
        else:
            print("invalid command")

