# TCPSocket

TCPSocket连接。在调用TCPSocket的方法前，需要先通过[socket.constructTCPSocketInstance](arkts-network-socket-constructtcpsocketinstance-f.md)创建 TCPSocket对象。

**起始版本：** 7

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { socket } from 'kits/@kit.NetworkKit';
```

## bind

```TypeScript
bind(address: NetAddress, callback: AsyncCallback<void>): void
```

绑定IP地址和端口，端口可以指定为0由系统随机分配或由用户指定为其它非0端口。使用callback异步回调。

> **说明：**&gt;
> bind方法如果因为端口冲突而执行失败，则会由系统随机分配端口号。&gt;
> TCP客户端可先调用该接口(tcp.bind)显式绑定IP地址和端口号，再调用tcp.connect完成与服务端的连接；也可直接调用tcp.connect由系统自动绑定IP地址和端口号，完成与服务端的连接。&gt;
> bind的IP为'localhost'或'127.0.0.1'时，只允许本地回环接口的连接，即服务端和客户端运行在同一台机器上。

**起始版本：** 7

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

## bind

```TypeScript
bind(address: NetAddress): Promise<void>
```

绑定IP地址和端口，端口可以指定为0由系统随机分配或由用户指定为其它非0端口。使用Promise异步回调。

> **说明：**&gt;
> bind方法如果因为端口冲突而执行失败，则会由系统随机分配端口号。&gt;
> TCP客户端可先调用该接口(tcp.bind)显式绑定IP地址和端口号，再调用tcp.connect完成与服务端的连接；也可直接调用tcp.connect由系统自动绑定IP地址和端口号，完成与服务端的连接。&gt;
> bind的IP为'localhost'或'127.0.0.1'时，只允许本地回环接口的连接，即服务端和客户端运行在同一台机器上。

**起始版本：** 7

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

## close

```TypeScript
close(callback: AsyncCallback<void>): void
```

关闭TCPSocket连接。使用callback异步回调。

**起始版本：** 7

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## close

```TypeScript
close(): Promise<void>
```

关闭TCPSocket连接。使用Promise异步回调。

**起始版本：** 7

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

## connect

```TypeScript
connect(options: TCPConnectOptions, callback: AsyncCallback<void>): void
```

连接到指定的IP地址和端口。使用callback异步回调。

> **说明：**&gt;
> 在没有执行tcp.bind的情况下，也可以直接调用该接口完成与TCP服务端的连接

**起始版本：** 7

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [TCPConnectOptions](arkts-network-socket-tcpconnectoptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [2301206](../errorcode-net-socket.md#2301206-socks5连接代理服务器失败) |
| [2301207](../errorcode-net-socket.md#2301207-socks5认证用户名或密码无效) |
| [2301208](../errorcode-net-socket.md#2301208-socks5连接远程服务器失败) |
| [2301209](../errorcode-net-socket.md#2301209-socks5协商认证方式失败) |
| [2301210](../errorcode-net-socket.md#2301210-socks5发送消息失败) |
| [2301211](../errorcode-net-socket.md#2301211-socks5接收消息失败) |
| [2301212](../errorcode-net-socket.md#2301212-socks5消息序列化失败) |
| [2301213](../errorcode-net-socket.md#2301213-socks5消息反序列化失败) |

## connect

```TypeScript
connect(options: TCPConnectOptions): Promise<void>
```

连接到指定的IP地址和端口。使用Promise异步回调。

> **说明：**&gt;
> 在没有执行tcp.bind的情况下，也可以直接调用该接口完成与TCP服务端的连接。

**起始版本：** 7

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [TCPConnectOptions](arkts-network-socket-tcpconnectoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [2301206](../errorcode-net-socket.md#2301206-socks5连接代理服务器失败) |
| [2301207](../errorcode-net-socket.md#2301207-socks5认证用户名或密码无效) |
| [2301208](../errorcode-net-socket.md#2301208-socks5连接远程服务器失败) |
| [2301209](../errorcode-net-socket.md#2301209-socks5协商认证方式失败) |
| [2301210](../errorcode-net-socket.md#2301210-socks5发送消息失败) |
| [2301211](../errorcode-net-socket.md#2301211-socks5接收消息失败) |
| [2301212](../errorcode-net-socket.md#2301212-socks5消息序列化失败) |
| [2301213](../errorcode-net-socket.md#2301213-socks5消息反序列化失败) |

## getLocalAddress

```TypeScript
getLocalAddress(): Promise<NetAddress>
```

获取TCPSocket的本地Socket地址。使用Promise异步回调。

> **说明：**&gt;
> bind方法调用成功后，才可调用此方法。

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

## getRemoteAddress

```TypeScript
getRemoteAddress(callback: AsyncCallback<NetAddress>): void
```

获取对端Socket地址。使用callback异步回调。

> **说明：**&gt;
> connect方法调用成功后，才可调用此方法。

**起始版本：** 7

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;NetAddress&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## getRemoteAddress

```TypeScript
getRemoteAddress(): Promise<NetAddress>
```

获取对端Socket地址。使用Promise异步回调。

> **说明：**&gt;
> connect方法调用成功后，才可调用此方法。

**起始版本：** 7

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetStack

**返回值：**

| 类型 |
| --- |
| Promise & lt;NetAddress & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## getSocketFd

```TypeScript
getSocketFd(callback: AsyncCallback<number>): void
```

获取TCPSocket的文件描述符。使用callback异步回调。

> **说明：**&gt;
> - bind或connect方法调用成功后，才可调用此方法。&gt;
> - 文件描述符的生命周期由系统管理，应用可以通过[close](arkts-network-socket-udpsocket-i.md#close)方法关闭Socket连接，避免直接操作
> 文件描述符进行关闭。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## getSocketFd

```TypeScript
getSocketFd(): Promise<number>
```

获取TCPSocket的文件描述符。使用Promise异步回调。

> **说明：**&gt;
> - bind或connect方法调用成功后，才可调用此方法。&gt;
> - 文件描述符的生命周期由系统管理，应用可以通过[close](arkts-network-socket-udpsocket-i.md#close)方法关闭Socket连接，避免直接操作
> 文件描述符进行关闭。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.NetStack

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## getState

```TypeScript
getState(callback: AsyncCallback<SocketStateBase>): void
```

获取TCPSocket状态。使用callback异步回调。

> **说明：**&gt;
> bind或connect方法调用成功后，才可调用此方法。

**起始版本：** 7

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

## getState

```TypeScript
getState(): Promise<SocketStateBase>
```

获取TCPSocket状态。使用Promise异步回调。

> **说明：**&gt;
> bind或connect方法调用成功后，才可调用此方法。

**起始版本：** 7

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

## off('message')

```TypeScript
off(type: 'message', callback?: Callback<SocketMessageInfo>): void
```

取消订阅TCPSocket连接的接收消息事件。使用callback异步回调。

**起始版本：** 7

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'message' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SocketMessageInfo](arkts-network-socket-socketmessageinfo-i.md)&gt; | 否 |

## off('connect' | 'close')

```TypeScript
off(type: 'connect' | 'close', callback?: Callback<void>): void
```

取消订阅TCPSocket的连接事件或关闭事件。使用callback异步回调。

**起始版本：** 7

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'connect' \| 'close' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 |

## off('connect' | 'close')

```TypeScript
off(type: 'connect' | 'close', callback?: Callback<void>): void
```

取消订阅TCPSocket的连接事件或关闭事件。使用callback异步回调。

**起始版本：** 7

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'connect' \| 'close' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 |

## off('error')

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

取消订阅TCPSocket连接的error事件。使用callback异步回调。

**起始版本：** 7

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'error' | 是 |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 否 |

## on('message')

```TypeScript
on(type: 'message', callback: Callback<SocketMessageInfo>): void
```

订阅TCPSocket连接的接收消息事件。使用callback异步回调。

**起始版本：** 7

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'message' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SocketMessageInfo](arkts-network-socket-socketmessageinfo-i.md)&gt; | 是 |

## on('connect' | 'close')

```TypeScript
on(type: 'connect' | 'close', callback: Callback<void>): void
```

订阅TCPSocket的连接事件或关闭事件。使用callback异步回调。

**起始版本：** 7

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'connect' \| 'close' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

## on('connect' | 'close')

```TypeScript
on(type: 'connect' | 'close', callback: Callback<void>): void
```

订阅TCPSocket的连接事件或关闭事件。使用callback异步回调。

**起始版本：** 7

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'connect' \| 'close' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

订阅TCPSocket连接的error事件。使用callback异步回调。

**起始版本：** 7

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'error' | 是 |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 是 |

## send

```TypeScript
send(options: TCPSendOptions, callback: AsyncCallback<void>): void
```

通过TCPSocket连接发送数据。使用callback异步回调。

> **说明：**&gt;
> connect方法调用成功后，才可调用此方法。该接口为耗时操作，请在Worker线程或taskpool线程调用该接口。

**起始版本：** 7

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [TCPSendOptions](arkts-network-socket-tcpsendoptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## send

```TypeScript
send(options: TCPSendOptions): Promise<void>
```

通过TCPSocket连接发送数据。使用Promise异步回调。

> **说明：**&gt;
> connect方法调用成功后，才可调用此方法。该接口为耗时操作，请在Worker线程或taskpool线程调用该接口。

**起始版本：** 7

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [TCPSendOptions](arkts-network-socket-tcpsendoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## setExtraOptions

```TypeScript
setExtraOptions(options: TCPExtraOptions, callback: AsyncCallback<void>): void
```

设置TCPSocket连接的其他属性。使用callback异步回调。

> **说明：**&gt;
> bind或connect方法调用成功后，才可调用此方法。

**起始版本：** 7

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## setExtraOptions

```TypeScript
setExtraOptions(options: TCPExtraOptions): Promise<void>
```

设置TCPSocket连接的其他属性。使用Promise异步回调。

> **说明：**&gt;
> bind或connect方法调用成功后，才可调用此方法。

**起始版本：** 7

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
