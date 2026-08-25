# queryBundleStatsInfoByInterval (System API)

## Modules to Import

```TypeScript
import { usageStatistics } from 'kits/@kit.BackgroundTasksKit';
```

## queryBundleStatsInfoByInterval

```TypeScript
function queryBundleStatsInfoByInterval(
    byInterval: IntervalType,
    begin: number,
    end: number,
    callback: AsyncCallback<Array<BundleStatsInfo>>
  ): void
```

Queries usage information about each bundle within a specified period at a specified interval.

**Since:** 9

**Required permissions:** ohos.permission.BUNDLE_ACTIVE_INFO

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| byInterval | [IntervalType](arkts-backgroundtasks-bundlestate-intervaltype-e.md) | Yes |
| begin | number | Yes |
| end | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;BundleStatsInfo&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [10000001](../errorcode-DeviceUsageStatistics.md#10000001-memory-operation-failure) |
| [10000002](../errorcode-DeviceUsageStatistics.md#10000002-ipc-parcel-write-failure) |
| [10000003](../errorcode-DeviceUsageStatistics.md#10000003-system-service-operation-failure) |
| [10000004](../errorcode-DeviceUsageStatistics.md#10000004-ipc-failure) |
| [10000006](../errorcode-DeviceUsageStatistics.md#10000006-failed-to-obtain-application-information) |
| [10000007](../errorcode-DeviceUsageStatistics.md#10000007-time-operation-failure) |


## queryBundleStatsInfoByInterval

```TypeScript
function queryBundleStatsInfoByInterval(
    byInterval: IntervalType,
    begin: number,
    end: number
  ): Promise<Array<BundleStatsInfo>>
```

Queries usage information about each bundle within a specified period at a specified interval.

**Since:** 9

**Required permissions:** ohos.permission.BUNDLE_ACTIVE_INFO

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| byInterval | [IntervalType](arkts-backgroundtasks-bundlestate-intervaltype-e.md) | Yes |
| begin | number | Yes |
| end | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;BundleStatsInfo & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [10000001](../errorcode-DeviceUsageStatistics.md#10000001-memory-operation-failure) |
| [10000002](../errorcode-DeviceUsageStatistics.md#10000002-ipc-parcel-write-failure) |
| [10000003](../errorcode-DeviceUsageStatistics.md#10000003-system-service-operation-failure) |
| [10000004](../errorcode-DeviceUsageStatistics.md#10000004-ipc-failure) |
| [10000006](../errorcode-DeviceUsageStatistics.md#10000006-failed-to-obtain-application-information) |
| [10000007](../errorcode-DeviceUsageStatistics.md#10000007-time-operation-failure) |
