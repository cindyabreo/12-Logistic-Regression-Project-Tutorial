import pandas as pd 

url = 'https://raw.githubusercontent.com/4GeeksAcademy/logistic-regression-project-tutorial/main/bank-marketing-campaign-data.csv'
df = pd.read_csv(url, header=0, sep=";")

df.head(5)

df.info()

df.describe()

df.isnull().sum()

sns.countplot(x=df['y'], data=df)
plt.show()

plt.figure(figsize=(15,10))
sns.countplot(x=df['job'],data=df)
plt.show()

plt.figure(figsize=(15,10))
sns.countplot(x=df['job'],data=df,hue=df['y'])
plt.show()

plt.figure(figsize=(15,10))
sns.countplot(x=df['month'],data=df)
plt.show()

plt.figure(figsize=(15,10))
sns.countplot(x=df['month'],data=df,hue=df['y'])
plt.show()

df=df.drop_duplicates()

df['job'].value_counts()
df['job'].replace('unknown', df['job'].value_counts().idxmax() , inplace = True)

df['marital'].value_counts()
df['marital'].replace('unknown', df['marital'].value_counts().idxmax() , inplace = True)

df['education'].value_counts()
df['education'].replace('unknown', df['education'].value_counts().idxmax() , inplace = True)

df['default'].value_counts()
df['default'].replace('unknown', df['default'].value_counts().idxmax() , inplace = True)

df['housing'].value_counts()
df['housing'].replace('unknown', df['housing'].value_counts().idxmax() , inplace = True)

df['housing'].value_counts()
df['housing'].replace('unknown', df['housing'].value_counts().idxmax() , inplace = True)

df['loan'].value_counts()
df['loan'].replace('unknown', df['loan'].value_counts().idxmax() , inplace = True)

round(df['duration'].mean())
df['duration'].replace('unknown', round(df['duration'].mean()) , inplace = True)

df['campaign'].mean()
df['campaign'].replace('unknown', round(df['campaign'].mean()) , inplace = True)

df['pdays'].mean()
df['pdays'].replace('unknown', round(df['pdays'].mean()) , inplace = True)

df['previous'].replace('unknown', round(df['previous'].mean()) , inplace = True)

out_age= df['age'].describe()
print(out_age)

IQR = out_age['75%']-out_age['25%']
upper = out_age['75%'] + 1.5*IQR
lower = out_age['25%'] - 1.5*IQR
print('The upper & lower bounds for suspected outliers are {} and {}.'.format(upper,lower))

grupo_edad = pd.cut(df['age'],bins=[10,20,30,40,50,60,70,80,90,100],
                    labels=['10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-89','90-100'])

#inserting the new column
df.insert(1,'grupo_edad',grupo_edad)

#dropping age column
df.drop('age',axis=1,inplace=True)