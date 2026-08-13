# OnWindowStageWillDestroyFn

```TypeScript
type OnWindowStageWillDestroyFn = (ability: UIAbility, windowStage: window.WindowStage) => void
```

Defines a onWindowStageWillDestroy function.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-type OnWindowStageWillDestroyFn = (ability: UIAbility, windowStage: window.WindowStage) => void--><!--Device-unnamed-type OnWindowStageWillDestroyFn = (ability: UIAbility, windowStage: window.WindowStage) => void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | Yes | Indicates the ability to register for listening. |
| windowStage | window.WindowStage | Yes | window stage to create |

