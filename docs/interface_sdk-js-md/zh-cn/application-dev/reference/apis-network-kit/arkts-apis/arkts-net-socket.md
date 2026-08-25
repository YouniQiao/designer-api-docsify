# @ohos.net.socket(Socket连接)

本模块提供利用Socket进行数据传输的能力，支持TCPSocket、UDPSocket、WebSocket和TLSSocket。

> **说明：**&gt;
> 本模块API使用时建议放在worker线程或者taskpool中做网络操作，否则可能会导致UI线程卡顿。

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为7。

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { socket } from '@kit.NetworkKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [constructLocalSocketInstance(Socket连接)](arkts-network-socket-constructlocalsocketinstance-f.md) |
| [constructLocalSocketServerInstance(Socket连接)](arkts-network-socket-constructlocalsocketserverinstance-f.md) |
| [constructMulticastSocketInstance(Socket连接)](arkts-network-socket-constructmulticastsocketinstance-f.md) |
| [constructTCPSocketInstance(Socket连接)](arkts-network-socket-constructtcpsocketinstance-f.md) |
| [constructTCPSocketServerInstance(Socket连接)](arkts-network-socket-constructtcpsocketserverinstance-f.md) |
| [constructTLSSocketInstance(Socket连接)](arkts-network-socket-constructtlssocketinstance-f.md) |
| [constructTLSSocketInstance(Socket连接)](arkts-network-socket-constructtlssocketinstance-f.md) |
| [constructTLSSocketServerInstance(Socket连接)](arkts-network-socket-constructtlssocketserverinstance-f.md) |
| [constructUDPSocketInstance(Socket连接)](arkts-network-socket-constructudpsocketinstance-f.md) |

### 接口

| 名称 |
| --- |
| [ExtraOptionsBase(Socket连接)](arkts-network-socket-extraoptionsbase-i.md) |
| [LocalAddress(Socket连接)](arkts-network-socket-localaddress-i.md) |
| [LocalConnectOptions(Socket连接)](arkts-network-socket-localconnectoptions-i.md) |
| [LocalSendOptions(Socket连接)](arkts-network-socket-localsendoptions-i.md) |
| [LocalSocket(Socket连接)](arkts-network-socket-localsocket-i.md) |
| [LocalSocketConnection(Socket连接)](arkts-network-socket-localsocketconnection-i.md) |
| [LocalSocketMessageInfo(Socket连接)](arkts-network-socket-localsocketmessageinfo-i.md) |
| [LocalSocketServer(Socket连接)](arkts-network-socket-localsocketserver-i.md) |
| [MulticastSocket(Socket连接)](arkts-network-socket-multicastsocket-i.md) |
| [ProxyOptions(Socket连接)](arkts-network-socket-proxyoptions-i.md) |
| [SocketMessageInfo(Socket连接)](arkts-network-socket-socketmessageinfo-i.md) |
| [SocketRemoteInfo(Socket连接)](arkts-network-socket-socketremoteinfo-i.md) |
| [SocketStateBase(Socket连接)](arkts-network-socket-socketstatebase-i.md) |
| [TCPConnectOptions(Socket连接)](arkts-network-socket-tcpconnectoptions-i.md) |
| [TCPExtraOptions(Socket连接)](arkts-network-socket-tcpextraoptions-i.md) |
| [TCPSendOptions(Socket连接)](arkts-network-socket-tcpsendoptions-i.md) |
| [TCPSocket(Socket连接)](arkts-network-socket-tcpsocket-i.md) |
| [TCPSocketConnection(Socket连接)](arkts-network-socket-tcpsocketconnection-i.md) |
| [TCPSocketServer(Socket连接)](arkts-network-socket-tcpsocketserver-i.md) |
| [TLSConnectOptions(Socket连接)](arkts-network-socket-tlsconnectoptions-i.md) |
| [TLSSecureOptions(Socket连接)](arkts-network-socket-tlssecureoptions-i.md) |
| [TLSSocket(Socket连接)](arkts-network-socket-tlssocket-i.md) |
| [TLSSocketConnection(Socket连接)](arkts-network-socket-tlssocketconnection-i.md) |
| [TLSSocketServer(Socket连接)](arkts-network-socket-tlssocketserver-i.md) |
| [UDPExtraOptions(Socket连接)](arkts-network-socket-udpextraoptions-i.md) |
| [UDPSendOptions(Socket连接)](arkts-network-socket-udpsendoptions-i.md) |
| [UDPSocket(Socket连接)](arkts-network-socket-udpsocket-i.md) |

### 枚举

| 名称 |
| --- |
| [Protocol(Socket连接)](arkts-network-socket-protocol-e.md) |
| [ProxyTypes(Socket连接)](arkts-network-socket-proxytypes-e.md) |

### 类型

| 名称 |
| --- |
| [X509CertRawData(Socket连接)](arkts-network-socket-x509certrawdata-t.md) |
