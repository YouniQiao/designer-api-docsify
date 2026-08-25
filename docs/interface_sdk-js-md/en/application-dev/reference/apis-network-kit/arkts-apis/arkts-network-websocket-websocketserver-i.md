# WebSocketServer

Defines a **WebSocketServer** object. You need to use [webSocket.createWebSocketServer](arkts-network-websocket-createwebsocketserver-f.md) to create a **WebSocketServer** object before using its methods.

**Since:** 19

**System capability:** SystemCapability.Communication.NetStack

## Modules to Import

```TypeScript
import { webSocket } from 'kits/@kit.NetworkKit';
```

## close

```TypeScript
close(connection: WebSocketConnection, options?: webSocket.WebSocketCloseOptions): Promise<boolean>
```

Closes a WebSocket connection. This API uses a promise to return the result.

**Since:** 19

**Required permissions:** ohos.permission.INTERNET

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [connection](arkts-net-connection.md) | [WebSocketConnection](arkts-network-websocket-websocketconnection-i.md) | Yes |
| options | [webSocket.WebSocketCloseOptions](arkts-network-websocket-websocketcloseoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 2302006 |

## listAllConnections

```TypeScript
listAllConnections(): WebSocketConnection[]
```

Obtains information about all clients connected to the server.  
**Required permission**: ohos.permission.INTERNET

> **NOTE：**&gt;
> This API is called asynchronously. The **await** keyword needs to be used to wait until the asynchronous
> operation is complete, ensuring that information about all clients connected to the server can be correctly
> obtained.

**Since:** 19

**Required permissions:** ohos.permission.INTERNET

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [WebSocketConnection](arkts-network-websocket-websocketconnection-i.md)[] |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |

## off('connect')

```TypeScript
off(type: 'connect', callback?: Callback<WebSocketConnection>): void
```

Unsubscribes from WebSocketServer connection events (the connection between the client and server is successfully established). This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> You can pass the callback of the **on** function if you want to cancel listening for a certain type of event.
> If you do not pass the callback, you will cancel listening for all events.

**Since:** 19

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'connect' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[WebSocketConnection](arkts-network-websocket-websocketconnection-i.md)&gt; | No |

## off('messageReceive')

```TypeScript
off(type: 'messageReceive', callback?: Callback<WebSocketMessage>): void
```

Unsubscribes from the WebSocketServer event of receiving client messages. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> You can pass the callback of the **on** function if you want to cancel listening for a certain type of event.
> If you do not pass the callback, you will cancel listening for all events.

**Since:** 19

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'messageReceive' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[WebSocketMessage](arkts-network-websocket-websocketmessage-i.md)&gt; | No |

## off('close')

```TypeScript
off(type: 'close', callback?: ClientConnectionCloseCallback): void
```

Unsubscribes from WebSocketServer close events. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> You can pass the callback of the **on** function if you want to cancel listening for a certain type of event.
> If you do not pass the callback, you will cancel listening for all events.

**Since:** 19

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'close' | Yes |
| callback | [ClientConnectionCloseCallback](arkts-network-websocket-clientconnectionclosecallback-t.md) | No |

## off('error')

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

Unsubscribes from WebSocketServer error events. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> You can pass the callback of the **on** function if you want to cancel listening for a certain type of event.
> If you do not pass the callback, you will cancel listening for all events.

**Since:** 19

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'error' | Yes |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No |

## on('connect')

```TypeScript
on(type: 'connect', callback: Callback<WebSocketConnection>): void
```

Subscribes to the WebSocketServer connection event (the connection between the client and server is successfully established). This API uses an asynchronous callback to return the result.

**Since:** 19

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'connect' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[WebSocketConnection](arkts-network-websocket-websocketconnection-i.md)&gt; | Yes |

## on('messageReceive')

```TypeScript
on(type: 'messageReceive', callback: Callback<WebSocketMessage>): void
```

Subscribes to the WebSocketServer event of receiving client messages. This API uses an asynchronous callback to return the result.

**Since:** 19

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'messageReceive' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[WebSocketMessage](arkts-network-websocket-websocketmessage-i.md)&gt; | Yes |

## on('close')

```TypeScript
on(type: 'close', callback: ClientConnectionCloseCallback): void
```

Subscribes to WebSocketServer close events. This API uses an asynchronous callback to return the result.

**Since:** 19

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'close' | Yes |
| callback | [ClientConnectionCloseCallback](arkts-network-websocket-clientconnectionclosecallback-t.md) | Yes |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

Subscribes to WebSocketServer error events. This API uses an asynchronous callback to return the result.

**Since:** 19

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'error' | Yes |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes |

## send

```TypeScript
send(data: string | ArrayBuffer, connection: WebSocketConnection): Promise<boolean>
```

Sends data through the WebSocket connection. This API uses a promise to return the result.

> **NOTE：**&gt;
> The **send** API can be called only after a **connect** event is listened.
> **Required permission**: ohos.permission.INTERNET

**Since:** 19

**Required permissions:** ohos.permission.INTERNET

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | string \| ArrayBuffer | Yes |
| [connection](arkts-net-connection.md) | [WebSocketConnection](arkts-network-websocket-websocketconnection-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 2302006 |

## start

```TypeScript
start(config: WebSocketServerConfig): Promise<boolean>
```

Starts the WebSocketServer service based on the specified **config**. This API uses a promise to return the result.

> **NOTE：**&gt;
> You are advised not to listen for the same port when calling this API multiple times.
> **Required permission**: ohos.permission.INTERNET

**Since:** 19

**Required permissions:** ohos.permission.INTERNET

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [WebSocketServerConfig](arkts-network-websocket-websocketserverconfig-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [2302002](../errorcode-net-webSocket.md#2302002-websocket-certificate-does-not-exist) |
| [2302004](../errorcode-net-webSocket.md#2302004-listening-failed-on-the-specified-nic) |
| [2302005](../errorcode-net-webSocket.md#2302005-listening-failed-on-the-specified-port) |
| [2302999](../errorcode-net-webSocket.md#2302999-internal-error) |
| [2302007](../errorcode-net-webSocket.md#2302007-listening-port-already-occupied) |

## stop

```TypeScript
stop(): Promise<boolean>
```

Stops the WebSocketServer service. This API uses a promise to return the result.

**Since:** 19

**Required permissions:** ohos.permission.INTERNET

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
