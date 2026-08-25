# unregisterAppGroupCallBack (System API)

## Modules to Import

```TypeScript
import { usageStatistics } from 'kits/@kit.BackgroundTasksKit';
```

## unregisterAppGroupCallBack

```TypeScript
function unregisterAppGroupCallBack(callback: AsyncCallback<void>): void
```

Unregister appGroup change callback from service.

**Since:** 9

**Required permissions:** ohos.permission.BUNDLE_ACTIVE_INFO

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.AppGroup

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

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
| [10100001](../errorcode-DeviceUsageStatistics.md#10100001-duplicate-application-group-operation) |


## unregisterAppGroupCallBack

```TypeScript
function unregisterAppGroupCallBack(): Promise<void>
```

Unregister appGroup change callback from service.

**Since:** 9

**Required permissions:** ohos.permission.BUNDLE_ACTIVE_INFO

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.AppGroup

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

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
| [10100001](../errorcode-DeviceUsageStatistics.md#10100001-duplicate-application-group-operation) |
