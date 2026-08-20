# queryNotificationEventStats (System API)

## Modules to Import

```TypeScript
import { usageStatistics } from '@kit.BackgroundTasksKit';
```

## queryNotificationEventStats

```TypeScript
function queryNotificationEventStats(
    begin: long,
    end: long,
    callback: AsyncCallback<Array<DeviceEventStats>>
  ): void
```

Queries app notification number within a specified period identified by the start and end time.

**Since:** 23

**Required permissions:** ohos.permission.BUNDLE_ACTIVE_INFO

<!--Device-usageStatistics-function queryNotificationEventStats(    begin: long,    end: long,    callback: AsyncCallback<Array<DeviceEventStats>>  ): void--><!--Device-usageStatistics-function queryNotificationEventStats(    begin: long,    end: long,    callback: AsyncCallback<Array<DeviceEventStats>>  ): void-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| begin | long | Yes | Indicates the start time of the query period, in milliseconds. <br> Unit:ms |
| end | long | Yes | Indicates the end time of the query period, in milliseconds. <br> Unit:ms |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;Array&lt;[DeviceEventStats](arkts-backgroundtasks-usagestatistics-deviceeventstats-i-sys.md)&gt;&gt; | Yes | Callback used to return the result. If the query is successful, **err** is **undefined**, and data is the [DeviceEventStats](arkts-backgroundtasks-usagestatistics-deviceeventstats-i-sys.md) object Array containing the event states data. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; <br> 2. Incorrect parameters types; 3. Parameter verification failed. |
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

usageStatistics.queryNotificationEventStats(0, 20000000000000, (err: BusinessError, res: Array<usageStatistics.DeviceEventStats>) => {
  if(err) {
    console.error('BUNDLE_ACTIVE queryNotificationEventStats callback failed. code is: ' + err.code + ',message is: ' + err.message);
  } else {
    console.info('BUNDLE_ACTIVE queryNotificationEventStats callback success.');
    console.info('BUNDLE_ACTIVE queryNotificationEventStats callback result ' + JSON.stringify(res));
  }
});
```


## queryNotificationEventStats

```TypeScript
function queryNotificationEventStats(begin: long, end: long): Promise<Array<DeviceEventStats>>
```

Queries app notification number within a specified period identified by the start and end time.

**Since:** 23

**Required permissions:** ohos.permission.BUNDLE_ACTIVE_INFO

<!--Device-usageStatistics-function queryNotificationEventStats(begin: long, end: long): Promise<Array<DeviceEventStats>>--><!--Device-usageStatistics-function queryNotificationEventStats(begin: long, end: long): Promise<Array<DeviceEventStats>>-End-->

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
| Promise&lt;Array&lt;[DeviceEventStats](arkts-backgroundtasks-usagestatistics-deviceeventstats-i-sys.md)&gt;&gt; | the promise returned by queryNotificationEventStats. the { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; <br> 2. Incorrect parameters types; 3. Parameter verification failed. |
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

usageStatistics.queryNotificationEventStats(0, 20000000000000).then((res: Array<usageStatistics.DeviceEventStats>) => {
  console.info('BUNDLE_ACTIVE queryNotificationEventStats promise success.');
  console.info('BUNDLE_ACTIVE queryNotificationEventStats promise result ' + JSON.stringify(res));
}).catch((err: BusinessError) => {
  console.error('BUNDLE_ACTIVE queryNotificationEventStats promise failed. code is: ' + err.code + ',message is: ' + err.message);
});
```

