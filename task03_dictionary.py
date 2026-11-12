"""AT3 Q3: complaint word frequencies and district grouping."""
from collections import Counter
import random,time,string
calls=['seeds not received seeds delayed','fertiliser price high','seeds price high subsidy not received']
STOP={'not','high'}
def frequencies(texts,stop):
    counts={}
    for text in texts:
        for word in text.lower().translate(str.maketrans('','',string.punctuation)).split():
            if word not in stop: counts[word]=counts.get(word,0)+1
    return counts
def top(counts,k): return sorted(counts.items(),key=lambda item:(-item[1],item[0]))[:k]
print(top(frequencies(calls,STOP),3))
complaints=[('North','rice price high'),('South','seeds delayed'),('North','water shortage')]
by_district={}
for district,msg in complaints: by_district.setdefault(district,[]).append(msg)
print('By district:',by_district)
for n in (1000,10000,100000):
    data=['seed price complaint']*n
    t=time.perf_counter(); frequencies(data,set()); print('dict',n,round(time.perf_counter()-t,5))
    t=time.perf_counter(); Counter(' '.join(data).split()); print('Counter',n,round(time.perf_counter()-t,5))
