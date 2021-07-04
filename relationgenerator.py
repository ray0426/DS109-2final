import json
from random import randint, sample
def relation_generator():

    with open('data.json', 'r') as obj:
        data = json.load(obj)
    num = len(data)
    people_n_pa = [0.1322,0.1594,0.2113,0.2259,0.1289,0.1423]
    jobtype = 50
    joblimit = 5
    ans = []
    people_n_num = [int(num*people_n_pa[i]) for i in range(6)]
    for i in range(1,6):
        if people_n_num[i] % (i+1) != 0:
            people_n_num[i] += i+1 - people_n_num[i] % (i+1)
        if i == 5:
            people_n_num[0] = num - sum(people_n_num[1:])
    house_n_num = [int(people_n_num[i]/(i+1)) for i in range(6)]
    if num != sum(people_n_num):
        raise 'Wrong: in relation_Generator people_n_num'
    people_lst = {}
    for i in range(num):
        people_lst[i] = True
    ans1 = [[] for i in range(6)]
    for i in range(5,0,-1):  
        for j in range(house_n_num[i]):
            tmp = sample(list(people_lst), i+1)
            ans1[i].append(tmp)
            for k in tmp:
                people_lst.pop(k,None)
    for x in ans1[1:]:
        for y in x:
            ans.append({'people':y,'type':'home'})
    ans1[0] = [[x] for x in list(people_lst)]
    jobnum = [(house_n_num[i]) * (i-1) for i in range(6)]
    jobnum[0], jobnum[1] =  people_n_num[0], people_n_num[1]
    jobnum = sum(jobnum)
    tmp = [jobnum//jobtype, jobnum-(jobtype-1)*(jobnum//jobtype)]
    job_num_lst = [tmp[0] if i != 0 else tmp[1] for i in range(jobtype)]
    tmp = {i:1 for i in range(jobtype)}
    for i in range(jobtype//2):
        x = sample(list(tmp),2)
        for y in x:
            tmp.pop(y,None)
        k = int(job_num_lst[x[0]] * (randint(30,70)/100))
        k = min(k,job_num_lst[x[0]])
        job_num_lst[x[0]] -= k
        job_num_lst[x[1]] += k
    if sum(job_num_lst) != jobnum:
        raise 'Wrong: in relation_Generator jobnum'
    job_work_people_lst = [[] for i in range(jobtype)]
    job_work_num_lst = [[] for i in range(jobtype)]
    for i, x in enumerate(job_num_lst):
        while True:
            if x > joblimit*2-1:
                job_work_num_lst[i].append(joblimit)
                x -= joblimit
            else:
                job_work_num_lst[i].append(x)
                break
    jobkind_num = sum([len(x) for x in job_work_num_lst])
    tmp = {}
    idx = 0
    for i,x in enumerate(job_work_num_lst):
        for j,y in enumerate(x):
            job_work_people_lst[i].append([])
            tmp[idx] = {'num':y,'where':(i,j)}
            idx += 1
    ##　count = 0
    for x in ans1:
        for y in x:
            t = y[2:] if len(y) > 2 else y
            for z in t:
                ## count += 1
                i = sample(list(tmp),1)[0]
                where = tmp[i]['where']
                job_work_people_lst[where[0]][where[1]].append(z)
                tmp[i]['num'] -= 1
                if tmp[i]['num'] == 0:
                    tmp.pop(i,None)
    ## print(count,jobnum, len(tmp)==0)
    ## print(sum([len(job_work_people_lst[i]) for i in range(jobtype) ] ), jobkind_num )

    for i,x in enumerate(job_work_people_lst):
        for j,y in enumerate(x):
            type_string = 'job{}'.format(i)
            ans.append({'people':y,'type':type_string})
    with open('relationship.json', 'w') as obj:
        json.dump(ans, obj)