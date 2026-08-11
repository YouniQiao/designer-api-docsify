# queryLastUseTime (System API)

## Modules to Import

```TypeScript
import { usageStatistics } from 'kits/@kit.BackgroundTasksKit';
```

## queryLastUseTime

```TypeScript
function queryLastUseTime(appInfo: Record<string, Array<long>>): Promise<AppStatsMap>
```

Queries the last usage timestamp by bundleName and app index.

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.BUNDLE_ACTIVE_INFO

<!--Device-usageStatistics-function queryLastUseTime(appInfo: Record<string, Array<long>>): Promise<AppStatsMap>--><!--Device-usageStatistics-function queryLastUseTime(appInfo: Record<string, Array<long>>): Promise<AppStatsMap>-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| appInfo | ArkTS-Dyn: [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Array&lt;number&gt;&gt;  <br>ArkTS-Sta：[Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Array&lt;long&gt;&gt; | Yes | bundle name and app index info for each application. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;AppStatsMap&gt; | the promise returned by queryLastUseTime. the { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible cause: Parameter verification failed. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [10000001](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000001-memory-operation-failure) | Memory operation failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |
| [10000002](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000002-ipc-parcel-write-failure) | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; &lt;br&gt; 2. Failed to apply for memory. |
| [10000003](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000003-system-service-operation-failure) | Failed to get system ability manager. |
| [10000004](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000004-ipc-failure) | Failed to access the device usage service. |
| [10000006](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000006-failed-to-obtain-application-information) | Failed to get the application information. |
| [10000007](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000007-time-operation-failure) | Failed to get the system time. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Replace com.ohos.camera with the actual bundle name.
usageStatistics.queryLastUseTime({"com.ohos.camera": [0]}).then((res:usageStatistics.AppStatsMap) => {
  console.info('queryLastUseTime promise success.');
  console.info('queryLastUseTime promise result ' + JSON.stringify(res));
}).catch((err: BusinessError) => {
  console.error('queryLastUseTime promise failed. code is: ' + err.code + ',message is: ' + err.message);
});
```

