# -*- coding: utf-8 -*-
# author: Tac
# contact: gzzhanghuaxiong@corp.netease.com

import os

# 依赖库
_DEPENDENCY = [
    'PyQt4',
]


def check_dependency():
    """
    检查第三方依赖库
    为用户安装第三方依赖库
    Returns:
        None
    """
    for lib_name in _DEPENDENCY:
        try:
            __import__(lib_name)
        except ImportError:
            from py_chakura import logger
            if os.system('py -2.7 -m pip install %s' % lib_name):
                logger.info('py -2.7 -m pip install %s FAILED, try python', lib_name)
                if os.system('python -m pip install %s' % lib_name):
                    logger.error('python -m pip install %s FAILED!!!', lib_name)
                    logger.log_last_except()
                    exit(1)
            __import__(lib_name)
