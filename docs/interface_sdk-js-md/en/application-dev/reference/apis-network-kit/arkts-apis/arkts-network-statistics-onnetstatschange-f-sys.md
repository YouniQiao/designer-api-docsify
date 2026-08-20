# onNetStatsChange (System API)

## Modules to Import

```TypeScript
import { statistics } from '@kit.NetworkKit';
```

## onNetStatsChange

```TypeScript
function onNetStatsChange(callback: Callback<NetStatsChangeInfo>): void
```

Register notifications of network traffic updates.

**Since:** 23

**Required permissions:** ohos.permission.GET_NETWORK_STATS

<!--Device-statistics-function onNetStatsChange(callback: Callback<NetStatsChangeInfo>): void--><!--Device-statistics-function onNetStatsChange(callback: Callback<NetStatsChangeInfo>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[NetStatsChangeInfo](arkts-network-statistics-netstatschangeinfo-i-sys.md)&gt; | Yes | The callback of on. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) | Failed to connect to the service. |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) | System internal error. |

