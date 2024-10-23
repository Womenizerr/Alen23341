import random
ad = []
da = []
with open(f'questions.txt','r',encoding='utf-8') as file:
    m = file.readlines()
    for line in m:
        ad.append(line.strip())
with open(f'response.txt','r',encoding='utf-8') as my_file:
    data = my_file.readlines()
    for line in data:
        da.append(line.strip())
g_ad = random.randint(0, len(ad)-1)
g_da = random.randint(0, len(da)-1)
print('Question')
print(ad[g_ad])
print('Response')
print(ad[g_da])
