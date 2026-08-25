# MulticastSocket

Defines a **MulticastSocket** connection. Before calling MulticastSocket APIs, you need to call [socket.constructMulticastSocketInstance](arkts-network-socket-constructmulticastsocketinstance-f.md) to create a **MulticastSocket** object.

**Inheritance/Implementation:** MulticastSocket extends [UDPSocket](arkts-network-socket-udpsocket-i.md)

**Since:** 11

**System capability:** SystemCapability.Communication.NetStack

## Modules to Import

```TypeScript
import { socket } from 'kits/@kit.NetworkKit';
```

## addMembership

```TypeScript
addMembership(multicastAddress: NetAddress, callback: AsyncCallback<void>): void
```

Adds a member to a multicast group. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> The IP addresses used for multicast belong to a specific range, for example, 224.0.0.0 to 239.255.255.255.&gt;
> A member in a multicast group can serve as a sender or a receiver. Data is transmitted in broadcast mode,
> regardless of the client or server.

**Since:** 11

**Required permissions:** ohos.permission.INTERNET

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| multicastAddress | [NetAddress](arkts-network-connection-netaddress-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 2301022 |
| 2301088 |
| 2301098 |

## addMembership

```TypeScript
addMembership(multicastAddress: NetAddress): Promise<void>
```

Adds a member to a multicast group. This API uses a promise to return the result.

> **NOTE：**&gt;
> The IP addresses used for multicast belong to a specific range, for example, 224.0.0.0 to 239.255.255.255.&gt;
> A member in a multicast group can serve as a sender or a receiver. Data is transmitted in broadcast mode,
> regardless of the client or server.

**Since:** 11

**Required permissions:** ohos.permission.INTERNET

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| multicastAddress | [NetAddress](arkts-network-connection-netaddress-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 2301088 |
| 2301098 |

## dropMembership

```TypeScript
dropMembership(multicastAddress: NetAddress, callback: AsyncCallback<void>): void
```

Drops a member from a multicast group. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> The IP addresses used for multicast belong to a specific range, for example, 224.0.0.0 to 239.255.255.255.&gt;
> You can drop only a member that has been added to a multicast group by using
> [addMembership](#addmembership).

**Since:** 11

**Required permissions:** ohos.permission.INTERNET

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| multicastAddress | [NetAddress](arkts-network-connection-netaddress-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 2301088 |
| 2301098 |

## dropMembership

```TypeScript
dropMembership(multicastAddress: NetAddress): Promise<void>
```

Drops a member from a multicast group. This API uses a promise to return the result.

> **NOTE：**&gt;
> The IP addresses used for multicast belong to a specific range, for example, 224.0.0.0 to 239.255.255.255.&gt;
> You can drop only a member that has been added to a multicast group by using
> [addMembership](#addmembership).

**Since:** 11

**Required permissions:** ohos.permission.INTERNET

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| multicastAddress | [NetAddress](arkts-network-connection-netaddress-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 2301088 |
| 2301098 |

## getLoopbackMode

```TypeScript
getLoopbackMode(callback: AsyncCallback<boolean>): void
```

Obtains the loopback mode flag for multicast communication. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> Use this API to check whether the loopback mode is enabled.&gt;
> The value **true** indicates that the loopback mode is enabled, and the value **false** indicates the opposite.
> When the loopback mode is disabled, the host does not receive the multicast packets sent by itself.&gt;
> This API is effective only after
> [addMembership](#addmembership)
> is called.

**Since:** 11

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 2301088 |

## getLoopbackMode

```TypeScript
getLoopbackMode(): Promise<boolean>
```

Obtains the loopback mode flag for multicast communication. This API uses a promise to return the result.

> **NOTE：**&gt;
> Use this API to check whether the loopback mode is enabled.&gt;
> The value **true** indicates that the loopback mode is enabled, and the value **false** indicates the opposite.
> When the loopback mode is disabled, the host does not receive the multicast packets sent by itself.&gt;
> This API is effective only after
> [addMembership](#addmembership)
> is called.

**Since:** 11

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 2301088 |

## getMulticastTTL

```TypeScript
getMulticastTTL(callback: AsyncCallback<number>): void
```

Obtains the TTL for multicast packets. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> TTL is used to limit the maximum number of router hops for packet transmission on a network.&gt;
> The value ranges from 0 to 255. The default value is **1**.&gt;
> If the TTL value is **1**, multicast packets can be transmitted only to the host directly connected to the
> sender. If the TTL is set to a large value, multicast packets can be transmitted over a longer distance.&gt;
> This API is effective only after
> [addMembership](#addmembership)
> is called.

**Since:** 11

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 2301088 |

## getMulticastTTL

```TypeScript
getMulticastTTL(): Promise<number>
```

Obtains the TTL for multicast packets. This API uses a promise to return the result.

> **NOTE：**&gt;
> TTL is used to limit the maximum number of router hops for packet transmission on a network.&gt;
> The value ranges from 0 to 255. The default value is **1**.&gt;
> If the TTL value is **1**, multicast packets can be transmitted only to the host directly connected to the
> sender. If the TTL is set to a large value, multicast packets can be transmitted over a longer distance.&gt;
> This API is effective only after
> [addMembership](#addmembership)
> is called.

**Since:** 11

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 2301088 |

## getSocketFd

```TypeScript
getSocketFd(): Promise<number>
```

Obtains the file descriptor of the MulticastSocket. This API uses a promise to return the result.

> **NOTE：**&gt;
> - This API can be called only after
> [bind](arkts-network-socket-udpsocket-i.md#bind) is successfully called.&gt;
> - This API returns **-1** in abnormal cases such as bind exceptions or socket closed (for example, after close
> is called).&gt;
> - The lifecycle of the file descriptor is managed by the system. The application can use the
> [close](arkts-network-socket-udpsocket-i.md#close) method to close the socket connection,
> instead of directly operating the file descriptor.

**Since:** 23

**Required permissions:** ohos.permission.INTERNET

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |

## setLoopbackMode

```TypeScript
setLoopbackMode(flag: boolean, callback: AsyncCallback<void>): void
```

Sets the loopback mode flag for multicast communication. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> Use this API to enable or disable the loopback mode. By default, the loopback mode is enabled.&gt;
> The value **true** indicates that the host is allowed to receive the multicast packets sent by itself, and the
> value **false** indicates the opposite.&gt;
> This API is effective only after
> [addMembership](#addmembership)
> is called.

**Since:** 11

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| flag | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 2301088 |

## setLoopbackMode

```TypeScript
setLoopbackMode(flag: boolean): Promise<void>
```

Sets the loopback mode flag for multicast communication. This API uses a promise to return the result.

> **NOTE：**&gt;
> Use this API to enable or disable the loopback mode. By default, the loopback mode is enabled.&gt;
> The value **true** indicates that the host is allowed to receive the multicast packets sent by itself, and the
> value **false** indicates the opposite.&gt;
> This API is effective only after
> [addMembership](#addmembership)
> is called.

**Since:** 11

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| flag | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 2301088 |

## setMulticastTTL

```TypeScript
setMulticastTTL(ttl: number, callback: AsyncCallback<void>): void
```

Sets the time to live (TTL) for multicast packets. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> TTL is used to limit the maximum number of router hops for packet transmission on a network.&gt;
> The value ranges from 0 to 255. The default value is **1**.&gt;
> If the TTL value is **1**, multicast packets can be transmitted only to the host directly connected to the
> sender. If the TTL is set to a large value, multicast packets can be transmitted over a longer distance.&gt;
> This API is effective only after
> [addMembership](#addmembership)
> is called.

**Since:** 11

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ttl | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 2301022 |
| 2301088 |

## setMulticastTTL

```TypeScript
setMulticastTTL(ttl: number): Promise<void>
```

Sets the TTL for multicast packets. This API uses a promise to return the result.

> **NOTE：**&gt;
> TTL is used to limit the maximum number of router hops for packet transmission on a network.&gt;
> The value ranges from 0 to 255. The default value is **1**.&gt;
> If the TTL value is **1**, multicast packets can be transmitted only to the host directly connected to the
> sender. If the TTL is set to a large value, multicast packets can be transmitted over a longer distance.&gt;
> This API is effective only after
> [addMembership](#addmembership)
> is called.

**Since:** 11

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ttl | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 2301022 |
| 2301088 |

## setReuseAddress

```TypeScript
setReuseAddress(reuse: boolean): void
```

Sets whether the multicast socket supports address reuse. This API is called in synchronous mode.

> **NOTE：**&gt;
> This API is used to control whether to enable address reuse when a multicast socket is bound to a port.&gt;
> To bind an occupied port, ensure that the address reuse capability is enabled for the party that occupies the
> port. In addition, the service needs to call this API before calling
> [bind](arkts-network-socket-udpsocket-i.md#bind) to enable the address
> reuse capability.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| reuse | boolean | Yes |
