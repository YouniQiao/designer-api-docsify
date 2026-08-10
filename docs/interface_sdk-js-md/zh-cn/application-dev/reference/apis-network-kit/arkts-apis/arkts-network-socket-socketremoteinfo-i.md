# SocketRemoteInfo

Defines information about the socket connection.

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-socket-export interface SocketRemoteInfo--><!--Device-socket-export interface SocketRemoteInfo-End-->

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { socket } from 'kits/@kit.NetworkKit';
```

## address

```TypeScript
address: string
```

Bound IP address.

**类型：** string

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-SocketRemoteInfo-address: string--><!--Device-SocketRemoteInfo-address: string-End-->

**系统能力：** SystemCapability.Communication.NetStack

## family

```TypeScript
family: 'IPv4' | 'IPv6'
```

Network protocol type. The options are as follows: IPv4, IPv6.

**类型：** 'IPv4' \| 'IPv6'

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-SocketRemoteInfo-family: 'IPv4' | 'IPv6'--><!--Device-SocketRemoteInfo-family: 'IPv4' | 'IPv6'-End-->

**系统能力：** SystemCapability.Communication.NetStack

## port

```TypeScript
port: number
```

Port number. The value ranges from 0 to 65535.

**类型：** number

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-SocketRemoteInfo-port: number--><!--Device-SocketRemoteInfo-port: number-End-->

**系统能力：** SystemCapability.Communication.NetStack

## size

```TypeScript
size: number
```

Length of the server response message, in bytes.

**类型：** number

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-SocketRemoteInfo-size: number--><!--Device-SocketRemoteInfo-size: number-End-->

**系统能力：** SystemCapability.Communication.NetStack

