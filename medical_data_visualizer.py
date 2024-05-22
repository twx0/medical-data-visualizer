import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
def overweight_indicator(bmi):
    if bmi > 25:
        return 1
    else:
        return 0
    
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2).apply(overweight_indicator)

# 3
def health_indicator(value):
    if value == 1:
        return 0
    else:
        return 1

df['cholesterol'] = df['cholesterol'].apply(health_indicator)
df['gluc'] = df['gluc'].apply(health_indicator)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars='cardio', value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    

    # 7
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar').figure


    # 8
    fig = fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & 
                (df['height'] >= df['height'].quantile(0.025)) & 
                (df['height'] <= df['height'].quantile(0.975)) & 
                (df['weight'] >= df['weight'].quantile(0.025)) & 
                (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # 14
    fig, ax = plt.subplots(figsize=(12, 12))

    # 15
    sns.heatmap(corr, annot=True, fmt='.1f', linewidths=1, mask=mask, square=True, cbar_kws={'shrink': 0.5})


    # 16
    fig.savefig('heatmap.png')
    return fig
