#Three lines of code to make the compiler draw

import sys
import matplotlib
matplotlib.use('Agg')

import pandas as pd
impot matplotlib.pyplot as plt


df = pd.read_csv('data.csv')
df['Duration'].plot(kind = 'hist')

plt.show()

# Two lines of code to make the compiler draw

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

