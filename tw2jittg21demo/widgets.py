
from tw2jittg21demo import model
from tw2.jit import SQLARadialGraph
from tw2.core import JSSymbol

def makeUserGraph():
    class UserGraph(SQLARadialGraph):
        id = 'whatever'
        base_url = '/jit_data'
        entities = [model.User, model.Group, model.Permission]
        excluded_columns = ['_password', 'password',
                            'user_id', 'group_id', 'permission_id']
        width = '920'
        height = '525'
        rootObject = model.User.query.first()

        # Try to match colors to the TG banner
        backgroundcolor = '#FFFFFF'
        background = { 'CanvasStyles': { 'strokeStyle' : '#FFFFFF' } }
        Node = { 'color' : '#ffcb2f' }
        Edge = { 'color' : '#307e8a', 'lineWidth':1.5, }

        # Override the label style
        onPlaceLabel = JSSymbol(src="""
            (function(domElement, node){
                domElement.style.display = "none";
                domElement.innerHTML = node.name;
                domElement.style.display = "";
                var left = parseInt(domElement.style.left);
                domElement.style.width = '120px';
                domElement.style.height = '';
                var w = domElement.offsetWidth;
                domElement.style.left = (left - w /2) + 'px';

                domElement.style.cursor = 'pointer';
                if ( node._depth <= 1 )
                    domElement.style.color = 'black';
                else
                    domElement.style.color = 'grey';
            })""")

    return UserGraph
