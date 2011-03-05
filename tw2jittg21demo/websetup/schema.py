# -*- coding: utf-8 -*-
"""Setup the tw2.jit-tg2.1-demo application"""

import logging
import transaction
from tg import config

def setup_schema(command, conf, vars):
    """Place any commands to setup tw2jittg21demo here"""
    # Load the models

    # <websetup.websetup.schema.before.model.import>
    from tw2jittg21demo import model
    # <websetup.websetup.schema.after.model.import>

    
    # <websetup.websetup.schema.before.metadata.create_all>
    print "Creating tables"
    model.metadata.create_all(bind=config['pylons.app_globals'].sa_engine)
    # <websetup.websetup.schema.after.metadata.create_all>
    transaction.commit()
