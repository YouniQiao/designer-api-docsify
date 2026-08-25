# getTrafficStatsByIface（系统接口）

## 导入模块

```TypeScript
import { statistics } from 'kits/@kit.NetworkKit';
```

## getTrafficStatsByIface

```TypeScript
function getTrafficStatsByIface(ifaceInfo: IfaceInfo, callback: AsyncCallback<NetStatsInfo>): void
```

获取指定网卡历史流量信息，使用 callback 异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.GET_NETWORK_STATS

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [ifaceInfo](arkts-network-statistics-uidinfo-i-sys.md) | [IfaceInfo](arkts-network-statistics-ifaceinfo-i-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[NetStatsInfo](arkts-network-statistics-netstatsinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2100001](../errorcode-net-connection.md#2100001-非法参数值) |
| [2100002](../errorcode-net-connection.md#2100002-连接服务失败) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |
| [2103017](../errorcode-net-statistics.md#2103017-读取数据库失败) |


## getTrafficStatsByIface

```TypeScript
function getTrafficStatsByIface(ifaceInfo: IfaceInfo): Promise<NetStatsInfo>
```

获取指定网卡历史流量信息，使用 Promise 异步回调。  
| 参数名 | 类型 | 必填 | 说明 | | --------- | ------------------------- | ---- | --------------------------------------------------- | | [ifaceInfo](arkts-network-statistics-uidinfo-i-sys.md) | [IfaceInfo](arkts-network-statistics-ifaceinfo-i-sys.md) | 是 |

**起始版本：** 10

**需要权限：** ohos.permission.GET_NETWORK_STATS

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [ifaceInfo](arkts-network-statistics-uidinfo-i-sys.md) | [IfaceInfo](arkts-network-statistics-ifaceinfo-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[NetStatsInfo](arkts-network-statistics-netstatsinfo-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2100001](../errorcode-net-connection.md#2100001-非法参数值) |
| [2100002](../errorcode-net-connection.md#2100002-连接服务失败) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |
| [2103017](../errorcode-net-statistics.md#2103017-读取数据库失败) |
