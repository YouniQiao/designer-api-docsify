# OnFontSizeScaleUpdatedFn

```TypeScript
type OnFontSizeScaleUpdatedFn = (fontSizeScale: number) => void
```

在注册系统环境变化的监听后，当系统字体大小缩放比例变化时触发回调。

**起始版本：** 24

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-systemConfiguration-type OnFontSizeScaleUpdatedFn = (fontSizeScale: double) => void--><!--Device-systemConfiguration-type OnFontSizeScaleUpdatedFn = (fontSizeScale: double) => void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [fontSizeScale](arkts-ability-app-ability-configuration-configuration-i.md) | number | 是 |
