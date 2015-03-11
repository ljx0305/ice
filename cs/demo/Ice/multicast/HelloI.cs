// **********************************************************************
//
// Copyright (c) 2003-2011 ZeroC, Inc. All rights reserved.
//
// This copy of Ice is licensed to you under the terms described in the
// ICE_LICENSE file included in this distribution.
//
// **********************************************************************

using Demo;

public class HelloI : HelloDisp_
{
    public override void
    sayHello(Ice.Current current)
    {
        System.Console.Out.WriteLine("Hello World!");
    }
}