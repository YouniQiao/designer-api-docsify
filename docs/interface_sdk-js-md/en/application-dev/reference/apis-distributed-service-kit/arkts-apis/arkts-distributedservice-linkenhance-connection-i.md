# Connection

Represents a **Connection** object, which provides methods for connecting to and disconnecting from a peer device, obtaining the device's ID, sending data, and registering or unregistering event callbacks.

**Since:** 20

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## Modules to Import

```TypeScript
import { linkEnhance } from 'kits/@kit.DistributedServiceKit';
```

## close

```TypeScript
close(): void
```

Destroys the **Connection** object to release resources. If the device needs to interact with the peer device again, create a **Connection** object again and call **connect()** to initiate a connection. **close()** is called to destroy the **Connection** object and release resources. If the call is successful, the **Connection** object needs to be re-created when it is needed again. **disconnect()** is called for disconnection. If the call is successful, the **Connection** object can still be connected. If the connection needs to be re-established, call **disconnect()**. If the service is no longer needed, call **close()**.

**Since:** 20

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |

## connect

```TypeScript
connect(): void
```

Connects to the server on the client after the **Connection** object is successfully created. A maximum number of 10 connections are supported. You are advised to register a callback listener using **on('connectResult')** and then call this method to obtain the connection result. After the connection is successful, you can call **sendData()** to send data. When the connection is no longer needed, call **disconnect()** to disconnect from the server.

**Since:** 20

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [32390204](../errorcode-link-enhance.md#32390204-number-of-connections-exceeding-the-limit) |
| [32390300](../errorcode-link-enhance.md#32390300-internal-error) |

## disconnect

```TypeScript
disconnect(): void
```

Disconnects from the peer device. The created **Connection** object remains valid after this API is called. You can call **connect()** to reconnect to the peer device if necessary.

**Since:** 20

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |

## getPeerDeviceId

```TypeScript
getPeerDeviceId(): string
```

Obtains the device ID of the peer device. This API is called when the connection is established successfully either by initiating a connection or accepting an incoming connection.

**Since:** 20

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |

## off('connectResult')

```TypeScript
off(type: 'connectResult', callback?: Callback<ConnectResult>): void
```

Unregisters the listener for **connectResult** events.

**Since:** 20

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'connectResult' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ConnectResult&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [32390206](../errorcode-link-enhance.md#32390206-invalid-parameter) |

## off('disconnected')

```TypeScript
off(type: 'disconnected', callback?: Callback<number>): void
```

Unregisters the listener for **disconnected** events. This API uses an asynchronous callback to return the result.

**Since:** 20

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'disconnected' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [32390206](../errorcode-link-enhance.md#32390206-invalid-parameter) |

## off('dataReceived')

```TypeScript
off(type: 'dataReceived', callback?: Callback<ArrayBuffer>): void
```

Unregisters the listener for **dataReceived** events.

**Since:** 20

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'dataReceived' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ArrayBuffer&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [32390206](../errorcode-link-enhance.md#32390206-invalid-parameter) |

## on('connectResult')

```TypeScript
on(type: 'connectResult', callback: Callback<ConnectResult>): void
```

Registers a listener for **connectResult** events. This API uses an asynchronous callback to return the result. You must register this listener before calling **connect()**. Otherwise, the connection result cannot be obtained. When the listener is no longer needed, you are advised to call **off('connectResult')** to unregister the listener to prevent memory leak.

**Since:** 20

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'connectResult' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ConnectResult&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [32390206](../errorcode-link-enhance.md#32390206-invalid-parameter) |

## on('disconnected')

```TypeScript
on(type: 'disconnected', callback: Callback<number>): void
```

Registers a listener for **disconnected** events. This API uses an asynchronous callback to return the result.

**Since:** 20

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'disconnected' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [32390206](../errorcode-link-enhance.md#32390206-invalid-parameter) |

## on('dataReceived')

```TypeScript
on(type: 'dataReceived', callback: Callback<ArrayBuffer>): void
```

Registers a listener for the **dataReceived** events. This API uses an asynchronous callback to return the result.

**Since:** 20

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'dataReceived' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ArrayBuffer&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [32390206](../errorcode-link-enhance.md#32390206-invalid-parameter) |

## sendData

```TypeScript
sendData(data: ArrayBuffer): void
```

Sends data to the server after a connection is established successfully. When the server receives the connection callback, it can also send data to the client.

**Since:** 20

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | ArrayBuffer | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [32390206](../errorcode-link-enhance.md#32390206-invalid-parameter) |
| [32390205](../errorcode-link-enhance.md#32390205-connection-unavailable) |
| [32390300](../errorcode-link-enhance.md#32390300-internal-error) |
