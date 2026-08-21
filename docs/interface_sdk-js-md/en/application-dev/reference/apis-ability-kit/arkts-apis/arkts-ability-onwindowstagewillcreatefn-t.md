# OnWindowStageWillCreateFn

```TypeScript
type OnWindowStageWillCreateFn = (ability: UIAbility, windowStage: window.WindowStage) => void
```

Defines a onWindowStageWillCreate function.

**Since:** 23

<!--Device-unnamed-type OnWindowStageWillCreateFn = (ability: UIAbility, windowStage: window.WindowStage) => void--><!--Device-unnamed-type OnWindowStageWillCreateFn = (ability: UIAbility, windowStage: window.WindowStage) => void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-appabilityuiability-uiability-c.md) | Yes | Indicates the ability to register for listening. |
| windowStage | window.WindowStage | Yes | window stage to create |

