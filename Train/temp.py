import pandas as pd
df = pd.read_csv('C:/Users/solda/Music/GitHub/Kyrc/train.csv')

df.drop(['id','city','followers_count','relation','city','last_seen','career_end','career_start','occupation_type', 'occupation_name', 'graduation'], inplace=True, axis=1 )

# mobile
def mobile(m):
    if m == 1.0:
        return 1
    if m == 0.0:
        return 0
df['has_mobile'] = df['has_mobile'].apply(mobile)

# sex
def sexi(s):
    if s == 1:
        return (0)
    elif s == 2:
        return (1)
df['sex'] = df['sex'].apply(sexi)

# ed_form
df[list(pd.get_dummies(df['education_form']).columns)] = pd.get_dummies(df['education_form'])
df.drop('education_form', axis=1, inplace=True)

# ed_stat
def stat(s):
    if s == 'PhD':
        return 'PhD'
    elif s == 'Undergraduate applicant':
        return 'Undergraduate applicant'
    elif s == 'Candidate of Sciences':
        return 'Candidate of Sciences'
    else:
        s = s.split(' ')
        s = s[0]
        return s
df['education_status']  = df['education_status'].apply(stat)
df[list(pd.get_dummies(df['education_status']).columns)] = pd.get_dummies(df['education_status'])
df.drop('education_status', axis=1, inplace=True)

# langs
def lan(l):
    l = l.split(';')
    for i in l:
        if i == 'English':
            a = 1
        else:
            a = 0
    if a == 1:
        return 1
    else:
        return 0
df['langs'] = df['langs'].apply(lan)

# life_main 
def life(l):
    if l == 0 or l == 6 or l == 7:
        return "50+life"
    else:
        return '50-Life'
df['life_main'] = df['life_main'].apply(life)
df[list(pd.get_dummies(df['life_main']).columns)] = pd.get_dummies(df['life_main'])
df.drop('life_main', axis=1, inplace=True)

# people_main
def people(po):
    if po == '3':
        return "people_3"
    elif po == '4':
        return "people_4"
    else:
        return "0"
df['people_main'] = df['people_main'].apply(people)
df[list(pd.get_dummies(df['people_main']).columns)] = pd.get_dummies(df['people_main'])
df.drop('people_main', axis=1, inplace=True)
df.drop('0', axis=1,inplace=True)

# date
import numpy as np
def date(d):
    try:
        d = d.split('.')
    except:
        return np.nan   
    if len(d) == 3:
        b = d[-1]
        b = int(b)
        b = 2022 - b
        if b>0 and b<11:
            return '1-10'
        elif b>10 and b<21:
            return '11-20'
        elif b>20 and b<31:
            return '21-30'
        elif b>30 and b<41:
            return '31-40'
        elif b>40 and b<51:
            return '41-50'
        elif b>50 and b<61:
            return '51-60'
        else:
            return np.nan
    else :
        return np.nan
df['bdate'] = df['bdate'].apply(date)
df['bdate'] = df['bdate'].dropna()

def replacing(row):
    if row['Alumnus'] == 1:
        row['bdate'] = '31-40'
    elif row['Student'] == 1:
        row['bdate'] = '31-40'
    elif row['PhD'] == 1:
        row['bdate'] = '31-40'
    elif row['Undergraduate applicant'] == 1:
        row['bdate'] = '31-40'
    elif row['Candidate of Sciences'] == 1:
        row['bdate'] = '41-50'
    return row
df = df.apply(replacing, axis=1)
df[list(pd.get_dummies(df['bdate']).columns)] = pd.get_dummies(df['bdate'])
df.drop('bdate', axis=1, inplace=True)

# Scalern
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

x = df.drop('result', axis = 1)
y = df['result']

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.25)

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)
percent = accuracy_score(y_test, y_pred) *100
print(f'Успешность модели: {percent} %')