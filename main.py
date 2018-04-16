from DatumBox import DatumBox
import sys
import json

import func


srcfile=sys.argv[1]
f = open(srcfile)
context=f.read()

datum_box = DatumBox("0524ce14843851b0ffcf479659fb2a34")

#print(context)

#---------------------1.Topic----------------------
print("1.Topic :".center(80,'-'))
Topic=datum_box.topic_classification(context)
print(Topic)
func.copyfile(srcfile,Topic)
#---------------------2.Keyword----------------------
print("2.Keyword :".center(80,'-'))
Keyword=datum_box.keyword_extract(context)
func.beautiful_keyword(Keyword)
#-------------------3.Sentiment----------------------
print("3.Sentiment :".center(80,'-'))
Sentiment=datum_box.twitter_sentiment_analysis(context)
print(Sentiment)


