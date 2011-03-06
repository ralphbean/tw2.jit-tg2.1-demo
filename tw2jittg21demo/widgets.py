
from tw2jittg21demo import model
from tw2.jit import SQLARadialGraph

def makeUserGraph():
    class UserGraph(SQLARadialGraph):
        id = 'whatever'
        base_url = '/jit_data'
        entities = [model.User, model.Group, model.Permission]
        excluded_columns = ['_password', 'password',
                            'user_id', 'group_id', 'permission_id']
        width = '980'
        height = '980'
        rootObject = model.User.query.first()
    
    return UserGraph
