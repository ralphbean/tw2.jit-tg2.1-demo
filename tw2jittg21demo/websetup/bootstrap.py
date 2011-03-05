# -*- coding: utf-8 -*-
"""Setup the tw2.jit-tg2.1-demo application"""

import logging
from tg import config
from tw2jittg21demo import model

import transaction

from random import choice, randint

def add_random_users():
    """ Add 9 random users """
    import string
    chars = string.letters
    for first in [u'Sally', u'John', u'Tim']:
        for last in [u'Anderson', u'Flanderson', u'Block']:
            user = model.User()
            user.user_name = unicode((first[0] + last).lower())
            user.display_name = u'%s %s' % (first, last)
            user.email_address = u'%s@socialistworker.org' % user.user_name
            user.password = u''.join([choice(chars) for i in range(12)])
            model.DBSession.add(user)

    model.DBSession.flush()

def add_random_groups():
    """ Generate a number of random groups and add users to them """
    for name in ['developer', 'system admin', 'shmeveloper', 'crispin gladbin']:
        group = model.Group()
        group.group_name = name
        group.display_name = (u"%ss group" % name).title()
        model.DBSession.add(group)

        all_users = model.User.query.all()
        for i in range(randint(0, len(all_users)-2)):
            user = choice(all_users)
            while user in group.users:
                user = choice(all_users)
            
            group.users.append(user)


    model.DBSession.flush()

def bootstrap(command, conf, vars):
    """Place any commands to setup tw2jittg21demo here"""

    # <websetup.bootstrap.before.auth
    from sqlalchemy.exc import IntegrityError
    try:
        u = model.User()
        u.user_name = u'manager'
        u.display_name = u'Example manager'
        u.email_address = u'manager@somedomain.com'
        u.password = u'managepass'
    
        model.DBSession.add(u)
    
        g = model.Group()
        g.group_name = u'managers'
        g.display_name = u'Managers Group'
    
        g.users.append(u)
    
        model.DBSession.add(g)
    
        p = model.Permission()
        p.permission_name = u'manage'
        p.description = u'This permission give an administrative right to the bearer'
        p.groups.append(g)
    
        model.DBSession.add(p)
    
        u1 = model.User()
        u1.user_name = u'editor'
        u1.display_name = u'Example editor'
        u1.email_address = u'editor@somedomain.com'
        u1.password = u'editpass'
    
        model.DBSession.add(u1)
        model.DBSession.flush()

        add_random_users()
        add_random_groups()

        transaction.commit()
    except IntegrityError:
        print 'Warning, there was a problem adding your auth data, it may have already been added:'
        import traceback
        print traceback.format_exc()
        transaction.abort()
        print 'Continuing with bootstrapping...'
        

    # <websetup.bootstrap.after.auth>
