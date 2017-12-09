
# coding: utf-8

# In[1]:

import matplotlib.pyplot as plt
from matplotlib import rc
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patches as mpatches
from scipy import stats, integrate
import pandas as pd
import numpy as np
import seaborn as sns
sns.set()

# In[2]:

# READ DATA SOURCES, MERGE AND CLEAN THE COMBINED DATAFRAME
# Read the two data sources
happiness_df = pd.read_csv("2016happiness.csv", encoding="ISO-8859-1")
web_access_df = pd.read_csv("web_access.csv", encoding="ISO-8859-1")

# Merge then on common column 'Country' with type 'inner'.
happyweb_pd = pd.merge(happiness_df,
                 web_access_df,
                 on='Country',
                 how ='inner')

# clean dataframe rows using dropna()
happyweb_pd = happyweb_pd.dropna(axis=0, thresh=1)  

happyweb_pd


# In[3]:


# Add column ['Penetration_f'] that is equal to 'Penetration' column percentages converted to floats. 
# Added this column because percentage values are strings and can't be sorted - e.g.float('52%') doesn't work, so astype() is used.

happyweb_pd = happyweb_pd.assign(Penetration_f = happyweb_pd["Penetration (% of Pop)"].replace('%','',regex=True).astype('float'))

# Float values in 'Penetration_f' column are sorted (which sorts the dataframe using Penetration_f column) 

happyweb_pd = happyweb_pd.sort_values(['Penetration_f'], ascending=False)

happyweb_pd


# In[4]:


# INTERNET PENETRATION BY COUNTRIES

# Set x axis and tick locations
x_axis = np.arange(len(happyweb_pd))
x_tick_locations = [value+0.4 for value in x_axis]

# Create a list indicating where to write x labels and set figure size to adjust for space
plt.figure(figsize=(14, 5))
y_axis = happyweb_pd["Penetration_f"]
plt.bar(x_axis, y_axis, color='r', alpha=0.7, align="edge")
plt.xticks(x_tick_locations, happyweb_pd["Country"], rotation="vertical", fontsize = 6)
plt.yticks(fontsize = 16)
# Set x and y limits
plt.xlim(-0.25, len(x_axis))
# Set a Title and labels
plt.title("Internet penetration by countries", fontsize = 18)
plt.xlabel("Countries", fontsize = 18)
plt.ylabel("Internet users Percent of Population", fontsize = 18)
# Save our graph and show the grap
plt.tight_layout()
plt.savefig("Internet penetration by countries")
plt.show()


# In[5]:


# HEALTHY LIFE EXPECTANCY) BY INTERNET PENETRATION BY COUNTRIES - VISUALIZATION #1
# plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))

markersize = 50 
kws = dict(s=markersize, linewidth=.8, edgecolor="bk")
sns.set(font_scale = 1.2)

xlim_max = happyweb_pd["Penetration_f"].max()
ylim_max = happyweb_pd["Healthy Life Expectancy"].max()
xlim_min = happyweb_pd["Penetration_f"].min()
ylim_min = happyweb_pd["Healthy Life Expectancy"].min()

pyber_palette = ['#c6fcff','#1b919a','#ff0033','#000099','#ffff66']  
# light Sky blue, Green, Red, blue, Yellow

sns.jointplot(x="Penetration_f", y="Healthy Life Expectancy", data=happyweb_pd, kind="reg");

#plt.text(8, 45, "Note: add text", horizontalalignment='left',size='medium', color='green', weight='light')
#plt.title("Health ((Life Expectancy) vs Internet penetration by countries", fontsize = 15)
plt.ylabel("Healthy Life Expectancy", fontsize = 15)
plt.xlabel("% Internet penetration", fontsize = 15)
plt.xlim(xlim_min-1, xlim_max+2)    # margins so plot doesn't end at max values
plt.ylim(ylim_min-.025, ylim_max+.025)

# Save the figure
plt.savefig("Healthy Life Expectancy vs Internet penetration By Countries")

plt.show()


# In[6]:


g = sns.jointplot(x="Penetration_f", y="Healthy Life Expectancy", data=happyweb_pd, kind="kde", color="r")
g.plot_joint(plt.scatter, c="w", s=30, linewidth=1, marker="+")
g.ax_joint.collections[0].set_alpha(0)
#g.set_axis_labels("$Percent Internet Penetration$", "Healthy Life Expectancy$");
plt.ylabel("Healthy Life Expectancy", fontsize = 15)
plt.xlabel("% Internet penetration \n \n KERNAL DENSITY DISTRIBUTION PLOT ", fontsize = 15)

# Save the figure
plt.savefig("Healthy Life Expectancy vs Internet penetration by countries")
plt.show


# In[7]:


# HAPPINESS BY INTERNET PENETRATION BY COUNTRIES

markersize = 50 
kws = dict(s=markersize, linewidth=.8, edgecolor="bk")
sns.set(font_scale = 1.2)

