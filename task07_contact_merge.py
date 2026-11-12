"""AT3 Q7: merge contacts by normalised phone number."""
import re,time,random
contacts=[{'name':'Dr. Ravi','phone':'+91 98400 12345','email':'ravi@x.com'}, {'name':'ravi kumar','phone':'9840012345','email':'r.kumar@x.com'}, {'name':'Anu','phone':'9876543210','email':''}]
def normalise_phone(phone):
    digits=re.sub(r'\D','',phone or '')
    return digits[2:] if len(digits)==12 and digits.startswith('91') else digits
def merge(records):
    merged={}
    for c in records:
        key=normalise_phone(c.get('phone',''))
        if not key: continue
        item=merged.setdefault(key,{'names':set(),'phones':set(),'emails':set()})
        if c.get('name'): item['names'].add(c['name'].strip().title())
        item['phones'].add(c['phone'].strip())
        if c.get('email'): item['emails'].add(c['email'].strip().lower())
    return merged
print(merge(contacts))
for n in (1000,100000):
    data=[{'name':f'Person{i}','phone':f'+91 90000 {i:05d}','email':''} for i in range(n)]
    t=time.perf_counter(); merge(data); print(n,'contacts:',round(time.perf_counter()-t,5),'seconds')
