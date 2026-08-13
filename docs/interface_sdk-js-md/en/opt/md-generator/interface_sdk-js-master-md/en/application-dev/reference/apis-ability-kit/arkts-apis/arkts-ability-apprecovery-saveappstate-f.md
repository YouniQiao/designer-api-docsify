# saveAppState

## Modules to Import

```TypeScript
import { appRecovery } from '@kit.AbilityKit';
```

## saveAppState

```TypeScript
function saveAppState(): boolean
```

Saves the application state. This API can be used together with the APIs of [errorManager](arkts-app-ability-errormanager.md#@ohos.app.ability.errorManager).

**Since:** 9

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-appRecovery-function saveAppState(): boolean--><!--Device-appRecovery-function saveAppState(): boolean-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

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

Saves the ability state, which will be used for recovery. This API can be used together with the APIs of [errorManager](arkts-app-ability-errormanager.md#@ohos.app.ability.errorManager).

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-appRecovery-function saveAppState(context?: UIAbilityContext): boolean--><!--Device-appRecovery-function saveAppState(context?: UIAbilityContext): boolean-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIAbilityContext](arkts-ability-uiabilitycontext-c.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

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
