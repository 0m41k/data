import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/solda/Music/GitHub/Kyrc/train.csv')

def fix_people_main(people_main):
    if people_main == 'False':
        return 0
    else:
        return int(people_main)

df['life_main'] = df['life_main'].apply(fix_people_main)
summ = 0
for i in range(0, 9):
    bad = df[(df['result'] == 0) & (df['life_main'] == i)]
    well = df[(df['result'] == 1) & (df['life_main'] == i)]
    bad = len(bad)
    well = len(well)
    procent = well / (bad + well) * 100
    summ += procent
    print('Life_main = {}, well procent = {}%'.format(i, round(procent, 2)))

print('Average = {}%'.format(round(summ / 7, 2)))
