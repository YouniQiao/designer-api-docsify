# PreloadedUIExtensionAbilityLoadedFn (System API)

```TypeScript
export type PreloadedUIExtensionAbilityLoadedFn = (preloadId: int) => void
```

预加载[UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md)被加载时的回调函数类型。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-abilityManager-export type PreloadedUIExtensionAbilityLoadedFn = (preloadId: int) => void--><!--Device-abilityManager-export type PreloadedUIExtensionAbilityLoadedFn = (preloadId: int) => void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| preloadId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | The preload UIExtensionAbility ID. |

