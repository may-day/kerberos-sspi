# -*- coding: utf-8 -*-
import kerberos_sspi as k
import base64
import sys

if sys.version_info >= (3,1)
    def decodestring(stringvalue):
        return base64.decodebytes(stringvalue.encode("ascii"))
    def encodestring(bytesvalue):
        return base64.encodebytes(bytesvalue).decode("utf-8")
    def b(stringvalue):
        return stringvalue.encode("ascii")
    def u(stringvalue):
        return stringvalue
else:
    def decodestring(stringvalue):
        return base64.decodestring(stringvalue)
    def encodestring(bytesvalue):
        return base64.encodestring(bytesvalue)
    def b(stringvalue):
        return stringvalue
    def u(stringvalue):
        return stringvalue.decode("utf-8")

flags=k.GSS_C_CONF_FLAG|k.GSS_C_INTEG_FLAG|k.GSS_C_MUTUAL_FLAG|k.GSS_C_SEQUENCE_FLAG

errc, client = k.authGSSClientInit("test@vm-win7-kraemer", gssflags=flags)

# to run a kerberos enabled server under my account i set as domain admin:
#  setspn -A test/vm-win7-kraemer MYDOMAIN\kraemer
# (might have to wait a few minutes before all DCs in active directory pick it up)
errs, server = k.authGSSServerInit("test@vm-win7-kraemer")

cres = sres= k.AUTH_GSS_CONTINUE
response = ""
round = 0
while sres == k.AUTH_GSS_CONTINUE or cres == k.AUTH_GSS_CONTINUE:

    if cres == k.AUTH_GSS_CONTINUE:
        cres = k.authGSSClientStep(client, response)
        if cres == -1:
            print("clientstep error")
            break
        response = k.authGSSClientResponse(client)
    if sres == k.AUTH_GSS_CONTINUE:
        sres = k.authGSSServerStep(server, response)
        if sres == -1:
            print( "serverstep error")
            break
        response = k.authGSSServerResponse(server)

    print( "round:", round)
    print( "server status :", sres)
    print( "client status :", cres)
    round += 1

if sres == k.AUTH_GSS_COMPLETE and cres == k.AUTH_GSS_COMPLETE:
    print( "client: my username:", k.authGSSClientUserName(client))
    print( "server: who authenticated to me:", k.authGSSServerUserName(server))
    print( "server: my spn:", k.authGSSServerTargetName(server))
    print( "********* encryption test ***********")
    err=k.authGSSClientWrap(client, encodestring(b("Hello")))
    if err == 1:
        encstring=k.authGSSClientResponse(client)
        print( "encstring:", encstring, encodestring(b("Hello")))
        decerr=k.authGSSClientUnwrap(server, encstring)
        if decerr == 1:
          encstring=k.authGSSServerResponse(server)
          print( decodestring(encstring))

    # user case on wrap
    import struct
    import logging
    logging.basicConfig(level=logging.INFO)
    # set max size=1000 and server flags = AUTH_P_NONE|AUTH_P_INTEGRITY|AUTH_P_PRIVACY
    err=k.authGSSClientWrap(client, encodestring(b(struct.pack("!L", 1000 | 0x07000000)+"Hello")), user=u("ümay-day"))
    if err == 1:
        encstring=k.authGSSClientResponse(client)
        print( "encstring:", encstring, encodestring(b("Hello")))
        decerr=k.authGSSClientUnwrap(server, encstring)
        if decerr == 1:
          encstring=k.authGSSServerResponse(server)
          print( decodestring(encstring))


