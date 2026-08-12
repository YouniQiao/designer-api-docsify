# queryBundleStatsInfos (System API)

## Modules to Import

```TypeScript
import { usageStatistics } from '@kit.BackgroundTasksKit';
```

## queryBundleStatsInfos

```TypeScript
function queryBundleStatsInfos(begin: long, end: long, callback: AsyncCallback<BundleStatsMap>): void
```

Queries usage information about each bundle within a specified period.

This method queries usage information at the [BY_OPTIMIZED](#BY_OPTIMIZED) interval by default.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.BUNDLE_ACTIVE_INFO

<!--Device-usageStatistics-function queryBundleStatsInfos(begin: long, end: long, callback: AsyncCallback<BundleStatsMap>): void--><!--Device-usageStatistics-function queryBundleStatsInfos(begin: long, end: long, callback: AsyncCallback<BundleStatsMap>): void-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| begin | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | Indicates the start time of the query period, in milliseconds. &lt;br&gt; Unit:ms |
| end | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | Indicates the end time of the query period, in milliseconds. &lt;br&gt; Unit:ms |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[BundleStatsMap](arkts-backgroundtasks-usagestatistics-bundlestatsmap-t-sys.md)&gt; | Yes | Callback used to return the result. If the query is successful, **err** is **undefined**, and data is the [BundleStatsMap](arkts-backgroundtasks-usagestatistics-bundlestatsmap-t-sys.md#BundleStatsMap) objects containing the usage information about each bundle. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible cause: Parameter verification failed. |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [10000001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000001-memory-operation-failure) | Memory operation failed. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |
| [10000002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000002-ipc-parcel-write-failure) | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; &lt;br&gt; 2. Failed to apply for memory. |
| [10000003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000003-system-service-operation-failure) | Failed to get system ability manager. |
| [10000004](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000004-ipc-failure) | Failed to access the device usage service. |
| [10000006](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000006-failed-to-obtain-application-information) | Failed to get the application information. |
| [10000007](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000007-time-operation-failure) | Failed to get the system time. |

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

Queries usage information about each bundle within a specified period.

This method queries usage information at the [BY_OPTIMIZED](#BY_OPTIMIZED) interval by default.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.BUNDLE_ACTIVE_INFO

<!--Device-usageStatistics-function queryBundleStatsInfos(begin: long, end: long): Promise<BundleStatsMap>--><!--Device-usageStatistics-function queryBundleStatsInfos(begin: long, end: long): Promise<BundleStatsMap>-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| begin | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | Indicates the start time of the query period, in milliseconds. &lt;br&gt; Unit:ms |
| end | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | Indicates the end time of the query period, in milliseconds. &lt;br&gt; Unit:ms |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[BundleStatsMap](arkts-backgroundtasks-usagestatistics-bundlestatsmap-t-sys.md)&gt; | the promise returned by queryBundleStatsInfos. the { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible cause: Parameter verification failed. |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [10000001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000001-memory-operation-failure) | Memory operation failed. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |
| [10000002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000002-ipc-parcel-write-failure) | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; &lt;br&gt; 2. Failed to apply for memory. |
| [10000003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000003-system-service-operation-failure) | Failed to get system ability manager. |
| [10000004](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000004-ipc-failure) | Failed to access the device usage service. |
| [10000006](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000006-failed-to-obtain-application-information) | Failed to get the application information. |
| [10000007](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000007-time-operation-failure) | Failed to get the system time. |

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

