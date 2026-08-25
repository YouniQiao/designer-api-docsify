# WebSocketServer

在调用WebSocketServer方法前，需要先通过[webSocket.createWebSocketServer](arkts-network-websocket-createwebsocketserver-f.md)创建一个 WebSocketServer。

**起始版本：** 19

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { webSocket } from 'kits/@kit.NetworkKit';
```

## close

```TypeScript
close(connection: WebSocketConnection, options?: webSocket.WebSocketCloseOptions): Promise<boolean>
```

关闭指定websocket连接。使用Promise异步回调。

**起始版本：** 19

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

## listAllConnections

```TypeScript
listAllConnections(): WebSocketConnection[]
```

获取与服务端连接的所有客户端信息。

> **说明：**&gt;
> 该接口为异步调用，返回结果需通过await关键字等待异步操作完成，以确保正确获取到所有客户端连接信息。

**起始版本：** 19

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

## off('connect')

```TypeScript
off(type: 'connect', callback?: Callback<WebSocketConnection>): void
```

取消订阅WebSocketServer的连接事件（客户端与服务端建链成功），使用callback异步回调。

> **说明：**&gt;
> 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**起始版本：** 19

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'connect' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[WebSocketConnection](arkts-network-websocket-websocketconnection-i.md)&gt; | 否 |

## off('messageReceive')

```TypeScript
off(type: 'messageReceive', callback?: Callback<WebSocketMessage>): void
```

取消订阅WebSocketServer的接收到客户端消息事件，使用callback异步回调。

> **说明：**&gt;
> 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**起始版本：** 19

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'messageReceive' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[WebSocketMessage](arkts-network-websocket-websocketmessage-i.md)&gt; | 否 |

## off('close')

```TypeScript
off(type: 'close', callback?: ClientConnectionCloseCallback): void
```

取消订阅WebSocketServer的关闭事件，使用callback异步回调。

> **说明：**&gt;
> 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**起始版本：** 19

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'close' | 是 |
| callback | [ClientConnectionCloseCallback](arkts-network-websocket-clientconnectionclosecallback-t.md) | 否 |

## off('error')

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

取消订阅WebSocketServer的Error事件，使用callback异步回调。

> **说明：**&gt;
> 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**起始版本：** 19

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'error' | 是 |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 否 |

## on('connect')

```TypeScript
on(type: 'connect', callback: Callback<WebSocketConnection>): void
```

订阅WebSocketServer的连接事件（客户端与服务端建链成功），使用callback异步回调。

**起始版本：** 19

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'connect' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[WebSocketConnection](arkts-network-websocket-websocketconnection-i.md)&gt; | 是 |

## on('messageReceive')

```TypeScript
on(type: 'messageReceive', callback: Callback<WebSocketMessage>): void
```

订阅WebSocketServer的接收客户端消息的事件，使用callback异步回调。

**起始版本：** 19

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'messageReceive' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[WebSocketMessage](arkts-network-websocket-websocketmessage-i.md)&gt; | 是 |

## on('close')

```TypeScript
on(type: 'close', callback: ClientConnectionCloseCallback): void
```

订阅WebSocketServer的关闭事件，使用callback异步回调。

**起始版本：** 19

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'close' | 是 |
| callback | [ClientConnectionCloseCallback](arkts-network-websocket-clientconnectionclosecallback-t.md) | 是 |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

订阅WebSocketServer的Error事件，使用callback异步回调。

**起始版本：** 19

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'error' | 是 |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 是 |

## send

```TypeScript
send(data: string | ArrayBuffer, connection: WebSocketConnection): Promise<boolean>
```

通过WebSocket连接发送数据。使用Promise异步回调。

> **说明：**&gt;
> send接口必须在监听到connect事件后才可以调用。

**起始版本：** 19

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

## start

```TypeScript
start(config: WebSocketServerConfig): Promise<boolean>
```

配置config参数，启动服务端service。使用Promise异步回调。

> **说明：**&gt;
> 在多次调用该接口时，应避免监听同一端口。

**起始版本：** 19

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

## stop

```TypeScript
stop(): Promise<boolean>
```

停止服务端服务。使用Promise异步回调。

**起始版本：** 19

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
