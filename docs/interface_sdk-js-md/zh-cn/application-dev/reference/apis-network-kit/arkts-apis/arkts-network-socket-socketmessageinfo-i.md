# SocketMessageInfo

Defines the socket connection information.

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

<!--Device-socket-export interface SocketMessageInfo--><!--Device-socket-export interface SocketMessageInfo-End-->

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { socket } from 'kits/@kit.NetworkKit';
```

## message

```TypeScript
message: ArrayBuffer
```

Receive the message event.

**类型：** ArrayBuffer

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

<!--Device-SocketMessageInfo-message: ArrayBuffer--><!--Device-SocketMessageInfo-message: ArrayBuffer-End-->

**系统能力：** SystemCapability.Communication.NetStack

## remoteInfo

```TypeScript
remoteInfo: SocketRemoteInfo
```

Socket connection information.

**类型：** [SocketRemoteInfo](arkts-network-socket-socketremoteinfo-i.md)

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

<!--Device-SocketMessageInfo-remoteInfo: SocketRemoteInfo--><!--Device-SocketMessageInfo-remoteInfo: SocketRemoteInfo-End-->

**系统能力：** SystemCapability.Communication.NetStack

