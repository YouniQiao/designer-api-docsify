# LocalConnectOptions

Defines LocalSocket connection parameters.

**Since:** 12

<!--Device-socket-export interface LocalConnectOptions--><!--Device-socket-export interface LocalConnectOptions-End-->

**System capability:** SystemCapability.Communication.NetStack

## Modules to Import

```TypeScript
import { socket } from '@kit.NetworkKit';
```

## address

```TypeScript
address: LocalAddress
```

Bound Local address.

**Type:** LocalAddress

**Since:** 12

<!--Device-LocalConnectOptions-address: LocalAddress--><!--Device-LocalConnectOptions-address: LocalAddress-End-->

**System capability:** SystemCapability.Communication.NetStack

## timeout

```TypeScript
timeout?: number
```

Timeout duration of the LocalSocket connection, in milliseconds.

**Type:** number

**Since:** 12

<!--Device-LocalConnectOptions-timeout?: number--><!--Device-LocalConnectOptions-timeout?: number-End-->

**System capability:** SystemCapability.Communication.NetStack

