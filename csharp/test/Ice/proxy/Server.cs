// **********************************************************************
//
// Copyright (c) 2003-2017 ZeroC, Inc. All rights reserved.
//
// This copy of Ice is licensed to you under the terms described in the
// ICE_LICENSE file included in this distribution.
//
// **********************************************************************

using System;
using System.Reflection;

[assembly: CLSCompliant(true)]

[assembly: AssemblyTitle("IceTest")]
[assembly: AssemblyDescription("Ice test")]
[assembly: AssemblyCompany("ZeroC, Inc.")]

public class Server : TestCommon.Application
{
    public override int run(string[] args)
    {
        //
        // We don't want connection warnings because of the timeout test.
        //
        communicator().getProperties().setProperty("Ice.Warn.Connections", "0");
        communicator().getProperties().setProperty("Ice.Warn.Dispatch", "0");

        communicator().getProperties().setProperty("TestAdapter.Endpoints", getTestEndpoint(0) + ":udp");
        Ice.ObjectAdapter adapter = communicator().createObjectAdapter("TestAdapter");
        adapter.add(new MyDerivedClassI(), Ice.Util.stringToIdentity("test"));
        adapter.activate();

        communicator().waitForShutdown();
        return 0;
    }

    public static int Main(string[] args)
    {
        Server app = new Server();
        return app.runmain(args);
    }
}
