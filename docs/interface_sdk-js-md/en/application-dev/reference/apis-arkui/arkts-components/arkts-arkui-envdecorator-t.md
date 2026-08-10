# EnvDecorator

```TypeScript
declare type EnvDecorator = (value: SystemProperties) => PropertyDecorator
```

定义EnvDecorator属性装饰器类型。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-unnamed-declare type EnvDecorator = (value: SystemProperties) => PropertyDecorator--><!--Device-unnamed-declare type EnvDecorator = (value: SystemProperties) => PropertyDecorator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [SystemProperties](arkts-arkui-systemproperties-e.md) | Yes | 环境变量属性名，用于指定要获取的系统环境变量。 |

**Return value:**

| Type | Description |
| --- | --- |
| PropertyDecorator | 属性装饰器，开发者无需关注该返回值。 |

