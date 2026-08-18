# setPowerSaveMode

## Modules to Import

```TypeScript
```

## setPowerSaveMode

```TypeScript
function setPowerSaveMode(pid: number, powerSaveMode: PowerSaveMode): Promise<void>
```

Sets the power saving mode for a process. This API uses a promise to return the result. You can set to enter the power saving mode when: - The application is not focused, and there are no audio operations or UI updates. - The application cannot obtain the power lock through the system framework. - The application needs to perform time-consuming computing tasks, such as compression, decompression, and compilation, which are significantly restricted by CPU resources. (In this case, the power saving mode will be enabled forcibly.)

**Since:** 23

**Required permissions:** ohos.permission.BACKGROUND_MANAGER_POWER_SAVE_MODE

<!--Device-backgroundProcessManager-function setPowerSaveMode(pid: int, powerSaveMode: PowerSaveMode): Promise<void>--><!--Device-backgroundProcessManager-function setPowerSaveMode(pid: int, powerSaveMode: PowerSaveMode): Promise<void>-End-->

**System capability:** SystemCapability.Resourceschedule.BackgroundProcessManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pid | number | Yes |
| powerSaveMode | [PowerSaveMode](arkts-backgroundtasks-backgroundprocessmanager-powersavemode-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [31800004](../../apis-backgroundtasks-kit/errorcode-backgroundProcessManager.md#31800004-setting-failure-due-to-system-scheduling) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [31800003](../../apis-backgroundtasks-kit/errorcode-backgroundProcessManager.md#31800003-setting-overriden-by-task-manager) |
| [31800002](../../apis-backgroundtasks-kit/errorcode-backgroundProcessManager.md#31800002-invalid-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { backgroundProcessManager } from '@kit.BackgroundTasksKit';

let pid = 33333;
try {
    backgroundProcessManager.setPowerSaveMode(pid, backgroundProcessManager.PowerSaveMode.EFFICIENCY_MODE); 
} catch (error) {
    console.error(`setPowerSaveMode failed, errCode: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
}
```
