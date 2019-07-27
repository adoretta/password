password = 'a123456'
c = 3 #輸入密碼次數
while c >0:
    pwd = int(input('請輸入密碼: '))
    c -= 1
    if pwd == password:
    	print('登入成功!')
    	break
    else:
    	print('密碼錯誤!')
    	if c > 0:
    		print('還有', c, '次機會')
    	else:
    		print('沒機會嘗試了!沒機會嘗試了')

