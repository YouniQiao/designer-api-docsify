# WebSocketServer

&lt;p&gt;Defines a WebSocketServer object. Before invoking WebSocketServer APIs,you need to call webSocketServer.createWebSocketServer to create a WebSocket Server.&lt;/p&gt;

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

<!--Device-webSocket-export interface WebSocketServer--><!--Device-webSocket-export interface WebSocketServer-End-->

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { webSocket } from 'kits/@kit.NetworkKit';
```

## close

```TypeScript
close(connection: WebSocketConnection, options?: webSocket.WebSocketCloseOptions): Promise<boolean>
```

Close a given WebSocket connection.

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**需要权限：** ohos.permission.INTERNET

<!--Device-WebSocketServer-close(connection: WebSocketConnection, options?: webSocket.WebSocketCloseOptions): Promise<boolean>--><!--Device-WebSocketServer-close(connection: WebSocketConnection, options?: webSocket.WebSocketCloseOptions): Promise<boolean>-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| connection | [WebSocketConnection](arkts-network-websocket-websocketconnection-i.md) | 是 | which on to be closed. |
| options | webSocket.WebSocketCloseOptions | 否 | Optional parameters {@link WebSocketCloseOptions}. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | Indicating whether the connection is closed sucessfully. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2302006 | websocket connection does not exist. |
| 201 | Permission denied. |

## 示例

```TypeScript
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let localServer: webSocket.WebSocketServer;
let config: webSocket.WebSocketServerConfig = {
  serverPort: 8080, // 监听端口
  maxConcurrentClientsNumber: 10,
  maxConnectionsForOneClient: 10,
}

localServer = webSocket.createWebSocketServer();
localServer.start(config).then((success: boolean) => {
  if (success) {
    console.info('webSocket server start success');
  } else {
    console.error('websocket server start failed');
  }
}).catch((error: BusinessError) => {
  console.error(`Failed to start. Code: ${error.code}, message: ${error.message}`);
});

localServer.on('connect', (connection: webSocket.WebSocketConnection) => {
  console.info(`New client connected! Client ip: ${connection.clientIP}, Client port: ${connection.clientPort}`);
  localServer.close(connection).then((success: boolean) => {
    if (success) {
      console.info('close client successfully');
    } else {
      console.error('close client failed');
    }
  });
});
```

## listAllConnections

```TypeScript
listAllConnections(): WebSocketConnection[]
```

List all alive connections.

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**需要权限：** ohos.permission.INTERNET

<!--Device-WebSocketServer-listAllConnections(): WebSocketConnection[]--><!--Device-WebSocketServer-listAllConnections(): WebSocketConnection[]-End-->

**系统能力：** SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WebSocketConnection](arkts-network-websocket-websocketconnection-i.md)[] | an array consists connections from all clients. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

## 示例

```TypeScript
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let connections: webSocket.WebSocketConnection[] = [];
let localServer: webSocket.WebSocketServer;
let config: webSocket.WebSocketServerConfig = {
  serverPort: 8080, // 监听端口
  maxConcurrentClientsNumber: 10,
  maxConnectionsForOneClient: 10,
}

localServer = webSocket.createWebSocketServer();
localServer.start(config).then((success: boolean) => {
  if (success) {
    console.info('webSocket server start success');
  } else {
    console.error('websocket server start failed');
  }
}).catch((error: BusinessError) => {
  console.error(`Failed to start. Code: ${error.code}, message: ${error.message}`);
});

