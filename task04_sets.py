"""AT3 Q4: elective registration clash detection."""
ai={'192311001','192311004','192311007','192311009'}
iot={'192311002','192311004','192311009','192311010'}
all_students={f'1923110{i:02d}' for i in range(1,11)}
both=ai & iot
exactly_one=ai ^ iot
neither=all_students-(ai|iot)
print('clash :',sorted(both)); print('exactly one:',sorted(exactly_one)); print('neither :',sorted(neither))
# Repeat using set methods
print('Methods:',ai.intersection(iot),ai.symmetric_difference(iot),all_students.difference(ai.union(iot)))
