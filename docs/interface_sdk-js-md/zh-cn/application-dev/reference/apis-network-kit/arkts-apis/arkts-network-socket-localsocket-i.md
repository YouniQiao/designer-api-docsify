# LocalSocket

LocalSocket连接。在调用LocalSocket的方法前，需要先通过 [socket.constructLocalSocketInstance](arkts-network-socket-constructlocalsocketinstance-f.md)创建LocalSocket对象。

**起始版本：** 11

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { socket } from 'kits/@kit.NetworkKit';
```

## bind

```TypeScript
bind(address: LocalAddress): Promise<void>
```

绑定本地套接字文件的路径。使用Promise异步回调。

> **说明：**&gt;
> bind方法可以使客户端确保有个明确的本地套接字路径，显式的绑定一个本地套接字文件。&gt;
> bind方法在本地套接字通信中非必须。

**起始版本：** 11

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| address | [LocalAddress](arkts-network-socket-localaddress-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2301013](../errorcode-net-socket.md#2301013-权限不足) |
| 2301022 |
| 2301098 |

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

## connect

```TypeScript
connect(options: LocalConnectOptions): Promise<void>
```

连接到指定的套接字文件。使用Promise异步回调。

> **说明：**&gt;
> 在没有执行localsocket.bind的情况下，也可以直接调用该接口完成与LocalSocket服务端的连接。

**起始版本：** 11

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [LocalConnectOptions](arkts-network-socket-localconnectoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2301013](../errorcode-net-socket.md#2301013-权限不足) |
| 2301022 |
| 2301111 |
| 2301099 |

## getExtraOptions

```TypeScript
getExtraOptions(): Promise<ExtraOptionsBase>
```

获取LocalSocket的套接字属性。使用Promise异步回调。

> **说明：**&gt;
> bind或connect方法调用成功后，才可调用此方法。

**起始版本：** 11

**系统能力：** SystemCapability.Communication.NetStack

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ExtraOptionsBase](arkts-network-socket-extraoptionsbase-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [2301009](../errorcode-net-socket.md#2301009-错误文件描述符) |

## getLocalAddress

```TypeScript
getLocalAddress(): Promise<string>
```

获取LocalSocket的本地Socket地址。使用Promise异步回调。

> **说明：**&gt;
> bind方法调用成功后，才可调用此方法。

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

获取LocalSocket的文件描述符。使用Promise异步回调。

> **说明：**&gt;
> - bind或connect方法调用成功后，才可调用此方法。&gt;
> - 获取由系统内核分配的唯一文件描述符，用于标识当前使用的套接字。&gt;
> - 文件描述符的生命周期由系统管理，应用可以通过[close](#close)方法关闭Socket连接，避免直接操作文件描述符进行关闭。

**起始版本：** 11

**系统能力：** SystemCapability.Communication.NetStack

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## getState

```TypeScript
getState(): Promise<SocketStateBase>
```

获取LocalSocket状态。使用Promise异步回调。

> **说明：**&gt;
> bind或connect方法调用成功后，才可调用此方法。

**起始版本：** 11

**系统能力：** SystemCapability.Communication.NetStack

**返回值：**

| 类型 |
| --- |
| Promise&lt;[SocketStateBase](arkts-network-socket-socketstatebase-i.md)&gt; |

## off('message')

```TypeScript
off(type: 'message', callback?: Callback<LocalSocketMessageInfo>): void
```

取消订阅LocalSocket连接的接收消息事件。使用callback异步回调。

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

## off('connect')

```TypeScript
off(type: 'connect', callback?: Callback<void>): void
```

取消订阅LocalSocket的连接事件。使用callback异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'connect' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off('close')

```TypeScript
off(type: 'close', callback?: Callback<void>): void
```

取消订阅LocalSocket的关闭事件。使用callback异步回调。

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

取消订阅LocalSocket连接的error事件。使用callback异步回调。

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

订阅LocalSocket连接的接收消息事件。使用callback异步回调。

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

## on('connect')

```TypeScript
on(type: 'connect', callback: Callback<void>): void
```

订阅LocalSocket的连接事件。使用callback异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'connect' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## on('close')

```TypeScript
on(type: 'close', callback: Callback<void>): void
```

订阅LocalSocket的关闭事件。使用callback异步回调。

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

订阅LocalSocket连接的error事件。使用callback异步回调。

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

通过LocalSocket连接发送数据。使用Promise异步回调。

> **说明：**&gt;
> connect方法调用成功后，才可调用此方法。

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

## setExtraOptions

```TypeScript
setExtraOptions(options: ExtraOptionsBase): Promise<void>
```

设置LocalSocket的套接字属性。使用Promise异步回调。

> **说明：**&gt;
> bind或connect方法调用成功后，才可调用此方法。

**起始版本：** 11

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [ExtraOptionsBase](arkts-network-socket-extraoptionsbase-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2301009](../errorcode-net-socket.md#2301009-错误文件描述符) |
