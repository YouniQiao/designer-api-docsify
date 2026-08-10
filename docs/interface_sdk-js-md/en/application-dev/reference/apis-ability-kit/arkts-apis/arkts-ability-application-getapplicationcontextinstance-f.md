# getApplicationContextInstance

## Modules to Import

```TypeScript
import { application } from 'kits/@kit.AbilityKit';
```

## getApplicationContextInstance

```TypeScript
export function getApplicationContextInstance(): ApplicationContext
```

获取应用上下文。开发者使用该接口时，无需依赖Context基类。重复调用该接口，将获取同一个ApplicationContext实例。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-application-export function getApplicationContextInstance(): ApplicationContext--><!--Device-application-export function getApplicationContextInstance(): ApplicationContext-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| [ApplicationContext](arkts-ability-applicationcontext-c.md) | 应用上下文。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000050 | Internal error. Possible causes: Memory operation error. |

## Examples

```TypeScript
import { AbilityConstant, UIAbility, application, Want, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      let applicationContext: common.ApplicationContext = application.getApplicationContextInstance();
    } catch (error) {
      let code: number = (error as BusinessError).code;
      let message: string = (error as BusinessError).message;
      console.error(`getApplicationContextInstance failed, error.code: ${code}, error.message: ${message}`);
    }
  }
}
```

