import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('diabetes.csv')

#print(df.head())
# shows interesting facts about age group, missing values, and bell curves
# df.hist(figsize=(10,7))
# plt.show()

# for col in df.columns:
#     sns.scatterplot(x=col, y='Glucose', data=df, hue="Outcome")
#     plt.show()

for col in df.columns:
    sns.distplot(df.loc[df.Outcome == 0][col], hist=False, kde_kws={"linestyle":"-", "color":"black", "label": "No Diabetes"})
    sns.distplot(df.loc[df.Outcome == 1][col], hist=False, kde_kws={"linestyle":"--", "color":"red", "label": "Diabetes"})

    plt.show()
