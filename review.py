data = []   #建立一個空清單來存取第六行讀取出來的資料
count = 0
with open('reviews.txt', 'r') as f :
    for line in f:   #line每次讀取一行所以將此變數去名為line
        data.append(line)
        count += 1 # count = count + 1
        if count % 10000 == 0: #求餘數
            print(len(data)) #data是一個清單，計算data裡有幾個物件
print('Done! Totally', len(data), 'reviews')

sum_len = 0
for d in data: #d是個字串
    sum_len += len(d)

print ('留言平均', sum_len/ len(data), '字')