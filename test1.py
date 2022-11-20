import pandas as pd

df = pd.read_csv('C:/Users/solda/OneDrive/Документы/GitHub/data/Space_Corrected.csv')  #читаем файл

temp = df['Rocket'].dropna()                                                        #преобразовываем стоимость миссии в цифры ( но нам это не надо )
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

def Country(c):                                                                     #достаем страну из локации
    c = c.split(',')
    c = c[-1]
    return c
df["Location"] = df['Location'].apply(Country)

def Status(stat):                                                                   #говорим что если миссия прошла успешно, это 1. А если не успешно то это 0
    if stat == 'Success':
        return float(1)
    else:
        return float(0)
df['Status Mission'] = df['Status Mission'].apply(Status)
# cортировка

temp1 = df[df['Location'] == 'Russia']['Status Mission'].mean()                     #находим средний показатель успешности запуска рокеты
temp2 = df[df['Location'] != 'Russia']['Status Mission'].mean()

temp1 = temp1*100                                                                       # преобразовывае в проценты
temp2 = temp2*100


print(temp1)
print(temp2)
