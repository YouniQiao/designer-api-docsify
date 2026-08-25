# LocalSocketServer

Defines a local socket server connection. Before calling LocalSocketServer APIs, you need to call [socket.constructLocalSocketServerInstance](arkts-network-socket-constructlocalsocketserverinstance-f.md) to create a **LocalSocketServer** object.

**Since:** 11

**System capability:** SystemCapability.Communication.NetStack

## Modules to Import

```TypeScript
import { socket } from 'kits/@kit.NetworkKit';
```

## close

```TypeScript
close(): Promise<void>
```

Stops listening for events of the **LocalSocketServer** object and releases the port bound by [listen](#listen). This API uses a promise to return the result.

> **NOTE：**&gt;
> This API does not close existing connections. To close the connection, call the [close] (#close11-1) API of
> [LocalSocketConnection] (#localsocketconnection11).

**Since:** 20

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [2300002](../errorcode-net-socket.md#2300002-system-internal-error) |

## getExtraOptions

```TypeScript
getExtraOptions(): Promise<ExtraOptionsBase>
```

Obtains the socket properties of the **LocalSocketServer** object. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API can be called only after **listen** is successfully called.

**Since:** 11

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ExtraOptionsBase](arkts-network-socket-extraoptionsbase-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## getLocalAddress

```TypeScript
getLocalAddress(): Promise<string>
```

Obtains the local socket address of a **LocalSocketServer** connection. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API can be called only after **listen** is successfully called.

**Since:** 12

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

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

Obtains the file descriptor bound to the LocalSocketServer listening port. This API uses a promise to return the result.

> **NOTE：**&gt;
> - This method can be called only after the [listen](#listen) method is
> successfully called.&gt;
> - This API returns **-1** in abnormal cases such as listening exceptions or socket closed (for example, after
> close is called).&gt;
> - The lifecycle of the file descriptor is managed by the system. The application can use the
> [close](arkts-network-socket-tcpsocketserver-i.md#close) method to close the socket connection, instead of directly
> operating the file descriptor.

**Since:** 23

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

## getState

```TypeScript
getState(): Promise<SocketStateBase>
```

Obtains the status of a local socket server connection. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API can be called only after **listen** is successfully called.

**Since:** 11

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[SocketStateBase](arkts-network-socket-socketstatebase-i.md)&gt; |

## listen

```TypeScript
listen(address: LocalAddress): Promise<void>
```

Binds the address of the local socket file. The server listens to and accepts local socket connections established over the socket. Multiple threads are used to process client data concurrently. This API uses a promise to return the result.

> **NOTE：**&gt;
> The server uses this API to complete the **bind**, **listen**, and **accept** operations. If the address of the
> local socket file is passed for binding, a socket file is automatically created when this API is called.

**Since:** 11

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| address | [LocalAddress](arkts-network-socket-localaddress-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2303109](../errorcode-net-socket.md#2303109-error-file-number) |
| [2301013](../errorcode-net-socket.md#2301013-insufficient-permissions) |
| 2301022 |
| 2301098 |

## off('connect')

```TypeScript
off(type: 'connect', callback?: Callback<LocalSocketConnection>): void
```

Unsubscribes from **connect** events of the **LocalSocketServer** object. This API uses an asynchronous callback to return the result.

**Since:** 11

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'connect' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[LocalSocketConnection](arkts-network-socket-localsocketconnection-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## off('error')

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

Unsubscribes from **error** events of the **LocalSocketServer** object. This API uses an asynchronous callback to return the result.

**Since:** 11

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
on(type: 'connect', callback: Callback<LocalSocketConnection>): void
```

Subscribes to **connect** events of the **LocalSocketServer** object. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API can be called only after **listen** is successfully called.

**Since:** 11

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'connect' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[LocalSocketConnection](arkts-network-socket-localsocketconnection-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

Subscribes to **error** events of the **LocalSocketServer** object. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API can be called only after **listen** is successfully called.

**Since:** 11

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
setExtraOptions(options: ExtraOptionsBase): Promise<void>
```

Sets the socket properties of the **LocalSocketServer** object. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API can be called only after **listen** is successfully called.

**Since:** 11

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [ExtraOptionsBase](arkts-network-socket-extraoptionsbase-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2301009](../errorcode-net-socket.md#2301009-bad-file-descriptor) |
