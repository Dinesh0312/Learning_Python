
authorized_users = {'nikhil':'1234','ram':'2345','anil':'3456'}

@authorized
def get_acess(username,password):
    return 'acessed'

@authorized()
def get_logs(username,password):
    return 'loged'

def authorized(func):

    def wrapper(username,password):
        if username in authorized_users.keys():
            if password == authorized_users[username]:
                return func(username,password)
        return 'Not authorized!'
    return wrapper


print(get_logs('nikhil',''))



