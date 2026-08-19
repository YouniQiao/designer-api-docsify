# queryBundleStatsInfoByInterval (System API)

## Modules to Import

```TypeScript
import { usageStatistics } from '@kit.BackgroundTasksKit';
```

## queryBundleStatsInfoByInterval

```TypeScript
function queryBundleStatsInfoByInterval(
    byInterval: IntervalType,
    begin: long,
    end: long,
    callback: AsyncCallback<Array<BundleStatsInfo>>
  ): void
```

Queries usage information about each bundle within a specified period at a specified interval.

**Since:** 23

**Required permissions:** ohos.permission.BUNDLE_ACTIVE_INFO

<!--Device-usageStatistics-function queryBundleStatsInfoByInterval(    byInterval: IntervalType,    begin: long,    end: long,    callback: AsyncCallback<Array<BundleStatsInfo>>  ): void--><!--Device-usageStatistics-function queryBundleStatsInfoByInterval(    byInterval: IntervalType,    begin: long,    end: long,    callback: AsyncCallback<Array<BundleStatsInfo>>  ): void-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byInterval | IntervalType | Yes | Indicates the interval at which the usage statistics are queried. The value can be BY_OPTIMIZED, BY_DAILY, BY_WEEKLY, BY_MONTHLY, or BY_ANNUALLY. |
| begin | long | Yes | Indicates the start time of the query period, in milliseconds. <br> Unit:ms |
| end | long | Yes | Indicates the end time of the query period, in milliseconds. <br> Unit:ms |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;Array&lt;BundleStatsInfo&gt;&gt; | Yes | Callback used to return the result. If the query is successful, **err** is **undefined**, and data is the list of [BundleStatsInfo](arkts-backgroundtasks-usagestatistics-bundlestatsinfo-i-sys.md) objects containing the usage information about each bundle. Otherwise, **err** is an error object. |

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

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

usageStatistics.queryBundleStatsInfoByInterval(0, 0, 20000000000000, (err: BusinessError, res: Array<usageStatistics.BundleStatsInfo>) => {
  if (err) {
    console.error('BUNDLE_ACTIVE queryBundleStatsInfoByInterval callback failed. code is: ' + err.code + ',message is: ' + err.message);
  } else {
    console.info('BUNDLE_ACTIVE queryBundleStatsInfoByInterval callback success.');
    for (let i = 0; i < res.length; i++) {
      console.info('BUNDLE_ACTIVE queryBundleStatsInfoByInterval callback number : ' + (i + 1));
      console.info('BUNDLE_ACTIVE queryBundleStatsInfoByInterval callback result ' + JSON.stringify(res[i]));
    }
  }
});
```


## queryBundleStatsInfoByInterval

```TypeScript
function queryBundleStatsInfoByInterval(
    byInterval: IntervalType,
    begin: long,
    end: long
  ): Promise<Array<BundleStatsInfo>>
```

Queries usage information about each bundle within a specified period at a specified interval.

**Since:** 23

**Required permissions:** ohos.permission.BUNDLE_ACTIVE_INFO

<!--Device-usageStatistics-function queryBundleStatsInfoByInterval(    byInterval: IntervalType,    begin: long,    end: long  ): Promise<Array<BundleStatsInfo>>--><!--Device-usageStatistics-function queryBundleStatsInfoByInterval(    byInterval: IntervalType,    begin: long,    end: long  ): Promise<Array<BundleStatsInfo>>-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byInterval | IntervalType | Yes | Indicates the interval at which the usage statistics are queried. The value can be BY_OPTIMIZED, BY_DAILY, BY_WEEKLY, BY_MONTHLY, or BY_ANNUALLY. |
| begin | long | Yes | Indicates the start time of the query period, in milliseconds. <br> Unit:ms |
| end | long | Yes | Indicates the end time of the query period, in milliseconds. <br> Unit:ms |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;BundleStatsInfo&gt;&gt; | Promise used to return the usage information about each bundle. |

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

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

usageStatistics.queryBundleStatsInfoByInterval(0, 0, 20000000000000).then((res: Array<usageStatistics.BundleStatsInfo>) => {
  console.info('BUNDLE_ACTIVE queryBundleStatsInfoByInterval promise success.');
  for (let i = 0; i < res.length; i++) {
    console.info('BUNDLE_ACTIVE queryBundleStatsInfoByInterval promise number : ' + (i + 1));
    console.info('BUNDLE_ACTIVE queryBundleStatsInfoByInterval promise result ' + JSON.stringify(res[i]));
  }
}).catch((err: BusinessError) => {
  console.error('BUNDLE_ACTIVE queryBundleStatsInfoByInterval promise failed. code is: ' + err.code + ',message is: ' + err.message);
});
```

