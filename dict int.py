Employe = {
    'Alice': {
        'Location': 'Mumbai'
        },
    'Beth': {
        'phone': 9102
        },
    'Randy': {
        'salary': 50000,
        }}

n = 'salary'

for k,v in Employe.items():
    if n in v:
        print(v[n])



print(Employe['Randy']['salary'])
