# TCPExtraOptions

Defines other properties of the TCPSocket connection.

**Inheritance/Implementation:** TCPExtraOptions extends [ExtraOptionsBase](arkts-network-socket-extraoptionsbase-i.md#ExtraOptionsBase)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-socket-export interface TCPExtraOptions--><!--Device-socket-export interface TCPExtraOptions-End-->

**System capability:** SystemCapability.Communication.NetStack

## Modules to Import

```TypeScript
import { socket } from 'socket';
```

## OOBInline

```TypeScript
OOBInline?: boolean
```

Whether to enable OOBInline. The default value is false.

**Type:** boolean

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-TCPExtraOptions-OOBInline?: boolean--><!--Device-TCPExtraOptions-OOBInline?: boolean-End-->

**System capability:** SystemCapability.Communication.NetStack

## TCPNoDelay

```TypeScript
TCPNoDelay?: boolean
```

Whether to enable no-delay on the TCPSocket connection. The default value is false.

**Type:** boolean

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-TCPExtraOptions-TCPNoDelay?: boolean--><!--Device-TCPExtraOptions-TCPNoDelay?: boolean-End-->

**System capability:** SystemCapability.Communication.NetStack

## keepAlive

```TypeScript
keepAlive?: boolean
```

Whether to keep the connection alive. The default value is false.

**Type:** boolean

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-TCPExtraOptions-keepAlive?: boolean--><!--Device-TCPExtraOptions-keepAlive?: boolean-End-->

**System capability:** SystemCapability.Communication.NetStack

## socketLinger

```TypeScript
socketLinger?: { on: boolean, linger: number }
```

Socket linger.

**Type:** { on: boolean, linger: number }

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-TCPExtraOptions-socketLinger?: { on: boolean, linger: number }--><!--Device-TCPExtraOptions-socketLinger?: { on: boolean, linger: number }-End-->

**System capability:** SystemCapability.Communication.NetStack

## tcpFastOpen

```TypeScript
tcpFastOpen?: boolean
```

Whether to enable TCP Fast Open (TFO) on the TCPSocket connection. The default value is false.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TCPExtraOptions-tcpFastOpen?: boolean--><!--Device-TCPExtraOptions-tcpFastOpen?: boolean-End-->

**System capability:** SystemCapability.Communication.NetStack

