import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('C:/Users/solda/Music/GitHub/data/Space_Corrected.csv')  #читаем файл

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

temp1 = df[(df['Location'] == ' Russia') | (df['Location'] == ' Kazakhstan')]['Status Mission'].mean()                     #находим средний показатель успешности запуска рокеты
temp2 = df[df['Location'] == ' USA']['Status Mission'].mean()
temp4 = df[df['Location'] == ' France']['Status Mission'].mean()
temp5 = df[df['Location'] == ' China']['Status Mission'].mean()
temp6 = df[df['Location'] == ' Japan']['Status Mission'].mean()

cost1 = df[(df['Location'] == ' Russia') | (df['Location'] == ' Kazakhstan')]['Rocket'].mean()                     #находим средний показатель цены запуска рокеты
cost2 = df[df['Location'] == ' USA']['Rocket'].mean()
cost4 = df[df['Location'] == ' France']['Rocket'].mean()
cost5 = df[df['Location'] == ' China']['Rocket'].mean()
cost6 = df[df['Location'] == ' Japan']['Rocket'].mean()

temp1 = temp1*100                                                                       # преобразовывае в проценты
temp2 = temp2*100
temp4 = temp4*100
temp5 = temp5*100
temp6 = temp6*100

final1 = temp1/cost1
final2 = temp2/cost2
final4 = temp4/cost4
final5 = temp5/cost5
final6 = temp6/cost6

print('    Russia:', temp1, '  ', cost1, '  ', final1)
print('       USA:', temp2, '  ', cost2, ' ', final2)
print('    France:', temp4, '  ', cost4, '   ', final4)
print('     China:', temp5, '  ', cost5, '  ', final5)
print('     Japan:', temp6, '  ', cost6, '  ', final6)


s5 = pd.Series(data = [final1, final2, final4, final5, final6], index = ['Russia', 'USA', 'France', 'China', 'Japan'])
s5.plot(kind = 'pie', autopct='%.2f', shadow=True)
plt.show()
#результаты
