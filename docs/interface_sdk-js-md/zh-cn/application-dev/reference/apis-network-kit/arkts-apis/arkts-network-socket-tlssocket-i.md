# TLSSocket

TLSSocket连接。在调用TLSSocket的方法前，需要先通过[socket.constructTLSSocketInstance](arkts-network-socket-constructtlssocketinstance-f.md)创建 TLSSocket对象。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { socket } from 'kits/@kit.NetworkKit';
```

## bind

```TypeScript
bind(address: NetAddress, callback: AsyncCallback<void>): void
```

绑定IP地址和端口。使用callback异步回调。

> **说明：**&gt;
> 如果TLSSocket对象是通过TCPSocket对象升级创建的，可以不用执行bind方法。

**起始版本：** 9

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
| [2303198](../errorcode-net-socket.md#2303198-网络地址已被使用) |
| [2300002](../errorcode-net-socket.md#2300002-系统内部错误) |

## bind

```TypeScript
bind(address: NetAddress): Promise<void>
```

绑定IP地址和端口。使用Promise异步回调。

> **说明：**&gt;
> 如果TLSSocket对象是通过TCPSocket对象升级创建的，可以不用执行bind方法。

**起始版本：** 9

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
| [2303198](../errorcode-net-socket.md#2303198-网络地址已被使用) |
| [2300002](../errorcode-net-socket.md#2300002-系统内部错误) |

## close

```TypeScript
close(callback: AsyncCallback<void>): void
```

在TLSSocket通信连接成功之后，断开连接，使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2303501](../errorcode-net-socket.md#2303501-ssl为空) |
| [2303505](../errorcode-net-socket.md#2303505-tls系统调用错误) |
| [2303506](../errorcode-net-socket.md#2303506-关闭tls连接失败) |
| [2300002](../errorcode-net-socket.md#2300002-系统内部错误) |

## close

```TypeScript
close(): Promise<void>
```

在TLSSocket通信连接成功之后，断开连接，使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.NetStack

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2303501](../errorcode-net-socket.md#2303501-ssl为空) |
| [2303505](../errorcode-net-socket.md#2303505-tls系统调用错误) |
| [2303506](../errorcode-net-socket.md#2303506-关闭tls连接失败) |
| [2300002](../errorcode-net-socket.md#2300002-系统内部错误) |

## connect

```TypeScript
connect(options: TLSConnectOptions, callback: AsyncCallback<void>): void
```

在TLSSocket上bind成功之后，进行通信连接，并创建和初始化TLS会话，实现建立连接过程，启动与服务器的TLS/SSL握手，实现数据传输功能，使用callback异步回调。需要注意options入参下 secureOptions内的ca在API11及之前的版本为必填项，需填入服务端的ca证书(用于认证校验服务端的数字证书)，证书内容以"-----BEGIN CERTIFICATE-----"开头，以"-----END CERTIFICATE-----"结尾，自API12开始，为非必填项。

**起始版本：** 9

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
| [2303104](../errorcode-net-socket.md#2303104-中断系统调用) |
| [2303109](../errorcode-net-socket.md#2303109-错误文件编号) |
| [2303111](../errorcode-net-socket.md#2303111-资源暂时不可用请重试) |
| [2303188](../errorcode-net-socket.md#2303188-非套接字的套接字操作) |
| [2303191](../errorcode-net-socket.md#2303191-socket协议类型错误) |
| [2303198](../errorcode-net-socket.md#2303198-网络地址已被使用) |
| [2303199](../errorcode-net-socket.md#2303199-不能分配请求的地址) |
| [2303210](../errorcode-net-socket.md#2303210-连接超时) |
| [2303501](../errorcode-net-socket.md#2303501-ssl为空) |
| [2303502](../errorcode-net-socket.md#2303502-tls读取错误) |
| [2303503](../errorcode-net-socket.md#2303503-tls写入错误) |
| [2303505](../errorcode-net-socket.md#2303505-tls系统调用错误) |
| [2303506](../errorcode-net-socket.md#2303506-关闭tls连接失败) |
| [2300002](../errorcode-net-socket.md#2300002-系统内部错误) |
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
connect(options: TLSConnectOptions): Promise<void>
```

