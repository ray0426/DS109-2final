# Readme
### 安裝與執行

1. 套件
    皆為內建module(pickle, json, time)
    
2. 執行環境
    windows10, mac mojave 10.14.6, Ubuntu 18.04.5 LTS
    python版本 3.8.3, 3.6.9
    
3. Clone repository
```
    $ git clone https://github.com/ray0426/DS109-2final.git
```

4. 切換到該目錄下, 執行main (今天限定 python 3.6 以上)
```
    $ python3 main.py
```

5. `python3 main.py`後的各種指令
    1. `exit` or `r0`  :  stop program
    2. `read by default` or `r1`  :  直接用我們的測試資料
    3. `save` or `r+`  :  儲存工作中的graph
    4. `load` or `r-`  :  讀取graph
    5. `read people` or `r2`  :  使用測試資料人自己的個資(手動輸入)
    6. `read relation` or `r3`  :  使用測試資料人與人關係(手動輸入)
    7. `show status` or `r4`  :  顯示目前圖
    8. `show personal status` or `r5`  :  顯示選定keys的個資
    9. `show who infected` or `r6`  :  顯示感染者的keys
    10. `add single relation` or `r7`  :  新增人與人的關係
    11. `add infected` or `r8`  :  新增感染者 和 infectable time
    12. `add isolated time` or `r9` :  新增隔離時間戳記
    13. `add tmp relation` or `r10`  :  新增臨時關係
    14. `find contacted` or `r11`  :  得到感染者接觸對象
    15. `find people by` or `r12`  :  用特定的key搜尋到對應的人的keys