localServer.on('connect', async (connection: webSocket.WebSocketConnection) => {
  console.info(`New client connected! Client ip: ${connection.clientIP}, Client port: ${connection.clientPort}`);
  try {
    connections = await localServer.listAllConnections();
    if (connections.length === 0) {
      console.info('client list is empty');
    } else {
      console.info(`client list cnt: ${connections.length}, client connections list is: ${connections}`);
    }
  } catch (error) {
    console.error(`Failed to listAllConnections. Code: ${error.code}, message: ${error.message}`);
  }
});
```

## off('error')

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

Cancels listening for the error events of a WebSocket Server.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为24。

<!--Device-WebSocketServer-off(type: 'error', callback?: ErrorCallback): void--><!--Device-WebSocketServer-off(type: 'error', callback?: ErrorCallback): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'error' | 是 | event indicating that the WebSocket Server has encountered an error. |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 否 | the callback used to return the result. |

## 示例

```TypeScript
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let localServer = webSocket.createWebSocketServer();
localServer.off('error');
```

## off('connect')

```TypeScript
off(type: 'connect', callback?: Callback<WebSocketConnection>): void
```

Cancels listening for events that a client requested to connect the server.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为24。

<!--Device-WebSocketServer-off(type: 'connect', callback?: Callback<WebSocketConnection>): void--><!--Device-WebSocketServer-off(type: 'connect', callback?: Callback<WebSocketConnection>): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'connect' | 是 | event indicating that a client requested to connect the server. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;WebSocketConnection&gt; | 否 | the callback used to return the result. |

## 示例

```TypeScript
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let localServer = webSocket.createWebSocketServer();
localServer.off('connect');
```

## off('close')

```TypeScript
off(type: 'close', callback?: ClientConnectionCloseCallback): void
```

Cancels listening for events that a connection from a given client has been closed.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为24。

<!--Device-WebSocketServer-off(type: 'close', callback?: ClientConnectionCloseCallback): void--><!--Device-WebSocketServer-off(type: 'close', callback?: ClientConnectionCloseCallback): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'close' | 是 | event indicating that a connection from a given client has been closed. |
| callback | [ClientConnectionCloseCallback](arkts-network-websocket-clientconnectionclosecallback-t.md) | 否 | the callback used to return the result. |

## 示例

```TypeScript
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let localServer = webSocket.createWebSocketServer();
localServer.off('close');
```

## off('messageReceive')

```TypeScript
off(type: 'messageReceive', callback?: Callback<WebSocketMessage>): void
```

Cancels listening for events that the server received a message.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为24。

<!--Device-WebSocketServer-off(type: 'messageReceive', callback?: Callback<WebSocketMessage>): void--><!--Device-WebSocketServer-off(type: 'messageReceive', callback?: Callback<WebSocketMessage>): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'messageReceive' | 是 | event indicating that the server received a message. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;WebSocketMessage&gt; | 否 | the callback used to return the result. |

## 示例

```TypeScript
import { webSocket } from '@kit.NetworkKit';
import { BusinessError, Callback } from '@kit.BasicServicesKit';

let localServer = webSocket.createWebSocketServer();
localServer.off('messageReceive');
```

## offConnect

```TypeScript
offConnect(callback?: Callback<WebSocketConnection>): void
```

Cancels listening for events that a client requested to connect the server.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-WebSocketServer-offConnect(callback?: Callback<WebSocketConnection>): void--><!--Device-WebSocketServer-offConnect(callback?: Callback<WebSocketConnection>): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;WebSocketConnection&gt; | 否 | the callback used to return the result. |

## offMessageReceive

```TypeScript
offMessageReceive(callback?: Callback<WebSocketMessage>): void
```

Cancels listening for events that the server received a message.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-WebSocketServer-offMessageReceive(callback?: Callback<WebSocketMessage>): void--><!--Device-WebSocketServer-offMessageReceive(callback?: Callback<WebSocketMessage>): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;WebSocketMessage&gt; | 否 | the callback used to return the result. |

## offWebSocketServerClose

```TypeScript
offWebSocketServerClose(callback?: ClientConnectionCloseCallback): void
```

Cancels listening for events that a connection from a given client has been closed.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-WebSocketServer-offWebSocketServerClose(callback?: ClientConnectionCloseCallback): void--><!--Device-WebSocketServer-offWebSocketServerClose(callback?: ClientConnectionCloseCallback): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ClientConnectionCloseCallback](arkts-network-websocket-clientconnectionclosecallback-t.md) | 否 | the callback used to return the result. |

## offWebSocketServerError

```TypeScript
offWebSocketServerError(callback?: ErrorCallback): void
```

Cancels listening for the error events of a WebSocket Server.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-WebSocketServer-offWebSocketServerError(callback?: ErrorCallback): void--><!--Device-WebSocketServer-offWebSocketServerError(callback?: ErrorCallback): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 否 | the callback used to return the result. |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

Enables listening for the error events of a WebSocket Server.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为24。

<!--Device-WebSocketServer-on(type: 'error', callback: ErrorCallback): void--><!--Device-WebSocketServer-on(type: 'error', callback: ErrorCallback): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'error' | 是 | event indicating that the WebSocket Server has encountered an error. |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 是 | the callback used to return the result. |

## 示例

```TypeScript
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wsServer: webSocket.WebSocketServer = webSocket.createWebSocketServer();
wsServer.on('error', (err: BusinessError) => {
  console.error(`error. Code: ${err.code}, message: ${err.message}`);
});
```

## on('connect')

```TypeScript
on(type: 'connect', callback: Callback<WebSocketConnection>): void
```

Enables listening for events that a client requested to connect the server.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为24。

<!--Device-WebSocketServer-on(type: 'connect', callback: Callback<WebSocketConnection>): void--><!--Device-WebSocketServer-on(type: 'connect', callback: Callback<WebSocketConnection>): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'connect' | 是 | event indicating that a client requested to connect the server. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;WebSocketConnection&gt; | 是 | the callback used to return the result. |

## 示例

```TypeScript
import { webSocket } from '@kit.NetworkKit';
import { BusinessError, Callback } from '@kit.BasicServicesKit';

