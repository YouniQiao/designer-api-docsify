# queryAppStatsInfos (System API)

## Modules to Import

```TypeScript
import { usageStatistics } from 'kits/@kit.BackgroundTasksKit';
```

## queryAppStatsInfos

```TypeScript
function queryAppStatsInfos(begin: number, end: number): Promise<AppStatsMap>
```

Queries usage information about each application within a specified period.

This method queries usage information at the {@link #BY_OPTIMIZED} interval by default.

**Since:** 15

**Required permissions:** ohos.permission.BUNDLE_ACTIVE_INFO

<!--Device-usageStatistics-function queryAppStatsInfos(begin: long, end: long): Promise<AppStatsMap>--><!--Device-usageStatistics-function queryAppStatsInfos(begin: long, end: long): Promise<AppStatsMap>-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| begin | number | Yes |
| end | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;AppStatsMap&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [10000001](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000001-memory-operation-failure) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [10000002](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000002-ipc-parcel-write-failure) |
| [10000003](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000003-system-service-operation-failure) |
| [10000004](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000004-ipc-failure) |
| [10000006](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000006-failed-to-obtain-application-information) |
| [10000007](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000007-time-operation-failure) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { usageStatistics } from '@kit.BackgroundTasksKit';

usageStatistics.queryAppStatsInfos(0, 20000000000000).then((res:usageStatistics.AppStatsMap) => {
  console.info('queryAppStatsInfos promise success.');
  console.info('queryAppStatsInfos promise result ' + JSON.stringify(res));
}).catch((err: BusinessError) => {
  console.error('queryAppStatsInfos promise failed. code is: ' + err.code + ',message is: ' + err.message);
});
```
