import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import pandas as pd

# this is called aliasing
# aliasing is used to call modules or libraries into a shorter form variable

import seaborn as sns
# a high level interface for plotting
# a beautifier for your plots and graphs

# This is the syntax on how you will open your data
df = pd.read_csv('all.csv', header = None, names = ['rating', 'review_count', 'isbn', 'booktype', 'author_url', 'year', 'genre_url',  'dir', 'rating_count', 'name'])

print (df.head)
print (df.dtypes)
print (df.shape)
print (df.rating.mean(), df.rating.std())
print (df.query("rating > 4.5"))

print (df[df.rating_count.isnull()])
print (df[df.review_count.isnull()])
print (df[df.year.isnull()])

df = df[df.year.notnull()]
print (df.shape)

df['rating_count'] = df.rating_count.astype(int)
df['review_count'] = df.review_count.astype(int)
df['year'] = df.year.astype(int)

print (df.dtypes)

# The last df is now cleaned and you can do more about it.