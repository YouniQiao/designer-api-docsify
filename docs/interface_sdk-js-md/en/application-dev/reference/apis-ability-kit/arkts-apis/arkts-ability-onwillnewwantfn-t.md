# OnWillNewWantFn

```TypeScript
type OnWillNewWantFn = (ability: UIAbility) => void
```

注册监听应用上下文的生命周期后，在UIAbility的onNewWant触发前回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-type OnWillNewWantFn = (ability: UIAbility) => void--><!--Device-unnamed-type OnWillNewWantFn = (ability: UIAbility) => void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | Yes | 当前Ability对象。 |

