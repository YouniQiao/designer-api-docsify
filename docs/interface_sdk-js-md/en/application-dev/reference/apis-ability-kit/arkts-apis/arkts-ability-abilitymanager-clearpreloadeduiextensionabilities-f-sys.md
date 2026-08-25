# clearPreloadedUIExtensionAbilities (System API)

## Modules to Import

```TypeScript
import { abilityManager } from 'kits/@kit.AbilityKit';
```

## clearPreloadedUIExtensionAbilities

```TypeScript
function clearPreloadedUIExtensionAbilities(): Promise<void>
```

Clears all preloaded [UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md) instances in the current process. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.PRELOAD_UI_EXTENSION_ABILITY

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
