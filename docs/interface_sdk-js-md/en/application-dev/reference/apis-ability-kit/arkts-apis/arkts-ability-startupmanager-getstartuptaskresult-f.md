# getStartupTaskResult

## Modules to Import

```TypeScript
import { startupManager } from 'kits/@kit.AbilityKit';
```

## getStartupTaskResult

```TypeScript
function getStartupTaskResult(startupTask: string): Object
```

获取指定启动任务或so预加载任务的执行结果。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-startupManager-function getStartupTaskResult(startupTask: string): Object--><!--Device-startupManager-function getStartupTaskResult(startupTask: string): Object-End-->

**System capability:** SystemCapability.Ability.AppStartup

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| startupTask | string | Yes | 启动任务[StartupTask](arkts-ability-app-appstartup-startuptask-startuptask-c.md)的名称或预加载so名称。 |

**Return value:**

| Type | Description |
| --- | --- |
| Object | 输入为启动任务名时，返回指定的启动任务 [init]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

## Examples

```TypeScript
import { AbilityConstant, UIAbility, Want, startupManager } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
    try {
      startupManager.run(['StartupTask_001']).then(() => {
        hilog.info(0x0000, 'testTag', 'StartupTask_001 init successful');
      }).catch((error: BusinessError) => {
        hilog.error(0x0000, 'testTag', `StartupTask_001 promise catch failed, error: %{public}s`,
          JSON.stringify(error) ?? '');
      });
    } catch (error) {
      hilog.error(0x0000, 'testTag', `StartupTask_001.run failed, error: %{public}s`, JSON.stringify(error) ?? '');
    }
  }

  onWindowStageCreate(windowStage: window.WindowStage) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
    let result = startupManager.getStartupTaskResult('StartupTask_001'); // Manually obtain the startup task result.
    hilog.info(0x0000, 'testTag', 'getStartupTaskResult result = %{public}s', result);
    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
        return;
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
    });
  }
}
```


## getStartupTaskResult

```TypeScript
function getStartupTaskResult(startupTask: string): Any
```

获取指定启动任务或so预加载任务的执行结果。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-startupManager-function getStartupTaskResult(startupTask: string): Any--><!--Device-startupManager-function getStartupTaskResult(startupTask: string): Any-End-->

**System capability:** SystemCapability.Ability.AppStartup

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| startupTask | string | Yes | 启动任务[StartupTask](arkts-ability-app-appstartup-startuptask-startuptask-c.md)的名称或预加载so名称。 |

**Return value:**

| Type | Description |
| --- | --- |
| Any | The result of specific startup task. |

