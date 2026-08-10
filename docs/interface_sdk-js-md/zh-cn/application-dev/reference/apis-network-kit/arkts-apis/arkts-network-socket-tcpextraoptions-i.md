# TCPExtraOptions

Defines other properties of the TCPSocket connection.

**继承/实现关系：** TCPExtraOptions extends [ExtraOptionsBase](arkts-network-socket-extraoptionsbase-i.md)

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-socket-export interface TCPExtraOptions extends ExtraOptionsBase--><!--Device-socket-export interface TCPExtraOptions extends ExtraOptionsBase-End-->

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { socket } from 'kits/@kit.NetworkKit';
```

## OOBInline

```TypeScript
OOBInline?: boolean
```

Whether to enable OOBInline. The default value is false.

**类型：** boolean

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-TCPExtraOptions-OOBInline?: boolean--><!--Device-TCPExtraOptions-OOBInline?: boolean-End-->

**系统能力：** SystemCapability.Communication.NetStack

## TCPNoDelay

```TypeScript
TCPNoDelay?: boolean
```

Whether to enable no-delay on the TCPSocket connection. The default value is false.

**类型：** boolean

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-TCPExtraOptions-TCPNoDelay?: boolean--><!--Device-TCPExtraOptions-TCPNoDelay?: boolean-End-->

**系统能力：** SystemCapability.Communication.NetStack

## keepAlive

```TypeScript
keepAlive?: boolean
```

Whether to keep the connection alive. The default value is false.

**类型：** boolean

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-TCPExtraOptions-keepAlive?: boolean--><!--Device-TCPExtraOptions-keepAlive?: boolean-End-->

**系统能力：** SystemCapability.Communication.NetStack

## socketLinger

```TypeScript
socketLinger?: { on: boolean, linger: number }
```

Socket linger.

**类型：** { on: boolean, linger: number }

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-TCPExtraOptions-socketLinger?: { on: boolean, linger: number }--><!--Device-TCPExtraOptions-socketLinger?: { on: boolean, linger: number }-End-->

**系统能力：** SystemCapability.Communication.NetStack

## tcpFastOpen

```TypeScript
tcpFastOpen?: boolean
```

Whether to enable TCP Fast Open (TFO) on the TCPSocket connection. The default value is false.

**类型：** boolean

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TCPExtraOptions-tcpFastOpen?: boolean--><!--Device-TCPExtraOptions-tcpFastOpen?: boolean-End-->

**系统能力：** SystemCapability.Communication.NetStack

