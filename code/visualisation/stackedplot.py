import matplotlib.pyplot as plt
import seaborn as sns

fig = plt.figure(1, figsize=(5,5))

categories = ['categorie1', 'categorie2', 'categorie3', 'categorie4']
the_colors = sns.cubehelix_palette(4, start=0.5, rot=-.75)
simulations = range(1,6)


y1 = [0.5, 0.1, 0.2, 0.3, 0.2]
y2 = [0.5, 0.6, 0.2, 0.3, 0.2]
y3 = [0, 0.1, 0.2, 0.25, 0.1]
y4 = [0, 0.2, 0.4, 0.15, 0.5]

# basic stacked area chart
plt.stackplot(simulations, y1, y2, y3, y4, labels=categories, colors=the_colors)

# define axes limits
plt.xlim([1, 5])
plt.ylim([0, 1])

# define axes labels
plt.ylabel('Percentage maluspunten per categorie %   ')
plt.xlabel('Simulaties')

# plot text & line on top of figure
# plt.axvline(x=, linestyle='dotted', color='black')
# plt.text(x-coordinate, y-coordinate, 'text')

# reverse legend color
current_handles, current_labels = plt.gca().get_legend_handles_labels()
plt.legend(list(reversed(current_handles)), list(reversed(current_labels)), fontsize=9)
plt.savefig('stacked_plot.png')