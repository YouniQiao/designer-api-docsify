# TCPConnectOptions

Defines TCPSocket connection parameters.

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-socket-export interface TCPConnectOptions--><!--Device-socket-export interface TCPConnectOptions-End-->

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { socket } from 'kits/@kit.NetworkKit';
```

## address

```TypeScript
address: NetAddress
```

Bound IP address and port number.

**类型：** [NetAddress](arkts-network-connection-netaddress-i.md)

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-TCPConnectOptions-address: NetAddress--><!--Device-TCPConnectOptions-address: NetAddress-End-->

**系统能力：** SystemCapability.Communication.NetStack

## proxy

```TypeScript
proxy?: ProxyOptions
```

Set this option for the proxy feature.

**类型：** [ProxyOptions](arkts-network-socket-proxyoptions-i.md)

**起始版本：** 18

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为18。

<!--Device-TCPConnectOptions-proxy?: ProxyOptions--><!--Device-TCPConnectOptions-proxy?: ProxyOptions-End-->

**系统能力：** SystemCapability.Communication.NetStack

## timeout

```TypeScript
timeout?: number
```

Timeout duration of the TCPSocket connection, in milliseconds.

**类型：** number

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-TCPConnectOptions-timeout?: number--><!--Device-TCPConnectOptions-timeout?: number-End-->

**系统能力：** SystemCapability.Communication.NetStack

