# TCPSocketServer

Defines a TCP socket server connection. Before calling TCPSocketServer APIs, you need to call [socket.constructTCPSocketServerInstance](arkts-network-socket-constructtcpsocketserverinstance-f.md) to create a **TCPSocketServer** object.

**Since:** 10

**System capability:** SystemCapability.Communication.NetStack

## Modules to Import

```TypeScript
import { socket } from 'kits/@kit.NetworkKit';
```

## close

```TypeScript
close(): Promise<void>
```

Stops listening for events of the **TCPSocketServer** object and releases the port bound by [listen](#listen). If [listen](#listen) has been called for multiple times, all listening ports of the **TCPSocketServer** object are released when this API is called. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API does not close existing connections. To close connections, call the
> [close](arkts-network-socket-tcpsocketconnection-i.md#close) API of
> [TCPSocketConnection](arkts-network-socket-tcpsocketconnection-i.md).

**Since:** 20

**Required permissions:** ohos.permission.INTERNET

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [2300002](../errorcode-net-socket.md#2300002-system-internal-error) |

## getLocalAddress

```TypeScript
getLocalAddress(): Promise<NetAddress>
```

Obtains the local socket address of a **TCPSocketServer** connection. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API can be called only after **listen** is successfully called.

**Since:** 12

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;NetAddress & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [2300002](../errorcode-net-socket.md#2300002-system-internal-error) |
| [2301009](../errorcode-net-socket.md#2301009-bad-file-descriptor) |
| [2303188](../errorcode-net-socket.md#2303188-socket-operations-on-non-sockets) |

## getSocketFd

```TypeScript
getSocketFd(): Promise<number>
```

Obtains the file descriptor bound to the TCPSocketServer listening port. This API uses a promise to return the result.

> **NOTE：**&gt;
> - This method can be called only after the
> [listen](#listen) method is
> successfully called. When listen is called for multiple times, the file descriptor bound to the latest
> listening port is obtained.&gt;
> - This API returns **-1** in abnormal cases such as listening exceptions or socket closed (for example, after
> close is called).&gt;
> - The lifecycle of the file descriptor is managed by the system. The application can use the
> [close](#close) method to close the socket connection, instead of directly
> operating the file descriptor.

**Since:** 23

**Required permissions:** ohos.permission.INTERNET

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |

## getState

```TypeScript
getState(callback: AsyncCallback<SocketStateBase>): void
```

Obtains the status of a TCP socket server connection. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API can be called only after **listen** is successfully called.

**Since:** 10

**Required permissions:** ohos.permission.INTERNET

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SocketStateBase](arkts-network-socket-socketstatebase-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2300002](../errorcode-net-socket.md#2300002-system-internal-error) |
| [2303188](../errorcode-net-socket.md#2303188-socket-operations-on-non-sockets) |

## getState

```TypeScript
getState(): Promise<SocketStateBase>
```

Obtains the status of a TCP socket server connection. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API can be called only after **listen** is successfully called.

**Since:** 10

**Required permissions:** ohos.permission.INTERNET

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[SocketStateBase](arkts-network-socket-socketstatebase-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [2300002](../errorcode-net-socket.md#2300002-system-internal-error) |
| [2303188](../errorcode-net-socket.md#2303188-socket-operations-on-non-sockets) |

## listen

```TypeScript
listen(address: NetAddress, callback: AsyncCallback<void>): void
```

Binds the IP address and port number. The port number can be specified or randomly allocated by the system. The server listens to and accepts TCP socket connections established over the socket. Multiple threads are used to process client data concurrently. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> The server uses this API to perform the **bind**, **listen**, and **accept** operations. If the **bind**
> operation fails, the system randomly allocates a port number.

**Since:** 10

**Required permissions:** ohos.permission.INTERNET

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| address | [NetAddress](arkts-network-connection-netaddress-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [2300002](../errorcode-net-socket.md#2300002-system-internal-error) |
| [2303109](../errorcode-net-socket.md#2303109-error-file-number) |
| [2303111](../errorcode-net-socket.md#2303111-requested-resource-temporarily-unavailable) |
| [2303198](../errorcode-net-socket.md#2303198-network-address-already-in-use) |
| [2303199](../errorcode-net-socket.md#2303199-failed-to-assign-the-requested-address) |

## listen

```TypeScript
listen(address: NetAddress): Promise<void>
```

Binds the IP address and port number. The port number can be specified or randomly allocated by the system. The server listens to and accepts TCP socket connections established over the socket. Multiple threads are used to process client data concurrently. This API uses a promise to return the result.

> **NOTE：**&gt;
> The server uses this API to perform the **bind**, **listen**, and **accept** operations. If the **bind**
> operation fails, the system randomly allocates a port number.

**Since:** 10

**Required permissions:** ohos.permission.INTERNET

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| address | [NetAddress](arkts-network-connection-netaddress-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [2300002](../errorcode-net-socket.md#2300002-system-internal-error) |
| [2303109](../errorcode-net-socket.md#2303109-error-file-number) |
| [2303111](../errorcode-net-socket.md#2303111-requested-resource-temporarily-unavailable) |
| [2303198](../errorcode-net-socket.md#2303198-network-address-already-in-use) |
| [2303199](../errorcode-net-socket.md#2303199-failed-to-assign-the-requested-address) |

## off('connect')

```TypeScript
off(type: 'connect', callback?: Callback<TCPSocketConnection>): void
```

Unsubscribes from **connect** events of the **TCPSocketServer** object. This API uses an asynchronous callback to return the result.

**Since:** 10

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'connect' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[TCPSocketConnection](arkts-network-socket-tcpsocketconnection-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## off('error')

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

Unsubscribes from **error** events of the **TCPSocketServer** object. This API uses an asynchronous callback to return the result.

**Since:** 10

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'error' | Yes |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## on('connect')

```TypeScript
on(type: 'connect', callback: Callback<TCPSocketConnection>): void
```

Subscribes to **connect** events of the **TCPSocketServer** object. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API can be called only after **listen** is successfully called.

**Since:** 10

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'connect' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[TCPSocketConnection](arkts-network-socket-tcpsocketconnection-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

Subscribes to **error** events of the **TCPSocketServer** object. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API can be called only after **listen** is successfully called.

**Since:** 10

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'error' | Yes |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## setExtraOptions

```TypeScript
setExtraOptions(options: TCPExtraOptions, callback: AsyncCallback<void>): void
```

Sets other properties of the **TCPSocketServer** object. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API can be called only after **listen** is successfully called.

**Since:** 10

**Required permissions:** ohos.permission.INTERNET

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [TCPExtraOptions](arkts-network-socket-tcpextraoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2300002](../errorcode-net-socket.md#2300002-system-internal-error) |
| [2303188](../errorcode-net-socket.md#2303188-socket-operations-on-non-sockets) |

## setExtraOptions

```TypeScript
setExtraOptions(options: TCPExtraOptions): Promise<void>
```

Sets other properties of the **TCPSocketServer** object. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API can be called only after **listen** is successfully called.

**Since:** 10

**Required permissions:** ohos.permission.INTERNET

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [TCPExtraOptions](arkts-network-socket-tcpextraoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2300002](../errorcode-net-socket.md#2300002-system-internal-error) |
| [2303188](../errorcode-net-socket.md#2303188-socket-operations-on-non-sockets) |
