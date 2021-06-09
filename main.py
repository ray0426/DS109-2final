import cProfile
import random
import queue
import math
from subMainFunc import subFunc
inf = math.inf




def covidSimulator(arg):
    
    peopleNum = arg['peopleNum']
    node_to_who = arg['node_to_who']
    initCovidNum = arg['initCovidNum']
    rapidTestLimit = arg['rapidTestLimit']
    p = arg['p']

    peopleNum = max(1000,peopleNum)
    everyMedPeoWorkLimit = 150
    dayTrack = 14
    day = 0
    dayToPeople1 = {}
    dayToPeople1[day] = {}
    people1 = {}  # 染疫人
    people2 = {}  # 完全健康人
    people3 = {}  # 排隊人
    people4 = {}  # 目前健康人(完全健康人+排隊人)
    people5 = {}  # 建立graph用
    graphDay = {}
    rapidTestLimit = 1000 if rapidTestLimit < 1000 else rapidTestLimit
    rapidTestLimit = int(peopleNum*0.02)*150 if rapidTestLimit > int(peopleNum*0.02)*150 else rapidTestLimit
    q = queue.Queue()
    for i in range(peopleNum):
        people2[i] = day
        people4[i] = day
    while True:
        who = random.randint(0,peopleNum-1)
        if people1.get(who) == None:
            dayToPeople1[day][who] = True
            people1[who] = day
            people2.pop(who,None)
            people4.pop(who,None)
        if len(people1.keys()) >= initCovidNum:
            break
    x,_ = zip(*people4.items())
    for i in range(peopleNum-initCovidNum):
        people5[i] = x
    rapidTestLimitTmp = rapidTestLimit
    while True:
        arg = {
            'day':day,
            'dayTrack':dayTrack,
            'peopleNum':peopleNum,
            'node_to_who':node_to_who,
            'rapidTestLimit':rapidTestLimit,
            'dayToPeople1':dayToPeople1,
            'people1':people1,
            'people3':people3,
            'people4':people4,
            'people5':people5,
            'q':q,
            'p':p,
            'graphDay':graphDay,
        }
        subFunc(arg)
        if q.qsize() <= 0:
            break
        if q.qsize() > peopleNum/20:
            rapidTestLimit = int(len(people4.keys())*0.002)*everyMedPeoWorkLimit
        else:
            rapidTestLimit = rapidTestLimitTmp
        x,_ = zip(*people4.items())
        people5 = {}
        for i in range(len(x)):
            people5[i] = x[i]
        deleteGraphDayTmp = max(-1,day-dayTrack-2)
        if deleteGraphDayTmp != -1:
            graphDay.pop(deleteGraphDayTmp,None)
        day += 1


if __name__ == '__main__':
    arg ={
        'peopleNum' : 100000 ,  # 總人口
        'node_to_who' : 20,  # 每人與人連結個數
        'initCovidNum' : 40 , # 起初感染源
        'rapidTestLimit' : 10000 , # 快篩最大量 
        'p' : 0.05 , # 確診陽性快篩機率
    }
    cProfile.run('covidSimulator( arg )')