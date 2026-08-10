# UDPSendOptions

Defines the parameters for sending data over the UDPSocket connection.

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-socket-export interface UDPSendOptions--><!--Device-socket-export interface UDPSendOptions-End-->

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { socket } from 'kits/@kit.NetworkKit';
```

## address

```TypeScript
address: NetAddress
```

Destination address.

**类型：** [NetAddress](arkts-network-connection-netaddress-i.md)

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-UDPSendOptions-address: NetAddress--><!--Device-UDPSendOptions-address: NetAddress-End-->

**系统能力：** SystemCapability.Communication.NetStack

## data

```TypeScript
data: string | ArrayBuffer
```

Data to send.

**类型：** string \| ArrayBuffer

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-UDPSendOptions-data: string | ArrayBuffer--><!--Device-UDPSendOptions-data: string | ArrayBuffer-End-->

**系统能力：** SystemCapability.Communication.NetStack

## proxy

```TypeScript
proxy?: ProxyOptions
```

Set this option for the proxy feature.

**类型：** [ProxyOptions](arkts-network-socket-proxyoptions-i.md)

**起始版本：** 18

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为18。

<!--Device-UDPSendOptions-proxy?: ProxyOptions--><!--Device-UDPSendOptions-proxy?: ProxyOptions-End-->

**系统能力：** SystemCapability.Communication.NetStack

