import json

if __name__ == '__main__':
    n = 10
    result = []
    for i in range(n):
        result.append({
            'name': 'name' + str(i),
            'id': 'id' + str(i),
            'age': 'age' + str(i),
            'birth': 'birth' + str(i),
            'die': 'birth' + str(i),
            'gender': 'gender' + str(i),
            'address': 'add' + str(i),
            'phone': 'phone' + str(i),
            'infected-time': '',
            'isolated-start': '',
            'isolated-end': ''
            })
    #print(result)
    #print(json.dumps(result))
    with open('data.json', 'w') as obj:
        json.dump(result, obj)
