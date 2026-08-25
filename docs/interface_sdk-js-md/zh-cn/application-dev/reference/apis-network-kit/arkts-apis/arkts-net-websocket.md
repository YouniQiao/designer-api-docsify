# @ohos.net.webSocket(WebSocket连接)

给第三方应用提供webSocket客户端和服务端服务器，实现客户端与服务端的双向连接。客户端：使用WebSocket建立服务器与客户端的双向连接，需要先通过[createWebSocket](arkts-network-websocket-createwebsocket-f.md)方法创建 [WebSocket](arkts-network-websocket-websocket-i.md)对象，然后通过 [connect](arkts-network-websocket-websocket-i.md#connect)方法连接到服务器。当连接成功后，客户端会收到 open事件的回调，之后客户端就可以通过 [send](arkts-network-websocket-websocket-i.md#send)方法与服务器进行通信。当服务器发信 息给客户端时，客户端会收到message事 件的回调。当客户端想要取消此连接时，通过调用[close](arkts-network-websocket-websocket-i.md#close)方法主动断开连接后，客户端会收到 close事件的回调。若在上述任一过程中发生错误，客户端会收到 [error](arkts-network-websocket-websocket-i.md#onerror)事件的回调。服务端：（从API version 23开始支持全设备使用，之前仅支持TV设备使用）使用WebSocket建立服务器与客户端的双向连接，需要先通过 [createWebSocketServer](arkts-network-websocket-createwebsocketserver-f.md)方法创建[WebSocketServer](arkts-network-websocket-websocketserver-i.md)对 象，然后通过[start](arkts-network-websocket-websocketserver-i.md#start)方法启动服务器，监听客户端的申请建链的消息。当连接成功后，服务端会收到 connect事件的回调，之后服务端可以通 过[send](arkts-network-websocket-websocketserver-i.md#send)方法与客户端进行通信，或者通过 [listAllConnections](arkts-network-websocket-websocketserver-i.md#listallconnections)方法列举出当前与服务端建链的所有客户端信息。当客户端给服务端发消息时，服务端会收到 messageReceive事件回 调。当服务端想断开与某个客户端的连接时，可以通过调用[close](arkts-network-websocket-websocketserver-i.md#close)方法主动断开与某个客户端的连接，之后服务端会收到 [close](arkts-network-websocket-websocketserver-i.md#onclose)事件的回调。当服务端想停止 service时，可以调用[stop](arkts-network-websocket-websocketserver-i.md#stop)方法。若在上述任一过程中发生错误，服务端会收到 [error](arkts-network-websocket-websocketserver-i.md#onerror)事件的回调。

**起始版本：** 6

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { webSocket } from 'kits/@kit.NetworkKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [createWebSocket(WebSocket连接)](arkts-network-websocket-createwebsocket-f.md) |
| [createWebSocketServer(WebSocket连接)](arkts-network-websocket-createwebsocketserver-f.md) |

### 接口

| 名称 |
| --- |
| [ClientCert(WebSocket连接)](arkts-network-websocket-clientcert-i.md) |
| [CloseResult(WebSocket连接)](arkts-network-websocket-closeresult-i.md) |
| [ServerCert(WebSocket连接)](arkts-network-websocket-servercert-i.md) |
| [WebSocket(WebSocket连接)](arkts-network-websocket-websocket-i.md) |
| [WebSocketCloseOptions(WebSocket连接)](arkts-network-websocket-websocketcloseoptions-i.md) |
| [WebSocketConnection(WebSocket连接)](arkts-network-websocket-websocketconnection-i.md) |
| [WebSocketMessage(WebSocket连接)](arkts-network-websocket-websocketmessage-i.md) |
| [WebSocketOpenInfo(WebSocket连接)](arkts-network-websocket-websocketopeninfo-i.md) |
| [WebSocketRequestOptions(WebSocket连接)](arkts-network-websocket-websocketrequestoptions-i.md) |
| [WebSocketServer(WebSocket连接)](arkts-network-websocket-websocketserver-i.md) |
| [WebSocketServerConfig(WebSocket连接)](arkts-network-websocket-websocketserverconfig-i.md) |

### 枚举

| 名称 |
| --- |
| [TlsProtocol(WebSocket连接)](arkts-network-websocket-tlsprotocol-e.md) |

### 类型

| 名称 |
| --- |
| [ClientConnectionCloseCallback(WebSocket连接)](arkts-network-websocket-clientconnectionclosecallback-t.md) |
| [HttpProxy(WebSocket连接)](arkts-network-websocket-httpproxy-t.md) |
| [ProxyConfiguration(WebSocket连接)](arkts-network-websocket-proxyconfiguration-t.md) |
| [ResponseHeaders(WebSocket连接)](arkts-network-websocket-responseheaders-t.md) |
