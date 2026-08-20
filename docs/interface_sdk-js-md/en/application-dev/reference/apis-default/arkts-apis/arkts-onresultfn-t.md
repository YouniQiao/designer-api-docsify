# OnResultFn

```TypeScript
type OnResultFn = (parameter: AbilityResult) => void
```

Called when the UIExtensionAbility is terminated.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type OnResultFn = (parameter: AbilityResult) => void--><!--Device-unnamed-type OnResultFn = (parameter: AbilityResult) => void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| parameter | [AbilityResult](../../apis-ability-kit/arkts-apis/arkts-ability-abilityresult-abilityresult-i.md) | Yes | Result returned when [terminateSelfWithResult](../../apis-ability-kit/arkts-apis/arkts-ability-uiextensioncontext-c.md#terminateselfwithresult) is called to terminate the UIExtensionAbility. |

