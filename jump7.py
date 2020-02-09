for a in range(1,101):
	if(a%7==0):
		pass
	elif(a%10==7):
		pass
	elif(a//7==10):
		pass
	elif(a//7==11 and a%11<=2):
		pass
	else:
		print(a)