let localServer = webSocket.createWebSocketServer();
localServer.on('connect', (connection: webSocket.WebSocketConnection) => {
  console.info(`New client connected! Client ip: ${connection.clientIP}, Client port: ${connection.clientPort}`);
});
```

## on('messageReceive')

```TypeScript
on(type: 'messageReceive', callback: Callback<WebSocketMessage>): void
```

Enables listening for events that the server received a message.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为24。

<!--Device-WebSocketServer-on(type: 'messageReceive', callback: Callback<WebSocketMessage>): void--><!--Device-WebSocketServer-on(type: 'messageReceive', callback: Callback<WebSocketMessage>): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'messageReceive' | 是 | event indicating that the server received a message. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;WebSocketMessage&gt; | 是 | the callback used to return the result. |

## 示例

```TypeScript
import { webSocket } from '@kit.NetworkKit';
import { BusinessError, Callback } from '@kit.BasicServicesKit';

let localServer = webSocket.createWebSocketServer();
localServer.on('messageReceive', (message: webSocket.WebSocketMessage) => {
  console.info(`on message received, client: ${message.clientConnection}, data: ${message.data}`);
});
```

## on('close')

```TypeScript
on(type: 'close', callback: ClientConnectionCloseCallback): void
```

Enables listening for events that a connection from a given client has been closed.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为24。

<!--Device-WebSocketServer-on(type: 'close', callback: ClientConnectionCloseCallback): void--><!--Device-WebSocketServer-on(type: 'close', callback: ClientConnectionCloseCallback): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'close' | 是 | event indicating that a connection from a given client has been closed. |
| callback | [ClientConnectionCloseCallback](arkts-network-websocket-clientconnectionclosecallback-t.md) | 是 | the callback function when a client connection is closed. |

## 示例

```TypeScript
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let localServer = webSocket.createWebSocketServer();
localServer.on('close', (clientConnection: webSocket.WebSocketConnection, closeReason: webSocket.CloseResult) => {
  console.info(`client close, client: ${clientConnection}, closeReason: Code: ${closeReason.code}, reason: ${closeReason.reason}`);
});
```

## onConnect

```TypeScript
onConnect(callback: Callback<WebSocketConnection>): void
```

Enables listening for events that a client requested to connect the server.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-WebSocketServer-onConnect(callback: Callback<WebSocketConnection>): void--><!--Device-WebSocketServer-onConnect(callback: Callback<WebSocketConnection>): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;WebSocketConnection&gt; | 是 | the callback used to return the result. |

## onMessageReceive

```TypeScript
onMessageReceive(callback: Callback<WebSocketMessage>): void
```

Enables listening for events that the server received a message.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-WebSocketServer-onMessageReceive(callback: Callback<WebSocketMessage>): void--><!--Device-WebSocketServer-onMessageReceive(callback: Callback<WebSocketMessage>): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;WebSocketMessage&gt; | 是 | the callback used to return the result. |

## onWebSocketServerClose

```TypeScript
onWebSocketServerClose(callback: ClientConnectionCloseCallback): void
```

Enables listening for events that a connection from a given client has been closed.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-WebSocketServer-onWebSocketServerClose(callback: ClientConnectionCloseCallback): void--><!--Device-WebSocketServer-onWebSocketServerClose(callback: ClientConnectionCloseCallback): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ClientConnectionCloseCallback](arkts-network-websocket-clientconnectionclosecallback-t.md) | 是 | the callback function when a client connection is closed. |

## onWebSocketServerError

```TypeScript
onWebSocketServerError(callback: ErrorCallback): void
```

Enables listening for the error events of a WebSocket Server.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-WebSocketServer-onWebSocketServerError(callback: ErrorCallback): void--><!--Device-WebSocketServer-onWebSocketServerError(callback: ErrorCallback): void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 是 | the callback used to return the result. |

## send

```TypeScript
send(data: string | ArrayBuffer, connection: WebSocketConnection): Promise<boolean>
```

Send a message using a specific connection.

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**需要权限：** ohos.permission.INTERNET

<!--Device-WebSocketServer-send(data: string | ArrayBuffer, connection: WebSocketConnection): Promise<boolean>--><!--Device-WebSocketServer-send(data: string | ArrayBuffer, connection: WebSocketConnection): Promise<boolean>-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | string \| ArrayBuffer | 是 | What to send. It can be a string or an ArrayBuffer. |
| connection | [WebSocketConnection](arkts-network-websocket-websocketconnection-i.md) | 是 | Where to sent. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | Indicating whether the message is sent sucessfully. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2302006 | websocket connection does not exist. |
| 201 | Permission denied. |

## 示例

```TypeScript
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let localServer: webSocket.WebSocketServer;
let config: webSocket.WebSocketServerConfig = {
  serverPort: 8080, // 监听端口
  maxConcurrentClientsNumber: 10,
  maxConnectionsForOneClient: 10,
}

