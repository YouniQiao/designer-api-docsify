# getPowerSaveMode

## Modules to Import

```TypeScript
import { backgroundProcessManager } from '@kit.BackgroundTasksKit';
```

## getPowerSaveMode

```TypeScript
function getPowerSaveMode(pid: int): Promise<PowerSaveMode>
```

Obtains the power saving mode of a process. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.BACKGROUND_MANAGER_POWER_SAVE_MODE

<!--Device-backgroundProcessManager-function getPowerSaveMode(pid: int): Promise<PowerSaveMode>--><!--Device-backgroundProcessManager-function getPowerSaveMode(pid: int): Promise<PowerSaveMode>-End-->

**System capability:** SystemCapability.Resourceschedule.BackgroundProcessManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pid | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Process ID.&lt;br&gt;Value range: any integer greater than 0. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[PowerSaveMode](arkts-backgroundtasks-backgroundprocessmanager-powersavemode-e.md)&gt; | Promise that returns the power saving mode of a process. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [31800002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-backgroundtasks-kit/errorcode-backgroundProcessManager.md#31800002-invalid-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |

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

