# @ohos.net.socket(Socket Connection)

The **socket** module implements data transfer over TCP, UDP, Web, and TLS socket connections.

> **NOTE：**&gt;
> You are advised to call the APIs of this module in the worker thread or taskpool to perform network-related
> operations. Otherwise, the UI thread may be suspended.

**Since:** 7

**System capability:** SystemCapability.Communication.NetStack

## Modules to Import

```TypeScript
import { socket } from 'kits/@kit.NetworkKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [constructLocalSocketInstance(Socket Connection)](arkts-network-socket-constructlocalsocketinstance-f.md) |
| [constructLocalSocketServerInstance(Socket Connection)](arkts-network-socket-constructlocalsocketserverinstance-f.md) |
| [constructMulticastSocketInstance(Socket Connection)](arkts-network-socket-constructmulticastsocketinstance-f.md) |
| [constructTCPSocketInstance(Socket Connection)](arkts-network-socket-constructtcpsocketinstance-f.md) |
| [constructTCPSocketServerInstance(Socket Connection)](arkts-network-socket-constructtcpsocketserverinstance-f.md) |
| [constructTLSSocketInstance(Socket Connection)](arkts-network-socket-constructtlssocketinstance-f.md) |
| [constructTLSSocketInstance(Socket Connection)](arkts-network-socket-constructtlssocketinstance-f.md) |
| [constructTLSSocketServerInstance(Socket Connection)](arkts-network-socket-constructtlssocketserverinstance-f.md) |
| [constructUDPSocketInstance(Socket Connection)](arkts-network-socket-constructudpsocketinstance-f.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ExtraOptionsBase(Socket Connection)](arkts-network-socket-extraoptionsbase-i.md) |
| [LocalAddress(Socket Connection)](arkts-network-socket-localaddress-i.md) |
| [LocalConnectOptions(Socket Connection)](arkts-network-socket-localconnectoptions-i.md) |
| [LocalSendOptions(Socket Connection)](arkts-network-socket-localsendoptions-i.md) |
| [LocalSocket(Socket Connection)](arkts-network-socket-localsocket-i.md) |
| [LocalSocketConnection(Socket Connection)](arkts-network-socket-localsocketconnection-i.md) |
| [LocalSocketMessageInfo(Socket Connection)](arkts-network-socket-localsocketmessageinfo-i.md) |
| [LocalSocketServer(Socket Connection)](arkts-network-socket-localsocketserver-i.md) |
| [MulticastSocket(Socket Connection)](arkts-network-socket-multicastsocket-i.md) |
| [ProxyOptions(Socket Connection)](arkts-network-socket-proxyoptions-i.md) |
| [SocketMessageInfo(Socket Connection)](arkts-network-socket-socketmessageinfo-i.md) |
| [SocketRemoteInfo(Socket Connection)](arkts-network-socket-socketremoteinfo-i.md) |
| [SocketStateBase(Socket Connection)](arkts-network-socket-socketstatebase-i.md) |
| [TCPConnectOptions(Socket Connection)](arkts-network-socket-tcpconnectoptions-i.md) |
| [TCPExtraOptions(Socket Connection)](arkts-network-socket-tcpextraoptions-i.md) |
| [TCPSendOptions(Socket Connection)](arkts-network-socket-tcpsendoptions-i.md) |
| [TCPSocket(Socket Connection)](arkts-network-socket-tcpsocket-i.md) |
| [TCPSocketConnection(Socket Connection)](arkts-network-socket-tcpsocketconnection-i.md) |
| [TCPSocketServer(Socket Connection)](arkts-network-socket-tcpsocketserver-i.md) |
| [TLSConnectOptions(Socket Connection)](arkts-network-socket-tlsconnectoptions-i.md) |
| [TLSSecureOptions(Socket Connection)](arkts-network-socket-tlssecureoptions-i.md) |
| [TLSSocket(Socket Connection)](arkts-network-socket-tlssocket-i.md) |
| [TLSSocketConnection(Socket Connection)](arkts-network-socket-tlssocketconnection-i.md) |
| [TLSSocketServer(Socket Connection)](arkts-network-socket-tlssocketserver-i.md) |
| [UDPExtraOptions(Socket Connection)](arkts-network-socket-udpextraoptions-i.md) |
| [UDPSendOptions(Socket Connection)](arkts-network-socket-udpsendoptions-i.md) |
| [UDPSocket(Socket Connection)](arkts-network-socket-udpsocket-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Protocol(Socket Connection)](arkts-network-socket-protocol-e.md) |
| [ProxyTypes(Socket Connection)](arkts-network-socket-proxytypes-e.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [X509CertRawData(Socket Connection)](arkts-network-socket-x509certrawdata-t.md) |
