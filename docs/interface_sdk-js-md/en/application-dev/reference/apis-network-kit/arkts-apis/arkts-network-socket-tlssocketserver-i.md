# TLSSocketServer

Defines a TLS socket server connection. Before calling TLSSocketServer APIs, you need to call [socket.constructTLSSocketServerInstance](arkts-network-socket-constructtlssocketserverinstance-f.md) to create a **TLSSocketServer** object.

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

Stops listening for events of the **TLSSocketServer** object and releases the port bound by [listen](arkts-network-socket-tcpsocketserver-i.md#listen). This API uses a promise to return the result.

> **NOTE：**&gt;
> This API does not close existing connections. To close the connection, call the
> [close](arkts-network-socket-tcpsocketconnection-i.md#close) API of
> [TLSSocketConnection](arkts-network-socket-tlssocketconnection-i.md).

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

## getCertificate

```TypeScript
getCertificate(callback: AsyncCallback<X509CertRawData>): void
```

Obtains the local digital certificate after a **TLSSocketServer** connection is established. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API can be called only after **listen** is successfully called.

**Since:** 10

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[X509CertRawData](arkts-network-socket-x509certrawdata-t.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2303501](../errorcode-net-socket.md#2303501-null-ssl) |
| [2303504](../errorcode-net-socket.md#2303504-x509-failed-to-look-up-the-x509-certificate) |
| [2300002](../errorcode-net-socket.md#2300002-system-internal-error) |

## getCertificate

```TypeScript
getCertificate(): Promise<X509CertRawData>
```

Obtains the local digital certificate after a **TLSSocketServer** connection is established. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API can be called only after **listen** is successfully called.

**Since:** 10

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[X509CertRawData](arkts-network-socket-x509certrawdata-t.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [2303501](../errorcode-net-socket.md#2303501-null-ssl) |
| [2303504](../errorcode-net-socket.md#2303504-x509-failed-to-look-up-the-x509-certificate) |
| [2300002](../errorcode-net-socket.md#2300002-system-internal-error) |

## getLocalAddress

```TypeScript
getLocalAddress(): Promise<NetAddress>
```

Obtains the local socket address of a **TLSSocketServer** connection. This API uses a promise to return the result.

> **NOTE：**&gt;
> Call this API only after the **TLSSocketServer** connection is successfully established.

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

## getProtocol

```TypeScript
getProtocol(callback: AsyncCallback<string>): void
```

Obtains the communication protocol version after a **TLSSocketServer** connection is established. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API can be called only after **listen** is successfully called.

**Since:** 10

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2303501](../errorcode-net-socket.md#2303501-null-ssl) |
| [2303505](../errorcode-net-socket.md#2303505-tls-system-call-error) |
| [2300002](../errorcode-net-socket.md#2300002-system-internal-error) |

## getProtocol

```TypeScript
getProtocol(): Promise<string>
```

Obtains the communication protocol version after a **TLSSocketServer** connection is established. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API can be called only after **listen** is successfully called.

**Since:** 10

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [2303501](../errorcode-net-socket.md#2303501-null-ssl) |
| [2303505](../errorcode-net-socket.md#2303505-tls-system-call-error) |
| [2300002](../errorcode-net-socket.md#2300002-system-internal-error) |

## getSocketFd

```TypeScript
getSocketFd(): Promise<number>
```

Obtains the file descriptor bound to the TLSSocketServer listening port. This API uses a promise to return the result.

> **NOTE：**&gt;
> - This method can be called only after the [listen](arkts-network-socket-tcpsocketserver-i.md#listen) method is successfully
> called. When listen is called for multiple times, the file descriptor bound to the latest listening port is
> obtained.&gt;
> - This API returns **-1** in abnormal cases such as listening exceptions or socket closed (for example, after
> close is called).&gt;
> - The lifecycle of the file descriptor is managed by the system. The application can use the
> [close](arkts-network-socket-tcpsocketserver-i.md#close) method to close the socket connection, instead of directly
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

Obtains the status of the TLS socket server connection upon successful listening. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API can be called only after **listen** is successfully called.

**Since:** 10

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SocketStateBase](arkts-network-socket-socketstatebase-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2303188](../errorcode-net-socket.md#2303188-socket-operations-on-non-sockets) |
| [2300002](../errorcode-net-socket.md#2300002-system-internal-error) |

## getState

```TypeScript
getState(): Promise<SocketStateBase>
```

Obtains the status of the TLS socket server connection upon successful listening. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API can be called only after **listen** is successfully called.

**Since:** 10

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[SocketStateBase](arkts-network-socket-socketstatebase-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [2303188](../errorcode-net-socket.md#2303188-socket-operations-on-non-sockets) |
| [2300002](../errorcode-net-socket.md#2300002-system-internal-error) |

## listen

```TypeScript
listen(options: TLSConnectOptions, callback: AsyncCallback<void>): void
```

Listens for client connections after **bind** is successfully called to bind the IP address and port of **TLSSocketServer**. This API uses an asynchronous callback to return the result. After a connection is established, a TLS session will be created and initialized and a certificate key will be loaded and verified.

> **NOTE：**&gt;
> If the IP address is set to 0.0.0.0, all local IP addresses can be listened on.

**Since:** 10

**Required permissions:** ohos.permission.INTERNET

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [TLSConnectOptions](arkts-network-socket-tlsconnectoptions-i.md) | Yes |
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
| [2303501](../errorcode-net-socket.md#2303501-null-ssl) |
| [2303502](../errorcode-net-socket.md#2303502-tls-read-error) |
| [2303503](../errorcode-net-socket.md#2303503-tls-write-error) |
| [2303505](../errorcode-net-socket.md#2303505-tls-system-call-error) |
| [2303506](../errorcode-net-socket.md#2303506-failed-to-close-tls-connections) |

## listen

```TypeScript
listen(options: TLSConnectOptions): Promise<void>
```

Listens for client connections after **bind** is successfully called to bind the IP address and port of **TLSSocketServer**. This API uses an asynchronous callback to return the result. After a connection is established, a TLS session will be created and initialized and a certificate key will be loaded and verified.

**Since:** 10

**Required permissions:** ohos.permission.INTERNET

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [TLSConnectOptions](arkts-network-socket-tlsconnectoptions-i.md) | Yes |

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
| [2303501](../errorcode-net-socket.md#2303501-null-ssl) |
| [2303502](../errorcode-net-socket.md#2303502-tls-read-error) |
| [2303503](../errorcode-net-socket.md#2303503-tls-write-error) |
| [2303505](../errorcode-net-socket.md#2303505-tls-system-call-error) |
| [2303506](../errorcode-net-socket.md#2303506-failed-to-close-tls-connections) |

## off('connect')

```TypeScript
off(type: 'connect', callback?: Callback<TLSSocketConnection>): void
```

Unsubscribes from **connect** events of the **TLSSocketServer** object. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API can be called only after **listen** is successfully called.&gt;
> You can pass the callback of the **on** function if you want to cancel listening for a certain type of events.
> If you do not pass the callback, you will cancel listening for all events.

**Since:** 10

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'connect' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[TLSSocketConnection](arkts-network-socket-tlssocketconnection-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## off('error')

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

Unsubscribes from **error** events of the **TLSSocketServer** object. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API can be called only after **listen** is successfully called.&gt;
> You can pass the callback of the **on** function if you want to cancel listening for a certain type of events.
> If you do not pass the callback, you will cancel listening for all events.

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
on(type: 'connect', callback: Callback<TLSSocketConnection>): void
```

Subscribes to TLS socket server connection events. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API can be called only after **listen** is successfully called.

**Since:** 10

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'connect' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[TLSSocketConnection](arkts-network-socket-tlssocketconnection-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

Subscribes to **error** events of the **TLSSocketServer** object. This API uses an asynchronous callback to return the result.

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

Sets other properties of the **TLSSocketServer** object after **listen** is successfully called. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API can be called only after **listen** is successfully called.

**Since:** 10

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [TCPExtraOptions](arkts-network-socket-tcpextraoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2303188](../errorcode-net-socket.md#2303188-socket-operations-on-non-sockets) |
| [2300002](../errorcode-net-socket.md#2300002-system-internal-error) |

## setExtraOptions

```TypeScript
setExtraOptions(options: TCPExtraOptions): Promise<void>
```

Sets other properties of the **TLSSocketServer** object after **listen** is successfully called. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API can be called only after **listen** is successfully called.

**Since:** 10

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2303188](../errorcode-net-socket.md#2303188-socket-operations-on-non-sockets) |
| [2300002](../errorcode-net-socket.md#2300002-system-internal-error) |
