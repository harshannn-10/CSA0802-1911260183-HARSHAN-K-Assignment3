"""AT3 Q1: Daily rainfall records - list slicing and moving averages."""
import random, time

def moving_average_naive(values, window=7):
    return [sum(values[i:i+window])/window for i in range(len(values)-window+1)] if len(values)>=window else []

def moving_average_running(values, window=7):
    if len(values)<window: return []
    current=sum(values[:window]); result=[current/window]
    for i in range(window,len(values)):
        current += values[i]-values[i-window]
        result.append(current/window)
    return result

def main():
    readings=[round(random.uniform(0,30),1) for _ in range(365)]
    weekly=[sum(readings[i:i+7]) for i in range(0,len(readings),7)]
    print('Weekly totals (last may be partial):', weekly)
    print('Wettest week:', max(enumerate(weekly,1),key=lambda x:x[1]))
    print('Driest week:', min(enumerate(weekly,1),key=lambda x:x[1]))
    print('7-day moving averages (first 10):', moving_average_running(readings)[:10])
    print('Dry days (day numbers):',[i+1 for i,v in enumerate(readings) if v==0])
    for n in (365,36500,365000):
        data=[random.random()*30 for _ in range(n)]
        for fn in (moving_average_naive,moving_average_running):
            start=time.perf_counter(); fn(data); print(n,fn.__name__,round(time.perf_counter()-start,6),'seconds')
    print('Short input test:',moving_average_running([1,2,3]))
if __name__=='__main__': main()
