# -*- coding: utf-8 -*-
"""Setup the tw2.jit-tg2.1-demo application"""

import logging

from tw2jittg21demo.config.environment import load_environment

__all__ = ['setup_app']

log = logging.getLogger(__name__)

from schema import setup_schema
import bootstrap

def setup_app(command, conf, vars):
    """Place any commands to setup tw2jittg21demo here"""
    load_environment(conf.global_conf, conf.local_conf)
    setup_schema(command, conf, vars)
    bootstrap.bootstrap(command, conf, vars)
