# IRemoteObject

该接口可用于查询或获取接口描述符、添加或删除死亡通知、转储对象状态到特定文件、发送消息。

**起始版本：** 7

<!--Device-rpc-abstract class IRemoteObject--><!--Device-rpc-abstract class IRemoteObject-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

## addDeathRecipient

```TypeScript
addDeathRecipient(recipient: DeathRecipient, flags: number): boolean
```

注册用于接收远程对象死亡通知的回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [registerDeathRecipient](arkts-ipc-rpc-iremoteobject-c.md#registerdeathrecipient)(recipient:

<!--Device-IRemoteObject-addDeathRecipient(recipient: DeathRecipient, flags: number): boolean--><!--Device-IRemoteObject-addDeathRecipient(recipient: DeathRecipient, flags: number): boolean-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| recipient | [DeathRecipient](arkts-ipc-rpc-deathrecipient-i.md) | 是 |
| flags | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## getDescriptor

```TypeScript
getDescriptor(): string
```

获取对象的接口描述符，接口描述符为字符串。

**起始版本：** 9

<!--Device-IRemoteObject-getDescriptor(): string--><!--Device-IRemoteObject-getDescriptor(): string-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [1900008](../errorcode-rpc.md#1900008-非法的ipc对象) |

## getInterfaceDescriptor

```TypeScript
getInterfaceDescriptor(): string
```

获取对象的接口描述符，接口描述符为字符串。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getDescriptor](arkts-ipc-rpc-iremoteobject-c.md#getdescriptor)()

<!--Device-IRemoteObject-getInterfaceDescriptor(): string--><!--Device-IRemoteObject-getInterfaceDescriptor(): string-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| string |

## getLocalInterface

```TypeScript
getLocalInterface(descriptor: string): IRemoteBroker
```

查询接口描述符的字符串。

**起始版本：** 9

<!--Device-IRemoteObject-getLocalInterface(descriptor: string): IRemoteBroker--><!--Device-IRemoteObject-getLocalInterface(descriptor: string): IRemoteBroker-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| descriptor | string | 是 |

**返回值：**

| 类型 |
| --- |
| [IRemoteBroker](arkts-ipc-rpc-iremotebroker-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## isObjectDead

```TypeScript
isObjectDead(): boolean
```

检查当前对象是否死亡。

**起始版本：** 7

<!--Device-IRemoteObject-isObjectDead(): boolean--><!--Device-IRemoteObject-isObjectDead(): boolean-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## queryLocalInterface

```TypeScript
queryLocalInterface(descriptor: string): IRemoteBroker
```

查询接口描述符的字符串。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getLocalInterface](arkts-ipc-rpc-iremoteobject-c.md#getlocalinterface)(descriptor:

<!--Device-IRemoteObject-queryLocalInterface(descriptor: string): IRemoteBroker--><!--Device-IRemoteObject-queryLocalInterface(descriptor: string): IRemoteBroker-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| descriptor | string | 是 |

**返回值：**

| 类型 |
| --- |
| [IRemoteBroker](arkts-ipc-rpc-iremotebroker-i.md) |

## registerDeathRecipient

```TypeScript
registerDeathRecipient(recipient: DeathRecipient, flags: number): void
```

注册用于接收远程对象死亡通知的回调。

**起始版本：** 9

<!--Device-IRemoteObject-registerDeathRecipient(recipient: DeathRecipient, flags: int): void--><!--Device-IRemoteObject-registerDeathRecipient(recipient: DeathRecipient, flags: int): void-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| recipient | [DeathRecipient](arkts-ipc-rpc-deathrecipient-i.md) | 是 |
| flags | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [1900008](../errorcode-rpc.md#1900008-非法的ipc对象) |
| [1900005](../errorcode-rpc.md#1900005-ipc对象权限错误) |

## removeDeathRecipient

```TypeScript
removeDeathRecipient(recipient: DeathRecipient, flags: number): boolean
```

注销用于接收远程对象死亡通知的回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [unregisterDeathRecipient](arkts-ipc-rpc-iremoteobject-c.md#unregisterdeathrecipient)(recipient:

<!--Device-IRemoteObject-removeDeathRecipient(recipient: DeathRecipient, flags: number): boolean--><!--Device-IRemoteObject-removeDeathRecipient(recipient: DeathRecipient, flags: number): boolean-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| recipient | [DeathRecipient](arkts-ipc-rpc-deathrecipient-i.md) | 是 |
| flags | number | 是 |

**返回值：**

| 类型 |
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

以同步或异步方式向对端进程发送MessageSequence消息。如果为选项设置了异步模式，则发送请求的响应结果立即返回，reply报文里没有内容，具体回复需要在业务侧的回调中获取。如果为选项设置了同步模式，则发送请求的响应结果将在sendMessageRequest返回时返回，回复内容在reply报文里。使用Promise异步回调。

**起始版本：** 9

<!--Device-IRemoteObject-sendMessageRequest(      code: int,      data: MessageSequence,      reply: MessageSequence,      options: MessageOption    ): Promise<RequestResult>--><!--Device-IRemoteObject-sendMessageRequest(      code: int,      data: MessageSequence,      reply: MessageSequence,      options: MessageOption    ): Promise<RequestResult>-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| code | number | 是 |
| data | [MessageSequence](arkts-ipc-rpc-messagesequence-c.md) | 是 |
| reply | [MessageSequence](arkts-ipc-rpc-messagesequence-c.md) | 是 |
| options | [MessageOption](arkts-ipc-rpc-messageoption-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;RequestResult&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

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

以同步或异步方式向对端进程发送MessageSequence消息。如果为选项设置了异步模式，则立即收到回调，reply报文里没有内容，具体回复需要在业务侧的回调中获取。如果为选项设置了同步模式，则将在sendRequest返回时收到回调，回复内容在reply报文里。

**起始版本：** 9

<!--Device-IRemoteObject-sendMessageRequest(      code: int,      data: MessageSequence,      reply: MessageSequence,      options: MessageOption,      callback: AsyncCallback<RequestResult>    ): void--><!--Device-IRemoteObject-sendMessageRequest(      code: int,      data: MessageSequence,      reply: MessageSequence,      options: MessageOption,      callback: AsyncCallback<RequestResult>    ): void-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| code | number | 是 |
| data | [MessageSequence](arkts-ipc-rpc-messagesequence-c.md) | 是 |
| reply | [MessageSequence](arkts-ipc-rpc-messagesequence-c.md) | 是 |
| options | [MessageOption](arkts-ipc-rpc-messageoption-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;RequestResult&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## sendRequest

```TypeScript
sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): boolean
```

以同步或异步方式向对端进程发送MessageParcel消息。如果为选项设置了异步模式，则立即返回，reply报文里没有内容。如果为选项设置了同步模式，则将在sendRequest返回时收到回复，回复内容在reply报文里。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [sendMessageRequest](arkts-ipc-rpc-iremoteobject-c.md#sendmessagerequest)(code:

<!--Device-IRemoteObject-sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): boolean--><!--Device-IRemoteObject-sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): boolean-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| code | number | 是 |
| data | [MessageParcel](arkts-ipc-rpc-messageparcel-c.md) | 是 |
| reply | [MessageParcel](arkts-ipc-rpc-messageparcel-c.md) | 是 |
| options | [MessageOption](arkts-ipc-rpc-messageoption-c.md) | 是 |

**返回值：**

| 类型 |
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

以同步或异步方式向对端进程发送MessageParcel消息。如果为选项设置了异步模式，则发送请求的响应结果立即返回，reply报文里没有内容，具体回复需要在业务侧的回调中获取。如果为选项设置了同步模式，则发送请求的响应结果将在sendRequest返回时返回，回复内容在reply报文里。使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [sendMessageRequest](arkts-ipc-rpc-iremoteobject-c.md#sendmessagerequest)(code:

<!--Device-IRemoteObject-sendRequest(      code: number,      data: MessageParcel,      reply: MessageParcel,      options: MessageOption    ): Promise<SendRequestResult>--><!--Device-IRemoteObject-sendRequest(      code: number,      data: MessageParcel,      reply: MessageParcel,      options: MessageOption    ): Promise<SendRequestResult>-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| code | number | 是 |
| data | [MessageParcel](arkts-ipc-rpc-messageparcel-c.md) | 是 |
| reply | [MessageParcel](arkts-ipc-rpc-messageparcel-c.md) | 是 |
| options | [MessageOption](arkts-ipc-rpc-messageoption-c.md) | 是 |

**返回值：**

| 类型 |
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

以同步或异步方式向对端进程发送MessageParcel消息。使用callback异步回调。如果为选项设置了异步模式，则立即收到回调，reply报文里没有内容，具体回复需要在业务侧的回调中获取。如果为选项设置了同步模式，则将在sendRequest返回时收到回调，回复内容在reply报文里。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [sendMessageRequest](arkts-ipc-rpc-iremoteobject-c.md#sendmessagerequest)(code:

<!--Device-IRemoteObject-sendRequest(      code: number,      data: MessageParcel,      reply: MessageParcel,      options: MessageOption,      callback: AsyncCallback<SendRequestResult>    ): void--><!--Device-IRemoteObject-sendRequest(      code: number,      data: MessageParcel,      reply: MessageParcel,      options: MessageOption,      callback: AsyncCallback<SendRequestResult>    ): void-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| code | number | 是 |
| data | [MessageParcel](arkts-ipc-rpc-messageparcel-c.md) | 是 |
| reply | [MessageParcel](arkts-ipc-rpc-messageparcel-c.md) | 是 |
| options | [MessageOption](arkts-ipc-rpc-messageoption-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;SendRequestResult&gt; | 是 |

## unregisterDeathRecipient

```TypeScript
unregisterDeathRecipient(recipient: DeathRecipient, flags: number): void
```

注销用于接收远程对象死亡通知的回调。

**起始版本：** 9

<!--Device-IRemoteObject-unregisterDeathRecipient(recipient: DeathRecipient, flags: int): void--><!--Device-IRemoteObject-unregisterDeathRecipient(recipient: DeathRecipient, flags: int): void-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| recipient | [DeathRecipient](arkts-ipc-rpc-deathrecipient-i.md) | 是 |
| flags | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [1900008](../errorcode-rpc.md#1900008-非法的ipc对象) |
| [1900005](../errorcode-rpc.md#1900005-ipc对象权限错误) |
