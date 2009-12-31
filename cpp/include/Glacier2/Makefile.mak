# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

top_srcdir	= ..\..

!include $(top_srcdir)/config/Make.rules.mak

install::
	@if not exist "$(install_includedir)\Glacier2" \
	    @echo "Creating $(install_includedir)\Glacier2..." && \
	    mkdir "$(install_includedir)\Glacier2"

	@for %i in ( *.h ) do \
	    @echo Installing %i && \
	    copy %i "$(install_includedir)\Glacier2"
