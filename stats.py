import pandas as pd
from bs4 import BeautifulSoup
import urllib.request

url = 'http://lib.stat.cmu.edu/DASL/Datafiles/AlcoholandTobacco.html'

html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')

raw_text = soup.pre.string

raw_list = [row.split('\t') for row in raw_text.split('\n')]

clean_list = raw_list[1:-2]

headers = clean_list[0]

df = pd.DataFrame(clean_list[1:], columns = headers, dtype = float)

for column in headers[1:]:
    print('The mean for '+column+' is: '+str(df[column].mean()))
    print('The median for '+column+' is: '+str(df[column].median()))
    if df[column].mode().empty == False:
        print('The mode for '+column+' is: '+str(df[column].mode()))
    else:
        print('The mode for '+column+' can not be calculated')
    print('The range for '+column+' is: '+str(df[column].max() - df[column].min()))
    print('The variance for '+column+' is: '+str(df[column].var()))
    print('The standard deviation for '+column+' is: '+str(df[column].std()))


