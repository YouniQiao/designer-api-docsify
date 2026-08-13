# getSelfTrafficStats

## Modules to Import

```TypeScript
import { statistics } from '@kit.NetworkKit';
```

## getSelfTrafficStats

```TypeScript
function getSelfTrafficStats(networkInfo: NetworkInfo): Promise<NetStatsInfo>
```

Get the traffic usage details of the specified network of the calling application in the specified time period and the specified networktype.

**Since:** 26.0.0

**Deprecated since:** -1

<!--Device-statistics-function getSelfTrafficStats(networkInfo: NetworkInfo): Promise<NetStatsInfo>--><!--Device-statistics-function getSelfTrafficStats(networkInfo: NetworkInfo): Promise<NetStatsInfo>-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| networkInfo | [NetworkInfo](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-cachedownload-networkinfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[NetStatsInfo](arkts-network-statistics-netstatsinfo-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
| [2103017](../errorcode-net-statistics.md#2103017-failed-to-read-the-database) |
| [2103019](../errorcode-net-statistics.md#2103019-invalid-timestamp) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { connection, statistics } from '@kit.NetworkKit';

let networkInfo: statistics.NetworkInfo = {
    type: connection.NetBearType.BEARER_CELLULAR,
    startTime: Math.floor(Date.now() / 1000) - 86400 * 31,
    endTime: Math.floor(Date.now() / 1000),
    simId: 1,
}

statistics.getSelfTrafficStats(networkInfo).then((stats: statistics.NetStatsInfo) => {
    console.info('getSelfTrafficStats success : ' + JSON.stringify(stats));
}).catch((err: BusinessError) => {
    console.error('getSelfTrafficStats error. code: ' + `${err.code}` + ', message: ' + `${err.message}`);
});
```
