#!/usr/bin/env python

from distutils.core import setup

setup(name='dumb_tf_loadbalance',
      version='0.0.1',
      description='The stupidest way to do load balancing with Tensorflow.',
      author='Gavin Gray',
      author_email='g.d.b.gray@sms.ed.ac.uk',
      packages=['dumb_tf_loadbalance'],
      install_requires=['nvidia-ml-py']
)
