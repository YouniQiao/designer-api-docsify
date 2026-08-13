# getStartupTaskResult

## Modules to Import

```TypeScript
import { startupManager } from '@kit.AbilityKit';
```

## getStartupTaskResult

```TypeScript
function getStartupTaskResult(startupTask: string): Object
```

Obtains the execution result of a startup task or .so file preloading task.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-startupManager-function getStartupTaskResult(startupTask: string): Object--><!--Device-startupManager-function getStartupTaskResult(startupTask: string): Object-End-->

**System capability:** SystemCapability.Ability.AppStartup

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| startupTask | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Object |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

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

Obtains specific startup task result.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-startupManager-function getStartupTaskResult(startupTask: string): Any--><!--Device-startupManager-function getStartupTaskResult(startupTask: string): Any-End-->

**System capability:** SystemCapability.Ability.AppStartup

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| startupTask | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Any |
