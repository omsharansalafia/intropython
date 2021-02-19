import numpy as np
import matplotlib.pyplot as plt
import pandas

# tweak matplotlib settings
plt.rcParams['figure.figsize']=10,12
plt.rcParams['font.family']='Liberation Sans'

# load csv data file
data = pandas.read_csv('entry_survey_responses.csv')
cols = data.columns

# create figure and title
fig = plt.figure()
fig.text(x=0.5,y=0.96,s='Entry Survey results ({0:d} responses)'.format(len(data)),ha='center',fontsize=16)


# create pie chart from Q1 responses

## extract data (responses are given as strings with items separated by ;)
codes = []
for i in range(len(data)):
    a = data[cols[1]].iloc[i].split(';')
    for c in a:
        codes.append(c)

## find frequency of each item
labels,freqs = np.unique(codes,return_counts=True)

## plot a pie chart in a subplot in the figure
plt.subplot(221)
plt.title('Q1: ' + cols[1].lstrip('Programming experience:'),fontsize=10)

plt.pie(freqs,labels=labels,shadow=True)


# Q2

## extract data (responses are given as strings with items separated by ;)
tasks = []
for i in range(len(data)):
    a = data[cols[2]].iloc[i].split(';')
    for t in a:
        tasks.append(t)

## find frequency of each item
labels,freqs = np.unique(tasks,return_counts=True)

## shorten labels longer than 50 characters
for i in range(len(labels)):
    if len(labels[i])>50:
        labels[i] = labels[i][:50] + '...'

## the bar plot needs the positions of the bars to be specified: 
## we choose uniformly spaced positions
xs = np.arange(len(labels))

## array of indices that sorts the frequencies (to show the responses in
## decreasing frequency order)
s = np.argsort(freqs)[::-1]

## produce bar chart in a subplot
plt.subplot(222)
plt.title('Q2: ' + cols[2].lstrip('Programming experience:'),fontsize=10)

plt.bar(xs,freqs[s],color='r')
plt.xticks(xs,labels[s],rotation=90) # set the labels


# Q3

## extract data (responses are given as strings with items separated by ;)
englevs = []
for i in range(len(data)):
    a = data[cols[3]].iloc[i].split(';')
    for c in a:
        englevs.append(c)

## find frequency of each item
labels,freqs = np.unique(englevs,return_counts=True)

## plot a pie chart in a subplot in the figure
plt.subplot(223)
plt.title('Q3: ' + cols[3],fontsize=10)

plt.pie(freqs,labels=labels,shadow=True)


# save figure
plt.savefig('entry_survey_results.pdf')

# show the figure in an interactive window
plt.show()
