# TLSSocket

Defines a TLS socket connection. Before calling TLSSocket APIs, you need to call [socket.constructTLSSocketInstance](arkts-network-socket-constructtlssocketinstance-f.md) to create a **TLSSocket** object.

**Since:** 9

**System capability:** SystemCapability.Communication.NetStack

## Modules to Import

```TypeScript
import { socket } from 'kits/@kit.NetworkKit';
```

## bind

```TypeScript
bind(address: NetAddress, callback: AsyncCallback<void>): void
```

Binds the IP address and port number. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> If the **TLSSocket** object is upgraded from a **TCPSocket** object, you do not need to execute the **bind**
> API.

**Since:** 9

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
| [2303198](../errorcode-net-socket.md#2303198-network-address-already-in-use) |
| [2300002](../errorcode-net-socket.md#2300002-system-internal-error) |

## bind

```TypeScript
bind(address: NetAddress): Promise<void>
```

Binds the IP address and port number. This API uses a promise to return the result.

> **NOTE：**&gt;
> If the **TLSSocket** object is upgraded from a **TCPSocket** object, you do not need to execute the **bind**
> API.

**Since:** 9

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
| [2303198](../errorcode-net-socket.md#2303198-network-address-already-in-use) |
| [2300002](../errorcode-net-socket.md#2300002-system-internal-error) |

## close

```TypeScript
close(callback: AsyncCallback<void>): void
```

Closes a **TLSSocket** connection. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2303501](../errorcode-net-socket.md#2303501-null-ssl) |
| [2303505](../errorcode-net-socket.md#2303505-tls-system-call-error) |
| [2303506](../errorcode-net-socket.md#2303506-failed-to-close-tls-connections) |
| [2300002](../errorcode-net-socket.md#2300002-system-internal-error) |

## close

```TypeScript
close(): Promise<void>
```

Closes a **TLSSocket** connection. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2303501](../errorcode-net-socket.md#2303501-null-ssl) |
| [2303505](../errorcode-net-socket.md#2303505-tls-system-call-error) |
| [2303506](../errorcode-net-socket.md#2303506-failed-to-close-tls-connections) |
| [2300002](../errorcode-net-socket.md#2300002-system-internal-error) |

## connect

```TypeScript
connect(options: TLSConnectOptions, callback: AsyncCallback<void>): void
```

Sets up a **TLSSocket** connection, and creates and initializes a TLS session after **bind** is successfully called. During this process, a TLS/SSL handshake is performed between the application and the server to implement data transmission. This API uses an asynchronous callback to return the result. Note that **ca** in **secureOptions** of the **options** parameter is mandatory in API version 11 or earlier. You need to enter the CA certificate of the server for certificate authentication. The certificate content starts with "-----BEGIN CERTIFICATE-----" and ends with "-----END CERTIFICATE-----". This field is optional since API version 12.

**Since:** 9

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
| [2303104](../errorcode-net-socket.md#2303104-system-call-interrupted) |
| [2303109](../errorcode-net-socket.md#2303109-error-file-number) |
| [2303111](../errorcode-net-socket.md#2303111-requested-resource-temporarily-unavailable) |
| [2303188](../errorcode-net-socket.md#2303188-socket-operations-on-non-sockets) |
| [2303191](../errorcode-net-socket.md#2303191-incorrect-socket-protocol-type) |
| [2303198](../errorcode-net-socket.md#2303198-network-address-already-in-use) |
| [2303199](../errorcode-net-socket.md#2303199-failed-to-assign-the-requested-address) |
| [2303210](../errorcode-net-socket.md#2303210-connection-timeout) |
| [2303501](../errorcode-net-socket.md#2303501-null-ssl) |
| [2303502](../errorcode-net-socket.md#2303502-tls-read-error) |
| [2303503](../errorcode-net-socket.md#2303503-tls-write-error) |
| [2303505](../errorcode-net-socket.md#2303505-tls-system-call-error) |
| [2303506](../errorcode-net-socket.md#2303506-failed-to-close-tls-connections) |
| [2300002](../errorcode-net-socket.md#2300002-system-internal-error) |
| [2301206](../errorcode-net-socket.md#2301206-failed-to-connect-to-the-proxy-server-via-socks5) |
| [2301207](../errorcode-net-socket.md#2301207-invalid-user-name-or-password-for-socks5-authentication) |
| [2301208](../errorcode-net-socket.md#2301208-failed-to-connect-to-the-remote-server-via-socks5) |
| [2301209](../errorcode-net-socket.md#2301209-authentication-mode-negotiation-failed-for-socks5) |
| [2301210](../errorcode-net-socket.md#2301210-failed-to-send-messages-via-socks5) |
| [2301211](../errorcode-net-socket.md#2301211-failed-to-receive-messages-via-socks5) |
| [2301212](../errorcode-net-socket.md#2301212-failed-to-serialize-messages-for-socks5) |
| [2301213](../errorcode-net-socket.md#2301213-failed-to-deserialize-messages-for-socks5) |

## connect

```TypeScript
connect(options: TLSConnectOptions): Promise<void>
```

Sets up a **TLSSocket** connection, and creates and initializes a TLS session after **bind** is successfully called. During this process, a TLS/SSL handshake is performed between the application and the server to implement data transmission. Both two-way and one-way authentication modes are supported. This API uses a promise to return the result. Note that **ca** in **secureOptions** of the **options** parameter is mandatory in API version 11 or earlier. You need to enter the CA certificate of the server for certificate authentication. The certificate content starts with "-----BEGIN CERTIFICATE-----" and ends with "-----END CERTIFICATE-----". This field is optional since API version 12.

**Since:** 9

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
| [2303104](../errorcode-net-socket.md#2303104-system-call-interrupted) |
| [2303109](../errorcode-net-socket.md#2303109-error-file-number) |
| [2303111](../errorcode-net-socket.md#2303111-requested-resource-temporarily-unavailable) |
| [2303188](../errorcode-net-socket.md#2303188-socket-operations-on-non-sockets) |
| [2303191](../errorcode-net-socket.md#2303191-incorrect-socket-protocol-type) |
| [2303198](../errorcode-net-socket.md#2303198-network-address-already-in-use) |
| [2303199](../errorcode-net-socket.md#2303199-failed-to-assign-the-requested-address) |
| [2303210](../errorcode-net-socket.md#2303210-connection-timeout) |
| [2303501](../errorcode-net-socket.md#2303501-null-ssl) |
| [2303502](../errorcode-net-socket.md#2303502-tls-read-error) |
| [2303503](../errorcode-net-socket.md#2303503-tls-write-error) |
| [2303505](../errorcode-net-socket.md#2303505-tls-system-call-error) |
| [2303506](../errorcode-net-socket.md#2303506-failed-to-close-tls-connections) |
| [2300002](../errorcode-net-socket.md#2300002-system-internal-error) |
| [2301206](../errorcode-net-socket.md#2301206-failed-to-connect-to-the-proxy-server-via-socks5) |
| [2301207](../errorcode-net-socket.md#2301207-invalid-user-name-or-password-for-socks5-authentication) |
| [2301208](../errorcode-net-socket.md#2301208-failed-to-connect-to-the-remote-server-via-socks5) |
| [2301209](../errorcode-net-socket.md#2301209-authentication-mode-negotiation-failed-for-socks5) |
| [2301210](../errorcode-net-socket.md#2301210-failed-to-send-messages-via-socks5) |
| [2301211](../errorcode-net-socket.md#2301211-failed-to-receive-messages-via-socks5) |
| [2301212](../errorcode-net-socket.md#2301212-failed-to-serialize-messages-for-socks5) |
| [2301213](../errorcode-net-socket.md#2301213-failed-to-deserialize-messages-for-socks5) |

## getCertificate

```TypeScript
getCertificate(callback: AsyncCallback<X509CertRawData>): void
```

Obtains the local digital certificate after a **TLSSocket** connection is established. This API is applicable to two-way authentication. It uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[X509CertRawData](arkts-network-socket-x509certrawdata-t.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [2303501](../errorcode-net-socket.md#2303501-null-ssl) |
| [2303504](../errorcode-net-socket.md#2303504-x509-failed-to-look-up-the-x509-certificate) |
| [2300002](../errorcode-net-socket.md#2300002-system-internal-error) |

## getCertificate

```TypeScript
getCertificate(): Promise<X509CertRawData>
```

Obtains the local digital certificate after a **TLSSocket** connection is established. This API is applicable to two-way authentication. It uses a promise to return the result.

**Since:** 9

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

## getCipherSuite

```TypeScript
getCipherSuite(callback: AsyncCallback<Array<string>>): void
```

Obtains the cipher suite negotiated by both communication parties after a **TLSSocket** connection is established. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [2303501](../errorcode-net-socket.md#2303501-null-ssl) |
| [2303502](../errorcode-net-socket.md#2303502-tls-read-error) |
| [2303505](../errorcode-net-socket.md#2303505-tls-system-call-error) |
| [2300002](../errorcode-net-socket.md#2300002-system-internal-error) |

## getCipherSuite

```TypeScript
getCipherSuite(): Promise<Array<string>>
```

Obtains the cipher suite negotiated by both communication parties after a **TLSSocket** connection is established. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [2303501](../errorcode-net-socket.md#2303501-null-ssl) |
| [2303502](../errorcode-net-socket.md#2303502-tls-read-error) |
| [2303505](../errorcode-net-socket.md#2303505-tls-system-call-error) |
| [2300002](../errorcode-net-socket.md#2300002-system-internal-error) |

## getLocalAddress

```TypeScript
getLocalAddress(): Promise<NetAddress>
```

Obtains the local socket address of a **TLSSocket** connection. This API uses a promise to return the result.

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

Obtains the communication protocol version after a **TLSSocket** connection is established. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [2303501](../errorcode-net-socket.md#2303501-null-ssl) |
| [2303505](../errorcode-net-socket.md#2303505-tls-system-call-error) |
| [2300002](../errorcode-net-socket.md#2300002-system-internal-error) |

## getProtocol

```TypeScript
getProtocol(): Promise<string>
```

Obtains the communication protocol version after a **TLSSocket** connection is established. This API uses a promise to return the result.

**Since:** 9

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

## getRemoteAddress

```TypeScript
getRemoteAddress(callback: AsyncCallback<NetAddress>): void
```

Obtains the remote address of a TLS socket connection. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;NetAddress&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [2303188](../errorcode-net-socket.md#2303188-socket-operations-on-non-sockets) |
| [2300002](../errorcode-net-socket.md#2300002-system-internal-error) |

## getRemoteAddress

```TypeScript
getRemoteAddress(): Promise<NetAddress>
```

Obtains the remote address of a TLS socket connection. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;NetAddress & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [2303188](../errorcode-net-socket.md#2303188-socket-operations-on-non-sockets) |
| [2300002](../errorcode-net-socket.md#2300002-system-internal-error) |

## getRemoteCertificate

```TypeScript
getRemoteCertificate(callback: AsyncCallback<X509CertRawData>): void
```

Obtains the digital certificate of the server after a **TLSSocket** connection is established. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[X509CertRawData](arkts-network-socket-x509certrawdata-t.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [2303501](../errorcode-net-socket.md#2303501-null-ssl) |
| [2300002](../errorcode-net-socket.md#2300002-system-internal-error) |

## getRemoteCertificate

```TypeScript
getRemoteCertificate(): Promise<X509CertRawData>
```

Obtains the digital certificate of the server after a **TLSSocket** connection is established. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[X509CertRawData](arkts-network-socket-x509certrawdata-t.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [2303501](../errorcode-net-socket.md#2303501-null-ssl) |
| [2300002](../errorcode-net-socket.md#2300002-system-internal-error) |

## getSignatureAlgorithms

```TypeScript
getSignatureAlgorithms(callback: AsyncCallback<Array<string>>): void
```

Obtains the signing algorithm negotiated by both communication parties after a **TLSSocket** connection is established. This API is applicable to two-way authentication. It uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [2303501](../errorcode-net-socket.md#2303501-null-ssl) |
| [2300002](../errorcode-net-socket.md#2300002-system-internal-error) |

## getSignatureAlgorithms

```TypeScript
getSignatureAlgorithms(): Promise<Array<string>>
```

Obtains the signing algorithm negotiated by both communication parties after a **TLSSocket** connection is established. This API is applicable to two-way authentication. It uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [2303501](../errorcode-net-socket.md#2303501-null-ssl) |
| [2300002](../errorcode-net-socket.md#2300002-system-internal-error) |

## getSocketFd

```TypeScript
getSocketFd(): Promise<number>
```

Obtains the file descriptor of the **TLSSocket** object. This API uses a promise to return the result.

> **NOTE：**&gt;
> - This API can be called only after **bind** is successfully called.&gt;
> - The lifecycle of the file descriptor is managed by the system. The application can use the
> [close](#close) method to close the socket connection,
> instead of directly operating the file descriptor.

**Since:** 16

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

## getState

```TypeScript
getState(callback: AsyncCallback<SocketStateBase>): void
```

Obtains the status of the TLS socket connection. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SocketStateBase](arkts-network-socket-socketstatebase-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [2303188](../errorcode-net-socket.md#2303188-socket-operations-on-non-sockets) |
| [2300002](../errorcode-net-socket.md#2300002-system-internal-error) |

## getState

```TypeScript
getState(): Promise<SocketStateBase>
```

Obtains the status of the TLS socket connection. This API uses a promise to return the result.

**Since:** 9

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

## off('message')

```TypeScript
off(type: 'message', callback?: Callback<SocketMessageInfo>): void
```

Unsubscribes from **message** events of the **TLSSocket** object. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'message' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SocketMessageInfo](arkts-network-socket-socketmessageinfo-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## off('connect' | 'close')

```TypeScript
off(type: 'connect' | 'close', callback?: Callback<void>): void
```

Unsubscribes from **connect** or **close** events of the **TLSSocket** object. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'connect' \| 'close' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## off('connect' | 'close')

```TypeScript
off(type: 'connect' | 'close', callback?: Callback<void>): void
```

Unsubscribes from **connect** or **close** events of the **TLSSocket** object. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'connect' \| 'close' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## off('error')

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

Unsubscribes from **error** events of the **TLSSocket** object. This API uses an asynchronous callback to return the result.

**Since:** 9

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

## on('message')

```TypeScript
on(type: 'message', callback: Callback<SocketMessageInfo>): void
```

Subscribes to **message** events of the **TLSSocket** object. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API can be called only after **bind** is successfully called.

**Since:** 9

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'message' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SocketMessageInfo](arkts-network-socket-socketmessageinfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## on('connect' | 'close')

```TypeScript
on(type: 'connect' | 'close', callback: Callback<void>): void
```

Subscribes to **connect** or **close** events of the **TLSSocket** object. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API can be called only after **bind** is successfully called.

**Since:** 9

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'connect' \| 'close' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## on('connect' | 'close')

```TypeScript
on(type: 'connect' | 'close', callback: Callback<void>): void
```

Subscribes to **connect** or **close** events of the **TLSSocket** object. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API can be called only after **bind** is successfully called.

**Since:** 9

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'connect' \| 'close' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

Subscribes to **error** events of the **TLSSocket** object. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API can be called only after **bind** is successfully called.

**Since:** 9

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

## send

```TypeScript
send(data: string | ArrayBuffer, callback: AsyncCallback<void>): void
```

Sends a message to the server after a **TLSSocket** connection is established. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | string \| ArrayBuffer | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2303501](../errorcode-net-socket.md#2303501-null-ssl) |
| [2303503](../errorcode-net-socket.md#2303503-tls-write-error) |
| [2303505](../errorcode-net-socket.md#2303505-tls-system-call-error) |
| [2303506](../errorcode-net-socket.md#2303506-failed-to-close-tls-connections) |
| [2300002](../errorcode-net-socket.md#2300002-system-internal-error) |

## send

```TypeScript
send(data: string | ArrayBuffer): Promise<void>
```

Sends a message to the server after a **TLSSocket** connection is established. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | string \| ArrayBuffer | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2303501](../errorcode-net-socket.md#2303501-null-ssl) |
| [2303503](../errorcode-net-socket.md#2303503-tls-write-error) |
| [2303505](../errorcode-net-socket.md#2303505-tls-system-call-error) |
| [2303506](../errorcode-net-socket.md#2303506-failed-to-close-tls-connections) |
| [2300002](../errorcode-net-socket.md#2300002-system-internal-error) |

## setExtraOptions

```TypeScript
setExtraOptions(options: TCPExtraOptions, callback: AsyncCallback<void>): void
```

Sets other properties of the **TCPSocket** object after **bind** is successfully called. This API uses an asynchronous callback to return the result.

**Since:** 9

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

Sets other properties of the **TCPSocket** object after **bind** is successfully called. This API uses a promise to return the result.

**Since:** 9

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
