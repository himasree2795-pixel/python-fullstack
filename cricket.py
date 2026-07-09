fobj = open("sachin.txt","r")

strike_rates=[]
for line in fobj:
    columns=line.split()
    runs=int(columns[2])
    balls=int(columns[3])
    strike_rate=runs/balls*100
    strike_rates.append(strike_rate)


import statistics 
deviation=statistics.stdev(strike_rates)
print(deviation)

fobj = open("virat.txt","r")

strike_rates=[]
for line in fobj:
    columns=line.split()
    runs=int(columns[2])
    balls=int(columns[3])
    strike_rate=runs/balls*100
    strike_rates.append(strike_rate)


import statistics 
deviation=statistics.stdev(strike_rates)
print(deviation)

fobj = open("yuvraj.txt","r")

strike_rates=[]
for line in fobj:
    columns=line.split()
    runs=int(columns[2])
    balls=int(columns[3])
    strike_rate=runs/balls*100
    strike_rates.append(strike_rate)


import statistics 
deviation=statistics.stdev(strike_rates)
print(deviation)

fobj = open("dravid.txt","r")

strike_rates=[]
for line in fobj:
    columns=line.split()
    runs=int(columns[2])
    balls=int(columns[3])
    strike_rate=runs/balls*100
    strike_rates.append(strike_rate)


import statistics 
deviation=statistics.stdev(strike_rates)
print(deviation)