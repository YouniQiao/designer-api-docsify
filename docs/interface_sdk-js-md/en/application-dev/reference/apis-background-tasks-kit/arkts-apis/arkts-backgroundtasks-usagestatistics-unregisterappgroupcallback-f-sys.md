# unregisterAppGroupCallBack (System API)

## Modules to Import

```TypeScript
import { usageStatistics } from 'usageStatistics';
```

## unregisterAppGroupCallBack

```TypeScript
function unregisterAppGroupCallBack(callback: AsyncCallback<void>): void
```

Unregister appGroup change callback from service.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.BUNDLE_ACTIVE_INFO

<!--Device-usageStatistics-function unregisterAppGroupCallBack(callback: AsyncCallback<void>): void--><!--Device-usageStatistics-function unregisterAppGroupCallBack(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.AppGroup

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the cancellation of registration is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; <br> 2. Incorrect parameters types; 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [10000001](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000001-memory-operation-failure) | Memory operation failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |
| [10000002](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000002-ipc-parcel-write-failure) | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; <br> 2. Failed to apply for memory. |
| [10000003](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000003-system-service-operation-failure) | Failed to get system ability manager. |
| [10100001](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10100001-duplicate-application-group-operation) | Repeated operation on the application group. |
| [10000004](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000004-ipc-failure) | Failed to access the device usage service. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

usageStatistics.unregisterAppGroupCallBack((err: BusinessError) => {
  if(err) {
    console.error('BUNDLE_ACTIVE unregisterAppGroupCallBack callback failed. code is: ' + err.code + ',message is: ' + err.message);
  } else {
    console.info('BUNDLE_ACTIVE unregisterAppGroupCallBack callback success.');
  }
});
```


## unregisterAppGroupCallBack

```TypeScript
function unregisterAppGroupCallBack(): Promise<void>
```

Unregister appGroup change callback from service.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.BUNDLE_ACTIVE_INFO

<!--Device-usageStatistics-function unregisterAppGroupCallBack(): Promise<void>--><!--Device-usageStatistics-function unregisterAppGroupCallBack(): Promise<void>-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.AppGroup

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by unregisterAppGroupCallBack. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; <br> 2. Incorrect parameters types; 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [10000001](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000001-memory-operation-failure) | Memory operation failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |
| [10000002](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000002-ipc-parcel-write-failure) | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; <br> 2. Failed to apply for memory. |
| [10000003](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000003-system-service-operation-failure) | Failed to get system ability manager. |
| [10100001](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10100001-duplicate-application-group-operation) | Repeated operation on the application group. |
| [10000004](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000004-ipc-failure) | Failed to access the device usage service. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

usageStatistics.unregisterAppGroupCallBack().then( () => {
  console.info('BUNDLE_ACTIVE unregisterAppGroupCallBack promise succeeded.');
}).catch((err: BusinessError) => {
  console.error('BUNDLE_ACTIVE unregisterAppGroupCallBack promise failed. code is: ' + err.code + ',message is: ' + err.message);
});
```

