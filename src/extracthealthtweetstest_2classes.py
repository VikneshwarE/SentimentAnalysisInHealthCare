import csv

businesscsv=open("../dataset/yelp_test_set_business.csv","rb")
csvreader=csv.reader(businesscsv)

business=[]
rnum=0
for row in csvreader :
	if rnum == 0 :
		header=row
	else :
		cnum=0
		for col in row :
			col=col.replace("\n","")
			col=col.replace("\'","")
			col=col.replace("\"","")
			business.append(str(header[cnum])+":"+str(col))
			cnum=cnum+1
	rnum=rnum+1
businesscsv.close()

healthids=[]
healthcategories=[]
for i in range(len(business)) :
	if i%13==3 :
		healthids.append(business[i-3])
		healthcategories.append(business[i])

healthiddict={}
for i in range(len(healthcategories)) :
	c=healthcategories[i]
	c=c.split(":")
	if "Health" in c[1] or "Medical" in c[1] or "Medicine" in c[1] or "Doctors" in c[1] or "Dentists" in c[1] or "Hospitals" in c[1] or "Massage" in c[1] or "Urgent Care" in c[1] or "Naturopathic" in c[1] or "Acupuncture" in c[1] or "Surgeons" in c[1] or "Opticians" in c[1] or "Pediatricians" in c[1] or "Orthopedists" in c[1] or "Gynecologists" in c[1] or "Allergists" in c[1] or "Ophthalmologists" in c[1] or "Optometrists" in c[1] or "Chiropractors" in c[1] or "Dentistry" in c[1] or "Therapy" in c[1] or "Periodontists" in c[1] or "Obstetricians" in c[1] or "Laser Eye Surgery" in c[1] or "Lasik" in c[1] :
		#print "Categories:"+str(c[1])
		d=healthids[i]
		d=d.split(':')
		#print "HealthID:"+str(d[1])
		healthiddict[str(d[1])]=1


reviewcsv=open("../dataset/yelp_test_set_review.csv","rb")
csvreader=csv.reader(reviewcsv)

totalreviews=[]
rnum=0
for row in csvreader :
	if rnum == 0 :
		header=row
	else :
		cnum=0
		for col in row :
			col=col.replace("\n","")
			col=col.replace("\'","")
			col=col.replace("\"","")
			totalreviews.append(str(header[cnum])+":"+str(col))
			cnum=cnum+1
	rnum=rnum+1
reviewcsv.close()

health_ratings=[]
health_reviews=[]
for i in range(len(totalreviews)) :
	d=totalreviews[i].split(':')
	if i%7 == 3 and d[1] in healthiddict :
		stars=int(totalreviews[i+1].split(':')[1])
		if stars >= 3 :
			health_ratings.append("+")
		else :
			health_ratings.append("-")
		c=totalreviews[i-1].split(':')
		health_reviews.append(c[1])
for i in range(len(health_ratings)) :
	print health_ratings[i]+"\t"+health_reviews[i]




