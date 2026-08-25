# PreloadedUIExtensionAbilityLoadedFn（系统接口）

```TypeScript
export type PreloadedUIExtensionAbilityLoadedFn = (preloadId: int) => void
```

预加载[UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md)被加载时的回调函数类型。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| preloadId | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
