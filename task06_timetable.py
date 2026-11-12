"""AT3 Q6: nested railway timetable with station index."""
import time,sys
# Each train stores name, station tuples (station, arrival, departure), and running days.
timetable={
 '12601':{'name':'Chennai Express','stops':[('Chennai','06:00','06:10'),('Vijayawada','12:00','12:05'),('Warangal','16:00','16:05')],'days':{'Mon','Wed','Fri'}},
 '12602':{'name':'Coastal Express','stops':[('Chennai','07:00','07:15'),('Nellore','10:00','10:05'),('Vijayawada','13:00','13:10')],'days':{'Tue','Thu','Sat'}},
 '12603':{'name':'Southern Express','stops':[('Bengaluru','05:00','05:10'),('Chennai','09:00','09:10'),('Vijayawada','15:00','15:05')],'days':{'Mon','Tue','Sun'}},
 '12604':{'name':'City Link','stops':[('Chennai','08:00','08:05'),('Katpadi','10:00','10:05')],'days':{'Mon','Tue','Wed'}},
 '12605':{'name':'Night Mail','stops':[('Hyderabad','18:00','18:05'),('Warangal','21:00','21:05'),('Chennai','04:00','04:10')],'days':{'Fri','Sat'}}}
index={}
for train,info in timetable.items():
    for station,arr,dep in info['stops']: index.setdefault(station,[]).append(train)
def query(station,day):
    found=[]
    for train in index.get(station,[]):
        info=timetable[train]
        if day in info['days']:
            stop=next(s for s in info['stops'] if s[0]==station)
            found.append((stop[2],train,info['name']))
    return sorted(found,key=lambda x:x[0])
print('Chennai Monday:',query('Chennai','Mon'))
print('Unknown station:',query('Unknown','Mon'))
print('Third station departure of 12601:',timetable['12601']['stops'][2][2])
print('Index approximate bytes:',sys.getsizeof(index))
