# getExemptedApps (System API)

## Modules to Import

```TypeScript
import { deviceStandby } from 'kits/@kit.BackgroundTasksKit';
```

## getExemptedApps

```TypeScript
function getExemptedApps(resourceTypes: number, callback: AsyncCallback<Array<ExemptedAppInfo>>): void
```

Returns the information about the specified exempted application.

**Since:** 10

**Required permissions:** ohos.permission.DEVICE_STANDBY_EXEMPTION

**System capability:** SystemCapability.ResourceSchedule.DeviceStandby

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resourceTypes | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[ExemptedAppInfo](arkts-backgroundtasks-devicestandby-exemptedappinfo-i-sys.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9800001](../errorcode-backgroundTaskMgr.md#9800001-memory-operation-failure) |
| [9800002](../errorcode-backgroundTaskMgr.md#9800002-parcel-operation-failure) |
| [9800003](../errorcode-backgroundTaskMgr.md#9800003-ipc-failure) |
| [9800004](../errorcode-backgroundTaskMgr.md#9800004-system-service-failure) |
| [18700001](../errorcode-backgroundTaskMgr.md#18700001-caller-information-verification-failure-for-an-energy-resource-request) |


## getExemptedApps

```TypeScript
function getExemptedApps(resourceTypes: number): Promise<Array<ExemptedAppInfo>>
```

Returns the information about the specified exempted application.

**Since:** 10

**Required permissions:** ohos.permission.DEVICE_STANDBY_EXEMPTION

**System capability:** SystemCapability.ResourceSchedule.DeviceStandby

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resourceTypes | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[ExemptedAppInfo](arkts-backgroundtasks-devicestandby-exemptedappinfo-i-sys.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9800001](../errorcode-backgroundTaskMgr.md#9800001-memory-operation-failure) |
| [9800002](../errorcode-backgroundTaskMgr.md#9800002-parcel-operation-failure) |
| [9800003](../errorcode-backgroundTaskMgr.md#9800003-ipc-failure) |
| [9800004](../errorcode-backgroundTaskMgr.md#9800004-system-service-failure) |
| [18700001](../errorcode-backgroundTaskMgr.md#18700001-caller-information-verification-failure-for-an-energy-resource-request) |
