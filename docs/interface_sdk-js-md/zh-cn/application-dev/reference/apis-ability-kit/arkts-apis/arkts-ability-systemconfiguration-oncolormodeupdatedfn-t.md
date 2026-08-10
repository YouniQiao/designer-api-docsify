# OnColorModeUpdatedFn

```TypeScript
type OnColorModeUpdatedFn = (colorMode: ConfigurationConstant.ColorMode) => void
```

Defines an OnColorModeUpdatedFn function.

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-systemConfiguration-type OnColorModeUpdatedFn = (colorMode: ConfigurationConstant.ColorMode) => void--><!--Device-systemConfiguration-type OnColorModeUpdatedFn = (colorMode: ConfigurationConstant.ColorMode) => void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colorMode | ConfigurationConstant.ColorMode | 是 | Indicates the system's light or dark color mode |

