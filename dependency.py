# -*- coding: utf-8 -*-
# author: Tac
# contact: gzzhanghuaxiong@corp.netease.com

import os
import platform

# 依赖库
_DEPENDENCY = [
    'wheel',
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
            install_name = get_install_name(lib_name)
            if os.system('py -2.7 -m pip install %s' % install_name):
                logger.info('py -2.7 -m pip install %s FAILED, try python', install_name)
                if os.system('python -m pip install %s' % install_name):
                    logger.error('python -m pip install %s FAILED, try pip', install_name)
                    if os.system('pip install %s' % install_name):
                        logger.log_last_except()
                        exit(1)
            __import__(lib_name)


def get_install_name(lib_name):
    """
    获取第三方库的安装名
    Args:
        lib_name: [str]库名
    Returns:
        安装名
    """
    if lib_name != 'PyQt4':
        return lib_name
    if platform.architecture()[0].startswith('32'):
        return 'PyQt4-4.11.4-cp27-cp27m-win32.whl'
    return 'PyQt4-4.11.4-cp27-cp27m-win_amd64.whl'
