data = []   #建立一個空清單來存取第六行讀取出來的資料
count = 0
with open('reviews.txt', 'r') as f :
    for line in f:   #line每次讀取一行所以將此變數去名為line
        data.append(line)
        count += 1 # count = count + 1
        if count % 10000 == 0: #求餘數
            print(len(data)) #data是一個清單，計算data裡有幾個物件
print('Done! Totally', len(data), 'reviews')

#計算每則留言平均有幾個字
sum_len = 0
for d in data: #d是個字串
    sum_len += len(d)
print ('留言平均', sum_len/ len(data), '字')

#計算有幾則小於100字的留言
new = [] #建立新的清單
for d in data:
	if len(d) < 100:
		new.append(d)
print('共有幾筆', len(new), '比小於100字')
print(new[-1])

# ---印出清單裡面的每一筆資料 ---
for comment in new:
    print(comment) # 每跑一次迴圈，就印出一則留言
    print('--------------------') # 加個分隔線比較好閱讀

# ---印出清單裡面有bad詞的資料 ---
for b in data:
    if 'bad' in b.lower():
        print(b)
        print('---------------')