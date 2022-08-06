import matplotlib.pyplot as plt
import numpy as np
from math import cos,sin,pi

with open("pi.txt", "r") as file:
    pi_digit = file.readline()

def next(previous,digit):
    return (previous[0]+cos(-pi/2-digit*pi/5)*(1),previous[1]+sin(-pi/2-digit*pi/5)*(1))

nb_points = 314159

colors = []

print("Generating points")

points=[(0,0)]

pi_digit=list(pi_digit)[:nb_points]
for d in pi_digit:
    points.append(next(points[-1],int(d)))

x=[t[0] for t in points]
y=[t[1] for t in points]

# Possible color values : 'magma', 'inferno', 'plasma', 'viridis', 'cividis',
# 'twilight', 'twilight_shifted', 'turbo', 'Blues', 'BrBG', 'BuGn', 'BuPu',
# 'CMRmap', 'GnBu', 'Greens', 'Greys', 'OrRd', 'Oranges', 'PRGn', 'PiYG',
# 'PuBu', 'PuBuGn', 'PuOr', 'PuRd', 'Purples', 'RdBu', 'RdGy', 'RdPu',
# 'RdYlBu', 'RdYlGn', 'Reds', 'Spectral', 'Wistia', 'YlGn', 'YlGnBu', 'YlOrBr',
# 'YlOrRd', 'afmhot', 'autumn', 'binary', 'bone', 'brg', 'bwr', 'cool',
# 'coolwarm', 'copper', 'cubehelix', 'flag', 'gist_earth', 'gist_gray',
# 'gist_heat', 'gist_ncar', 'gist_rainbow', 'gist_stern', 'gist_yarg',
# 'gnuplot', 'gnuplot2', 'gray', 'hot', 'hsv', 'jet', 'nipy_spectral', 'ocean',
# 'pink', 'prism', 'rainbow', 'seismic', 'spring', 'summer', 'terrain',
# 'winter', 'Accent', 'Dark2', 'Paired', 'Pastel1', 'Pastel2', 'Set1', 'Set2',
# 'Set3', 'tab10', 'tab20', 'tab20b', 'tab20c', 'magma_r', 'inferno_r',
# 'plasma_r', 'viridis_r', 'cividis_r', 'twilight_r', 'twilight_shifted_r',
# 'turbo_r', 'Blues_r', 'BrBG_r', 'BuGn_r', 'BuPu_r', 'CMRmap_r', 'GnBu_r',
# 'Greens_r', 'Greys_r', 'OrRd_r', 'Oranges_r', 'PRGn_r', 'PiYG_r', 'PuBu_r',
# 'PuBuGn_r', 'PuOr_r', 'PuRd_r', 'Purples_r', 'RdBu_r', 'RdGy_r', 'RdPu_r',
# 'RdYlBu_r', 'RdYlGn_r', 'Reds_r', 'Spectral_r', 'Wistia_r', 'YlGn_r',
# 'YlGnBu_r', 'YlOrBr_r', 'YlOrRd_r', 'afmhot_r', 'autumn_r', 'binary_r',
# 'bone_r', 'brg_r', 'bwr_r', 'cool_r', 'coolwarm_r', 'copper_r',
# 'cubehelix_r', 'flag_r', 'gist_earth_r', 'gist_gray_r', 'gist_heat_r',
# 'gist_ncar_r', 'gist_rainbow_r', 'gist_stern_r', 'gist_yarg_r', 'gnuplot_r',
# 'gnuplot2_r', 'gray_r', 'hot_r', 'hsv_r', 'jet_r', 'nipy_spectral_r',
# 'ocean_r', 'pink_r', 'prism_r', 'rainbow_r', 'seismic_r', 'spring_r',
# 'summer_r', 'terrain_r', 'winter_r', 'Accent_r', 'Dark2_r', 'Paired_r',
# 'Pastel1_r', 'Pastel2_r', 'Set1_r', 'Set2_r', 'Set3_r', 'tab10_r', 'tab20_r',
# 'tab20b_r', 'tab20c_r'

print("Generating graph")

c = "RdBu"
plt.clf()
colors = plt.cm.get_cmap(c)(np.linspace(0, 1, nb_points))
for i in range(nb_points):
    plt.plot(x[i:i+2], y[i:i+2], c = colors[i], alpha = 1, linewidth = 0.1)
plt.axis("square")
plt.axis("off")
name = c + ".jpeg"
namesvg = c + ".svg"
print("Saving jpeg")
plt.savefig(name, dpi=6000)
print("Saving svg")
plt.savefig(namesvg)
