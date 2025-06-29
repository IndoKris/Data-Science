'''
Assignment:
Create a pie chart showing the market share of mobile OS (Android, iOS, others). Then recreate the same
using a horizontal bar chart and observe which is easier to understand.
'''
#imports
import matplotlib.pyplot as plt 

#data with others expanded 
data = [72, 27, 0.4, 0.3, 0.2, 0.1]
labels = ['Android', 'iOS', 'KaiOS', 'Windows Phone', 'Samsung', 'Other']
colors = ['#304852','#36595F','#5F818A','#405559','#C7EEFF','#B9DBE6']
#pie chart
plt.pie(
    x = data,
    labels = labels,
    colors = colors,
    shadow = True,
    autopct = '%.1f%%',
    frame = False,
    wedgeprops={
        'edgecolor': 'black',
        'linewidth': 1 
    }
)
plt.title('Market share of mobile OS')
plt.tight_layout()
plt.show()