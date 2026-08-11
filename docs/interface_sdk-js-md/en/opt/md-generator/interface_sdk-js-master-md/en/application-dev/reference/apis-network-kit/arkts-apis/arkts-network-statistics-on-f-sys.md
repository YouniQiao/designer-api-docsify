# on (System API)

## Modules to Import

```TypeScript
import { statistics } from 'kits/@kit.NetworkKit';
```

## on('netStatsChange')

```TypeScript
function on(type: 'netStatsChange', callback: Callback<NetStatsChangeInfo>): void
```

Register notifications of network traffic updates.

**Since:** 11

**Required permissions:** ohos.permission.GET_NETWORK_STATS

<!--Device-statistics-function on(type: 'netStatsChange', callback: Callback<NetStatsChangeInfo>): void--><!--Device-statistics-function on(type: 'netStatsChange', callback: Callback<NetStatsChangeInfo>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'netStatsChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;NetStatsChangeInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { statistics } from '@kit.NetworkKit';

class IFace {
  iface: string = ""
  uid?: number = 0
}
statistics.on('netStatsChange', (data: IFace) => {
  console.info('on netStatsChange' + JSON.stringify(data));
});
```
