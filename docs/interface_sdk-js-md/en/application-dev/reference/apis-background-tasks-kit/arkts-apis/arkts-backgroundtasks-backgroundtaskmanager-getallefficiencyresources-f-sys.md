# getAllEfficiencyResources (System API)

## Modules to Import

```TypeScript
import { backgroundTaskManager } from 'kits/@kit.BackgroundTasksKit';
```

## getAllEfficiencyResources

```TypeScript
function getAllEfficiencyResources(): Promise<EfficiencyResourcesInfo[]>
```

Obtains all information about the requested efficiency resources, including the resource type. This API uses a promise to return the result.

**Since:** 20

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.EfficiencyResourcesApply

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[EfficiencyResourcesInfo](arkts-backgroundtasks-backgroundtaskmanager-efficiencyresourcesinfo-i-sys.md)[]&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [18700001](../errorcode-backgroundTaskMgr.md#18700001-caller-information-verification-failure-for-an-energy-resource-request) |
| [18700002](../errorcode-backgroundTaskMgr.md#18700002-parcel-operation-failure) |
| [18700004](../errorcode-backgroundTaskMgr.md#18700004-system-service-failure) |
