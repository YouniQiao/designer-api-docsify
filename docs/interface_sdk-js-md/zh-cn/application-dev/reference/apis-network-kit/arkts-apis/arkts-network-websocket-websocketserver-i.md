# WebSocketServer

在调用WebSocketServer方法前，需要先通过[webSocket.createWebSocketServer](arkts-network-websocket-createwebsocketserver-f.md)创建一个 WebSocketServer。

**起始版本：** 19

**ArkTS模式：** ArkTS-Dyn起始版本为19；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { webSocket } from '@kit.NetworkKit';
```

## close

```TypeScript
close(connection: WebSocketConnection, options?: webSocket.WebSocketCloseOptions): Promise<boolean>
```

关闭指定websocket连接。使用Promise异步回调。

**起始版本：** 19

**ArkTS模式：** ArkTS-Dyn起始版本为19；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [connection](arkts-net-connection.md) | [WebSocketConnection](arkts-network-websocket-websocketconnection-i.md) | 是 |
| options | [webSocket.WebSocketCloseOptions](arkts-network-websocket-websocketcloseoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| 2302006 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();
ws.close((err: BusinessError) => {
  if (!err) {
    console.info("close success");
  } else {
    console.error(`close fail. Code: ${err.code}, message: ${err.message}`);
  }
});
```

ArkTS-Sta示例：

```TypeScript
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();
ws.close((err: BusinessError<void>|null, value: Boolean|undefined) => {
  if (!err) {
    console.info("close success");
  } else {
    console.error(`close fail. Code: ${err.code}, message: ${err.message}`);
  }
});
```

ArkTS-Dyn示例：

```TypeScript
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();

let options: webSocket.WebSocketCloseOptions | undefined;
if (options != undefined) {
    options.code = 1000;
    options.reason = "your reason";
}
ws.close(options, (err: BusinessError) => {
    if (!err) {
        console.info("close success");
    } else {
        console.error(`close fail. Code: ${err.code}, message: ${err.message}`);
    }
});
```

ArkTS-Sta示例：

```TypeScript
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();

let options: webSocket.WebSocketCloseOptions;
if (options != undefined) {
    options.code = 1000;
    options.reason = "your reason";
}
ws.close(options, (err: BusinessError<void>|null, value: Boolean|undefined) => {
    if (!err) {
        console.info("close success");
    } else {
        console.error(`close fail. Code: ${err.code}, message: ${err.message}`);
    }
});
```

ArkTS-Dyn示例：

```TypeScript
import { webSocket } from '@kit.NetworkKit';

let ws = webSocket.createWebSocket();
let options: webSocket.WebSocketCloseOptions | undefined;
if (options != undefined) {
    options.code = 1000;
    options.reason = "your reason";
}
let promise = ws.close();
promise.then((value: boolean) => {
    console.info("close success");
}).catch((err:string) => {
    console.error("close fail, error:" + JSON.stringify(err));
});
```

ArkTS-Sta示例：

```TypeScript
import { webSocket } from '@kit.NetworkKit';

let ws = webSocket.createWebSocket();
let options: webSocket.WebSocketCloseOptions;
if (options != undefined) {
    options.code = 1000;
    options.reason = "your reason";
}
let promise = ws.close();
promise.then((value: boolean) => {
    console.info("close success");
}).catch((err: Error) => {
    console.error(`close fail, error: ${err}`);
});
```

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

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
}).catch((err: Error) => {
  let error = err as BusinessError;
  console.error(`Failed to start. Code: ${error.code}, message: ${error.message}`);
});

localServer.onConnect((connection: webSocket.WebSocketConnection) => {
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

获取与服务端连接的所有客户端信息。

> **说明：**&gt;
> 该接口为异步调用，返回结果需通过await关键字等待异步操作完成，以确保正确获取到所有客户端连接信息。

**起始版本：** 19

**ArkTS模式：** ArkTS-Dyn起始版本为19；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetStack

**返回值：**

| 类型 |
| --- |
| [WebSocketConnection](arkts-network-websocket-websocketconnection-i.md)[] |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

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
}).catch((err: Error) => {
  let error = err as BusinessError;
  console.error(`Failed to start. Code: ${error.code}, message: ${error.message}`);
});

localServer.onConnect((connection: webSocket.WebSocketConnection) => {
  console.info(`New client connected! Client ip: ${connection.clientIP}, Client port: ${connection.clientPort}`);
  try {
    connections = localServer.listAllConnections();
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

## off('connect')

```TypeScript
off(type: 'connect', callback?: Callback<WebSocketConnection>): void
```

取消订阅WebSocketServer的连接事件（客户端与服务端建链成功），使用callback异步回调。

> **说明：**&gt;
> 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**起始版本：** 19

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为19。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'connect' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[WebSocketConnection](arkts-network-websocket-websocketconnection-i.md)&gt; | 否 |

**示例**

```TypeScript
import { webSocket } from '@kit.NetworkKit';

let localServer = webSocket.createWebSocketServer();
localServer.off('connect');
```

## off('messageReceive')

```TypeScript
off(type: 'messageReceive', callback?: Callback<WebSocketMessage>): void
```

取消订阅WebSocketServer的接收到客户端消息事件，使用callback异步回调。

> **说明：**&gt;
> 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**起始版本：** 19

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为19。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'messageReceive' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[WebSocketMessage](arkts-network-websocket-websocketmessage-i.md)&gt; | 否 |

**示例**

```TypeScript
import { webSocket } from '@kit.NetworkKit';

let localServer = webSocket.createWebSocketServer();
localServer.off('messageReceive');
```

## off('close')

```TypeScript
off(type: 'close', callback?: ClientConnectionCloseCallback): void
```

取消订阅WebSocketServer的关闭事件，使用callback异步回调。

> **说明：**&gt;
> 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**起始版本：** 19

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为19。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'close' | 是 |
| callback | [ClientConnectionCloseCallback](arkts-network-websocket-clientconnectionclosecallback-t.md) | 否 |

**示例**

```TypeScript
import { webSocket } from '@kit.NetworkKit';

let localServer = webSocket.createWebSocketServer();
localServer.off('close');
```

## off('error')

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

取消订阅WebSocketServer的Error事件，使用callback异步回调。

> **说明：**&gt;
> 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**起始版本：** 19

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为19。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'error' | 是 |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 否 |

**示例**

```TypeScript
import { webSocket } from '@kit.NetworkKit';

let localServer = webSocket.createWebSocketServer();
localServer.off('error');
```

## offConnect

```TypeScript
offConnect(callback?: Callback<WebSocketConnection>): void
```

取消订阅客户端请求连接服务器的事件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** 
- API版本23+：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[WebSocketConnection](arkts-network-websocket-websocketconnection-i.md)&gt; | 否 |

**示例**

```TypeScript
import { webSocket } from '@kit.NetworkKit';

let localServer = webSocket.createWebSocketServer();
let callback = (connection: webSocket.WebSocketConnection) => {
  console.info(`connections: ${JSON.stringify(connection)}`);
}
localServer.onConnect(callback);
localServer.offConnect(callback);
```

## offMessageReceive

```TypeScript
offMessageReceive(callback?: Callback<WebSocketMessage>): void
```

取消订阅服务器收到消息的事件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** 
- API版本23+：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[WebSocketMessage](arkts-network-websocket-websocketmessage-i.md)&gt; | 否 |

**示例**

```TypeScript
import { webSocket } from '@kit.NetworkKit';

let localServer = webSocket.createWebSocketServer();
let callback = (message: webSocket.WebSocketMessage) => {
  console.info(`message: ${JSON.stringify(message)}}`);
}
localServer.onMessageReceive(callback);
localServer.offMessageReceive(callback);
```

## offWebSocketServerClose

```TypeScript
offWebSocketServerClose(callback?: ClientConnectionCloseCallback): void
```

Cancels listening for events that a connection from a given client has been closed.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ClientConnectionCloseCallback](arkts-network-websocket-clientconnectionclosecallback-t.md) | 否 |

**示例**

```TypeScript
import { webSocket } from '@kit.NetworkKit';

let localServer = webSocket.createWebSocketServer();
let closeCallback = (clientConnection: webSocket.WebSocketConnection, closeReason: webSocket.CloseResult) => {
  console.info(`connection: ${JSON.stringify(clientConnection)}, closeReason: ${JSON.stringify(closeReason)}`);
}
localServer.onWebSocketServerClose(closeCallback);
localServer.offWebSocketServerClose(closeCallback);
```

## offWebSocketServerError

```TypeScript
offWebSocketServerError(callback?: ErrorCallback): void
```

取消订阅WebSocket服务器的错误事件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** 
- API版本23+：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 否 |

**示例**

```TypeScript
import { webSocket } from '@kit.NetworkKit';

let localServer = webSocket.createWebSocketServer();
let callback = (err: Error) => {
  console.info(`error. Code: ${err.code}, message: ${err.message}`);
}
localServer.onWebSocketServerError(callback);
localServer.offWebSocketServerError(callback);
localServer.offWebSocketServerError();
```

## on('connect')

```TypeScript
on(type: 'connect', callback: Callback<WebSocketConnection>): void
```

订阅WebSocketServer的连接事件（客户端与服务端建链成功），使用callback异步回调。

**起始版本：** 19

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为19。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'connect' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[WebSocketConnection](arkts-network-websocket-websocketconnection-i.md)&gt; | 是 |

**示例**

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

订阅WebSocketServer的接收客户端消息的事件，使用callback异步回调。

**起始版本：** 19

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为19。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'messageReceive' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[WebSocketMessage](arkts-network-websocket-websocketmessage-i.md)&gt; | 是 |

**示例**

```TypeScript
import { webSocket } from '@kit.NetworkKit';

let localServer = webSocket.createWebSocketServer();
localServer.on('messageReceive', (message: webSocket.WebSocketMessage) => {
  console.info(`on message received, client: ${message.clientConnection}, data: ${message.data}`);
});
```

## on('close')

```TypeScript
on(type: 'close', callback: ClientConnectionCloseCallback): void
```

订阅WebSocketServer的关闭事件，使用callback异步回调。

**起始版本：** 19

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为19。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'close' | 是 |
| callback | [ClientConnectionCloseCallback](arkts-network-websocket-clientconnectionclosecallback-t.md) | 是 |

**示例**

```TypeScript
import { webSocket } from '@kit.NetworkKit';

let localServer = webSocket.createWebSocketServer();
localServer.on('close', (clientConnection: webSocket.WebSocketConnection, closeReason: webSocket.CloseResult) => {
  console.info(`client close, client: ${clientConnection}, closeReason: Code: ${closeReason.code}, reason: ${closeReason.reason}`);
});
```

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

订阅WebSocketServer的Error事件，使用callback异步回调。

**起始版本：** 19

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为19。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'error' | 是 |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 是 |

**示例**

```TypeScript
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let localServer = webSocket.createWebSocketServer();
localServer.on('error', (err: BusinessError) => {
  console.error(`error. Code: ${error.code}, message: ${error.message}`);
});
```

## onConnect

```TypeScript
onConnect(callback: Callback<WebSocketConnection>): void
```

订阅客户端请求连接服务器的事件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** 
- API版本23+：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[WebSocketConnection](arkts-network-websocket-websocketconnection-i.md)&gt; | 是 |

**示例**

```TypeScript
import { webSocket } from '@kit.NetworkKit';
import { BusinessError, Callback } from '@kit.BasicServicesKit';

let localServer = webSocket.createWebSocketServer();
localServer.onConnect((connection: webSocket.WebSocketConnection) => {
  console.info(`New client connected! Client ip: ${connection.clientIP}, Client port: ${connection.clientPort}`);
});
```

## onMessageReceive

```TypeScript
onMessageReceive(callback: Callback<WebSocketMessage>): void
```

订阅服务器收到消息的事件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** 
- API版本23+：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[WebSocketMessage](arkts-network-websocket-websocketmessage-i.md)&gt; | 是 |

**示例**

```TypeScript
import { webSocket } from '@kit.NetworkKit';

let localServer = webSocket.createWebSocketServer();
localServer.onMessageReceive((message: webSocket.WebSocketMessage) => {
  console.info(`on message received, client: ${message.clientConnection}, data: ${message.data}`);
});
```

## onWebSocketServerClose

```TypeScript
onWebSocketServerClose(callback: ClientConnectionCloseCallback): void
```

Enables listening for events that a connection from a given client has been closed.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ClientConnectionCloseCallback](arkts-network-websocket-clientconnectionclosecallback-t.md) | 是 |

**示例**

```TypeScript
import { webSocket } from '@kit.NetworkKit';

let localServer = webSocket.createWebSocketServer();
localServer.onWebSocketServerClose((clientConnection: webSocket.WebSocketConnection, closeReason: webSocket.CloseResult) => {
  console.info(`client close, client: ${clientConnection}, closeReason: Code: ${closeReason.code}, reason: ${closeReason.reason}`);
});
```

## onWebSocketServerError

```TypeScript
onWebSocketServerError(callback: ErrorCallback): void
```

订阅WebSocket服务器的错误事件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** 
- API版本23+：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 是 |

**示例**

```TypeScript
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let localServer = webSocket.createWebSocketServer();
localServer.onWebSocketServerError((err: BusinessError) => {
  console.error(`error. Code: ${err.code}, message: ${err.message}`);
});
```

## send

```TypeScript
send(data: string | ArrayBuffer, connection: WebSocketConnection): Promise<boolean>
```

通过WebSocket连接发送数据。使用Promise异步回调。

> **说明：**&gt;
> send接口必须在监听到connect事件后才可以调用。

**起始版本：** 19

**ArkTS模式：** ArkTS-Dyn起始版本为19；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | string \| ArrayBuffer | 是 |
| [connection](arkts-net-connection.md) | [WebSocketConnection](arkts-network-websocket-websocketconnection-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| 2302006 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();
let url = "ws://"
class OutValue {
  status: number = 0
  message: string = ""
}
ws.connect(url, (err: BusinessError, value: boolean) => {
    if (!err) {
      console.info("connect success")
    } else {
      console.error(`connect fail. Code: ${err.code}, message: ${err.message}`)
    }
});
ws.on('open', (err: BusinessError, value: Object) => {
  console.info("on open, status:" + (value as OutValue).status + ", message:" + (value as OutValue).message)
    ws.send("Hello, server!", (err: BusinessError, value: boolean) => {
    if (!err) {
      console.info("send success")
    } else {
      console.error(`send fail. Code: ${err.code}, message: ${err.message}`)
    }
  });
});
```

ArkTS-Sta示例：

```TypeScript
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let url = "ws://";
const ws : webSocket.WebSocket = webSocket.createWebSocket();

ws.onOpen((data: webSocket.OpenResult | undefined) => {
  console.info(`onopen value is ${data?.status}`);
  ws.send('Hello, server!', (err: BusinessError<void>|null, value: boolean|undefined) => {
    if (err?.code) {
      console.error(`send fail: ${err?.code} ${err?.message}`);
    } else {
      console.info(`send success and value is ${value}`);
    }
  })
});
ws.connect(url, (err: BusinessError<void>|null, value: boolean|undefined) => {
  if (err?.code) {
    console.error(`test connect fail ${err?.code} ${err?.message}`);
  } else {
    console.info(`test connect success and value is ${value}`);
  }
});
```

ArkTS-Dyn示例：

```TypeScript
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();
let url = "ws://";
class OutValue {
  status: number = 0
  message: string = ""
}
ws.connect(url, (err: BusinessError, value: boolean) => {
    if (!err) {
      console.info("connect success");
    } else {
      console.error(`connect fail. Code: ${err.code}, message: ${err.message}`);
    }
});

ws.on('open', (err: BusinessError, value: Object) => {
  console.info("on open, status:" + (value as OutValue).status + ", message:" + (value as OutValue).message);
  let promise = ws.send("Hello, server!");
  promise.then((value: boolean) => {
    console.info("send success");
  }).catch((err:string) => {
    console.error("send fail, error:" + JSON.stringify(err));
  });
});
```

ArkTS-Sta示例：

```TypeScript
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import hilog from '@ohos.hilog';

let domain: int = 0x0000;
let tag: string = ' WebsocketTestTag';
let url = "ws://";

const ws : webSocket.WebSocket = webSocket.createWebSocket();
ws.onOpen((data: webSocket.OpenResult | undefined) => {
  hilog.info(domain, tag, `onopen value is ${data?.status}`);
  ws.send('Hello, server!').then((value: boolean) => {
    hilog.info(domain, tag, `send success and value is ${value}`);
  }).catch((err: Error) => {
    hilog.info(domain, tag, `send fail ${err}`);
  })
});
ws.connect(url, (err: BusinessError<void>|null, value: boolean|undefined) => {
  if (err?.code) {
    hilog.info(domain, tag, `test connect fail ${err}`);
  } else {
    hilog.info(domain, tag, `test connect success and value is ${value}`);
  }
});
```

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

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
}).catch((err: Error) => {
  let error = err as BusinessError;
  console.error(`Failed to start. Code: ${error?.code}, message: ${error?.message}`);
});

localServer.onConnect((connection: webSocket.WebSocketConnection) => {
  console.info(`New client connected! Client ip: ${connection.clientIP}, Client port: ${connection.clientPort}`);
  // 当收到onConnect事件时，可以通过send()方法与客户端进行通信
  localServer.send("Hello, I'm server!", connection).then((success: boolean) => {
    if (success) {
      console.info('message send successfully');
    } else {
      console.error('message send failed');
    }
  }).catch((err: Error) => {
    let error = err as BusinessError;
    console.error(`message send failed, Code: ${error?.code}, message: ${error?.message}`);
  });
});
```

## start

```TypeScript
start(config: WebSocketServerConfig): Promise<boolean>
```

配置config参数，启动服务端service。使用Promise异步回调。

> **说明：**&gt;
> 在多次调用该接口时，应避免监听同一端口。

**起始版本：** 19

**ArkTS模式：** ArkTS-Dyn起始版本为19；ArkTS-Sta起始版本为24。

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [WebSocketServerConfig](arkts-network-websocket-websocketserverconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [2302002](../errorcode-net-webSocket.md#2302002-websocket-证书不存在) |
| [2302004](../errorcode-net-webSocket.md#2302004-websocketserver-无法在指定的nic网络接口上进行网络监听) |
| [2302005](../errorcode-net-webSocket.md#2302005-websocketserver-无法在指定的端口上进行网络监听) |
| [2302999](../errorcode-net-webSocket.md#2302999-内部错误) |
| [2302007](../errorcode-net-webSocket.md#2302007-websocketserver当前监听的端口已被占用) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

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
}).catch((err: Error) => {
  let error = err as BusinessError;
  console.error(`Failed to start. Code: ${error.code}, message: ${error.message}`);
});
```

## stop

```TypeScript
stop(): Promise<boolean>
```

停止服务端服务。使用Promise异步回调。

**起始版本：** 19

**ArkTS模式：** ArkTS-Dyn起始版本为19；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetStack

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

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
}).catch((err: Error) => {
  let error = err as BusinessError;
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
