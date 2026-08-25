# offPreloadedUIExtensionAbilityDestroyed (System API)

## Modules to Import

```TypeScript
import { abilityManager } from 'kits/@kit.AbilityKit';
```

## offPreloadedUIExtensionAbilityDestroyed

```TypeScript
function offPreloadedUIExtensionAbilityDestroyed(callback?: PreloadedUIExtensionAbilityDestroyedFn): void
```

Unsubscribes from loaded events of a preloaded [UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md) instance in the current process.

**Since:** 23

**Required permissions:** ohos.permission.PRELOAD_UI_EXTENSION_ABILITY

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [PreloadedUIExtensionAbilityDestroyedFn](arkts-ability-abilitymanager-preloadeduiextensionabilitydestroyedfn-t-sys.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
