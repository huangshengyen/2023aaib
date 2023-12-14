# a = [1,1,2,3,5,8,13,21](這個寫法不好)
a = [1, 1]
for i in range(2,40): #課本的第3-6頁，有介紹.append()
  #a[i] = a[i-1] + a[i-2](不對的寫法)
  a.append( a[i-1] + a[i-2] )#利用 .append()在後面加1項

print(a)