# releaseExemptionResource (System API)

## Modules to Import

```TypeScript
import { deviceStandby } from 'kits/@kit.BackgroundTasksKit';
```

## releaseExemptionResource

```TypeScript
function releaseExemptionResource(request: ResourceRequest): void
```

Releases exemption resources.

**Since:** 10

**Required permissions:** ohos.permission.DEVICE_STANDBY_EXEMPTION

**System capability:** SystemCapability.ResourceSchedule.DeviceStandby

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| request | [ResourceRequest](arkts-backgroundtasks-devicestandby-resourcerequest-i-sys.md) | Yes |

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
