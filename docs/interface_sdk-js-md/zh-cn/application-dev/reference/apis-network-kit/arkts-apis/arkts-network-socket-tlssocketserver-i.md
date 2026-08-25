# TLSSocketServer

TLSSocketServer连接。在调用TLSSocketServer的方法前，需要先通过 [socket.constructTLSSocketServerInstance](arkts-network-socket-constructtlssocketserverinstance-f.md)创建TLSSocketServer对象。

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

TLSSocketServer停止监听并释放通过[listen](arkts-network-socket-tcpsocketserver-i.md#listen)方法绑定的端口。使用Promise异步回调。

> **说明：**&gt;
> 该方法不会关闭已有连接。如需关闭，请调用[TLSSocketConnection](arkts-network-socket-tlssocketconnection-i.md)的
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

## getCertificate

```TypeScript
getCertificate(callback: AsyncCallback<X509CertRawData>): void
```

在TLSSocketServer通信连接成功之后，获取本地的数字证书，使用callback异步回调。

> **说明：**&gt;
> listen方法调用成功后，才可调用此方法。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[X509CertRawData](arkts-network-socket-x509certrawdata-t.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2303501](../errorcode-net-socket.md#2303501-ssl为空) |
| [2303504](../errorcode-net-socket.md#2303504-查找x509时出错) |
| [2300002](../errorcode-net-socket.md#2300002-系统内部错误) |

## getCertificate

```TypeScript
getCertificate(): Promise<X509CertRawData>
```

在TLSSocketServer通信连接之后，获取本地的数字证书，使用Promise异步回调。

> **说明：**&gt;
> listen方法调用成功后，才可调用此方法。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.NetStack

**返回值：**

| 类型 |
| --- |
| Promise&lt;[X509CertRawData](arkts-network-socket-x509certrawdata-t.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [2303501](../errorcode-net-socket.md#2303501-ssl为空) |
| [2303504](../errorcode-net-socket.md#2303504-查找x509时出错) |
| [2300002](../errorcode-net-socket.md#2300002-系统内部错误) |

## getLocalAddress

```TypeScript
getLocalAddress(): Promise<NetAddress>
```

获取TLSSocketServer的本地Socket地址。使用Promise异步回调。

> **说明：**&gt;
> 在TLSSocketServer通信连接成功之后，才可调用此方法。

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

## getProtocol

```TypeScript
getProtocol(callback: AsyncCallback<string>): void
```

在TLSSocketServer通信连接成功之后，获取通信的协议版本，使用callback异步回调。

> **说明：**&gt;
> listen方法调用成功后，才可调用此方法。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2303501](../errorcode-net-socket.md#2303501-ssl为空) |
| [2303505](../errorcode-net-socket.md#2303505-tls系统调用错误) |
| [2300002](../errorcode-net-socket.md#2300002-系统内部错误) |

## getProtocol

```TypeScript
getProtocol(): Promise<string>
```

在TLSSocketServer通信连接成功之后，获取通信的协议版本，使用Promise异步回调。

> **说明：**&gt;
> listen方法调用成功后，才可调用此方法。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.NetStack

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [2303501](../errorcode-net-socket.md#2303501-ssl为空) |
| [2303505](../errorcode-net-socket.md#2303505-tls系统调用错误) |
| [2300002](../errorcode-net-socket.md#2300002-系统内部错误) |

## getSocketFd

```TypeScript
getSocketFd(): Promise<number>
```

获取TLSSocketServer监听端口绑定的文件描述符。使用Promise异步回调。

> **说明：**&gt;
> - [listen](arkts-network-socket-tcpsocketserver-i.md#listen)方法调用成功后，才可调用此方法。多次调用listen时，会获取最新监听端口绑定的文件描述符。&gt;
> - 监听异常、Socket已关闭（如调用close后）等异常情况下调用本接口会返回-1。&gt;
> - 文件描述符的生命周期由系统管理，应用可以通过[close](arkts-network-socket-tcpsocketserver-i.md#close)方法关闭Socket连接，避免直接操作文件描述符进行关闭。

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

在TLSSocketServer的listen成功之后，获取TLSSocketServer状态。使用callback异步回调。

> **说明：**&gt;
> listen方法调用成功后，才可调用此方法。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SocketStateBase](arkts-network-socket-socketstatebase-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2303188](../errorcode-net-socket.md#2303188-非套接字的套接字操作) |
| [2300002](../errorcode-net-socket.md#2300002-系统内部错误) |

## getState

```TypeScript
getState(): Promise<SocketStateBase>
```

在TLSSocketServer的listen成功之后，获取TLSSocketServer状态。使用Promise异步回调。

> **说明：**&gt;
> listen方法调用成功后，才可调用此方法。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.NetStack

**返回值：**

| 类型 |
| --- |
| Promise&lt;[SocketStateBase](arkts-network-socket-socketstatebase-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [2303188](../errorcode-net-socket.md#2303188-非套接字的套接字操作) |
| [2300002](../errorcode-net-socket.md#2300002-系统内部错误) |

## listen

```TypeScript
listen(options: TLSConnectOptions, callback: AsyncCallback<void>): void
```

绑定IP地址和端口，在TLSSocketServer上bind成功之后，监听客户端的连接，创建和初始化TLS会话，实现建立连接过程，加载证书秘钥并验证，使用callback异步回调。

> **注意：**&gt;
> IP地址设置为0.0.0.0时，可以监听本机所有地址。

**起始版本：** 10

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [TLSConnectOptions](arkts-network-socket-tlsconnectoptions-i.md) | 是 |
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
| [2303501](../errorcode-net-socket.md#2303501-ssl为空) |
| [2303502](../errorcode-net-socket.md#2303502-tls读取错误) |
| [2303503](../errorcode-net-socket.md#2303503-tls写入错误) |
| [2303505](../errorcode-net-socket.md#2303505-tls系统调用错误) |
| [2303506](../errorcode-net-socket.md#2303506-关闭tls连接失败) |

## listen

```TypeScript
listen(options: TLSConnectOptions): Promise<void>
```

绑定IP地址和端口，在TLSSocketServer上bind成功之后，监听客户端的连接，并创建和初始化TLS会话，实现建立连接过程，加载证书秘钥并验证，使用Promise异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [TLSConnectOptions](arkts-network-socket-tlsconnectoptions-i.md) | 是 |

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
| [2303501](../errorcode-net-socket.md#2303501-ssl为空) |
| [2303502](../errorcode-net-socket.md#2303502-tls读取错误) |
| [2303503](../errorcode-net-socket.md#2303503-tls写入错误) |
| [2303505](../errorcode-net-socket.md#2303505-tls系统调用错误) |
| [2303506](../errorcode-net-socket.md#2303506-关闭tls连接失败) |

## off('connect')

```TypeScript
off(type: 'connect', callback?: Callback<TLSSocketConnection>): void
```

取消订阅TLSSocketServer的连接事件。使用callback异步回调。

> **说明：**&gt;
> listen方法调用成功后，才可调用此方法。&gt;
> 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'connect' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[TLSSocketConnection](arkts-network-socket-tlssocketconnection-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off('error')

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

取消订阅TLSSocketServer连接的error事件。使用callback异步回调。

> **说明：**&gt;
> listen方法调用成功后，才可调用此方法。&gt;
> 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

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
on(type: 'connect', callback: Callback<TLSSocketConnection>): void
```

订阅TLSSocketServer的连接事件。使用callback异步回调。

> **说明：**&gt;
> listen方法调用成功后，才可调用此方法。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'connect' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[TLSSocketConnection](arkts-network-socket-tlssocketconnection-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

订阅TLSSocketServer连接的error事件。使用callback异步回调。

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

在TLSSocketServer的listen成功之后，设置TLSSocketServer连接的其他属性。使用callback异步回调。

> **说明：**&gt;
> listen方法调用成功后，才可调用此方法。

**起始版本：** 10

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
| [2303188](../errorcode-net-socket.md#2303188-非套接字的套接字操作) |
| [2300002](../errorcode-net-socket.md#2300002-系统内部错误) |

## setExtraOptions

```TypeScript
setExtraOptions(options: TCPExtraOptions): Promise<void>
```

在TLSSocketServer的listen成功之后，设置TLSSocketServer连接的其他属性，使用Promise异步回调。

> **说明：**&gt;
> listen方法调用成功后，才可调用此方法。

**起始版本：** 10

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
| [2303188](../errorcode-net-socket.md#2303188-非套接字的套接字操作) |
| [2300002](../errorcode-net-socket.md#2300002-系统内部错误) |
