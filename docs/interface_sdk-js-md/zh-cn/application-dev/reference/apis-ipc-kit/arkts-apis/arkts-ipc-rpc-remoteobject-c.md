# RemoteObject

实现远程对象。服务提供者必须继承此类。

**继承/实现关系：** RemoteObject extends [IRemoteObject](arkts-ipc-rpc-iremoteobject-c.md)

**起始版本：** 7

**系统能力：** SystemCapability.Communication.IPC.Core

## 导入模块

```TypeScript
import { rpc } from 'kits/@kit.IPCKit';
```

## attachLocalInterface

```TypeScript
attachLocalInterface(localInterface: IRemoteBroker, descriptor: string): void
```

此接口用于把接口描述符和IRemoteBroker对象绑定。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [modifyLocalInterface](#modifylocalinterface)(localInterface: IRemoteBroker, descriptor: string)

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localInterface | [IRemoteBroker](arkts-ipc-rpc-iremotebroker-i.md) | 是 |
| descriptor | string | 是 |

## constructor

```TypeScript
constructor(descriptor: string)
```

RemoteObject构造函数。

**起始版本：** 7

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| descriptor | string | 是 |

## getCallingPid

```TypeScript
getCallingPid(): number
```

获取通信对端的进程Pid。

**起始版本：** 7

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number |

## getCallingUid

```TypeScript
getCallingUid(): number
```

获取通信对端的进程Uid。

**起始版本：** 7

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number |

## getDescriptor

```TypeScript
getDescriptor(): string
```

获取对象的接口描述符。接口描述符为字符串。

**起始版本：** 9

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

查询接口描述符。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getDescriptor](arkts-ipc-rpc-iremoteobject-c.md#getdescriptor)()

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
| [401](../../errorcode-universal.md#401-参数检查失败) |

## modifyLocalInterface

```TypeScript
modifyLocalInterface(localInterface: IRemoteBroker, descriptor: string): void
```

此接口用于把接口描述符和IRemoteBroker对象绑定。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localInterface | [IRemoteBroker](arkts-ipc-rpc-iremotebroker-i.md) | 是 |
| descriptor | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## onRemoteMessageRequest

```TypeScript
onRemoteMessageRequest(
      code: number,
      data: MessageSequence,
      reply: MessageSequence,
      options: MessageOption
    ): boolean | Promise<boolean>
```

sendMessageRequest请求的响应处理函数，服务端在该函数里同步或异步地处理请求，回复结果。

> **说明：**&gt;&gt;开发者应优先选择重写onRemoteMessageRequest方法，其中可以自由实现同步和异步的消息处理。&gt;&gt;开发者同时重写onRemoteRequest和onRemoteMessageRequest方法时，仅onRemoteMessageRequest方法生效。

**起始版本：** 9

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

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

sendMessageRequest请求的响应处理函数，服务端在该函数里同步或异步地处理请求，回复结果，该接口可从入参callingInfo中获取IPC上下文信息。

> **说明：**&gt;
> 开发者应优先选择重写带有CallingInfo参数的onRemoteMessageRequest方法，其中可以自由实现同步和异步的消息处理。&gt;
> 开发者同时重写onRemoteRequest和onRemoteMessageRequest方法时，仅onRemoteMessageRequest方法生效。

**起始版本：** 23

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| code | number | 是 |
| data | [MessageSequence](arkts-ipc-rpc-messagesequence-c.md) | 是 |
| reply | [MessageSequence](arkts-ipc-rpc-messagesequence-c.md) | 是 |
| options | [MessageOption](arkts-ipc-rpc-messageoption-c.md) | 是 |
| callingInfo | [CallingInfo](arkts-ipc-rpc-callinginfo-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| boolean \| Promise & lt;boolean & gt; |

## onRemoteRequest

```TypeScript
onRemoteRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): boolean
```

sendRequest请求的响应处理函数，服务端在该函数里处理请求，回复结果。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [onRemoteMessageRequest](#onremotemessagerequest)(code: int, data: MessageSequence, reply: MessageSequence,
     *     options: MessageOption)

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

## queryLocalInterface

```TypeScript
queryLocalInterface(descriptor: string): IRemoteBroker
```

查询并获取当前接口描述符对应的远端对象是否已经存在。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getLocalInterface](arkts-ipc-rpc-iremoteobject-c.md#getlocalinterface)(descriptor: string)

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| descriptor | string | 是 |

**返回值：**

| 类型 |
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

以同步或异步方式向对端进程发送MessageSequence消息。如果为选项设置了异步模式，则发送请求的响应结果立即返回，reply报文里没有内容，具体回复需要在业务侧的回调中获取。如果为选项设置了同步模式，则发送请求的响应结 果将在sendMessageRequest返回时返回，回复内容在reply报文里。使用Promise异步回调。

**起始版本：** 9

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
| Promise & lt;RequestResult & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

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

以同步或异步方式向对端进程发送MessageSequence消息。使用callback异步回调。如果为选项设置了异步模式，则立即收到回调，reply报文里没有内容，具体回复需要在业务侧的回调中获取。如果为选项设置了同步模式，则 将在sendMessageRequest返回时收到回调，回复内容在reply报文里。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| code | number | 是 |
| data | [MessageSequence](arkts-ipc-rpc-messagesequence-c.md) | 是 |
| reply | [MessageSequence](arkts-ipc-rpc-messagesequence-c.md) | 是 |
| options | [MessageOption](arkts-ipc-rpc-messageoption-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;RequestResult&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## sendRequest

```TypeScript
sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): boolean
```

以同步或异步方式向对端进程发送MessageParcel消息。如果为选项设置了异步模式，则立即返回，reply报文里没有内容，具体回复需要在业务侧的回调中获取。 如果为选项设置了同步模式，则将在sendRequest返回时收到回复，回复内容在reply报文里。

**起始版本：** 7

**废弃版本：** 8

**替代接口：** [sendMessageRequest](arkts-ipc-rpc-iremoteobject-c.md#sendmessagerequest)(code: int, data: MessageSequence, reply: MessageSequence,
     *     options: MessageOption)

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

以同步或异步方式向对端进程发送MessageParcel消息。如果为选项设置了异步模式，则发送请求的响应结果立即返回，reply报文里没有内容，具体回复需要在业务侧的回调中获取。如果为选项设置了同步模式，则发送请求的响应结果将 在sendRequest返回时返回，回复内容在reply报文里。使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [sendMessageRequest](arkts-ipc-rpc-iremoteobject-c.md#sendmessagerequest)(code: int, data: MessageSequence, reply: MessageSequence,
     *     options: MessageOption)

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

以同步或异步方式向对端进程发送MessageParcel消息。使用callback异步回调。如果为选项设置了异步模式，则立即收到回调，reply报文里没有内容，具体回复需要在业务侧的回调中获取。如果为选项设置了同步模式，则将在 sendRequest返回时收到回调，回复内容在reply报文里。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [sendMessageRequest](arkts-ipc-rpc-iremoteobject-c.md#sendmessagerequest)(code: int, data: MessageSequence, reply: MessageSequence,
     *     options: MessageOption, callback: AsyncCallback&lt;RequestResult&gt;)

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| code | number | 是 |
| data | [MessageParcel](arkts-ipc-rpc-messageparcel-c.md) | 是 |
| reply | [MessageParcel](arkts-ipc-rpc-messageparcel-c.md) | 是 |
| options | [MessageOption](arkts-ipc-rpc-messageoption-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SendRequestResult](arkts-ipc-rpc-sendrequestresult-i.md)&gt; | 是 |
