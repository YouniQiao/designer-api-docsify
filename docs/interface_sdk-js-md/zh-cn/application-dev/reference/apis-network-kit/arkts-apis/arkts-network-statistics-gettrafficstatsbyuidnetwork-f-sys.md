# getTrafficStatsByUidNetwork（系统接口）

## 导入模块

```TypeScript
import { statistics } from 'kits/@kit.NetworkKit';
```

## getTrafficStatsByUidNetwork

```TypeScript
function getTrafficStatsByUidNetwork(uid: number, networkInfo: NetworkInfo): Promise<NetStatsInfoSequence>
```

获取指定时间段内，应用在指定网络中的流量使用详情，使用 Promise 异步回调。

**起始版本：** 12

**需要权限：** ohos.permission.GET_NETWORK_STATS

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uid | number | 是 |
| networkInfo | [NetworkInfo](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-cachedownload-networkinfo-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;NetStatsInfoSequence & gt; |

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