localServer = webSocket.createWebSocketServer();
localServer.start(config).then((success: boolean) => {
  if (success) {
    console.info('webSocket server start success');
  } else {
    console.error('websocket server start failed');
  }
}).catch((error: BusinessError) => {
  console.error(`Failed to start. Code: ${error.code}, message: ${error.message}`);
});

localServer.on('connect', async (connection: webSocket.WebSocketConnection) => {
  console.info(`New client connected! Client ip: ${connection.clientIP}, Client port: ${connection.clientPort}`);
  // 当收到on('connect')事件时，可以通过send()方法与客户端进行通信
  localServer.send("Hello, I'm server!", connection).then((success: boolean) => {
    if (success) {
      console.info('message send successfully');
    } else {
      console.error('message send failed');
    }
  }).catch((error: BusinessError) => {
    console.error(`message send failed, Code: ${error.code}, message: ${error.message}`);
  });
});
```

## start

```TypeScript
start(config: WebSocketServerConfig): Promise<boolean>
```

Start the WebSocket Server, and listen to a given port.

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**需要权限：** ohos.permission.INTERNET

<!--Device-WebSocketServer-start(config: WebSocketServerConfig): Promise<boolean>--><!--Device-WebSocketServer-start(config: WebSocketServerConfig): Promise<boolean>-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [WebSocketServerConfig](arkts-network-websocket-websocketserverconfig-i.md) | 是 | setting for the server, such as ip address and port to listen to. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | Indicating whether the server starts sucessfully. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2302002 | Websocket certificate file does not exist. |
| 2302007 | Websocket port already occupied. |
| 2302999 | Websocket other unknown error. |
| 2302005 | Can't listen on the given Port. |
| 2302004 | Can't listen on the given NIC. |
| 201 | Permission denied. |

## 示例

```TypeScript
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let localServer: webSocket.WebSocketServer;
let config: webSocket.WebSocketServerConfig = {
  serverPort: 8080, // 监听端口
  maxConcurrentClientsNumber: 10,
  maxConnectionsForOneClient: 10,
}

localServer = webSocket.createWebSocketServer();
localServer.start(config).then((success: boolean) => {
  if (success) {
    console.info('webSocket server start success');
  } else {
    console.error('websocket server start failed');
  }
}).catch((error: BusinessError) => {
  console.error(`Failed to start. Code: ${error.code}, message: ${error.message}`);
});
```

## stop

```TypeScript
stop(): Promise<boolean>
```

Stop listening.

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**需要权限：** ohos.permission.INTERNET

<!--Device-WebSocketServer-stop(): Promise<boolean>--><!--Device-WebSocketServer-stop(): Promise<boolean>-End-->

**系统能力：** SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | The Indicating whether the server stops sucessfully. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

## 示例

```TypeScript
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let localServer: webSocket.WebSocketServer;
let config: webSocket.WebSocketServerConfig = {
  serverPort: 8080, // 监听端口
  maxConcurrentClientsNumber: 10,
  maxConnectionsForOneClient: 10,
}

localServer = webSocket.createWebSocketServer();
localServer.start(config).then((success: boolean) => {
  if (success) {
    console.info('webSocket server start success');
  } else {
    console.error('websocket server start failed');
  }
}).catch((error: BusinessError) => {
  console.error(`Failed to start. Code: ${error.code}, message: ${error.message}`);
});

localServer.stop().then((success: boolean) => {
  if (success) {
    console.info('server stop service successfully');
  } else {
    console.error('server stop service failed');
  }
});
```

