# LocalSocketMessageInfo

Defines the local socket connection information.

**Since:** 12

<!--Device-socket-export interface LocalSocketMessageInfo--><!--Device-socket-export interface LocalSocketMessageInfo-End-->

**System capability:** SystemCapability.Communication.NetStack

## Modules to Import

```TypeScript
import { socket } from '@kit.NetworkKit';
```

## address

```TypeScript
address: string
```

Bound local socket address.

**Type:** string

**Since:** 12

<!--Device-LocalSocketMessageInfo-address: string--><!--Device-LocalSocketMessageInfo-address: string-End-->

**System capability:** SystemCapability.Communication.NetStack

## message

```TypeScript
message: ArrayBuffer
```

Message data.

**Type:** ArrayBuffer

**Since:** 12

<!--Device-LocalSocketMessageInfo-message: ArrayBuffer--><!--Device-LocalSocketMessageInfo-message: ArrayBuffer-End-->

**System capability:** SystemCapability.Communication.NetStack

## size

```TypeScript
size: number
```

Length of the message, in bytes.

**Type:** number

**Since:** 12

<!--Device-LocalSocketMessageInfo-size: number--><!--Device-LocalSocketMessageInfo-size: number-End-->

**System capability:** SystemCapability.Communication.NetStack

