# TCPSocketServer

TCPSocketServer连接。在调用TCPSocketServer的方法前，需要先通过 [socket.constructTCPSocketServerInstance](arkts-network-socket-constructtcpsocketserverinstance-f.md)创建TCPSocketServer对象。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { socket } from 'kits/@kit.NetworkKit';
```

## close

```TypeScript
close(): Promise<void>
```

TCPSocketServer停止监听并释放通过 [listen](#listen)方法绑定的端口。若多次调用 [listen](#listen)方法，再调用此方法时会释放 TCPSocketServer的所有监听端口。使用Promise异步回调。

> **说明：**&gt;
> 该方法不会关闭已有连接。如需关闭，请调用[TCPSocketConnection](arkts-network-socket-tcpsocketconnection-i.md)的
> [close](arkts-network-socket-tcpsocketconnection-i.md#close)方法。

**起始版本：** 20

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetStack

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [2300002](../errorcode-net-socket.md#2300002-系统内部错误) |

## getLocalAddress

```TypeScript
getLocalAddress(): Promise<NetAddress>
```

获取TCPSocketServer的本地Socket地址。使用Promise异步回调。

> **说明：**&gt;
> listen方法调用成功后，才可调用此方法。

**起始版本：** 12

**系统能力：** SystemCapability.Communication.NetStack

**返回值：**

| 类型 |
| --- |
| Promise & lt;NetAddress & gt; |

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

获取TCPSocketServer监听端口绑定的文件描述符。使用Promise异步回调。

> **说明：**&gt;
> - [listen](#listen)方法调用成功后，才可调用
> 此方法。多次调用listen时，会获取最新监听端口绑定的文件描述符。&gt;
> - 监听异常、Socket已关闭（如调用close后）等异常情况下调用本接口会返回-1。&gt;
> - 文件描述符的生命周期由系统管理，应用可以通过[close](#close)方法关闭Socket连接，避免直接操作文件描述符进行关闭。

**起始版本：** 23

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetStack

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## getState

```TypeScript
getState(callback: AsyncCallback<SocketStateBase>): void
```

获取TCPSocketServer状态。使用callback异步回调。

> **说明：**&gt;
> listen方法调用成功后，才可调用此方法。

**起始版本：** 10

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SocketStateBase](arkts-network-socket-socketstatebase-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2300002](../errorcode-net-socket.md#2300002-系统内部错误) |
| [2303188](../errorcode-net-socket.md#2303188-非套接字的套接字操作) |

## getState

```TypeScript
getState(): Promise<SocketStateBase>
```

获取TCPSocketServer状态。使用Promise异步回调。

> **说明：**&gt;
> listen方法调用成功后，才可调用此方法。

**起始版本：** 10

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetStack

**返回值：**

| 类型 |
| --- |
| Promise&lt;[SocketStateBase](arkts-network-socket-socketstatebase-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [2300002](../errorcode-net-socket.md#2300002-系统内部错误) |
| [2303188](../errorcode-net-socket.md#2303188-非套接字的套接字操作) |

## listen

```TypeScript
listen(address: NetAddress, callback: AsyncCallback<void>): void
```

绑定IP地址和端口，端口可以指定或由系统随机分配。监听并接受与此套接字建立的TCPSocket连接。该接口使用多线程并发处理客户端的数据。使用callback异步回调。

> **说明：**&gt;
> 服务端使用该方法完成bind，listen，accept操作，bind方法失败会由系统随机分配端口号。

**起始版本：** 10

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| address | [NetAddress](arkts-network-connection-netaddress-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [2300002](../errorcode-net-socket.md#2300002-系统内部错误) |
| [2303109](../errorcode-net-socket.md#2303109-错误文件编号) |
| [2303111](../errorcode-net-socket.md#2303111-资源暂时不可用请重试) |
| [2303198](../errorcode-net-socket.md#2303198-网络地址已被使用) |
| [2303199](../errorcode-net-socket.md#2303199-不能分配请求的地址) |

## listen

```TypeScript
listen(address: NetAddress): Promise<void>
```

绑定IP地址和端口，端口可以指定或由系统随机分配。监听并接受与此套接字建立的TCPSocket连接。该接口使用多线程并发处理客户端的数据。使用Promise异步回调。

> **说明：**&gt;
> 服务端使用该方法完成bind，listen，accept操作，bind方法失败会由系统随机分配端口号。

**起始版本：** 10

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| address | [NetAddress](arkts-network-connection-netaddress-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [2300002](../errorcode-net-socket.md#2300002-系统内部错误) |
| [2303109](../errorcode-net-socket.md#2303109-错误文件编号) |
| [2303111](../errorcode-net-socket.md#2303111-资源暂时不可用请重试) |
| [2303198](../errorcode-net-socket.md#2303198-网络地址已被使用) |
| [2303199](../errorcode-net-socket.md#2303199-不能分配请求的地址) |

## off('connect')

```TypeScript
off(type: 'connect', callback?: Callback<TCPSocketConnection>): void
```

取消订阅TCPSocketServer的连接事件。使用callback异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'connect' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[TCPSocketConnection](arkts-network-socket-tcpsocketconnection-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off('error')

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

取消订阅TCPSocketServer连接的error事件。使用callback异步回调。

**起始版本：** 10

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
on(type: 'connect', callback: Callback<TCPSocketConnection>): void
```

订阅TCPSocketServer的连接事件。使用callback异步回调。

> **说明：**&gt;
> listen方法调用成功后，才可调用此方法。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'connect' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[TCPSocketConnection](arkts-network-socket-tcpsocketconnection-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

订阅TCPSocketServer连接的error事件。使用callback异步回调。

> **说明：**&gt;
> listen方法调用成功后，才可调用此方法。

**起始版本：** 10

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
setExtraOptions(options: TCPExtraOptions, callback: AsyncCallback<void>): void
```

设置TCPSocketServer连接的其他属性。使用callback异步回调。

> **说明：**&gt;
> listen方法调用成功后，才可调用此方法。

**起始版本：** 10

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [TCPExtraOptions](arkts-network-socket-tcpextraoptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2300002](../errorcode-net-socket.md#2300002-系统内部错误) |
| [2303188](../errorcode-net-socket.md#2303188-非套接字的套接字操作) |

## setExtraOptions

```TypeScript
setExtraOptions(options: TCPExtraOptions): Promise<void>
```

设置TCPSocketServer连接的其他属性。使用Promise异步回调。

> **说明：**&gt;
> listen方法调用成功后，才可调用此方法。

**起始版本：** 10

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [TCPExtraOptions](arkts-network-socket-tcpextraoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2300002](../errorcode-net-socket.md#2300002-系统内部错误) |
| [2303188](../errorcode-net-socket.md#2303188-非套接字的套接字操作) |
