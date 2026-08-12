# OnResultFn

```TypeScript
type OnResultFn = (parameter: AbilityResult) => void
```

拉起UIExtensionAbility终止时的回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-unnamed-type OnResultFn = (parameter: AbilityResult) => void--><!--Device-unnamed-type OnResultFn = (parameter: AbilityResult) => void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| parameter | [AbilityResult](arkts-ability-abilityresult-abilityresult-i.md) | 是 | 当调用 [terminateSelfWithResult](arkts-ability-uiextensioncontext-c.md#terminateSelfWithResult) 方法终止UIExtensionAbility时返回的结果。 |

