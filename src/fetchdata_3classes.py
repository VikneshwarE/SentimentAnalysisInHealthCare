
from stemming.porter2 import stem
import re
stop={}
with open("../dataset/stopwords.txt","r") as so :
	for line in so :
		stop[line]=1
fw=open("../dataset/yelphealthreviewstrain-stemmed_3classes.txt","w")
with open("../dataset/yelphealthreviewstrain3.txt","r") as fo :
	for line in fo :
		c=line.split('\t')
		noshort=""
		words=c[1].split(' ')
		for word in words :
			word=word.replace('\n','')
			word=word.lower()
			word=re.sub('\W','',word)
			if word not in stop :
				noshort=str(noshort)+stem(word)+" "
		fw.write(c[0]+"\t"+str(noshort)+"\n")
fw.close() 


fw=open("../dataset/yelphealthreviewstest-stemmed_3classes.txt","w")
with open("../dataset/yelphealthreviewstest3.txt","r") as fo :
	for line in fo :
		c=line.split('\t')
		noshort=""
		words=c[1].split(' ')
		for word in words :
			word=word.replace('\n','')
			word=word.lower()
			word=re.sub('\W','',word)
			if word not in stop :
				noshort=str(noshort)+stem(word)+" "
		fw.write(c[0]+"\t"+str(noshort)+"\n")
fw.close() 




