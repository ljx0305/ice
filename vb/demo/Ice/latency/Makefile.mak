# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

top_srcdir	= ..\..\..

TARGETS		= client.exe server.exe

C_SRCS		= Client.vb
S_SRCS		= Server.vb

GEN_SRCS	= $(GDIR)\Latency.cs

SLICE_SRCS	= $(SDIR)/Latency.ice

SLICE_ASSEMBLY  = latencySlice.dll

SDIR		= .

GDIR		= generated

!include $(top_srcdir)\config\Make.rules.mak.vb

VBCFLAGS	= $(VBCFLAGS) -target:exe

client.exe: $(C_SRCS) $(SLICE_ASSEMBLY)
	$(VBC) $(VBCFLAGS) -out:$@ -r:"$(csbindir)\Ice.dll" -r:$(SLICE_ASSEMBLY) $(C_SRCS)

server.exe: $(S_SRCS) $(SLICE_ASSEMBLY)
	$(VBC) $(VBCFLAGS) -out:$@ -r:"$(csbindir)\Ice.dll" -r:$(SLICE_ASSEMBLY) $(S_SRCS)

!include .depend.mak