6. 各指令功能
* (command: `read`)新增個人資料： 
可以記錄個人的姓名、身分證字號、生日、年齡、性別、住址、電話、工作。如下圖所示。
![](https://i.imgur.com/n8BAIl7.png)

* (command: `read relation`, `add single relation`)
新增「常駐人際關係」及「臨時人際關係」資料：
可以讀整個json檔大量輸入，也可以一個一個單獨建立。人與人會有「常駐人際關係」以及「臨時人際關係」即是 Graph 中的 Edge，例如該圖女子會有與家人的常駐關係以及今日去超市買菜所建立的人際臨時關係，如下圖若該名女子有任何異變, 可進行對其他人的通知跟抓捕
![](https://i.imgur.com/xg8dlmd.png)

* (command: `save`)存檔：
儲存目前的graph
    
* (command: `load`)讀檔：
當上次離開程式前有預先存檔時，下次再進入的話可以讀上次的檔。

* (command: `show personal status`)顯示個人狀態：
輸入一串要查詢的人的index，會顯示出這些人的個人資料如：姓名、身份證字號、年齡、職業、確診時間、發病時間、開始隔離時間、結束隔離時間

* (command: `show who infected`)顯示感染者：
顯示所有感染者的index。

* (command: `add infected`)新增確診者：
當確診者出現時，可以在確診者的個人資料中註記確診時間(infected-time)及發病時間(infectable)

* (command: `add tmp relation_main`)新增「臨時人際關係」：
「臨時人際關係」是指在不特定場所和時間下遇到的人，因此會連同接觸時間及接觸對象一起儲存。

* (command: `find contacted`)尋找接觸者：
輸入一串人的index，若此人為確診者，則尋找所有在發病時間後與確診者接觸過的人的index。

* (command: `find by`)從某個項目尋找人：
可以選擇要找的項目有：名字、工作、年齡、性別、確診時間、發病時間、開始隔離時間、結束隔離時間。然後輸入想要的特徵，可以得到一串符合這個特徵的人的index。

* (command: `add isolated time`)記錄隔離者：
記錄隔離者的開始被隔離的時間和結束隔離的時間

* (command: `find n people needed`)尋找前n個需要被隔離的人：
輸入一個數字n，得到相對應人數的需要被隔離的人的index

* (command: `show status`)顯示疫情狀態：
顯示項目包括當前人口數、總關係數目、確診人數、隔離者人數及個人資料。

# Report
### **題目介紹**：
這個程式的目的是讓中央疫情指揮中心或其他政府機關掌握。
主要功能有紀錄或刪除個人資料、紀錄或刪除人際關係資料(包含「臨時人際關係」和「常駐人際關係」)、紀錄確診及發病時間、尋找相關接觸者、追蹤感染源並尋找未確認的可能帶原者、根據現有篩檢量能尋找優先篩檢對象。

### **必要性**：
現在台灣正飽受新冠肺炎的影響而沒辦法正常生活，為了改變目前的困境，我們必須快速且有效率的將疫情控制住。疫情指揮中心可以透過這個程式將人員的資料妥善的儲存管理，並且在得到確診名單後，快速地得到相關人員的名單並進行進一步的隔離，也可以有效地分配篩檢資源，讓篩檢的效果極大化。

### **功能介紹**：
* (command: `read`)新增個人資料： 
可以記錄個人的姓名、身分證字號、生日、年齡、性別、住址、電話、工作。如下圖所示。
**實作方式：在個人資料的hashmap中新增資料**
![](https://i.imgur.com/n8BAIl7.png)


* (command: `read relation`, `add single relation`)
新增「常駐人際關係」及「臨時人際關係」資料：
可以讀整個json檔大量輸入，也可以一個一個單獨建立。人與人會有「常駐人際關係」以及「臨時人際關係」即是 Graph 中的 Edge，例如該圖女子會有與家人的常駐關係以及今日去超市買菜所建立的人際臨時關係，如下圖若該名女子有任何異變, 可進行對其他人的通知跟抓捕
**實作方式：在關係的hashmap中新增關係資料**
![](https://i.imgur.com/xg8dlmd.png)


* (command: `save`)存檔：
儲存目前的graph
**實作方式：使用pickle將目前資料存入檔案**
    
* (command: `load`)讀檔：
當上次離開程式前有預先存檔時，下次再進入的話可以讀上次的檔。
**實作方式：使用pickle從檔案讀入資料**

* (command: `show personal status`)顯示個人狀態：
輸入一串要查詢的人的index，會顯示出這些人的個人資料如：姓名、身份證字號、年齡、職業、確診時間、發病時間、開始隔離時間、結束隔離時間
**實作方式：輸入一個list的人的key，從個人資料hashmap中尋找這些人，並print出他們的資料**

* (command: `show who infected`)顯示感染者：
顯示所有感染者的index。
**實作方式：檢查所有個人資料，只要infected-time不是空字串則為感染者，並回傳這些人**

* (command: `add infected`)新增確診者：
當確診者出現時，可以在確診者的個人資料中註記確診時間(infected-time)及發病時間(infectable)
**實作方式：輸入一個list的人的key，從個人資料hashmap中尋找這些人，將infected-time改為輸入時間**

* (command: `add tmp relation_main`)新增「臨時人際關係」：
「臨時人際關係」是指在不特定場所和時間下遇到的人，因此會連同接觸時間及接觸對象一起儲存。
**實作方式：輸入一個list的人的key，以及一個時間，在人際關係的hashmap新增此關係**

* (command: `find contacted`)尋找接觸者：
輸入一串人的index，若此人為確診者，則尋找所有在發病時間後與確診者接觸過的人的index。
**實作方式：輸入一個list的人的key，判斷是否為確診者，找出這些人的infectable時間。使用常駐人際關係hashmap找出常駐人際關係相關的人們A，使用臨時人際關係hashmap，找出在infectable時間以後接觸的人們B，並回傳全部的人A+B**

* (command: `find by`)從某個項目尋找人：
可以選擇要找的項目有：名字、工作、年齡、性別、確診時間、發病時間、開始隔離時間、結束隔離時間。然後輸入想要的特徵，可以得到一串符合這個特徵的人的index。
**實作方式：輸入一個想尋找的tag，從個人資料hashmap中尋找符合這個tag及數值的人們，將他們回傳**

* (command: `add isolated time`)記錄隔離者：
記錄隔離者的開始被隔離的時間和結束隔離的時間
**實作方式：輸入一個list的人的key，在個人資料的hashmap新增isolation時間**

* (command: `find n people needed`)尋找前n個需要被隔離的人：
輸入一個數字n，得到相對應人數的需要被隔離的人的index
**實作方式：輸入一個數字n代表想要取得n個人，將感染者的所有接觸者列出，給予每個人不同分數，若接觸感染者越多則分數越高，最後找出分數最高的n個的key回傳**

* (command: `show status`)顯示疫情狀態：
顯示項目包括當前人口數、總關係數目、確診人數、隔離者人數。
**實作方式：人口總數、確診人數及隔離者人數由個人資料的hashmap找出、總人際關係數由人際關係的hashmap得出**

### **測資產生**：
* 測資的產生包括產生個人資料和產生常駐人際關係資料。
每筆個人資料的輸入格式為：
```python=
{	
    "name": "name0", 	        # 姓名
    "id": "id0", 		# 身分證字號
    "age": "age0", 		# 年齡
    "birth": "birth0", 	# 生日
    "die": "birth0", 	        # 死亡日期
    "gender": "gender0",       # 性別
    "address": "add0", 	# 住址
    "phone": "phone0", 	# 手機號碼
    "job": "", 		# 工作
    "infected-time": "", 	# 確診時間
    "infectable": "",  	# 患者自認發病時間
    "isolated-start": "", 	# 開始隔離時間
    "isolated-end": ""	        # 結束隔離時間
}
```
* 按照這個格式，將其中的數字0依序抽換成1、2、3……直到n-1為止，可以產生n筆個人資料
每筆常駐人際關係資料的輸入格式為：
```python=
{
    'people' : [0, 4, 6, 7, 3],
    'type' : 'home',
},
{
    'people' : [1, 5, 9, 13],
    'type' : 'job3',
}
"""
其中的數字代表的是每個人的個人資料存在graph裡的index
中括號[ ]包再一起的index代表屬於同一群體，因此兩兩間互有關係
Type代表家庭或其他工作類別
常駐人際關係主要考慮了同居人和工作同事
為了貼近真實情況
我們參考了內政部提供的家庭結構比例
"""
```
總人口：23551889 (23000000)

|          | 1人家戶   | 2人家戶   | 3人家戶   | 4人家戶   | 5人家戶   | 6人以上   |    總共    |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |  -------- |
| 居住人數  | 3041975  | 1833256  | 1619929  | 1298696  |  592634  | 546523   |  8,933,814|
| 人數比  | 13.22%   | 15.94%   | 21.13%   | 22.59%   |  12.89%  | 14.23%   |           |
| 戶數比  | 34.05%   | 20.52%   | 18.13%   | 14.54%   |  6.634%  | 6.117%   |           |

根據這個比例 
* 人口
10000人
* 家庭關係
    * 1313人是1人家庭, 1594人是2人家庭, 2115人是3人家庭
    * 2260人是4人家庭, 1290人是5人家庭, 1428人是6人家庭
    * 共計 3876 個家庭

* 如此下去分配各家庭裡的家人。
* 至於工作場所
    * 現實生活的實際資料難以取得，所以採取盡量隨機分配的方式
    * 同一人不出現兩種重複職業。
    * 職業種類共50種，每種職業的各有N個工作地點，每個工作地點的人員有5~10個且不會每人都有工作因為可能會有小孩及大人的分別

### **使用技術**：
這次的專題主要使用graph作為主要的資料結構。其中Graph的Vertex代表了某個人的個人資料，而Edge則代表了人和人之間的人際關係。因為Graph的Vertex可以和許多Vertex產生Edge，並且Vertex和Vertex之間沒有上下或先後的關係，所以十分適合作為紀錄人際關係的資料結構。

### **功能時間複雜度**：

**主程式**
|          | Time complexity   | Space complexity   |
| ----------- | ----------- | ----------- |
|Main Func | ----------- | ----------- |
|Read | O(N)  | O(N)  | 
|Read Relation | O(N)  | O(N)  | 
|Add Relation | O(N)  | O(N)  | 
|Show Personal Status| O(N) | O(N)  | 
|Show Who Infected | O(V) | O(1) | 
|Show Status | O(V) | O(1) | 
|Add Infected| O(N) | O(1) | 
|Add Isolated Time| O(N) | O(1) |
|Add Tmp Relation Main| O(N) | O(N) |
|Find Contacted| O(Nk)  | O(N) |
|Find By| O(V) | O(V) |
|Get Tracked N People| O(nk + V$\lg$V ) | O(nk) |
* V 是Graph中Vertex數
* n 感染者在Graph中個數
* k 所有感染者中最多的鄰居點數目
* **Read**: N筆人的資料, 我們會一個一個新增進Graph做Vertex
* **Read Relation**: N筆人的關係, 我們會一個一個加進Graph做Edge
* **Add Relation**: 同**Read Relation**
* **Show Personal Status**: 我們會輸出N個人(Vertex)的資料(properties)
* **Show Who Infected**: 我們會輸出多少確診者, 會檢查全部Vertex有沒有確診
* **Show Status**: 每次都會**Show Who Infected**這個func是O(V)所以整體是O(V)
* **Add Infected**: 新增感染者只需要做改Vertex的特性就可。複雜度->O(1)*N
* **Add Isolated Time**: 隔離情況同**Add Infected**
* **Add Tmp Relation Main**: 情況
* **Find Contacted**: 我們會把輸入對象的連接者抓出來。
* **Find By**: 我們會檢查每個點是否有這樣一個值跟所欲搜尋的值相同。
* **Get Tracked N People**: 因為我們會foreach所有感染者，並且把他們的鄰居抓出來檢查權重所以會有nK，又因為我們需要輸出N個人，所以我們會做排序NlgN。使用空間因為有可能在檢查鄰居時如果都不一樣則每個鄰居都會佔一個空間最終會需要nk個空間。

**Graph 的增刪改查**

|          | Time complexity   | Space complexity |
| ----------- | ----------- | ----------- |
|Graph | ----------- | ----------- |
|create vertex | O(1)  | O(1)  | 
|create edge | O(1)  | O(1)  | 
|delete vertex | O(k) | O(1)  | 
|delete edge | O(1) | O(1) | 
|update vertex | O(k)  | O(1) | 
|update edge | O(1) | O(1) |
* k 是該點的鄰居點數目
* 新增
    * 新增vertice: O(1) Hashmap New
    * 新增edge: O(1)  Hashmap New
* 刪除
    * 刪除vertice: O(k)  Hashmap Pop
        * k 為被刪除點所關聯到k個(in, out_neighbors)的點則會啟動K次刪除edge的動作
    * 刪除edge: O(1)  Hashmap Pop
* 修改
    * 修改vertice: O(k)
        * (I) 修改vertice的key影響到k個點
        * (II) 改動到k個(in, out_neighbors)的點則會啟動K次修改edge的動作
        * (III) 除了(I)(II)的情況才可能O(1)
    * 修改edge: O(1)
        * (I) 修改edge的值
        * (II) 修改edge的連接點(最多動到兩點所以也是O(1))
* 查詢
    * 查詢vertice: O(1)
        * 僅保證呼叫 Vertice.value
    * 查詢edge: O(1)
        * 僅保證呼叫 Edge.value

至於在Graph內部的分析, 因為時間複雜度已經如上面所說的定好了。
所以目前已能最便利的實現其複雜度(查O(1),增O(1),刪O(1))為主：
我們考慮了 list、hashmap。
```python=新增東西
import cProfile
num = 1000000
def ds1():
    global num
    a = []
    for i in range(num):
        a.append(True)
def ds2():
    global num
    b = {}
    for i in range(num):
        b[i] = True
cProfile.run('ds1()')
cProfile.run('ds2()')
```
![ds1()](https://i.imgur.com/fg2qDY0.png)->list
![ds2()](https://i.imgur.com/RekM8FP.png)->hashmap
以新增資料來看的話
若所新增的資料當成key的話
hashmap 可以新增資料比較快並且能多一個value去儲存必要資料

```python=刪除資料
import cProfile
num = 1000000
a = [i for i in range(num)]
b = {i:True for i in range(num)}
def ds1():
    global num,a
    for i in range(num//2):
        a.pop(i)
def ds2():
    global num,b
    for i in range(num//2):
        b.pop(i,None)
cProfile.run('ds1()')
cProfile.run('ds2()')
```
![](https://i.imgur.com/r3nf9oA.png)->list
![](https://i.imgur.com/kDXUVsR.png)->hashmap
當然我們可以針對一個list做一個O(1)的刪除, 但原生的結構hashmap還是會快一些

```python=取資料
import cProfile
num = 1000000
a = [i for i in range(num)]
b = {i:True for i in range(num)}
def ds1():
    global num,a
    for i in range(num):
        tmp = a[i]
def ds2():
    global num,b
    for i in range(num):
        tmp = b[i]
cProfile.run('ds1()')
cProfile.run('ds2()')
```
![](https://i.imgur.com/BW5NcdA.png)->list
![](https://i.imgur.com/g6K3Kim.png)->hashmap
以取資料來看, 若設計得當其取資料的數字並不輸以取資料速度著名的快的list
	


### **未來展望**：
以上我們的專題已經能確實的把資料儲存在graph中，利用這些資料我們還可以做出其他功能：
* 刪除個人資料：
當需要資料過期或不需要時可以刪除
* 刪除人際關係資料：
如人際關係過期或不需要時可以刪除
* 尋找未確認的可能帶原者：
從已知的確診者中，回溯他的傳染源，找出可能的潛在傳染者，避免繼續擴散。
* 尋找優先篩檢對象：
輸入目前能夠負擔的篩檢人數，從已知的確診者及接觸者資料中，找出最需要被篩檢的對應人數的人出來接受篩檢，使篩檢資源不被浪費。

我們的專題不只可以應用在新冠肺炎上，任何其他的傳染性疾病也適用。或者更進一步，這個概念可以套用在其他需要觀察關係的事情上，像是如果有一個大型的犯罪組織，裡面的成員人數眾多、組成複雜，這個程式也幫助警方追查毒品流向，或是找出可能的幕後黑手。


### 分工表
* 蕭淇元：utilities.py、report(主)、參與demo影片錄影(後半)
* 劉昱瑋：directedGraph.py、utilities1415.py、report(輔)、main.py、編輯影片
* 游耿睿：utilities2.py、main.py、datagenerator.py、ppt for demo、參與demo影片錄製(前半)
