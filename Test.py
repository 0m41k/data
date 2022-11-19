import pandas as pd
df = pd.read_csv('C:/Users/solda/Music/Pytion/DataScince/Project/Space_Corrected.csv')



temp = df['Rocket'] = df['Rocket'].dropna()
def cost_to_float(cost):
    cost = cost.replace(',', '')
    return float(cost)
temp = temp.apply(cost_to_float)
median_cost = temp.median()
def fill_rocket(rocket):
    if pd.isnull(rocket):
        return median_cost
    else:
        rocket = rocket.replace(',', '')
        return float(rocket)
df['Rocket'] = df['Rocket'].apply(fill_rocket)
df['Rocket'].fillna(median_cost, inplace=True)



def Country(c):
    c = c.split(',')
    c = c[-1]
    return c
df["Location"] = df['Location'].apply(Country)



def Status(stat):
    if stat == 'Success':
        return float(1)
    else:
        return float(0)
df['Status Mission'] = df['Status Mission'].apply(Status)
# cортировка

temp1 = df[df['Location'] == 'Russia']['Status Mission'].mean()
temp2 = df[df['Location'] != 'Russia']['Status Mission'].mean()

temp1 = temp1*100
temp2 = temp2*100


print(temp1)
print(temp2)

df['Status Mission'].head(50)