在TLSSocket上bind成功之后，进行通信连接，并创建和初始化TLS会话，实现建立连接过程，启动与服务器的TLS/SSL握手，实现数据传输功能，该连接包括两种认证方式，单向认证与双向认证，使用Promise异步回调。需要 注意options入参下secureOptions内的ca在API11及之前的版本为必填项，需填入服务端的ca证书(用于认证校验服务端的数字证书)，证书内容以"-----BEGIN CERTIFICATE-----"开头，以"-----END CERTIFICATE-----"结尾，自API12开始，为非必填项。

**起始版本：** 9

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
| [2303104](../errorcode-net-socket.md#2303104-中断系统调用) |
| [2303109](../errorcode-net-socket.md#2303109-错误文件编号) |
| [2303111](../errorcode-net-socket.md#2303111-资源暂时不可用请重试) |
| [2303188](../errorcode-net-socket.md#2303188-非套接字的套接字操作) |
| [2303191](../errorcode-net-socket.md#2303191-socket协议类型错误) |
| [2303198](../errorcode-net-socket.md#2303198-网络地址已被使用) |
| [2303199](../errorcode-net-socket.md#2303199-不能分配请求的地址) |
| [2303210](../errorcode-net-socket.md#2303210-连接超时) |
| [2303501](../errorcode-net-socket.md#2303501-ssl为空) |
| [2303502](../errorcode-net-socket.md#2303502-tls读取错误) |
| [2303503](../errorcode-net-socket.md#2303503-tls写入错误) |
| [2303505](../errorcode-net-socket.md#2303505-tls系统调用错误) |
| [2303506](../errorcode-net-socket.md#2303506-关闭tls连接失败) |
| [2300002](../errorcode-net-socket.md#2300002-系统内部错误) |
| [2301206](../errorcode-net-socket.md#2301206-socks5连接代理服务器失败) |
| [2301207](../errorcode-net-socket.md#2301207-socks5认证用户名或密码无效) |
| [2301208](../errorcode-net-socket.md#2301208-socks5连接远程服务器失败) |
| [2301209](../errorcode-net-socket.md#2301209-socks5协商认证方式失败) |
| [2301210](../errorcode-net-socket.md#2301210-socks5发送消息失败) |
| [2301211](../errorcode-net-socket.md#2301211-socks5接收消息失败) |
| [2301212](../errorcode-net-socket.md#2301212-socks5消息序列化失败) |
| [2301213](../errorcode-net-socket.md#2301213-socks5消息反序列化失败) |

## getCertificate

```TypeScript
getCertificate(callback: AsyncCallback<X509CertRawData>): void
```

在TLSSocket通信连接成功之后，获取本地的数字证书，该接口只适用于双向认证时，使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[X509CertRawData](arkts-network-socket-x509certrawdata-t.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [2303501](../errorcode-net-socket.md#2303501-ssl为空) |
| [2303504](../errorcode-net-socket.md#2303504-查找x509时出错) |
| [2300002](../errorcode-net-socket.md#2300002-系统内部错误) |

## getCertificate

```TypeScript
getCertificate(): Promise<X509CertRawData>
```

在TLSSocket通信连接之后，获取本地的数字证书，该接口只适用于双向认证时，使用Promise异步回调。

**起始版本：** 9

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

## getCipherSuite

```TypeScript
getCipherSuite(callback: AsyncCallback<Array<string>>): void
```

在TLSSocket通信连接成功之后，获取通信双方协商后的加密套件，使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [2303501](../errorcode-net-socket.md#2303501-ssl为空) |
| [2303502](../errorcode-net-socket.md#2303502-tls读取错误) |
| [2303505](../errorcode-net-socket.md#2303505-tls系统调用错误) |
| [2300002](../errorcode-net-socket.md#2300002-系统内部错误) |

## getCipherSuite

```TypeScript
getCipherSuite(): Promise<Array<string>>
```

在TLSSocket通信连接成功之后，获取通信双方协商后的加密套件，使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.NetStack

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [2303501](../errorcode-net-socket.md#2303501-ssl为空) |
| [2303502](../errorcode-net-socket.md#2303502-tls读取错误) |
| [2303505](../errorcode-net-socket.md#2303505-tls系统调用错误) |
| [2300002](../errorcode-net-socket.md#2300002-系统内部错误) |

## getLocalAddress

```TypeScript
getLocalAddress(): Promise<NetAddress>
```

获取TLSSocket的本地Socket地址。使用Promise异步回调。

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

在TLSSocket通信连接成功之后，获取通信的协议版本，使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [2303501](../errorcode-net-socket.md#2303501-ssl为空) |
| [2303505](../errorcode-net-socket.md#2303505-tls系统调用错误) |
| [2300002](../errorcode-net-socket.md#2300002-系统内部错误) |

## getProtocol

```TypeScript
getProtocol(): Promise<string>
```

在TLSSocket通信连接成功之后，获取通信的协议版本，使用Promise异步回调。

**起始版本：** 9

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

## getRemoteAddress

```TypeScript
getRemoteAddress(callback: AsyncCallback<NetAddress>): void
```

在TLSSocket通信连接成功之后，获取对端Socket地址。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;NetAddress&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [2303188](../errorcode-net-socket.md#2303188-非套接字的套接字操作) |
| [2300002](../errorcode-net-socket.md#2300002-系统内部错误) |

## getRemoteAddress

```TypeScript
getRemoteAddress(): Promise<NetAddress>
```

在TLSSocket通信连接成功之后，获取对端Socket地址。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.NetStack

**返回值：**

| 类型 |
| --- |
| Promise & lt;NetAddress & gt; |

**错误码：**

| 错误码ID |
| --- |
| [2303188](../errorcode-net-socket.md#2303188-非套接字的套接字操作) |
| [2300002](../errorcode-net-socket.md#2300002-系统内部错误) |

## getRemoteCertificate

```TypeScript
getRemoteCertificate(callback: AsyncCallback<X509CertRawData>): void
```

在TLSSocket通信连接成功之后，获取服务端的数字证书，使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[X509CertRawData](arkts-network-socket-x509certrawdata-t.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [2303501](../errorcode-net-socket.md#2303501-ssl为空) |
| [2300002](../errorcode-net-socket.md#2300002-系统内部错误) |

## getRemoteCertificate

```TypeScript
getRemoteCertificate(): Promise<X509CertRawData>
```

在TLSSocket通信连接成功之后，获取服务端的数字证书，使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.NetStack

**返回值：**

| 类型 |
| --- |
| Promise&lt;[X509CertRawData](arkts-network-socket-x509certrawdata-t.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [2303501](../errorcode-net-socket.md#2303501-ssl为空) |
| [2300002](../errorcode-net-socket.md#2300002-系统内部错误) |

## getSignatureAlgorithms

```TypeScript
getSignatureAlgorithms(callback: AsyncCallback<Array<string>>): void
```

在TLSSocket通信连接成功之后，获取通信双方协商后签名算法，该接口只适配双向认证模式下，使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [2303501](../errorcode-net-socket.md#2303501-ssl为空) |
| [2300002](../errorcode-net-socket.md#2300002-系统内部错误) |

## getSignatureAlgorithms

```TypeScript
getSignatureAlgorithms(): Promise<Array<string>>
```

在TLSSocket通信连接成功之后，获取通信双方协商后的签名算法，该接口只适配双向认证模式下，使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.NetStack

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [2303501](../errorcode-net-socket.md#2303501-ssl为空) |
| [2300002](../errorcode-net-socket.md#2300002-系统内部错误) |

## getSocketFd

```TypeScript
getSocketFd(): Promise<number>
```

获取TLSSocket的文件描述符。使用Promise异步回调。

> **说明：**&gt;
> - bind方法调用成功后，才可调用此方法。&gt;
> - 文件描述符的生命周期由系统管理，应用可以通过[close](#close)方法关闭Socket连接，避免直接操作
> 文件描述符进行关闭。

**起始版本：** 16

**系统能力：** SystemCapability.Communication.NetStack

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## getState

```TypeScript
getState(callback: AsyncCallback<SocketStateBase>): void
```

在TLSSocket的bind成功之后，获取TLSSocket状态。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SocketStateBase](arkts-network-socket-socketstatebase-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [2303188](../errorcode-net-socket.md#2303188-非套接字的套接字操作) |
| [2300002](../errorcode-net-socket.md#2300002-系统内部错误) |

## getState

```TypeScript
getState(): Promise<SocketStateBase>
```

在TLSSocket的bind成功之后，获取TLSSocket状态。使用Promise异步回调。

**起始版本：** 9

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

## off('message')

```TypeScript
off(type: 'message', callback?: Callback<SocketMessageInfo>): void
```

取消订阅TLSSocket连接的接收消息事件。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'message' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SocketMessageInfo](arkts-network-socket-socketmessageinfo-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off('connect' | 'close')

```TypeScript
off(type: 'connect' | 'close', callback?: Callback<void>): void
```

取消订阅TLSSocket的连接事件或关闭事件。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'connect' \| 'close' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off('connect' | 'close')

```TypeScript
off(type: 'connect' | 'close', callback?: Callback<void>): void
```

取消订阅TLSSocket的连接事件或关闭事件。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'connect' \| 'close' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off('error')

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

取消订阅TLSSocket连接的error事件。使用callback异步回调。

**起始版本：** 9

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
on(type: 'message', callback: Callback<SocketMessageInfo>): void
```

订阅TLSSocket连接的接收消息事件。使用callback异步回调。

> **说明：**&gt;
> bind方法调用成功后，才可调用此方法。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'message' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SocketMessageInfo](arkts-network-socket-socketmessageinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## on('connect' | 'close')

```TypeScript
on(type: 'connect' | 'close', callback: Callback<void>): void
```

订阅TLSSocket的连接事件或关闭事件。使用callback异步回调。

> **说明：**&gt;
> bind方法调用成功后，才可调用此方法。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'connect' \| 'close' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## on('connect' | 'close')

```TypeScript
on(type: 'connect' | 'close', callback: Callback<void>): void
```

订阅TLSSocket的连接事件或关闭事件。使用callback异步回调。

> **说明：**&gt;
> bind方法调用成功后，才可调用此方法。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'connect' \| 'close' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

订阅TLSSocket连接的error事件。使用callback异步回调。

> **说明：**&gt;
> bind方法调用成功后，才可调用此方法。

**起始版本：** 9

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
send(data: string | ArrayBuffer, callback: AsyncCallback<void>): void
```

在TLSSocket通信连接成功之后，向服务端发送消息，使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | string \| ArrayBuffer | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2303501](../errorcode-net-socket.md#2303501-ssl为空) |
| [2303503](../errorcode-net-socket.md#2303503-tls写入错误) |
| [2303505](../errorcode-net-socket.md#2303505-tls系统调用错误) |
| [2303506](../errorcode-net-socket.md#2303506-关闭tls连接失败) |
| [2300002](../errorcode-net-socket.md#2300002-系统内部错误) |

## send

```TypeScript
send(data: string | ArrayBuffer): Promise<void>
```

在TLSSocket通信连接成功之后，向服务端发送消息，使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | string \| ArrayBuffer | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2303501](../errorcode-net-socket.md#2303501-ssl为空) |
| [2303503](../errorcode-net-socket.md#2303503-tls写入错误) |
| [2303505](../errorcode-net-socket.md#2303505-tls系统调用错误) |
| [2303506](../errorcode-net-socket.md#2303506-关闭tls连接失败) |
| [2300002](../errorcode-net-socket.md#2300002-系统内部错误) |

## setExtraOptions

```TypeScript
setExtraOptions(options: TCPExtraOptions, callback: AsyncCallback<void>): void
```

在TLSSocket的bind成功之后，设置TCPSocket连接的其他属性。使用callback异步回调。

**起始版本：** 9

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

在TLSSocket的bind成功之后，设置TCPSocket连接的其他属性。使用Promise异步回调。

**起始版本：** 9

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
