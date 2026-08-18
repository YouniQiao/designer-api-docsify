# onPreloadedUIExtensionAbilityDestroyed (System API)

## Modules to Import

```TypeScript
```

## onPreloadedUIExtensionAbilityDestroyed

```TypeScript
function onPreloadedUIExtensionAbilityDestroyed(callback: PreloadedUIExtensionAbilityDestroyedFn): void
```

Subscribes to destroyed events of a preloaded [UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md#uiextensionability) instance in the current process.

**Since:** 23

**Required permissions:** ohos.permission.PRELOAD_UI_EXTENSION_ABILITY

**Model restriction:** This API can be used only in the stage model.

<!--Device-abilityManager-function onPreloadedUIExtensionAbilityDestroyed(callback: PreloadedUIExtensionAbilityDestroyedFn): void--><!--Device-abilityManager-function onPreloadedUIExtensionAbilityDestroyed(callback: PreloadedUIExtensionAbilityDestroyedFn): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [PreloadedUIExtensionAbilityDestroyedFn](arkts-ability-abilitymanager-preloadeduiextensionabilitydestroyedfn-t-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
import { abilityManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

function onPreloadDestroyed(preloadId: number) {
  console.info(`Preloaded UIExtensionAbility destroyed, preloadId: ${preloadId}`);
}

try {
  abilityManager.onPreloadedUIExtensionAbilityDestroyed(onPreloadDestroyed);
  console.info('onPreloadedUIExtensionAbilityDestroyed success.');
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(`onPreloadedUIExtensionAbilityDestroyed failed, code is ${code}, message is ${message}`);
}
```
