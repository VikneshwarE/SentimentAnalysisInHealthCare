#!/bin/bash

cd src
python jsoncsv.py ../dataset/yelp_test_set_business.json
python jsoncsv.py ../dataset/yelp_training_set_business.json
python jsoncsv.py ../dataset/yelp_test_set_review.json
python jsoncsv.py ../dataset/yelp_training_set_review.json

python extracthealthtweetstrain_2classes.py > ../dataset/yelphealthreviewstrain2.txt
python extracthealthtweetstrain_3classes.py > ../dataset/yelphealthreviewstrain3.txt
python extracthealthtweetstest_2classes.py > ../dataset/yelphealthreviewstest2.txt
python extracthealthtweetstest_3classes.py > ../dataset/yelphealthreviewstest3.txt


python fetchdata_2classes.py
python fetchdata_3classes.py

python sentimentclassify_2classes.py
python sentimentclassify_3classes.py
