# sample input:
# RuinerWorm null_nerd
# 80 120

import urllib.request, urllib.error, urllib.parse

users = input().split()
l, r =[int(x) for x in input().split()]

for user in users:
	ls=[]
	for i in range(l,r):
		number="{0:0=3d}".format(i)

		url = 'https://atcoder.jp/contests/abc'+number+'/submissions?f.Task=abc'+number+'_a&f.Language=&f.Status=AC&f.User='+user

		response = urllib.request.urlopen(url)
		webContent = response.read()
		result = webContent.decode("utf-8").find('class="text-right submission-score"') 
		if result!=-1:
			ls.append(str(i))
	print(user+" Accepted "+str(len(ls))+" problems: "+", ".join(ls))
