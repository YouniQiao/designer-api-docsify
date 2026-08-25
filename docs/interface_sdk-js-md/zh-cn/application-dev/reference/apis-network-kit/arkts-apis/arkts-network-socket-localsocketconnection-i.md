# LocalSocketConnection

LocalSocketConnection连接，即LocalSocket客户端与服务端的会话连接。在调用LocalSocketConnection的方法前，需要先获取LocalSocketConnection对象。

> **说明：**&gt;
> 客户端与服务端成功建立连接后，才能通过返回的LocalSocketConnection对象调用相应的接口。

**起始版本：** 11

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { socket } from 'kits/@kit.NetworkKit';
```

## close

```TypeScript
close(): Promise<void>
```

关闭LocalSocket连接。使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Communication.NetStack

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [2301009](../errorcode-net-socket.md#2301009-错误文件描述符) |

## getLocalAddress

```TypeScript
getLocalAddress(): Promise<string>
```

获取LocalSocketConnection连接中的本地Socket地址。使用Promise异步回调。

**起始版本：** 12

**系统能力：** SystemCapability.Communication.NetStack

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [2300002](../errorcode-net-socket.md#2300002-系统内部错误) |
| [2301009](../errorcode-net-socket.md#2301009-错误文件描述符) |
| [2303188](../errorcode-net-socket.md#2303188-非套接字的套接字操作) |

## getSocketFd

```TypeScript
getSocketFd(): Promise<number>
```

获取LocalSocketConnection连接的文件描述符。使用Promise异步回调。

> **说明：**&gt;
> - 成功建立连接后，才可调用此方法。&gt;
> - 连接断开、Socket已关闭（如调用close后）等异常情况下调用本接口会返回-1。&gt;
> - 文件描述符的生命周期由系统管理，应用可以通过[close](arkts-network-socket-localsocket-i.md#close)方法关闭Socket连接，避免直接操作文件描述符进行关闭。

**起始版本：** 23

**系统能力：** SystemCapability.Communication.NetStack

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## off('message')

```TypeScript
off(type: 'message', callback?: Callback<LocalSocketMessageInfo>): void
```

取消订阅LocalSocketConnection连接的接收消息事件。使用callback异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'message' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[LocalSocketMessageInfo](arkts-network-socket-localsocketmessageinfo-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off('close')

```TypeScript
off(type: 'close', callback?: Callback<void>): void
```

取消订阅LocalSocketConnection的关闭事件。使用callback异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'close' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off('error')

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

取消订阅LocalSocketConnection连接的error事件。使用callback异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'error' | 是 |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## on('message')

```TypeScript
on(type: 'message', callback: Callback<LocalSocketMessageInfo>): void
```

订阅LocalSocketConnection连接的接收消息事件。使用callback异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'message' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[LocalSocketMessageInfo](arkts-network-socket-localsocketmessageinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## on('close')

```TypeScript
on(type: 'close', callback: Callback<void>): void
```

订阅LocalSocketConnection的关闭事件。使用callback异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'close' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

订阅LocalSocketConnection连接的error事件。使用callback异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'error' | 是 |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## send

```TypeScript
send(options: LocalSendOptions): Promise<void>
```

通过LocalSocketConnection连接对象发送数据。使用Promise异步回调。

> **说明：**&gt;
> 服务端与客户端建立连接后，服务端通过connect事件回调得到LocalSocketConnection连接对象后，才可使用连接对象调用此方法。

**起始版本：** 11

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [LocalSendOptions](arkts-network-socket-localsendoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 2301011 |

## clientId

```TypeScript
clientId: number
```

客户端与服务端建立的会话连接的id。

**类型：** number

**起始版本：** 11

**系统能力：** SystemCapability.Communication.NetStack
