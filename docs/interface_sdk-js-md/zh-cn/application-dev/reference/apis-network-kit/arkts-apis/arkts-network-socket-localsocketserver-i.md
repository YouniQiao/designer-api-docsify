# LocalSocketServer

LocalSocketServer类。在调用LocalSocketServer的方法前，需要先通过 [socket.constructLocalSocketServerInstance](arkts-network-socket-constructlocalsocketserverinstance-f.md)创建LocalSocketServer对象。

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

LocalSocketServer停止监听并释放通过[listen](#listen)方法绑定的监听端口。使用Promise异步回调。

> **说明：**&gt;
> 该方法不会关闭已有连接。如需关闭，请调用[LocalSocketConnection](arkts-network-socket-localsocketconnection-i.md)的
> [close](arkts-network-socket-localsocket-i.md#close)方法。

**起始版本：** 20

**系统能力：** SystemCapability.Communication.NetStack

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [2300002](../errorcode-net-socket.md#2300002-系统内部错误) |

## getExtraOptions

```TypeScript
getExtraOptions(): Promise<ExtraOptionsBase>
```

获取LocalSocketServer中连接的套接字的属性。使用Promise异步回调。

> **说明：**&gt;
> listen方法调用成功后，才可调用此方法。

**起始版本：** 11

**系统能力：** SystemCapability.Communication.NetStack

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ExtraOptionsBase](arkts-network-socket-extraoptionsbase-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## getLocalAddress

```TypeScript
getLocalAddress(): Promise<string>
```

获取LocalSocketServer中本地Socket地址。使用Promise异步回调。

> **说明：**&gt;
> listen方法调用成功后，才可调用此方法。

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

获取LocalSocketServer监听端口绑定的文件描述符。使用Promise异步回调。

> **说明：**&gt;
> - [listen](#listen)方法调用成功后，才可调用此方法。&gt;
> - 监听异常、Socket已关闭（如调用close后）等异常情况下调用本接口会返回-1。&gt;
> - 文件描述符的生命周期由系统管理，应用可以通过[close](arkts-network-socket-tcpsocketserver-i.md#close)方法关闭Socket连接，避免直接操作文件描述符进行关闭。

**起始版本：** 23

**系统能力：** SystemCapability.Communication.NetStack

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## getState

```TypeScript
getState(): Promise<SocketStateBase>
```

获取LocalSocketServer状态。使用Promise异步回调。

> **说明：**&gt;
> listen方法调用成功后，才可调用此方法。

**起始版本：** 11

**系统能力：** SystemCapability.Communication.NetStack

**返回值：**

| 类型 |
| --- |
| Promise&lt;[SocketStateBase](arkts-network-socket-socketstatebase-i.md)&gt; |

## listen

```TypeScript
listen(address: LocalAddress): Promise<void>
```

绑定本地套接字文件，监听并接受与此套接字建立的LocalSocket连接。该接口使用多线程并发处理客户端的数据。使用Promise异步回调。

> **说明：**&gt;
> 服务端使用该方法完成bind，listen，accept操作，传入套接字文件路径，调用此接口后会自动生成本地套接字文件。

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
| [2303109](../errorcode-net-socket.md#2303109-错误文件编号) |
| [2301013](../errorcode-net-socket.md#2301013-权限不足) |
| 2301022 |
| 2301098 |

## off('connect')

```TypeScript
off(type: 'connect', callback?: Callback<LocalSocketConnection>): void
```

取消订阅LocalSocketServer的连接事件。使用callback异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'connect' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[LocalSocketConnection](arkts-network-socket-localsocketconnection-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off('error')

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

取消订阅LocalSocketServer连接的error事件。使用callback异步回调。

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

## on('connect')

```TypeScript
on(type: 'connect', callback: Callback<LocalSocketConnection>): void
```

订阅LocalSocketServer的连接事件。使用callback异步回调。

> **说明：**&gt;
> listen方法调用成功后，才可调用此方法。

**起始版本：** 11

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'connect' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[LocalSocketConnection](arkts-network-socket-localsocketconnection-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

订阅LocalSocketServer连接的error事件。使用callback异步回调。

> **说明：**&gt;
> listen方法调用成功后，才可调用此方法。

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

## setExtraOptions

```TypeScript
setExtraOptions(options: ExtraOptionsBase): Promise<void>
```

设置LocalSocketServer连接的套接字属性。使用Promise异步回调。

> **说明：**&gt;
> listen方法调用成功后，才可调用此方法。

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
