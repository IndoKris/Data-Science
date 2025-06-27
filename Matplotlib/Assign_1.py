import matplotlib.pyplot as plt

years = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
kohli_runs = [325, 995, 1381, 1026, 1268, 1054, 1380, 1215, 1460, 1202]
rohit_runs = [362, 405, 611, 563, 1196, 578, 815, 930, 1293, 1030]
sehwag_runs = [1236, 1462, 880, 1115, 1041, 754, 651, 384, 217, 96]

plt.plot(years,kohli_runs, color = "green", linestyle = '-.',linewidth = 2,label='KOHLI')
plt.plot(years,rohit_runs, color = "blue", linestyle = '--',linewidth = 1,label='ROHI')
plt.plot(years,sehwag_runs, color = "RED", linestyle = ':',linewidth = 3,label='SEHWAG')
plt.title('PLAYERS COMPARISION')
plt.xlabel('RUNS SCORED')
plt.ylabel('PLAYES')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.style.use('seaborn-v0_8-darkgrid')
plt.show()
