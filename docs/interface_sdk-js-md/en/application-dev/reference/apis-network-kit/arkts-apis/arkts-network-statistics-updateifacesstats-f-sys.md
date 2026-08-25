# updateIfacesStats (System API)

## Modules to Import

```TypeScript
import { statistics } from 'kits/@kit.NetworkKit';
```

## updateIfacesStats

```TypeScript
function updateIfacesStats(iface: string, start: number, end: number, stats: NetStatsInfo): Promise<void>
```

Updates network interface statistics data.

**Since:** 26.0.0

**Required permissions:** ohos.permission.GET_NETWORK_STATS

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| iface | string | Yes |
| start | number | Yes |
| end | number | Yes |
| stats | [NetStatsInfo](arkts-network-statistics-netstatsinfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
