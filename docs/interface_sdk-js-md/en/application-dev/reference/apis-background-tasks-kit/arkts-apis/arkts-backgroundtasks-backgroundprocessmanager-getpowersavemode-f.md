# getPowerSaveMode

## Modules to Import

```TypeScript
import { backgroundProcessManager } from 'kits/@kit.BackgroundTasksKit';
```

## getPowerSaveMode

```TypeScript
function getPowerSaveMode(pid: number): Promise<PowerSaveMode>
```

Obtains the power saving mode of a process. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.BACKGROUND_MANAGER_POWER_SAVE_MODE

**System capability:** SystemCapability.Resourceschedule.BackgroundProcessManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pid | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[PowerSaveMode](arkts-backgroundtasks-backgroundprocessmanager-powersavemode-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [31800002](../errorcode-backgroundProcessManager.md#31800002-invalid-parameter) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