xlim_max = happyweb_pd["Penetration_f"].max()
ylim_max = happyweb_pd["Happiness Score"].max()
xlim_min = happyweb_pd["Penetration_f"].min()
ylim_min = happyweb_pd["Happiness Score"].min()

pyber_palette = ['#c6fcff','#1b919a','#ff0033','#000099','#ffff66']  
# light Sky blue, Green, Red, blue, Yellow

sns.jointplot(x="Penetration_f", y="Happiness Score", data=happyweb_pd, kind="reg");

#plt.title("Health (Life Expectancy) vs Internet penetration by countries", fontsize = 15)
plt.ylabel("Happiness Score", fontsize = 15)
plt.xlabel("% Internet penetration", fontsize = 15)
plt.xlim(xlim_min-1, xlim_max+2)    # margins so plot doesn't end at max values
plt.ylim(ylim_min-1, ylim_max+0.25)

# Save the figure
plt.savefig("Happiness Score vs Percent Internet penetration")

plt.show()


# In[8]:


# Set x axis and tick locations
x_axis = np.arange(len(happyweb_pd))
x_tick_locations = [value+0.4 for value in x_axis]

# Create a list indicating where to write x labels and set figure size to adjust for space
plt.figure(figsize=(14, 5))
y_axis = happyweb_pd["Happiness Score"]
plt.plot(x_axis, y_axis, marker='o', color='r', linewidth=1.5, alpha=0.9)
#plt.bar(x_axis, y_axis, color='r', alpha=0.7, align="edge")
plt.xticks(x_tick_locations, happyweb_pd["Country"], rotation="vertical", fontsize = 6)
plt.yticks(fontsize = 16)
# Set x and y limits
plt.xlim(-0.25, len(x_axis))
# Set a Title and labels
plt.title("Happiness Score by countries", fontsize = 18)
plt.xlabel("Countries", fontsize = 18)
plt.ylabel("Happiness Score", fontsize = 18)
# Save our graph and show the grap
plt.tight_layout()
plt.savefig("Happiness Score by countries")
plt.show()


# In[9]:


# ECONOMY (GDP PER CAPITA) VS. INTERNET PENETRATION BY COUNTRIES

markersize = 50 
kws = dict(s=markersize, linewidth=.8, edgecolor="bk")
sns.set(font_scale = 1.2)

xlim_max = happyweb_pd["Penetration_f"].max()
ylim_max = happyweb_pd["Economy (GDP per Capita)"].max()
xlim_min = happyweb_pd["Penetration_f"].min()
ylim_min = happyweb_pd["Economy (GDP per Capita)"].min()

pyber_palette = ['#c6fcff','#1b919a','#ff0033','#000099','#ffff66']  
# light Sky blue, Green, Red, blue, Yellow

sns.jointplot(x="Penetration_f", y="Economy (GDP per Capita)", data=happyweb_pd, kind="reg");

#plt.text(8, 45, "Note: add text", horizontalalignment='left',size='medium', color='green', weight='light')
#plt.title("Health ((Life Expectancy) vs Internet penetration by countries", fontsize = 15)
plt.ylabel("Economy (GDP per Capita)", fontsize = 15)
plt.xlabel("% Internet penetration", fontsize = 15)
plt.xlim(xlim_min-2, xlim_max+2)    # margins so plot doesn't end at max values
plt.ylim(ylim_min-0.05, ylim_max+0.05)

# Save the figure
plt.savefig("Economy (GDP per Capita) vs Internet penetration by countries")
plt.show()


# In[10]:

fig = plt.figure()

ax= Axes3D(fig)
x= happyweb_pd["Penetration_f"]
y= happyweb_pd["Economy (GDP per Capita)"]
z= happyweb_pd["Happiness Score"]

ax.scatter(x, y, z, c='r', marker='o')

ax.set_xlabel("\n % Internet penetration")
ax.set_ylabel("\n Economy (GDP per Capita)")
ax.set_zlabel("\n Happiness Score")

plt.savefig("3D Plot of Economy(GDP) vs % Internet penetration vs Happiness Score")
plt.show()


# In[11]:


# GENEROSITY VS. INTERNET PENETRATION BY COUNTRIES
# plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))

markersize = 50 
kws = dict(s=markersize, linewidth=.8, edgecolor="bk")
sns.set(font_scale = 1.2)

xlim_max = happyweb_pd["Penetration_f"].max()
ylim_max = happyweb_pd["Generosity"].max()
xlim_min = happyweb_pd["Penetration_f"].min()
ylim_min = happyweb_pd["Generosity"].min()

pyber_palette = ['#c6fcff','#1b919a','#ff0033','#000099','#ffff66']  
# light Sky blue, Green, Red, blue, Yellow

sns.jointplot(x="Penetration_f", y="Generosity", data=happyweb_pd, kind="reg");

