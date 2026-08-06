# PreloadedUIExtensionAbilityDestroyedFn (System API)

```TypeScript
export type PreloadedUIExtensionAbilityDestroyedFn = (preloadId: int) => void
```

Defines the callback function when the preloaded  
[UIExtensionAbility]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ instance is destroyed.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-abilityManager-export type PreloadedUIExtensionAbilityDestroyedFn = (preloadId: int) => void--><!--Device-abilityManager-export type PreloadedUIExtensionAbilityDestroyedFn = (preloadId: int) => void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| preloadId | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | The preload UIExtensionAbility ID.  |

