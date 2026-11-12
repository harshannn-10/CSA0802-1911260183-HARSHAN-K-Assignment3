"""AT3 Q2: tuples, mutability, copying and independent grids."""
import copy, sys, time
rows,cols=3,4
bad=[[0]*cols]*rows; bad[0][1]=7
good=[[0 for _ in range(cols)] for _ in range(rows)]; good[0][1]=7
print('bad :',bad); print('good:',good); print(bad[0] is bad[1],good[0] is good[1])
stops={(13.0827,80.2707):'Chennai Central',(13.0418,80.2541):'T. Nagar'}
print(stops[(13.0418,80.2541)])
try: stops[[13.0418,80.2541]]='Invalid key'
except TypeError as e: print('List key error:',e)
original=[[1,2],[3,4]]; shallow=copy.copy(original); deep=copy.deepcopy(original)
shallow[0][0]=99; print('Original after shallow nested edit:',original)
deep[1][1]=88; print('Deep copy:',deep)
values=list(range(1_000_000)); tup=tuple(values)
print('List bytes:',sys.getsizeof(values),'Tuple bytes:',sys.getsizeof(tup))
start=time.perf_counter(); _=values[500000]; print('List index time:',time.perf_counter()-start)
start=time.perf_counter(); _=tup[500000]; print('Tuple index time:',time.perf_counter()-start)
