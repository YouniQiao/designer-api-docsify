# queryAppStatsInfos (System API)

## Modules to Import

```TypeScript
import { usageStatistics } from '@kit.BackgroundTasksKit';
```

## queryAppStatsInfos

```TypeScript
function queryAppStatsInfos(begin: long, end: long): Promise<AppStatsMap>
```

Queries usage information about each application within a specified period.This method queries usage information at the BY_OPTIMIZED interval by default.

**Since:** 23

**Required permissions:** ohos.permission.BUNDLE_ACTIVE_INFO

<!--Device-usageStatistics-function queryAppStatsInfos(begin: long, end: long): Promise<AppStatsMap>--><!--Device-usageStatistics-function queryAppStatsInfos(begin: long, end: long): Promise<AppStatsMap>-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| begin | long | Yes | Indicates the start time of the query period, in milliseconds. <br> Unit:ms |
| end | long | Yes | Indicates the end time of the query period, in milliseconds. <br> Unit:ms |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[AppStatsMap](arkts-backgroundtasks-usagestatistics-appstatsmap-t-sys.md)&gt; | the promise returned by queryAppStatsInfos. the { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible cause: Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [10000001](../errorcode-DeviceUsageStatistics.md#10000001-memory-operation-failure) | Memory operation failed. |
| [10000002](../errorcode-DeviceUsageStatistics.md#10000002-ipc-parcel-write-failure) | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; <br> 2. Failed to apply for memory. |
| [10000003](../errorcode-DeviceUsageStatistics.md#10000003-system-service-operation-failure) | Failed to get system ability manager. |
| [10000004](../errorcode-DeviceUsageStatistics.md#10000004-ipc-failure) | Failed to access the device usage service. |
| [10000006](../errorcode-DeviceUsageStatistics.md#10000006-failed-to-obtain-application-information) | Failed to get the application information. |
| [10000007](../errorcode-DeviceUsageStatistics.md#10000007-time-operation-failure) | Failed to get the system time. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

usageStatistics.queryAppStatsInfos(0, 20000000000000).then((res:usageStatistics.AppStatsMap) => {
  console.info('queryAppStatsInfos promise success.');
  console.info('queryAppStatsInfos promise result ' + JSON.stringify(res));
}).catch((err: BusinessError) => {
  console.error('queryAppStatsInfos promise failed. code is: ' + err.code + ',message is: ' + err.message);
});
```

