#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **********************************************************************
#
# Copyright (c) 2003-2011 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

import os, sys

path = [ ".", "..", "../..", "../../..", "../../../.." ]
head = os.path.dirname(sys.argv[0])
if len(head) > 0:
    path = [os.path.join(head, p) for p in path]
path = [os.path.abspath(p) for p in path if os.path.exists(os.path.join(p, "scripts", "TestUtil.py")) ]
if len(path) == 0:
    raise RuntimeError("can't find toplevel directory!")
sys.path.append(os.path.join(path[0], "scripts"))
import TestUtil

#
# Write config
#
if sys.version_info[0] == 2:
    configPath = "./config/\xe4\xb8\xad\xe5\x9b\xbd_client.config".decode("utf-8")
    TestUtil.createConfig(configPath, 
                          ["# Automatically generated by Ice test driver.", 
                           "Ice.Trace.Protocol=1",
                           "Ice.Trace.Network=1", 
                           "Ice.ProgramName=PropertiesClient", 
                           "Config.Path=./config/中国_client.config"])
else:
    configPath = "./config/\u4e2d\u56fd_client.config"
    TestUtil.createConfig(configPath, 
                          ["# Automatically generated by Ice test driver.", 
                           "Ice.Trace.Protocol=1",
                           "Ice.Trace.Network=1", 
                           "Ice.ProgramName=PropertiesClient", 
                           "Config.Path=" + configPath],
                           "utf-8")

TestUtil.simpleTest()

if os.path.exists(configPath):
    os.remove(configPath)
