# queryBundleStatsInfos (System API)

## Modules to Import

```TypeScript
import { usageStatistics } from 'usageStatistics';
```

## queryBundleStatsInfos

```TypeScript
function queryBundleStatsInfos(begin: long, end: long, callback: AsyncCallback<BundleStatsMap>): void
```

Queries usage information about each bundle within a specified period. This method queries usage information at the BY_OPTIMIZED interval by default.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.BUNDLE_ACTIVE_INFO

<!--Device-usageStatistics-function queryBundleStatsInfos(begin: long, end: long, callback: AsyncCallback<BundleStatsMap>): void--><!--Device-usageStatistics-function queryBundleStatsInfos(begin: long, end: long, callback: AsyncCallback<BundleStatsMap>): void-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| begin | long | Yes | Indicates the start time of the query period, in milliseconds. <br> Unit:ms |
| end | long | Yes | Indicates the end time of the query period, in milliseconds. <br> Unit:ms |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[BundleStatsMap](arkts-backgroundtasks-usagestatistics-bundlestatsmap-t-sys.md)&gt; | Yes | Callback used to return the result. If the query is successful, **err** is **undefined**, and data is the [BundleStatsMap](arkts-backgroundtasks-usagestatistics-bundlestatsmap-t-sys.md#BundleStatsMap-(System-API)) objects containing the usage information about each bundle. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible cause: Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [10000001](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000001-memory-operation-failure) | Memory operation failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |
| [10000002](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000002-ipc-parcel-write-failure) | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; <br> 2. Failed to apply for memory. |
| [10000003](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000003-system-service-operation-failure) | Failed to get system ability manager. |
| [10000004](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000004-ipc-failure) | Failed to access the device usage service. |
| [10000006](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000006-failed-to-obtain-application-information) | Failed to get the application information. |
| [10000007](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000007-time-operation-failure) | Failed to get the system time. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

usageStatistics.queryBundleStatsInfos(0, 20000000000000, (err: BusinessError, res:usageStatistics.BundleStatsMap) => {
  if (err) {
    console.error('BUNDLE_ACTIVE queryBundleStatsInfos callback failed. code is: ' + err.code + ',message is: ' + err.message);
  } else {
    console.info('BUNDLE_ACTIVE queryBundleStatsInfos callback success.');
    console.info('BUNDLE_ACTIVE queryBundleStatsInfos callback result ' + JSON.stringify(res));
  }
});
```


## queryBundleStatsInfos

```TypeScript
function queryBundleStatsInfos(begin: long, end: long): Promise<BundleStatsMap>
```

Queries usage information about each bundle within a specified period. This method queries usage information at the BY_OPTIMIZED interval by default.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.BUNDLE_ACTIVE_INFO

<!--Device-usageStatistics-function queryBundleStatsInfos(begin: long, end: long): Promise<BundleStatsMap>--><!--Device-usageStatistics-function queryBundleStatsInfos(begin: long, end: long): Promise<BundleStatsMap>-End-->

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
| Promise&lt;[BundleStatsMap](arkts-backgroundtasks-usagestatistics-bundlestatsmap-t-sys.md)&gt; | the promise returned by queryBundleStatsInfos. the { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible cause: Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [10000001](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000001-memory-operation-failure) | Memory operation failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |
| [10000002](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000002-ipc-parcel-write-failure) | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; <br> 2. Failed to apply for memory. |
| [10000003](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000003-system-service-operation-failure) | Failed to get system ability manager. |
| [10000004](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000004-ipc-failure) | Failed to access the device usage service. |
| [10000006](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000006-failed-to-obtain-application-information) | Failed to get the application information. |
| [10000007](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000007-time-operation-failure) | Failed to get the system time. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

usageStatistics.queryBundleStatsInfos(0, 20000000000000).then((res:usageStatistics.BundleStatsMap) => {
  console.info('BUNDLE_ACTIVE queryBundleStatsInfos promise success.');
  console.info('BUNDLE_ACTIVE queryBundleStatsInfos promise result ' + JSON.stringify(res));
}).catch((err: BusinessError) => {
  console.error('BUNDLE_ACTIVE queryBundleStatsInfos promise failed. code is: ' + err.code + ',message is: ' + err.message);
});
```

