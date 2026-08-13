# OnWindowStageWillCreateFn

```TypeScript
type OnWindowStageWillCreateFn = (ability: UIAbility, windowStage: window.WindowStage) => void
```

注册监听应用上下文的生命周期后，在UIAbility的onWindowStageCreate触发前回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-unnamed-type OnWindowStageWillCreateFn = (ability: UIAbility, windowStage: window.WindowStage) => void--><!--Device-unnamed-type OnWindowStageWillCreateFn = (ability: UIAbility, windowStage: window.WindowStage) => void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 |
| [windowStage](arkts-ability-uiabilitycontext-c.md) | window.WindowStage | 是 |
