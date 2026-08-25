# NetHandle

网络句柄。在调用NetHandle的方法之前，需要先获取NetHandle对象。例如可通过[getDefaultNet](arkts-network-connection-getdefaultnet-f.md)获取系统当前默认网络的网络句柄。

**起始版本：** 8

**系统能力：** SystemCapability.Communication.NetManager.Core

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## bindSocket

```TypeScript
bindSocket(socketParam: TCPSocket | UDPSocket, callback: AsyncCallback<void>): void
```

将TCPSocket或UDPSocket绑定到当前NetHandle对应的网络。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| socketParam | TCPSocket \| [UDPSocket](arkts-network-connection-udpsocket-t.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2100001](../errorcode-net-connection.md#2100001-非法参数值) |
| [2100002](../errorcode-net-connection.md#2100002-连接服务失败) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |

## bindSocket

```TypeScript
bindSocket(socketParam: TCPSocket | UDPSocket): Promise<void>
```

将TCPSocket或UDPSocket绑定到当前NetHandle对应的网络。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| socketParam | TCPSocket \| [UDPSocket](arkts-network-connection-udpsocket-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2100001](../errorcode-net-connection.md#2100001-非法参数值) |
| [2100002](../errorcode-net-connection.md#2100002-连接服务失败) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |

## getAddressByName

```TypeScript
getAddressByName(host: string, callback: AsyncCallback<NetAddress>): void
```

使用当前NetHandle对应的网络解析主机名获取到的第一个IP地址。使用callback异步回调。

**起始版本：** 8

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| host | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;NetAddress&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2100001](../errorcode-net-connection.md#2100001-非法参数值) |
| [2100002](../errorcode-net-connection.md#2100002-连接服务失败) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |

## getAddressByName

```TypeScript
getAddressByName(host: string): Promise<NetAddress>
```

使用当前NetHandle对应的网络解析主机名获取到的第一个IP地址。使用Promise异步回调。

**起始版本：** 8

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| host | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;NetAddress & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2100001](../errorcode-net-connection.md#2100001-非法参数值) |
| [2100002](../errorcode-net-connection.md#2100002-连接服务失败) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |

## getAddressesByName

```TypeScript
getAddressesByName(host: string, callback: AsyncCallback<Array<NetAddress>>): void
```

使用当前NetHandle对应的网络解析主机名获取到的所有IP地址。使用callback异步回调。

**起始版本：** 8

**需要权限：** ohos.permission.INTERNET

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| host | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;NetAddress&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2100001](../errorcode-net-connection.md#2100001-非法参数值) |
| [2100002](../errorcode-net-connection.md#2100002-连接服务失败) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |

## getAddressesByName

```TypeScript
getAddressesByName(host: string): Promise<Array<NetAddress>>
```

使用当前NetHandle对应的网络解析主机名获取到的所有IP地址。使用Promise异步回调。

**起始版本：** 8

**需要权限：** ohos.permission.INTERNET

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| host | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;NetAddress & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2100001](../errorcode-net-connection.md#2100001-非法参数值) |
| [2100002](../errorcode-net-connection.md#2100002-连接服务失败) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |

## getAddressesByNameWithOptions

```TypeScript
getAddressesByNameWithOptions(host: string, option?: QueryOptions): Promise<Array<NetAddress>>
```

使用当前NetHandle对应的网络基于指定IP类型进行DNS解析。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.INTERNET

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| host | string | 是 |
| option | [QueryOptions](arkts-network-connection-queryoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;NetAddress & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [2100001](../errorcode-net-connection.md#2100001-非法参数值) |
| [2100002](../errorcode-net-connection.md#2100002-连接服务失败) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |

## netId

```TypeScript
netId: number
```

网络ID，取值为0代表没有默认网络，其余有效取值必须大于等于100。

**类型：** number

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetManager.Core
