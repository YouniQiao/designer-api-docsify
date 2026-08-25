# RemoteObject

Provides methods to implement **RemoteObject**. The service provider must inherit from this class.

**Inheritance/Implementation:** RemoteObject extends [IRemoteObject](arkts-ipc-rpc-iremoteobject-c.md)

**Since:** 7

**System capability:** SystemCapability.Communication.IPC.Core

## Modules to Import

```TypeScript
import { rpc } from 'kits/@kit.IPCKit';
```

## attachLocalInterface

```TypeScript
attachLocalInterface(localInterface: IRemoteBroker, descriptor: string): void
```

Binds an interface descriptor to an **IRemoteBroker** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [modifyLocalInterface](#modifylocalinterface)(localInterface: IRemoteBroker, descriptor: string)

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localInterface | [IRemoteBroker](arkts-ipc-rpc-iremotebroker-i.md) | Yes |
| descriptor | string | Yes |

## constructor

```TypeScript
constructor(descriptor: string)
```

A constructor used to create a **RemoteObject** object.

**Since:** 7

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| descriptor | string | Yes |

## getCallingPid

```TypeScript
getCallingPid(): number
```

Obtains the PID of the remote process.

**Since:** 7

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getCallingUid

```TypeScript
getCallingUid(): number
```

Obtains the UID of the remote process.

**Since:** 7

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getDescriptor

```TypeScript
getDescriptor(): string
```

Obtains the interface descriptor of this object. The interface descriptor is a string.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [1900008](../errorcode-rpc.md#1900008-invalid-ipc-object) |

## getInterfaceDescriptor

```TypeScript
getInterfaceDescriptor(): string
```

Obtains the interface descriptor.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getDescriptor](arkts-ipc-rpc-iremoteobject-c.md#getdescriptor)()

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getLocalInterface

```TypeScript
getLocalInterface(descriptor: string): IRemoteBroker
```

Obtains the string of the interface descriptor.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| descriptor | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [IRemoteBroker](arkts-ipc-rpc-iremotebroker-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## modifyLocalInterface

```TypeScript
modifyLocalInterface(localInterface: IRemoteBroker, descriptor: string): void
```

Binds an interface descriptor to an **IRemoteBroker** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localInterface | [IRemoteBroker](arkts-ipc-rpc-iremotebroker-i.md) | Yes |
| descriptor | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## onRemoteMessageRequest

```TypeScript
onRemoteMessageRequest(
      code: number,
      data: MessageSequence,
      reply: MessageSequence,
      options: MessageOption
    ): boolean | Promise<boolean>
```

Called to return a response to **sendMessageRequest()**. The server processes the request synchronously or asynchronously and returns the result in this API.

> **NOTE：**&gt;
> - You are advised to overload **onRemoteMessageRequest** preferentially, which implements synchronous and
> asynchronous message processing.&gt;
> - If both **onRemoteRequest()** and **onRemoteMessageRequest()** are overloaded, only
> **onRemoteMessageRequest()** takes effect.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| code | number | Yes |
| data | [MessageSequence](arkts-ipc-rpc-messagesequence-c.md) | Yes |
| reply | [MessageSequence](arkts-ipc-rpc-messagesequence-c.md) | Yes |
| options | [MessageOption](arkts-ipc-rpc-messageoption-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean \| Promise & lt;boolean & gt; |

## onRemoteMessageRequest

```TypeScript
onRemoteMessageRequest(
      code: number,
      data: MessageSequence,
      reply: MessageSequence,
      options: MessageOption,
      callingInfo?: CallingInfo
    ): boolean | Promise<boolean>
```

Provides a response to **sendMessageRequest()**. The server processes the request and returns a response in this API. The IPC context can be obtained from the input parameter **callingInfo**.

> **NOTE：**&gt;
> You are advised to overload the **onRemoteMessageRequest** method with the **CallingInfo** parameter to
> implement synchronous and asynchronous message processing.
> If both **onRemoteRequest()** and **onRemoteMessageRequest()** are overloaded, only
> **onRemoteMessageRequest()** takes effect.

**Since:** 23

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| code | number | Yes |
| data | [MessageSequence](arkts-ipc-rpc-messagesequence-c.md) | Yes |
| reply | [MessageSequence](arkts-ipc-rpc-messagesequence-c.md) | Yes |
| options | [MessageOption](arkts-ipc-rpc-messageoption-c.md) | Yes |
| callingInfo | [CallingInfo](arkts-ipc-rpc-callinginfo-c.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean \| Promise & lt;boolean & gt; |

## onRemoteRequest

```TypeScript
onRemoteRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): boolean
```

Called to return a response to **sendRequest()**. The server processes the request and returns a response in this function.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [onRemoteMessageRequest](#onremotemessagerequest)(code: int, data: MessageSequence, reply: MessageSequence,
     *     options: MessageOption)

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| code | number | Yes |
| data | [MessageParcel](arkts-ipc-rpc-messageparcel-c.md) | Yes |
| reply | [MessageParcel](arkts-ipc-rpc-messageparcel-c.md) | Yes |
| options | [MessageOption](arkts-ipc-rpc-messageoption-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## queryLocalInterface

```TypeScript
queryLocalInterface(descriptor: string): IRemoteBroker
```

Checks whether the remote object corresponding to the specified interface token exists.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getLocalInterface](arkts-ipc-rpc-iremoteobject-c.md#getlocalinterface)(descriptor: string)

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| descriptor | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [IRemoteBroker](arkts-ipc-rpc-iremotebroker-i.md) |

## sendMessageRequest

```TypeScript
sendMessageRequest(
      code: number,
      data: MessageSequence,
      reply: MessageSequence,
      options: MessageOption
    ): Promise<RequestResult>
```

Sends a **MessageSequence** message to the remote process in synchronous or asynchronous mode. If asynchronous mode is set in **options**, a promise will be fulfilled immediately and the reply message is empty. The specific reply needs to be obtained from the callback on the service side. If synchronous mode is set in **options**, a promise will be fulfilled when the response to **sendMessageRequest** is returned, and the reply message contains the returned information.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| code | number | Yes |
| data | [MessageSequence](arkts-ipc-rpc-messagesequence-c.md) | Yes |
| reply | [MessageSequence](arkts-ipc-rpc-messagesequence-c.md) | Yes |
| options | [MessageOption](arkts-ipc-rpc-messageoption-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;RequestResult & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## sendMessageRequest

```TypeScript
sendMessageRequest(
      code: number,
      data: MessageSequence,
      reply: MessageSequence,
      options: MessageOption,
      callback: AsyncCallback<RequestResult>
    ): void
```

Sends a **MessageSequence** message to the remote process in synchronous or asynchronous mode. If asynchronous mode is set in **options**, a callback will be called immediately, and the reply message is empty. The specific reply needs to be obtained from the callback on the service side. If synchronous mode is set in **options**, a callback will be invoked when the response to **sendMessageRequest** is returned, and the reply message contains the returned information.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| code | number | Yes |
| data | [MessageSequence](arkts-ipc-rpc-messagesequence-c.md) | Yes |
| reply | [MessageSequence](arkts-ipc-rpc-messagesequence-c.md) | Yes |
| options | [MessageOption](arkts-ipc-rpc-messageoption-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;RequestResult&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## sendRequest

```TypeScript
sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): boolean
```

Sends a **MessageParcel** message to the remote process in synchronous or asynchronous mode. If asynchronous mode is set in **options**, a promise will be fulfilled immediately and the reply message is empty. The specific reply needs to be obtained from the callback on the service side. If synchronous mode is set in **options**, a promise will be fulfilled when the response to **sendRequest** is returned, and the reply message contains the returned information.

**Since:** 7

**Deprecated since:** 8

**Substitutes:** [sendMessageRequest](arkts-ipc-rpc-iremoteobject-c.md#sendmessagerequest)(code: int, data: MessageSequence, reply: MessageSequence,
     *     options: MessageOption)

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| code | number | Yes |
| data | [MessageParcel](arkts-ipc-rpc-messageparcel-c.md) | Yes |
| reply | [MessageParcel](arkts-ipc-rpc-messageparcel-c.md) | Yes |
| options | [MessageOption](arkts-ipc-rpc-messageoption-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## sendRequest

```TypeScript
sendRequest(
      code: number,
      data: MessageParcel,
      reply: MessageParcel,
      options: MessageOption
    ): Promise<SendRequestResult>
```

Sends a **MessageParcel** message to the remote process in synchronous or asynchronous mode. If asynchronous mode is set in **options**, a promise will be fulfilled immediately and the reply message is empty. The specific reply needs to be obtained from the callback on the service side. If synchronous mode is set in **options**, a promise will be fulfilled when the response to **sendRequest** is returned, and the reply message contains the returned information.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [sendMessageRequest](arkts-ipc-rpc-iremoteobject-c.md#sendmessagerequest)(code: int, data: MessageSequence, reply: MessageSequence,
     *     options: MessageOption)

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| code | number | Yes |
| data | [MessageParcel](arkts-ipc-rpc-messageparcel-c.md) | Yes |
| reply | [MessageParcel](arkts-ipc-rpc-messageparcel-c.md) | Yes |
| options | [MessageOption](arkts-ipc-rpc-messageoption-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[SendRequestResult](arkts-ipc-rpc-sendrequestresult-i.md)&gt; |

## sendRequest

```TypeScript
sendRequest(
      code: number,
      data: MessageParcel,
      reply: MessageParcel,
      options: MessageOption,
      callback: AsyncCallback<SendRequestResult>
    ): void
```

Sends a **MessageParcel** message to the remote process in synchronous or asynchronous mode. If asynchronous mode is set in **options**, a callback will be called immediately, and the reply message is empty. The specific reply needs to be obtained from the callback on the service side. If synchronous mode is set in **options**, a callback will be invoked when the response to **sendRequest** is returned, and the reply message contains the returned information.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [sendMessageRequest](arkts-ipc-rpc-iremoteobject-c.md#sendmessagerequest)(code: int, data: MessageSequence, reply: MessageSequence,
     *     options: MessageOption, callback: AsyncCallback&lt;RequestResult&gt;)

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| code | number | Yes |
| data | [MessageParcel](arkts-ipc-rpc-messageparcel-c.md) | Yes |
| reply | [MessageParcel](arkts-ipc-rpc-messageparcel-c.md) | Yes |
| options | [MessageOption](arkts-ipc-rpc-messageoption-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SendRequestResult](arkts-ipc-rpc-sendrequestresult-i.md)&gt; | Yes |
