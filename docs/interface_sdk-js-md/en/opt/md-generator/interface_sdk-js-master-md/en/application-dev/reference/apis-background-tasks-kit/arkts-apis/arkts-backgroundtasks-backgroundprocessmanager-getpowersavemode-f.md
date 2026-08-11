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

<!--Device-backgroundProcessManager-function getPowerSaveMode(pid: int): Promise<PowerSaveMode>--><!--Device-backgroundProcessManager-function getPowerSaveMode(pid: int): Promise<PowerSaveMode>-End-->

**System capability:** SystemCapability.Resourceschedule.BackgroundProcessManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pid | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;PowerSaveMode&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [31800002](../../apis-backgroundtasks-kit/errorcode-backgroundProcessManager.md#31800002-invalid-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { backgroundProcessManager } from '@kit.BackgroundTasksKit';
// Replace the process ID with the actual one.
let pid = 33333;
try {
    backgroundProcessManager.getPowerSaveMode(pid).then((result: backgroundProcessManager.PowerSaveMode) => {
        console.info("getPowerSaveMode: " + result.toString());
    });
} catch (error) {
    console.error(`getPowerSaveMode failed, errCode: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
}
```
