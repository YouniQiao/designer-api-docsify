# LocalConnectOptions

Defines LocalSocket connection parameters.

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

<!--Device-socket-export interface LocalConnectOptions--><!--Device-socket-export interface LocalConnectOptions-End-->

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { socket } from 'kits/@kit.NetworkKit';
```

## address

```TypeScript
address: LocalAddress
```

Bound Local address.

**类型：** [LocalAddress](arkts-network-socket-localaddress-i.md)

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

<!--Device-LocalConnectOptions-address: LocalAddress--><!--Device-LocalConnectOptions-address: LocalAddress-End-->

**系统能力：** SystemCapability.Communication.NetStack

## timeout

```TypeScript
timeout?: number
```

Timeout duration of the LocalSocket connection, in milliseconds.

**类型：** number

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

<!--Device-LocalConnectOptions-timeout?: number--><!--Device-LocalConnectOptions-timeout?: number-End-->

**系统能力：** SystemCapability.Communication.NetStack

