# OnResultFn

```TypeScript
type OnResultFn = (parameter: AbilityResult) => void
```

拉起UIExtensionAbility终止时的回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-type OnResultFn = (parameter: AbilityResult) => void--><!--Device-unnamed-type OnResultFn = (parameter: AbilityResult) => void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| parameter | [AbilityResult](arkts-ability-abilityresult-abilityresult-i.md) | Yes | 当调用 [terminateSelfWithResult](arkts-ability-uiextensioncontext-c.md#terminateselfwithresult) 方法终止UIExtensionAbility时返回的结果。 |

