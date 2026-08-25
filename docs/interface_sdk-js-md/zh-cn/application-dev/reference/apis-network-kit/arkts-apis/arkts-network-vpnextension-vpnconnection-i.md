# VpnConnection

VPN连接对象。在调用VpnConnection的方法前，需要先通过vpnExt.createVpnConnection创建VPN连接对象。

**起始版本：** 11

**系统能力：** SystemCapability.Communication.NetManager.Vpn

## 导入模块

```TypeScript
import { vpnExtension } from 'kits/@kit.NetworkKit';
```

## addRoute

```TypeScript
addRoute(routes: RouteInfo[], vpnId?: string): Promise<void>
```

为VPN网络添加路由

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NetManager.Vpn

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| routes | [RouteInfo[]](arkts-network-vpnextension-routeinfo-t.md) | 是 |
| vpnId | string | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [2200001](../errorcode-net-ethernet.md#2200001-非法参数值) |
| [2200002](../errorcode-net-ethernet.md#2200002-连接服务失败) |
| [2200003](../errorcode-net-ethernet.md#2200003-系统内部错误) |

## create

```TypeScript
create(config: VpnConfig): Promise<number>
```

使用config创建一个VPN网络。使用Promise异步回调。

> **说明：**&gt;
> 建议在不需要VPN网络的时候配对调用[destroy()](#destroy)或
> [destroy(vpnId: string)](#destroy)接口销毁启动的VPN网络，并执行资源清理等操作。

**起始版本：** 11

**系统能力：** SystemCapability.Communication.NetManager.Vpn

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [VpnConfig](arkts-network-vpnextension-vpnconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2200001](../errorcode-net-ethernet.md#2200001-非法参数值) |
| [2200002](../errorcode-net-ethernet.md#2200002-连接服务失败) |
| [2200003](../errorcode-net-ethernet.md#2200003-系统内部错误) |
| [2203001](../errorcode-net-vpn.md#2203001-vpn创建失败) |
| [2203002](../errorcode-net-vpn.md#2203002-vpn已存在) |

## delRoute

```TypeScript
delRoute(routes: RouteInfo[], vpnId?: string): Promise<void>
```

删除VPN网络的路由

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NetManager.Vpn

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| routes | [RouteInfo[]](arkts-network-vpnextension-routeinfo-t.md) | 是 |
| vpnId | string | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [2200001](../errorcode-net-ethernet.md#2200001-非法参数值) |
| [2200002](../errorcode-net-ethernet.md#2200002-连接服务失败) |
| [2200003](../errorcode-net-ethernet.md#2200003-系统内部错误) |

## destroy

```TypeScript
destroy(): Promise<void>
```

销毁启动的VPN网络。使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Communication.NetManager.Vpn

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2200002](../errorcode-net-ethernet.md#2200002-连接服务失败) |
| [2200003](../errorcode-net-ethernet.md#2200003-系统内部错误) |

## destroy

```TypeScript
destroy(vpnId: string): Promise<void>
```

根据vpnId销毁指定的VPN网络。使用Promise异步回调。

**起始版本：** 20

**系统能力：** SystemCapability.Communication.NetManager.Vpn

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| vpnId | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [19900001](../errorcode-net-vpn.md#19900001-无效参数) |
| [19900002](../errorcode-net-vpn.md#19900002-系统内部错误) |

## generateVpnId

```TypeScript
generateVpnId(): Promise<string>
```

生成VPN唯一标识。使用Promise异步回调。如需使用系统多VPN能力，需调用该接口生成vpnId，配置到VpnConfig中。

> **注意**&gt;
> 当前系统多VPN能力仅支持IPv4。

**起始版本：** 20

**系统能力：** SystemCapability.Communication.NetManager.Vpn

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [19900001](../errorcode-net-vpn.md#19900001-无效参数) |
| [19900002](../errorcode-net-vpn.md#19900002-系统内部错误) |

## protect

```TypeScript
protect(socketFd: number): Promise<void>
```

保护套接字不受VPN连接影响，通过该套接字发送的数据将直接基于物理网络收发，因此其流量不会通过VPN转发。使用Promise方式作为异步方法。

**起始版本：** 11

**系统能力：** SystemCapability.Communication.NetManager.Vpn

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| socketFd | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2200001](../errorcode-net-ethernet.md#2200001-非法参数值) |
| [2200002](../errorcode-net-ethernet.md#2200002-连接服务失败) |
| [2200003](../errorcode-net-ethernet.md#2200003-系统内部错误) |
| [2203004](../errorcode-net-vpn.md#2203004-无效描述符) |

## protectProcessNet

```TypeScript
protectProcessNet(): Promise<void>
```

保护应用进程不受VPN连接影响，被保护的进程直接基于物理网络收发数据，流量不通过VPN转发。使用Promise异步回调。

**起始版本：** 22

**系统能力：** SystemCapability.Communication.NetManager.Vpn

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |
