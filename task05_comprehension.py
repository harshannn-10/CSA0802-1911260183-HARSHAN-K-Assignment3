"""AT3 Q5: clean sensor readings and convert temperatures."""
import random,time,sys
readings=[-60,-2,4,7,9,55,6,3]
valid_loop=[]
for c in readings:
    if -50<=c<=50: valid_loop.append((c,round(c*9/5+32,2)))
valid_comp=[(c,round(c*9/5+32,2)) for c in readings if -50<=c<=50]
valid_map=list(map(lambda c:(c,round(c*9/5+32,2)),filter(lambda c:-50<=c<=50,readings)))
alarms=[minute for minute,c in enumerate(readings) if -50<=c<=50 and not 2<=c<=8]
print('Loop:',valid_loop); print('Comprehension:',valid_comp); print('map/filter:',valid_map); print('Alarm minutes:',alarms)
print('All equal:',valid_loop==valid_comp==valid_map)
for n in (10000,100000,1000000):
    data=[random.uniform(-55,55) for _ in range(n)]
    for label,fn in [('loop',lambda:[x for x in data if -50<=x<=50]),('comprehension',lambda:[x for x in data if -50<=x<=50]),('filter',lambda:list(filter(lambda x:-50<=x<=50,data)))]:
        t=time.perf_counter(); out=fn(); print(n,label,round(time.perf_counter()-t,5),'s')
    gen=(x for x in data if -50<=x<=50); print('List bytes / generator bytes:',sys.getsizeof([x for x in data if -50<=x<=50]),sys.getsizeof(gen))
