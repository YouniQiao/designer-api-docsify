# NetAddress

Defines a network address.

**Since:** 24

<!--Device-connection-export interface NetAddress--><!--Device-connection-export interface NetAddress-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## Modules to Import

```TypeScript
import { connection } from '@kit.NetworkKit';
```

## address

```TypeScript
address: string
```

Network address.

**Type:** string

**Since:** 24

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-NetAddress-address: string--><!--Device-NetAddress-address: string-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## family

```TypeScript
family?: number
```

Address family identifier. The value is 1 for IPv4 and 2 for IPv6. The default value is 1.

**Type:** number

**Since:** 24

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-NetAddress-family?: int--><!--Device-NetAddress-family?: int-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## port

```TypeScript
port?: number
```

Port number. The value ranges from 0 to 65535.

**Type:** number

**Since:** 24

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-NetAddress-port?: int--><!--Device-NetAddress-port?: int-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

