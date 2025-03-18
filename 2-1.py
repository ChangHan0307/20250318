#基本型態有7種

#字串
print("hello world")
#整數
print(123456)
#浮點數
print(10.12)
#布林值
print(True)
#列表
print({"123",456,True})
#字典
print({"name":"chinghan"})
#元組
print(('紅','橙','黃'))





#變數
#變數=一個同步的箱子，能一次改變很多東西
name='python'

print(name+'是一種程式語言')
print('你知道嗎？'+name+'是一種程式語言')

#input 使用者互動
# #\n是換行的意思
name=input('輸入程式語言\n')

print(name+'是一種程式語言')
print('我知道'+name+'是一種程式語言')
print('所以我想學會如何寫'+name+'語言')





#變數數字練習
#大家一起加分

AddScoro=20
MacScoro=80+AddScoro
KenScoro=60+AddScoro
CCCScoro=50+AddScoro

print(MacScoro,KenScoro,CCCScoro)





#取出變數箱子的值，再累加回去變數箱子
#例子-台灣原住民，額外加20分

AddScoro=20
MyScoro=40
MyScoro=MyScoro+AddScoro+20
print(MyScoro)





#數字和字串的型態變換->因為字串只能和字串相加，數字只能和數字相加。

#數字轉成字串  str  函式
print('答案是：'+str(5+10))
print(456+float('123'))
print('答案是：'+str(456+float('123')))





#數字運算

print(1+10)
print(5*2)
print(5/2)
print(5%2)
print(round(5.2))
#round=四捨五入





#輸入後運算八折練習

number=input('請輸入價錢：')
print('打八折後的價錢為'+str(round(float(number)*0.8)))





#字串練習

print('這是一本書，'+'這是兩本書')
print('123456')
print('apple is good.'.replace('apple','banana'))
print('I am good at coding'.find('coding'))