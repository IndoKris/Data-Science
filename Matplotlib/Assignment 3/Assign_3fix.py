#ASSIGNMENT 3 fix
#imports
import matplotlib.pyplot as plt 

#data with others expanded 
data = [72, 27, 1]
labels = ['Android', 'iOS', 'Other']
colors = ['#E5CFF7','#713ABE','#5B0888']
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