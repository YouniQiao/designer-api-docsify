# OnWindowStageRestoreFn

```TypeScript
type OnWindowStageRestoreFn = (ability: UIAbility, windowStage: window.WindowStage) => void
```

Defines a onWindowStageRestore function.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-type OnWindowStageRestoreFn = (ability: UIAbility, windowStage: window.WindowStage) => void--><!--Device-unnamed-type OnWindowStageRestoreFn = (ability: UIAbility, windowStage: window.WindowStage) => void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | Yes | Indicates the ability to register for listening. |
| windowStage | window.WindowStage | Yes | window stage to create |

