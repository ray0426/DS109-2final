from directedgraph import DirectedGraph
import random
import queue
import math
inf = math.inf
'''
    # dayToPeople1      # 用來追蹤每天確診名單 用於 復原(?) 死亡(?)
    # graphDay          # 用來追蹤足跡 會記錄連續14天
    # people1           # 染疫人名單 (key to day)
    # people2           # 完全健康人 (key to day)
    # people3           # 排隊人 (key to day)
    # people4           # 目前健康人(完全健康人+排隊人) (key to day)
    # people5           # 編號 to 完全健康人idx or 目前健康人idx (用於新增圖的線段)
    # node_to_who       # 每天每人會接觸到的人數
    # p                 # 快篩陽性機率
    # q                 # 快篩排隊用
    # rapidTestLimit    # 快篩每日最高數量
    # peopleNum         # 總人口
    # day               # 每天
'''
def subFunc(arg): # one level ver. (Hashmap) 
    day = arg['day']
    dayTrack = arg['dayTrack']
    peopleNum = arg['peopleNum']
    node_to_who = arg['node_to_who']
    rapidTestLimit = arg['rapidTestLimit']
    dayToPeople1 = arg['dayToPeople1']
    people1 = arg['people1']
    people3 = arg['people3']
    people4 = arg['people4']
    people5 = arg['people5']
    q = arg['q']
    graphDay = arg['graphDay']
    # initialize
    dayToPeople1[day] = {}
    if day != 0:
        node_to_who = node_to_who if len(dayToPeople1[day-1].keys()) <= peopleNum*0.002 else min(10,node_to_who)  # 昨天單日確診數大於 0.2%人口 (10p以下)
        node_to_who = node_to_who if node_to_who <= ( peopleNum - len(people1.keys()) )  else max(0,int(node_to_who/2))  # 極度恐懼(0p~5p)
    else:
        node_to_who = node_to_who if node_to_who <= ( peopleNum - len(people1.keys()) )  else ( peopleNum - len(people1.keys()) ) # 防呆
    node_to_who = int(2e7/peopleNum) if peopleNum * node_to_who > 2e7 else node_to_who  
    p = 0.05
    # make the graph
    G = DirectedGraph()
    if day == 0:
        for i in range(peopleNum):
            G.addNode(i)
    else:
        for i in people5.keys():
            G.addNode(people5[i])
    graphNodeNum = G.getNodeNumber()
    if node_to_who != 0:
        for node in G.getAllNodes():
            app = {}
            while True:
                if day == 0:
                    tmp = random.randint(0,graphNodeNum-1)
                else:
                    tmp = people5[random.randint(0,graphNodeNum-1)]
                if tmp != node:
                    app[tmp] = True
                if len(app.keys()) >= node_to_who:
                    break
            for x in app.keys():
                G.addEdge(node,x)
    graphDay[day] = G
    print(G)
    startNode = None
    first = False
    if day == 0:
        first = True
        startNode = []
        for x in people1.keys():
            startNode.append(x)
    # infect
    countRapidTest = 0
    while True:
        while True:
            if first:
                first = False
                break
            startNode = None
            if q.qsize() != 0:
                next = q.get()
                timeDelta = people3[next] - day
                people3.pop(next,None)
                countRapidTest += 1
                if p >= random.random():  # prob
                    if people1.get(next) == None:  # 確診
                        people1[next] = day
                        dayToPeople1[day][next] = True
                        people4.pop(next,None)
                        startNode = next
                        break
                if countRapidTest >= rapidTestLimit:
                    break
            else:
                break
        if startNode == None:
            break
        if type(startNode) == list and day == 0:
            for x in startNode:
                for y in G.getNodeOutNeighbors(x):
                    if people1.get(y) == None and people3.get(y) == None:
                        q.put(y)
                        people3[y] = day
        else:
            initDay = max(0,day-dayTrack-1)
            for i in range(initDay,day+1):
                tmpG = graphDay[i]
                for y in tmpG.getNodeOutNeighbors(startNode):
                    if people1.get(y) == None and people3.get(y) == None:
                        q.put(y)
                        people3[y] = day

    
    dayStr = str(day+1)
    if day%10 == 0:
        dayStr += 'st'
    elif day%10 == 1:
        dayStr += 'nd'
    elif day%10 == 2:
        dayStr += 'rd'
    else:
        dayStr += 'th'
    print('{} Day_report:  Total_People+:{}p (Day_People+:{}p)  Waitqueue:{}p  NodeEffect:{}p\n'.format(dayStr,len(people1.keys()),len(dayToPeople1[day].keys()),q.qsize(),node_to_who) )