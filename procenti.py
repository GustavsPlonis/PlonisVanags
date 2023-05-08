# Izveidoju funkciju, lai izreiķinātu procentus
def procentu_formula(pareizi, kopa):
    procenti = (pareizi / kopa) * 100
    return procenti
# Izrēķinu procentus un to noapaļo
kopa = pareizi+nepareizi
procenti = procentu_formula(pareizi, kopa)
noapaloti_procenti = math.ceil(procenti)
print('Tava precizitāte bija '"{}%".format(noapaloti_procenti))

            
   