# OnResultFn (System API)

```TypeScript
type OnResultFn = (parameter: AbilityResult) => void
```

Defines a onResult function.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type OnResultFn = (parameter: AbilityResult) => void--><!--Device-unnamed-type OnResultFn = (parameter: AbilityResult) => void-End-->

**System capability:** SystemCapability.Ability.AppExtension.VerticalPanel

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| parameter | [AbilityResult](arkts-ability-abilityresult-abilityresult-i.md) | Yes | The Parameter returned if the UIExtensionAbility call terminateSelfWithResult. |

