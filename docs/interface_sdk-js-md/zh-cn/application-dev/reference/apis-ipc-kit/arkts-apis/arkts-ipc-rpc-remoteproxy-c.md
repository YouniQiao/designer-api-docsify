# RemoteProxy

实现IRemoteObject代理对象。

**继承/实现关系：** RemoteProxy extends [IRemoteObject](arkts-ipc-rpc-iremoteobject-c.md)

**起始版本：** 7

**系统能力：** SystemCapability.Communication.IPC.Core

## 导入模块

```TypeScript
import { rpc } from 'kits/@kit.IPCKit';
```

## addDeathRecipient

```TypeScript
addDeathRecipient(recipient: DeathRecipient, flags: number): boolean
```

注册用于接收远程对象死亡通知的回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [registerDeathRecipient](arkts-ipc-rpc-iremoteobject-c.md#registerdeathrecipient)(recipient: DeathRecipient, flags: int)

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

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [1900007](../errorcode-rpc.md#1900007-远端对象通信失败) |
| [1900008](../errorcode-rpc.md#1900008-非法的ipc对象) |

## getInterfaceDescriptor

```TypeScript
getInterfaceDescriptor(): string
```

查询当前代理对象接口的描述符。

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
getLocalInterface(interfaceDes: string): IRemoteBroker
```

查询并获取当前接口描述符对应的本地接口对象。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| interfaceDes | string | 是 |

**返回值：**

| 类型 |
| --- |
| [IRemoteBroker](arkts-ipc-rpc-iremotebroker-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900006](../errorcode-rpc.md#1900006-ipc对象权限错误) |

## isObjectDead

```TypeScript
isObjectDead(): boolean
```

指示对应的RemoteObject是否死亡。

**起始版本：** 7

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## queryLocalInterface

```TypeScript
queryLocalInterface(interface: string): IRemoteBroker
```

查询并获取当前接口描述符对应的本地接口对象。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getLocalInterface](arkts-ipc-rpc-iremoteobject-c.md#getlocalinterface)(descriptor: string)

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| interface | string | 是 |

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

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| recipient | [DeathRecipient](arkts-ipc-rpc-deathrecipient-i.md) | 是 |
| flags | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900008](../errorcode-rpc.md#1900008-非法的ipc对象) |

## removeDeathRecipient

```TypeScript
removeDeathRecipient(recipient: DeathRecipient, flags: number): boolean
```

注销用于接收远程对象死亡通知的回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [unregisterDeathRecipient](arkts-ipc-rpc-iremoteobject-c.md#unregisterdeathrecipient)(recipient: DeathRecipient, flags: int)

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

以同步或异步方式向对端进程发送MessageSequence消息。使用callback异步回调。如果为选项设置了异步模式，则立即收到回调，reply报文里没有内容，具体回复需要在业务侧的回调中获取。如果为选项设置了同步模式，将 在[sendMessageRequest](arkts-ipc-rpc-iremoteobject-c.md#sendmessagerequest)返回后、服务端处理请求完成时执行回调， 回调中可读取[RequestResult](arkts-ipc-rpc-requestresult-i.md)获取服务端返回的数据。

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

以同步或异步方式向对端进程发送MessageParcel消息。如果为选项设置了异步模式，则立即收到回调，reply报文里没有内容，具体回复需要在业务侧的回调中获取。如果为选项设置了同步模式，则将在sendRequest返回时收 到回调，回复内容在reply报文里。

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

## unregisterDeathRecipient

```TypeScript
unregisterDeathRecipient(recipient: DeathRecipient, flags: number): void
```

注销用于接收远程对象死亡通知的回调。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| recipient | [DeathRecipient](arkts-ipc-rpc-deathrecipient-i.md) | 是 |
| flags | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900008](../errorcode-rpc.md#1900008-非法的ipc对象) |

## DUMP_TRANSACTION

```TypeScript
static readonly DUMP_TRANSACTION: number
```

内部指令码，获取IPC服务相关的状态信息。

**类型：** number

**默认值：** 1598311760

**起始版本：** 7

**系统能力：** SystemCapability.Communication.IPC.Core

## INTERFACE_TRANSACTION

```TypeScript
static readonly INTERFACE_TRANSACTION: number
```

内部指令码，获取对端接口描述符。

**类型：** number

**默认值：** 1598968902

**起始版本：** 7

**系统能力：** SystemCapability.Communication.IPC.Core

## MAX_TRANSACTION_ID

```TypeScript
static readonly MAX_TRANSACTION_ID: number
```

最大有效指令码。

**类型：** number

**默认值：** 0x00FFFFFF

**起始版本：** 7

**系统能力：** SystemCapability.Communication.IPC.Core

## MIN_TRANSACTION_ID

```TypeScript
static readonly MIN_TRANSACTION_ID: number
```

最小有效指令码。

**类型：** number

**默认值：** 0x1

**起始版本：** 7

**系统能力：** SystemCapability.Communication.IPC.Core

## PING_TRANSACTION

```TypeScript
static readonly PING_TRANSACTION: number
```

内部指令码，用于测试IPC服务是否正常。

**类型：** number

**默认值：** 1599098439

**起始版本：** 7

**系统能力：** SystemCapability.Communication.IPC.Core
