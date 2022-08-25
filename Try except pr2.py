
def devide(x,y):
    try:
        result = x/y
    except Exception as e:
        print("Sorry ! You are dividing by zero ",e)
    else:
        print("Yeah ! Your answer is :", result)
    finally:
        print('This is always executed')


devide(5,2)
devide(4,0)