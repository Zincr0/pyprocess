# -*- coding= utf-8 -*-
import commands, sys
from setproctitle import setproctitle

reload(sys)
sys.setdefaultencoding('utf-8')

def setSingleProcess(ProcName):
    """
    Set process name only if not exists.
    """
    proclist = commands.getoutput('ps -A')
    if ProcName in proclist:
        return False
    else:
        setproctitle(ProcName)
        return True
