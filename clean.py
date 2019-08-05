import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
from datetime import datetime

import glob

path = r'/Users/twochanz/capterra/data' # use your path
all_files = glob.glob(path + "/*.xlsx")

li = []

for filename in all_files:
    df = pd.read_excel(filename, index_col=None, header=0, encoding='iso-8859-1')
    li.append(df)

reviews = pd.concat(li, axis=0, ignore_index=True)

df = reviews.copy()

def after_comma(x):
    try:
        return str(re.match(".*,\s(\d+-\d+)\s.+", x).group(1))
    except:
        return ""

def before_comma(x):
    try:
        return str(re.match("(.*),", x).group(1))
    except:
        return ""

df['source'] = df['source'].str.replace('Source: ?', "")
df['usage'][df['usage'].str.find('Used the software for: ') == -1] = ""
df['usage'] = df['usage'].str.replace('Used the software for: ?', "")
df['comments'] = df['comments'].str.replace('Comments: ?', "")
df['pros'] = df['pros'].str.replace('Pros: ?', "")
df['cons'] = df['cons'].str.replace('Cons: ?', "")
df['overall'] = df['overall'].str.replace('Overall: ?', "")
df['recommendations to other buyers'] = df['recommendations to other buyers'].str.replace('Recommendations to other buyers: ?', "")
df['employees'] = df['industry'].map(after_comma)
df['industry'] = df['industry'].map(before_comma)


df.to_csv('./cleaned.csv')