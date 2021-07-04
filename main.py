from directGraph import DirectedGraph
from utilities import *
from utilities2 import *
from utilities1415 import *
import time
import json

def read(graph, filename):
    with open(filename, 'r') as obj:
        data = json.load(obj)
    add_people(graph, data)

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
    insert_infected(graph, people, infeced_time)
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
    print("find contacted conplete")

if __name__ == '__main__':
    print("start program")
    graph = DirectedGraph()
    while True:
        command = input("please input command: ")
        if command == 'exit':
            print("stop program")
            break
        print("command you input: " + command)
        if command == 'read people':
            filename = input("please input people file name: ")
            read(graph, filename)
            print("read people data complete!")
        elif command == 'show status':
            show_vertex_status(graph, 0, 10000, False)
        elif command == 'add single relation':
            add_single_relation(graph)
        elif command == 'add infected':
            add_infected(graph)
        elif command == 'add tmp relation':
            add_tmp_relation_main(graph)
        elif command == 'find contacted':
            find_contacted_main(graph)
        else:
            print("invalid command")

