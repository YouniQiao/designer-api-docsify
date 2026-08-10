# getTrafficStatsByNetwork（系统接口）

## 导入模块

```TypeScript
import { statistics } from 'kits/@kit.NetworkKit';
```

## getTrafficStatsByNetwork

```TypeScript
function getTrafficStatsByNetwork(networkInfo: NetworkInfo): Promise<UidNetStatsInfo>
```

Get the traffic usage details of the specified network of all applications in the specified time period.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.GET_NETWORK_STATS

<!--Device-statistics-function getTrafficStatsByNetwork(networkInfo: NetworkInfo): Promise<UidNetStatsInfo>--><!--Device-statistics-function getTrafficStatsByNetwork(networkInfo: NetworkInfo): Promise<UidNetStatsInfo>-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| networkInfo | [NetworkInfo](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-cachedownload-networkinfo-i.md) | 是 | Information about the network to be queried. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;UidNetStatsInfo&gt; | The statistics of the sim card. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 201 | Permission denied. |
| 2103017 | Failed to read the database. |
| 202 | Non-system applications use system APIs. |

## 示例

```TypeScript
import { connection, statistics } from '@kit.NetworkKit';

let networkInfo: statistics.NetworkInfo = {
  type: connection.NetBearType.BEARER_CELLULAR,
  startTime: Math.floor(Date.now() / 1000) - 86400 * 7, 
  endTime: Math.floor(Date.now() / 1000) + 5,
  simId: 1,
}

statistics.getTrafficStatsByNetwork(networkInfo).then((statsInfo: statistics.UidNetStatsInfo) => {
  let rank: Map<string, object> = new Map<string, object>(Object.entries(statsInfo));
  rank.forEach((value: object, key: string) => {
    console.info("getTrafficStatsByNetwork key=" + key + ", value=" + JSON.stringify(value));
  })
})
```