#plt.text(8, 45, "Note: add text", horizontalalignment='left',size='medium', color='green', weight='light')
#plt.title("Health ((Life Expectancy) vs Internet penetration by countries", fontsize = 15)
plt.ylabel("Generosity", fontsize = 15)
plt.xlabel("% Internet penetration", fontsize = 15)
plt.xlim(xlim_min-2, xlim_max+2)    # margins so plot doesn't end at max values
plt.ylim(ylim_min-0.025, ylim_max+0.025)

# Save the figure
plt.savefig("Generosity vs Internet penetration by countries")

plt.show()


# In[12]:


# Set x axis and tick locations
x_axis = np.arange(len(happyweb_pd))
x_tick_locations = [value+0.4 for value in x_axis]

greenbars = [i / j * 100 for i,j in zip(happyweb_pd["Economy (GDP per Capita)"], happyweb_pd["Happiness Score"])]
orangebars = [i / j * 100 for i,j in zip(happyweb_pd["Healthy Life Expectancy"], happyweb_pd["Happiness Score"])]
bluebars = [i / j * 100 for i,j in zip(happyweb_pd["Generosity"], happyweb_pd["Happiness Score"])]
redbars = [i / j * 100 for i,j in zip(happyweb_pd["Family"], happyweb_pd["Happiness Score"])]
yellowbars = [i / j * 100 for i,j in zip(happyweb_pd["Freedom"], happyweb_pd["Happiness Score"])]
skybluebars = [i / j * 100 for i,j in zip(happyweb_pd["Trust (Government Corruption)"], happyweb_pd["Happiness Score"])]
brownbars = [i / j * 100 for i,j in zip(happyweb_pd["Dystopia Residual"], happyweb_pd["Happiness Score"])]
                                      
# plot
barWidth = 1.2
plt.figure(figsize=(14,6))

# Create green Bars
plt.bar(x_tick_locations, greenbars, color='#b5ffb9', edgecolor='black', width=barWidth, align="edge")
# Create red Bars
plt.bar(x_tick_locations, redbars, bottom=greenbars, color='#ff0033', edgecolor='black', width=barWidth, align="edge")
# Create orange Bars
plt.bar(x_tick_locations, orangebars, bottom=[i+j for i,j in zip(greenbars, redbars)], color='#f9bc86', edgecolor='black', width=barWidth, align="edge")
# Create brown Bars
plt.bar(x_tick_locations, brownbars, bottom=[i+j+k for i,j,k in zip(greenbars, redbars, orangebars)], color='#cd6600', edgecolor='black', width=barWidth, align="edge")
# Create yellow Bars
plt.bar(x_tick_locations, yellowbars, bottom=[i+j+k+l for i,j,k,l in zip(greenbars, redbars, orangebars, brownbars)], color='#ffff66', edgecolor='black', width=barWidth, align="edge")
# Create blue Bars
plt.bar(x_tick_locations, bluebars, bottom=[i+j+k+l+m for i,j,k,l,m in zip(greenbars, redbars, orangebars, brownbars, yellowbars)], color='#a3acff', edgecolor='black', width=barWidth, align="edge")
# Create skyblue Bars
plt.bar(x_tick_locations, skybluebars, bottom=[i+j+k+l+m+n for i,j,k,l,m,n in zip(greenbars, redbars, orangebars, brownbars, yellowbars, bluebars)], color='#c6fcff', edgecolor='black', width=barWidth, align="edge")


# Custom x axis
plt.xticks(x_tick_locations, happyweb_pd["Country"], rotation="vertical", fontsize = 6)  
plt.yticks(fontsize = 14)
plt.xlabel("Countries", fontsize = 14)
plt.ylabel("Happiness Score normalized to 100% for Each Country", fontsize = 12)
plt.xlim(0, len(x_axis))
plt.title("% CONTRIBUTION OF FACTORS TO HAPPINESS SCORE OF EACH COUNTRY", fontsize = 14)
plt.tight_layout()
# '#dbb40c', '#c6fcff', '#ffd8b1' ->  Gold, light Sky blue, light coral

green_patch = mpatches.Patch(color='#b5ffb9', label='Economy(GDP)')
orange_patch = mpatches.Patch(color='#f9bc86', label='Healthy Life Expectancy')
blue_patch = mpatches.Patch(color='#a3acff', label='Generosity')
red_patch = mpatches.Patch(color='#ff0033', label='Family')
yellow_patch = mpatches.Patch(color='#ffff66', label='Freedom')
skyblue_patch = mpatches.Patch(color='#c6fcff', label='Trust (Government Corruption)')
brown_patch = mpatches.Patch(color='#cd6600', label='Dystopia Residual')

# Locate legend horizontally using ncol=7 for 7 names. The legend box is located below (0,0)- Graph rectangle is (0,0) to (1,1)
plt.legend(handles=[green_patch, red_patch, orange_patch, brown_patch, yellow_patch, blue_patch, skyblue_patch], fontsize = 10, loc = 'lower left', bbox_to_anchor=(0, -0.35), ncol=7, fancybox=True, shadow=True)

# Save graph and Show it
plt.savefig("Percent Contribution of Factors to Happiness Score of Each Country")
plt.show()

