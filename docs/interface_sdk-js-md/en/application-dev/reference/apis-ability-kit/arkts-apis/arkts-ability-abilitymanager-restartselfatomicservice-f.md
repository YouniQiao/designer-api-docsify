# restartSelfAtomicService

## Modules to Import

```TypeScript
import { abilityManager } from 'kits/@kit.AbilityKit';
```

## restartSelfAtomicService

```TypeScript
function restartSelfAtomicService(context: Context): void
```

重启当前原子化服务。

> **说明：**
> 
> - 当前仅支持以独立窗口方式拉起原子化服务。
> 
> - 在调用本接口成功后的3秒内，再次调用本接口、
> [ApplicationContext.restartApp()](arkts-ability-applicationcontext-c.md#restartapp)或
> [UIAbilityContext.restartApp()](arkts-ability-uiabilitycontext-c.md#restartapp)接口中的任一接口，系统将返回错误码1
> 6000064。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-abilityManager-function restartSelfAtomicService(context: Context): void--><!--Device-abilityManager-function restartSelfAtomicService(context: Context): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](arkts-ability-context-c.md) | Yes | 当前Ability的上下文。&lt;br&gt;**说明：**当前仅支持 [UIAbilityContext](arkts-ability-uiabilitycontext-c.md)。&lt;/br&gt; |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000053 | The ability is not on the top of the UI. |
| 16000086 | The context is not UIAbilityContext. |
| 16000064 | Restart too frequently. Try again at least 3s later. |
| 16000050 | Internal error. Possible causes: 1. Connect to system service failed; 2.Send restart message to system service failed; 3.System service failed to communicate with dependency module. |
| 16000090 | The caller is not an atomic service. |

## Examples

```TypeScript
import { AbilityConstant, EmbeddableUIAbility, Want, abilityManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends EmbeddableUIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      abilityManager.restartSelfAtomicService(this.context);
    } catch (e) {
      console.error(`restartSelfAtomicService error: ${JSON.stringify(e as BusinessError)}`);
    }
  }
}
```

