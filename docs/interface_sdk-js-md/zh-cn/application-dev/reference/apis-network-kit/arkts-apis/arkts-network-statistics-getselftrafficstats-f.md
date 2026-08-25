# getSelfTrafficStats

## 导入模块

```TypeScript
import { statistics } from 'kits/@kit.NetworkKit';
```

## getSelfTrafficStats

```TypeScript
function getSelfTrafficStats(networkInfo: NetworkInfo): Promise<NetStatsInfo>
```

获取指定时间段内，本应用在指定网络中的流量使用情况。使用Promise异步回调。

> **说明：**&gt;
> - 当前只支持获取蜂窝和Wi-Fi流量使用情况。

> - 当前只支持获取31天之内的流量使用情况，如果参数中传入的时间戳早于当前系统时间31天，会返回错误码2103019。&gt;
> - 本接口会有一定耗时，调用时请注意切勿频繁调用。

**起始版本：** 22

**系统能力：** SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| networkInfo | [NetworkInfo](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-cachedownload-networkinfo-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[NetStatsInfo](arkts-network-statistics-netstatsinfo-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [2100001](../errorcode-net-connection.md#2100001-非法参数值) |
| [2100002](../errorcode-net-connection.md#2100002-连接服务失败) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |
| [2103017](../errorcode-net-statistics.md#2103017-读取数据库失败) |
| [2103019](../errorcode-net-statistics.md#2103019-时间戳无效) |
