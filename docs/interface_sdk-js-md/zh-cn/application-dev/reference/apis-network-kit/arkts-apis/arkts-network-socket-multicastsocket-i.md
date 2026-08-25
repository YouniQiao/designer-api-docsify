# MulticastSocket

MulticastSocket连接。在调用MulticastSocket的方法前，需要先通过 [socket.constructMulticastSocketInstance](arkts-network-socket-constructmulticastsocketinstance-f.md)创建MulticastSocket对象。

**继承/实现关系：** MulticastSocket extends [UDPSocket](arkts-network-socket-udpsocket-i.md)

**起始版本：** 11

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { socket } from 'kits/@kit.NetworkKit';
```

## addMembership

```TypeScript
addMembership(multicastAddress: NetAddress, callback: AsyncCallback<void>): void
```

加入多播组。使用callback异步回调。

> **说明：**&gt;
> 多播使用的IP地址属于特定的范围（例如224.0.0.0到239.255.255.255）。&gt;
> 加入多播组后，既可以是发送端，也可以是接收端，相互之间以广播的形式传递数据，不区分客户端或服务端。

**起始版本：** 11

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| multicastAddress | [NetAddress](arkts-network-connection-netaddress-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 2301022 |
| 2301088 |
| 2301098 |

## addMembership

```TypeScript
addMembership(multicastAddress: NetAddress): Promise<void>
```

加入多播组。使用Promise异步回调。

> **说明：**&gt;
> 多播使用的IP地址属于特定的范围（例如224.0.0.0到239.255.255.255）。&gt;
> 加入多播组后，既可以是发送端，也可以是接收端，相互之间以广播的形式传递数据，不区分客户端或服务端。

**起始版本：** 11

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| multicastAddress | [NetAddress](arkts-network-connection-netaddress-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 2301088 |
| 2301098 |

## dropMembership

```TypeScript
dropMembership(multicastAddress: NetAddress, callback: AsyncCallback<void>): void
```

退出多播组。使用callback异步回调。

> **说明：**&gt;
> 多播使用的IP地址属于特定的范围（例如224.0.0.0到239.255.255.255）。&gt;
> 从已加入的多播组中退出，必须在加入多播组
> [addMembership](#addmembership)
> 之后退出才有效。

**起始版本：** 11

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| multicastAddress | [NetAddress](arkts-network-connection-netaddress-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 2301088 |
| 2301098 |

## dropMembership

```TypeScript
dropMembership(multicastAddress: NetAddress): Promise<void>
```

退出多播组。使用Promise异步回调。

> **说明：**&gt;
> 多播使用的IP地址属于特定的范围（例如224.0.0.0到239.255.255.255）。&gt;
> 从已加入的多播组中退出，必须在加入多播组
> [addMembership](#addmembership)
> 之后退出才有效。

**起始版本：** 11

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| multicastAddress | [NetAddress](arkts-network-connection-netaddress-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 2301088 |
| 2301098 |

## getLoopbackMode

```TypeScript
getLoopbackMode(callback: AsyncCallback<boolean>): void
```

获取多播通信中的环回模式状态。使用callback异步回调。

> **说明：**&gt;
> 用于获取当前环回模式开启或关闭的状态。&gt;
> 如果获取的属性值为 true，表示环回模式是开启的状态，允许主机在本地循环接收自己发送的多播数据包。如果为 false，则表示环回模式是关闭的状态，主机不会接收到自己发送的多播数据包。&gt;
> 在调用
> [addMembership](#addmembership)
> 之后，调用此接口才有效。

**起始版本：** 11

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 2301088 |

## getLoopbackMode

```TypeScript
getLoopbackMode(): Promise<boolean>
```

获取多播通信中的环回模式状态。使用Promise异步回调。

> **说明：**&gt;
> 用于获取当前环回模式开启或关闭的状态。&gt;
> 如果获取的属性值为 true，表示环回模式是开启的状态，允许主机在本地循环接收自己发送的多播数据包。如果为 false，则表示环回模式是关闭的状态，主机不会接收到自己发送的多播数据包。&gt;
> 在调用
> [addMembership](#addmembership)
> 之后，调用此接口才有效。

**起始版本：** 11

**系统能力：** SystemCapability.Communication.NetStack

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 2301088 |

## getMulticastTTL

```TypeScript
getMulticastTTL(callback: AsyncCallback<number>): void
```

获取数据包在网络传输过程中路由器最大跳数(TTL)的值。使用callback异步回调。

> **说明：**&gt;
> 用于限制数据包在网络中传输时能够经过的最大路由器跳数的字段，TTL (Time to live)。&gt;
> 范围为 0～255，默认值为 1 。&gt;
> 如果一个多播数据包的 TTL 值为 1，那么它只能被直接连接到发送者的主机接收。如果 TTL 被设置为一个较大的值，那么数据包就能够被传送到更远的网络范围内。&gt;
> 在调用
> [addMembership](#addmembership)
> 之后，调用此接口才有效。

**起始版本：** 11

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 2301088 |

## getMulticastTTL

```TypeScript
getMulticastTTL(): Promise<number>
```

获取数据包在网络传输过程中路由器最大跳数(TTL)的值。使用Promise异步回调。

> **说明：**&gt;
> 用于限制数据包在网络中传输时能够经过的最大路由器跳数的字段，TTL (Time to live)。&gt;
> 范围为 0～255，默认值为 1 。&gt;
> 如果一个多播数据包的 TTL 值为 1，那么它只能被直接连接到发送者的主机接收。如果 TTL 被设置为一个较大的值，那么数据包就能够被传送到更远的网络范围内。&gt;
> 在调用
> [addMembership](#addmembership)
> 之后，调用此接口才有效。

**起始版本：** 11

**系统能力：** SystemCapability.Communication.NetStack

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 2301088 |

## getSocketFd

```TypeScript
getSocketFd(): Promise<number>
```

获取MulticastSocket的文件描述符。使用Promise异步回调。

> **说明：**&gt;
> - [bind](arkts-network-socket-udpsocket-i.md#bind)方法调用成功后，才可调用此方法。&gt;
> - bind异常、Socket已关闭（如调用close后）等异常情况下调用本接口会返回-1。&gt;
> - 文件描述符的生命周期由系统管理，应用可以通过[close](arkts-network-socket-udpsocket-i.md#close)方法关闭Socket连接，避免直接操作
> 文件描述符进行关闭。

**起始版本：** 23

**需要权限：** ohos.permission.INTERNET

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NetStack

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## setLoopbackMode

```TypeScript
setLoopbackMode(flag: boolean, callback: AsyncCallback<void>): void
```

设置多播通信中的环回模式标志位。使用callback异步回调。

> **说明：**&gt;
> 用于设置环回模式，开启或关闭两种状态，默认为开启状态。&gt;
> 如果一个多播通信中环回模式设置值为 true，那么它允许主机在本地循环接收自己发送的多播数据包。如果为 false，则主机不会接收到自己发送的多播数据包。&gt;
> 在调用
> [addMembership](#addmembership)
> 之后，调用此接口才有效。

**起始版本：** 11

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| flag | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 2301088 |

## setLoopbackMode

```TypeScript
setLoopbackMode(flag: boolean): Promise<void>
```

设置多播通信中的环回模式标志位。使用Promise异步回调。

> **说明：**&gt;
> 用于设置环回模式，开启或关闭两种状态，默认为开启状态。&gt;
> 如果一个多播通信中环回模式设置值为 true，那么它允许主机在本地循环接收自己发送的多播数据包。如果为 false，则主机不会接收到自己发送的多播数据包。&gt;
> 在调用
> [addMembership](#addmembership)
> 之后，调用此接口才有效。

**起始版本：** 11

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| flag | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 2301088 |

## setMulticastTTL

```TypeScript
setMulticastTTL(ttl: number, callback: AsyncCallback<void>): void
```

设置多播通信时数据包在网络传输过程中路由器最大跳数。使用callback异步回调。

> **说明：**&gt;
> 用于限制数据包在网络中传输时能够经过的最大路由器跳数的字段，TTL (Time to live)。&gt;
> 范围为 0～255，默认值为 1 。&gt;
> 如果一个多播数据包的 TTL 值为 1，那么它只能被直接连接到发送者的主机接收。如果 TTL 被设置为一个较大的值，那么数据包就能够被传送到更远的网络范围内。&gt;
> 在调用
> [addMembership](#addmembership)
> 之后，调用此接口才有效。

**起始版本：** 11

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ttl | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 2301022 |
| 2301088 |

## setMulticastTTL

```TypeScript
setMulticastTTL(ttl: number): Promise<void>
```

设置多播通信时数据包在网络传输过程中路由器最大跳数。使用Promise异步回调。

> **说明：**&gt;
> 用于限制数据包在网络中传输时能够经过的最大路由器跳数的字段，TTL (Time to live)。&gt;
> 范围为 0～255，默认值为 1 。&gt;
> 如果一个多播数据包的 TTL 值为 1，那么它只能被直接连接到发送者的主机接收。如果 TTL 被设置为一个较大的值，那么数据包就能够被传送到更远的网络范围内。&gt;
> 在调用
> [addMembership](#addmembership)
> 之后，调用此接口才有效。

**起始版本：** 11

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ttl | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 2301022 |
| 2301088 |

## setReuseAddress

```TypeScript
setReuseAddress(reuse: boolean): void
```

设置多播Socket是否支持地址复用。使用同步方式调用。

> **说明：**&gt;
> 用于控制多播Socket绑定端口时是否开启地址复用能力。&gt;
> 如需绑定已被占用的端口，确保占用方开启了地址复用能力，同时本业务也需在调用
> [bind](arkts-network-socket-udpsocket-i.md#bind)前调用本接口以开启地址复用能力。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| reuse | boolean | 是 |
