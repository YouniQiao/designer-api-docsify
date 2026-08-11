# IRemoteObject

Provides methods to query of obtain interface descriptors, add or delete death notifications, dump object status to  specific files, and send messages.

**Since:** 7

<!--Device-rpc-abstract class IRemoteObject--><!--Device-rpc-abstract class IRemoteObject-End-->

**System capability:** SystemCapability.Communication.IPC.Core

## Modules to Import

```TypeScript
import { rpc } from 'kits/@kit.IPCKit';
```

## addDeathRecipient

```TypeScript
addDeathRecipient(recipient: DeathRecipient, flags: number): boolean
```

Adds a callback for receiving death notifications of the remote object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [registerDeathRecipient](arkts-ipc-rpc-iremoteobject-c.md#registerdeathrecipient)(recipient:

<!--Device-IRemoteObject-addDeathRecipient(recipient: DeathRecipient, flags: number): boolean--><!--Device-IRemoteObject-addDeathRecipient(recipient: DeathRecipient, flags: number): boolean-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| recipient | [DeathRecipient](arkts-ipc-rpc-deathrecipient-i.md) | Yes |
| flags | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## getDescriptor

```TypeScript
getDescriptor(): string
```

Obtains the interface descriptor (which is a string) of this object.

**Since:** 9

<!--Device-IRemoteObject-getDescriptor(): string--><!--Device-IRemoteObject-getDescriptor(): string-End-->

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

Obtains the interface descriptor (which is a string) of this object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getDescriptor](arkts-ipc-rpc-iremoteobject-c.md#getdescriptor)()

<!--Device-IRemoteObject-getInterfaceDescriptor(): string--><!--Device-IRemoteObject-getInterfaceDescriptor(): string-End-->

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

<!--Device-IRemoteObject-getLocalInterface(descriptor: string): IRemoteBroker--><!--Device-IRemoteObject-getLocalInterface(descriptor: string): IRemoteBroker-End-->

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
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## isObjectDead

```TypeScript
isObjectDead(): boolean
```

Checks whether this object is dead.

**Since:** 7

<!--Device-IRemoteObject-isObjectDead(): boolean--><!--Device-IRemoteObject-isObjectDead(): boolean-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## queryLocalInterface

```TypeScript
queryLocalInterface(descriptor: string): IRemoteBroker
```

Obtains the string of the interface descriptor.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getLocalInterface](arkts-ipc-rpc-iremoteobject-c.md#getlocalinterface)(descriptor:

<!--Device-IRemoteObject-queryLocalInterface(descriptor: string): IRemoteBroker--><!--Device-IRemoteObject-queryLocalInterface(descriptor: string): IRemoteBroker-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| descriptor | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [IRemoteBroker](arkts-ipc-rpc-iremotebroker-i.md) |

## registerDeathRecipient

```TypeScript
registerDeathRecipient(recipient: DeathRecipient, flags: number): void
```

Registers a callback for receiving death notifications of the remote object.

**Since:** 9

<!--Device-IRemoteObject-registerDeathRecipient(recipient: DeathRecipient, flags: int): void--><!--Device-IRemoteObject-registerDeathRecipient(recipient: DeathRecipient, flags: int): void-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| recipient | [DeathRecipient](arkts-ipc-rpc-deathrecipient-i.md) | Yes |
| flags | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [1900008](../errorcode-rpc.md#1900008-invalid-ipc-object) |
| [1900005](../errorcode-rpc.md#1900005-ipc-object-permission-error) |

## removeDeathRecipient

```TypeScript
removeDeathRecipient(recipient: DeathRecipient, flags: number): boolean
```

Removes the callback used to receive death notifications of the remote object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [unregisterDeathRecipient](arkts-ipc-rpc-iremoteobject-c.md#unregisterdeathrecipient)(recipient:

<!--Device-IRemoteObject-removeDeathRecipient(recipient: DeathRecipient, flags: number): boolean--><!--Device-IRemoteObject-removeDeathRecipient(recipient: DeathRecipient, flags: number): boolean-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| recipient | [DeathRecipient](arkts-ipc-rpc-deathrecipient-i.md) | Yes |
| flags | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## sendMessageRequest

```TypeScript
sendMessageRequest(
      code: number,
      data: MessageSequence,
      reply: MessageSequence,
      options: MessageOption
    ): Promise<RequestResult>
```

Sends a **MessageSequence** message to the remote process in synchronous or asynchronous mode. If asynchronous  mode is set in **options**, a promise will be fulfilled immediately and the reply message is empty. The  specific reply needs to be obtained from the callback on the service side. If synchronous mode is set  in **options**, a promise will be fulfilled when the response to **sendMessageRequest** is returned, and the  reply message contains the returned information.

**Since:** 9

<!--Device-IRemoteObject-sendMessageRequest(      code: int,      data: MessageSequence,      reply: MessageSequence,      options: MessageOption    ): Promise<RequestResult>--><!--Device-IRemoteObject-sendMessageRequest(      code: int,      data: MessageSequence,      reply: MessageSequence,      options: MessageOption    ): Promise<RequestResult>-End-->

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
| Promise&lt;RequestResult&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

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

Sends a **MessageSequence** message to the remote process in synchronous or asynchronous mode. If asynchronous  mode is set in **options**, a callback will be called immediately, and the reply message is empty. The  specific reply needs to be obtained from the callback on the service side. If synchronous mode is set in  
 **options**, a callback will be invoked when the response to **sendRequest** is returned, and the reply  message contains the returned information.

**Since:** 9

<!--Device-IRemoteObject-sendMessageRequest(      code: int,      data: MessageSequence,      reply: MessageSequence,      options: MessageOption,      callback: AsyncCallback<RequestResult>    ): void--><!--Device-IRemoteObject-sendMessageRequest(      code: int,      data: MessageSequence,      reply: MessageSequence,      options: MessageOption,      callback: AsyncCallback<RequestResult>    ): void-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| code | number | Yes |
| data | [MessageSequence](arkts-ipc-rpc-messagesequence-c.md) | Yes |
| reply | [MessageSequence](arkts-ipc-rpc-messagesequence-c.md) | Yes |
| options | [MessageOption](arkts-ipc-rpc-messageoption-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;RequestResult&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## sendRequest

```TypeScript
sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): boolean
```

Sends a **MessageParcel** message to the remote process in synchronous or asynchronous mode. If asynchronous mode  is set in **options**, a promise will be fulfilled immediately and the reply message does not contain any  content. If synchronous mode is set in **options**, a promise will be fulfilled when the response to  
 **sendRequest** is returned, and the reply message contains the returned information.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [sendMessageRequest](arkts-ipc-rpc-iremoteobject-c.md#sendmessagerequest)(code:

<!--Device-IRemoteObject-sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): boolean--><!--Device-IRemoteObject-sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): boolean-End-->

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

Sends a **MessageParcel** message to the remote process in synchronous or asynchronous mode. If asynchronous mode  is set in **options**, a promise will be fulfilled immediately and the reply message is empty. The specific  reply needs to be obtained from the callback on the service side. If synchronous mode is set in **options**, a promise will be fulfilled when the response to **sendRequest** is returned, and the reply message contains  the returned information.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [sendMessageRequest](arkts-ipc-rpc-iremoteobject-c.md#sendmessagerequest)(code:

<!--Device-IRemoteObject-sendRequest(      code: number,      data: MessageParcel,      reply: MessageParcel,      options: MessageOption    ): Promise<SendRequestResult>--><!--Device-IRemoteObject-sendRequest(      code: number,      data: MessageParcel,      reply: MessageParcel,      options: MessageOption    ): Promise<SendRequestResult>-End-->

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
| Promise&lt;SendRequestResult&gt; |

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

Sends a **MessageParcel** message to the remote process in synchronous or asynchronous mode. If asynchronous mode  is set in **options**, a callback will be called immediately, and the reply message is empty. The specific  reply needs to be obtained from the callback on the service side. If synchronous mode is set in **options**, a callback will be invoked when the response to **sendRequest** is returned, and the reply message contains  the returned information.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [sendMessageRequest](arkts-ipc-rpc-iremoteobject-c.md#sendmessagerequest)(code:

<!--Device-IRemoteObject-sendRequest(      code: number,      data: MessageParcel,      reply: MessageParcel,      options: MessageOption,      callback: AsyncCallback<SendRequestResult>    ): void--><!--Device-IRemoteObject-sendRequest(      code: number,      data: MessageParcel,      reply: MessageParcel,      options: MessageOption,      callback: AsyncCallback<SendRequestResult>    ): void-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| code | number | Yes |
| data | [MessageParcel](arkts-ipc-rpc-messageparcel-c.md) | Yes |
| reply | [MessageParcel](arkts-ipc-rpc-messageparcel-c.md) | Yes |
| options | [MessageOption](arkts-ipc-rpc-messageoption-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;SendRequestResult&gt; | Yes |

## unregisterDeathRecipient

```TypeScript
unregisterDeathRecipient(recipient: DeathRecipient, flags: number): void
```

Unregisters from the callback used to receive death notifications of the remote object.

**Since:** 9

<!--Device-IRemoteObject-unregisterDeathRecipient(recipient: DeathRecipient, flags: int): void--><!--Device-IRemoteObject-unregisterDeathRecipient(recipient: DeathRecipient, flags: int): void-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| recipient | [DeathRecipient](arkts-ipc-rpc-deathrecipient-i.md) | Yes |
| flags | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [1900008](../errorcode-rpc.md#1900008-invalid-ipc-object) |
| [1900005](../errorcode-rpc.md#1900005-ipc-object-permission-error) |
