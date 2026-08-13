# WebSocketMessage

Info about the message received from a specific client.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Deprecated since:** -1

<!--Device-webSocket-export interface WebSocketMessage--><!--Device-webSocket-export interface WebSocketMessage-End-->

**System capability:** SystemCapability.Communication.NetStack

## Modules to Import

```TypeScript
import { webSocket } from '@kit.NetworkKit';
```

## clientConnection

```TypeScript
clientConnection: WebSocketConnection
```

The connection where the message comes from.

**Type:** [WebSocketConnection](arkts-network-websocket-websocketconnection-i.md)

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Deprecated since:** -1

<!--Device-WebSocketMessage-clientConnection: WebSocketConnection--><!--Device-WebSocketMessage-clientConnection: WebSocketConnection-End-->

**System capability:** SystemCapability.Communication.NetStack

## data

```TypeScript
data: string | ArrayBuffer
```

Content of the message.

**Type:** string \| ArrayBuffer

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Deprecated since:** -1

<!--Device-WebSocketMessage-data: string | ArrayBuffer--><!--Device-WebSocketMessage-data: string | ArrayBuffer-End-->

**System capability:** SystemCapability.Communication.NetStack

