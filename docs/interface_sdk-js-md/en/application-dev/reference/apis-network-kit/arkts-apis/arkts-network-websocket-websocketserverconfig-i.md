# WebSocketServerConfig

Defines the WebSocketServer configuration.

**Since:** 23

<!--Device-webSocket-export interface WebSocketServerConfig--><!--Device-webSocket-export interface WebSocketServerConfig-End-->

**System capability:** SystemCapability.Communication.NetStack

## Modules to Import

```TypeScript
import { webSocket } from '@kit.NetworkKit';
```

## maxConcurrentClientsNumber

```TypeScript
maxConcurrentClientsNumber: int
```

Maximum number of concurrent clients. When the number of concurrent clients reaches the maximum, the server rejects new connections. The default value is **10**.

**Type:** int

**Since:** 23

<!--Device-WebSocketServerConfig-maxConcurrentClientsNumber: int--><!--Device-WebSocketServerConfig-maxConcurrentClientsNumber: int-End-->

**System capability:** SystemCapability.Communication.NetStack

## maxConnectionsForOneClient

```TypeScript
maxConnectionsForOneClient: int
```

Maximum number of connections for each client. The default value is **10**.

**Type:** int

**Since:** 23

<!--Device-WebSocketServerConfig-maxConnectionsForOneClient: int--><!--Device-WebSocketServerConfig-maxConnectionsForOneClient: int-End-->

**System capability:** SystemCapability.Communication.NetStack

## protocol

```TypeScript
protocol?: string
```

Custom protocol.

**Type:** string

**Since:** 23

<!--Device-WebSocketServerConfig-protocol?: string--><!--Device-WebSocketServerConfig-protocol?: string-End-->

**System capability:** SystemCapability.Communication.NetStack

## serverCert

```TypeScript
serverCert?: ServerCert
```

Certificate information, which includes the paths of the WebSocketServer certificate file and private key file.

**Type:** [ServerCert](arkts-network-websocket-servercert-i.md)

**Since:** 23

<!--Device-WebSocketServerConfig-serverCert?: ServerCert--><!--Device-WebSocketServerConfig-serverCert?: ServerCert-End-->

**System capability:** SystemCapability.Communication.NetStack

## serverIP

```TypeScript
serverIP?: string
```

IP address of the WebSocketServer. The default value is **0.0.0.0**.

**Type:** string

**Since:** 23

<!--Device-WebSocketServerConfig-serverIP?: string--><!--Device-WebSocketServerConfig-serverIP?: string-End-->

**System capability:** SystemCapability.Communication.NetStack

## serverPort

```TypeScript
serverPort: int
```

Port of the WebSocketServer.

**Type:** int

**Since:** 23

<!--Device-WebSocketServerConfig-serverPort: int--><!--Device-WebSocketServerConfig-serverPort: int-End-->

**System capability:** SystemCapability.Communication.NetStack

