# @ohos.net.webSocket(WebSocket Connection)

Provides WebSocket clients and servers for third-party applications to implement bidirectional connections between the client and server.On the WebSocket client: You can use WebSocket to establish a bidirectional connection between the server and client. Before doing this, you need to use the [createWebSocket](arkts-network-websocket-createwebsocket-f.md) API to create a [WebSocket](arkts-network-websocket-websocket-i.md) object and then use the [connect](arkts-network-websocket-websocket-i.md#connect) API to connect to the server. If the connection is successful, the client will receive a callback of the open event. Then, the client can communicate with the server using the [send](arkts-network-websocket-websocket-i.md#send) API. When the server sends a message to the client, the client will receive a callback of the message event. If the connection is no longer needed, the client can call the [close](arkts-network-websocket-websocket-i.md#close) API to close the connection. After successful disconnection, the client will receive a callback of the close event. If an error occurs in any of the preceding processes, the client will receive a callback of the [error](arkts-network-websocket-websocket-i.md#onerror) event.On the WebSocket server: Use the [createWebSocketServer](arkts-network-websocket-createwebsocketserver-f.md) method to create a [WebSocketServer](arkts-network-websocket-websocketserver-i.md) object, and then use the [start](arkts-network-websocket-websocketserver-i.md#start) method to start the server and listen to the link setup request message from the client. (The API version 23 and later versions support all devices. In earlier versions, only TV devices are supported.) If the connection is successful, the server receives the callback of the connect event. The server can then communicate with the client by using the [send](arkts-network-websocket-websocketserver-i.md#send) API or obtain information about all connected clients by using the [listAllConnections](arkts-network-websocket-websocketserver-i.md#listallconnections) API. When the client sends a message to the server, the server receives the callback of the messageReceive event. If the connection is no longer needed, the server can call the [close](arkts-network-websocket-websocketserver-i.md#close) API to close the connection. After successful disconnection, the server will receive a callback of the [close](arkts-network-websocket-websocketserver-i.md#onclose) event. To stop the service, the server can use the [stop](arkts-network-websocket-websocketserver-i.md#stop) API. If an error occurs in any of the preceding processes, the server will receive a callback of the [error](arkts-network-websocket-websocketserver-i.md#onerror) event.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Communication.NetStack

## Modules to Import

```TypeScript
import { webSocket } from '@kit.NetworkKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [createWebSocket(WebSocket Connection)](arkts-network-websocket-createwebsocket-f.md) |
| [createWebSocketServer(WebSocket Connection)](arkts-network-websocket-createwebsocketserver-f.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ClientCert(WebSocket Connection)](arkts-network-websocket-clientcert-i.md) |
| [CloseResult(WebSocket Connection)](arkts-network-websocket-closeresult-i.md) |
| [OpenResult(WebSocket Connection)](arkts-network-websocket-openresult-i.md) |
| [ServerCert(WebSocket Connection)](arkts-network-websocket-servercert-i.md) |
| [WebSocket(WebSocket Connection)](arkts-network-websocket-websocket-i.md) |
| [WebSocketCloseOptions(WebSocket Connection)](arkts-network-websocket-websocketcloseoptions-i.md) |
| [WebSocketConnection(WebSocket Connection)](arkts-network-websocket-websocketconnection-i.md) |
| [WebSocketMessage(WebSocket Connection)](arkts-network-websocket-websocketmessage-i.md) |
| [WebSocketOpenInfo(WebSocket Connection)](arkts-network-websocket-websocketopeninfo-i.md) |
| [WebSocketRequestOptions(WebSocket Connection)](arkts-network-websocket-websocketrequestoptions-i.md) |
| [WebSocketServer(WebSocket Connection)](arkts-network-websocket-websocketserver-i.md) |
| [WebSocketServerConfig(WebSocket Connection)](arkts-network-websocket-websocketserverconfig-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [TlsProtocol(WebSocket Connection)](arkts-network-websocket-tlsprotocol-e.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ClientConnectionCloseCallback(WebSocket Connection)](arkts-network-websocket-clientconnectionclosecallback-t.md) |
| [HttpProxy(WebSocket Connection)](arkts-network-websocket-httpproxy-t.md) |
| [ProxyConfiguration(WebSocket Connection)](arkts-network-websocket-proxyconfiguration-t.md) |
| [ResponseHeaders(WebSocket Connection)](arkts-network-websocket-responseheaders-t.md) |
