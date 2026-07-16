# WebSocketCloseOptions

Defines the optional parameters carried in the request for closing a WebSocket connection.

**Since:** 11

<!--Device-webSocket-export interface WebSocketCloseOptions--><!--Device-webSocket-export interface WebSocketCloseOptions-End-->

**System capability:** SystemCapability.Communication.NetStack

## Modules to Import

```TypeScript
import { webSocket } from '@kit.NetworkKit';
```

## code

```TypeScript
code?: number
```

Error code.

**Type:** number

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebSocketCloseOptions-code?: int--><!--Device-WebSocketCloseOptions-code?: int-End-->

**System capability:** SystemCapability.Communication.NetStack

## reason

```TypeScript
reason?: string
```

Error cause.

**Type:** string

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebSocketCloseOptions-reason?: string--><!--Device-WebSocketCloseOptions-reason?: string-End-->

**System capability:** SystemCapability.Communication.NetStack

