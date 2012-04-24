#!/usr/bin/env python
# **********************************************************************
#
# Copyright (c) 2003-2011 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

import sys, os

path = [ ".", "..", "../..", "../../..", "../../../.." ]
head = os.path.dirname(sys.argv[0])
if len(head) > 0:
    path = [os.path.join(head, p) for p in path]
path = [os.path.abspath(p) for p in path if os.path.exists(os.path.join(p, "demoscript")) ]
if len(path) == 0:
    raise RuntimeError("can't find toplevel directory!")
sys.path.append(path[0])

from demoscript import Util
from demoscript.IceBox import hello

# Override the service load line.
if Util.defaultHost:
    args = ' --IceBox.Service.Hello="HelloServiceI --Ice.Config=config.service %s"' % Util.defaultHost
else:
    args = ''

server = Util.spawn('java IceBox.Server --Ice.Config=config.icebox --Ice.PrintAdapterReady %s' % (args))
server.expect('.* ready')
client = Util.spawn('java Client')
client.expect('.*==>')

hello.run(client, server)
