# setPowerSaveMode

## Modules to Import

```TypeScript
import { backgroundProcessManager } from 'kits/@kit.BackgroundTasksKit';
```

## setPowerSaveMode

```TypeScript
function setPowerSaveMode(pid: int, powerSaveMode: PowerSaveMode): Promise<void>
```

设置进程的能效模式，使用Promise异步回调。

当应用满足以下条件时，可以设置自身是否进入能效模式：

- 应用未获取系统焦点，未执行音频或界面刷新操作。  
- 无法通过框架层获取电源锁。  
- 应用需要执行压缩、解压缩、编译等耗时较长的计算任务，不希望这些任务受到显著的CPU资源限制（即被迫进入能效模式）。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.BACKGROUND_MANAGER_POWER_SAVE_MODE

<!--Device-backgroundProcessManager-function setPowerSaveMode(pid: int, powerSaveMode: PowerSaveMode): Promise<void>--><!--Device-backgroundProcessManager-function setPowerSaveMode(pid: int, powerSaveMode: PowerSaveMode): Promise<void>-End-->

**System capability:** SystemCapability.Resourceschedule.BackgroundProcessManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pid | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 进程号。 |
| powerSaveMode | [PowerSaveMode](arkts-backgroundtasks-backgroundprocessmanager-powersavemode-e.md) | Yes | 能效模式。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 31800004 | The setting failed due to system scheduling reasons. |
| 801 | Capability not supported. |
| 31800003 | Setup error, This setting is overridden by settings in Task Manager |
| 31800002 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified; &lt;br&gt; 2. Incorrect parameter types; 3. PowerSaveMode status is out of range. |
| 201 | Permission denied. |

## Examples

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

