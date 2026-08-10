# saveAppState

## Modules to Import

```TypeScript
import { appRecovery } from 'kits/@kit.AbilityKit';
```

## saveAppState

```TypeScript
function saveAppState(): boolean
```

保存当前App状态，可以配合[errorManager](arkts-app-ability-errormanager.md)相关接口使用。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-appRecovery-function saveAppState(): boolean--><!--Device-appRecovery-function saveAppState(): boolean-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 保存成功与否。true：保存成功，false：保存失败。 |

## Examples

```TypeScript
import { appRecovery, errorManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let observer: errorManager.ErrorObserver = {
  onUnhandledException(errorMsg) {
    console.error('onUnhandledException, errorMsg: ', errorMsg);
    appRecovery.saveAppState();
  }
};

try {
  errorManager.on('error', observer);
} catch (paramError) {
  console.error(`error: ${(paramError as BusinessError).code}, ${(paramError as BusinessError).message}`);
}
```


## saveAppState

```TypeScript
function saveAppState(context?: UIAbilityContext): boolean
```

主动保存Ability的状态，这个状态将在下次恢复启动时使用。可以配合[errorManager](arkts-app-ability-errormanager.md)相关接口使用。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-appRecovery-function saveAppState(context?: UIAbilityContext): boolean--><!--Device-appRecovery-function saveAppState(context?: UIAbilityContext): boolean-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIAbilityContext](arkts-ability-uiabilitycontext-c.md) | No | 需要保存状态的UIAbility所对应的context。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 保存成功与否。true：保存成功，false：保存失败。 |

## Examples

```TypeScript
import { appRecovery, errorManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let observer: errorManager.ErrorObserver = {
  onUnhandledException(errorMsg) {
    console.error('onUnhandledException, errorMsg: ', errorMsg);
    appRecovery.saveAppState(this.context);
  }
};

try {
  errorManager.on('error', observer);
} catch (paramError) {
  console.error(`error: ${(paramError as BusinessError).code}, ${(paramError as BusinessError).message}`);
}
```

