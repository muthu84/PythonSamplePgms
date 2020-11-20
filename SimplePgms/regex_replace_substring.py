import sys
import re
while True:
    line = sys.stdin.readline()
    if not line:
        break
    line=line.strip('\n')
    issuerid,businessyear,statedesc,sourcename, defaulter ,networkurl = line.split('\t')
    #maskednetworkurl= networkurl.replace('a','x').replace('b','y').replace('c','z').replace('s','r').replace('.com','aaa')
    maskednetworkurl= re.sub('a','x',re.sub('b','y',re.sub('c','z',re.sub('r','s',re.sub('.com','aaa',networkurl)))))
    print('\t'.join([issuerid,businessyear,statedesc,sourcename, defaulter, maskednetworkurl]))