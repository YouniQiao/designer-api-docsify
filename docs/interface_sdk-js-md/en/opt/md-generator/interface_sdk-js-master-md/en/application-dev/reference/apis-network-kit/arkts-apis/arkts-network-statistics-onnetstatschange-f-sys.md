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

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_NETWORK_STATS

<!--Device-statistics-function onNetStatsChange(callback: Callback<NetStatsChangeInfo>): void--><!--Device-statistics-function onNetStatsChange(callback: Callback<NetStatsChangeInfo>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[NetStatsChangeInfo](arkts-network-statistics-netstatschangeinfo-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
