# Здесь должен быть твой код
import pandas as pd

df = pd.read_csv('C:/Users/solda/Music/GitHub/ML/ML/titanic.csv')

df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], inplace=True, axis=1)

age_1 = df[df['Pclass'] == 1]['Age'].median()
age_2 = df[df['Pclass'] == 2]['Age'].median()
age_3 = df[df['Pclass'] == 3]['Age'].median()

def fill_age(row):
    if pd.isnull(row['Age']):
        if row['Pclass'] == 1:
            return age_1
        elif row['Pclass'] == 2:
            return age_2
        else:
            return age_3
    else:
        return row['Age']

df['Age'] = df.apply(fill_age, axis=1)

df['Embarked'].fillna('S', inplace=True)

def fill_sex(sex):
    if sex == 'male':
        return 0
    else:
        return 1

df['Sex'] = df['Sex'].apply(fill_sex)

# print(df['Embarked'].value_counts())
df[list(pd.get_dummies(df['Embarked']).columns)] = pd.get_dummies(df['Embarked'])
df.drop('Embarked', axis=1, inplace=True)

df.info()