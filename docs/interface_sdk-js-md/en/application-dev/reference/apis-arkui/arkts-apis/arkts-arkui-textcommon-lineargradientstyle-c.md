# LinearGradientStyle

显示为线性渐变。LinearGradientStyle继承自[ShaderStyle](arkts-arkui-textcommon-shaderstyle-c.md)。

**Inheritance/Implementation:** LinearGradientStyle extends [ShaderStyle](arkts-arkui-textcommon-shaderstyle-c.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-unnamed-export declare class LinearGradientStyle extends ShaderStyle--><!--Device-unnamed-export declare class LinearGradientStyle extends ShaderStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(options: LinearGradientOptions)
```

用于创建LinearGradientStyle对象的构造函数。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LinearGradientStyle-constructor(options: LinearGradientOptions)--><!--Device-LinearGradientStyle-constructor(options: LinearGradientOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [LinearGradientOptions](../arkts-components/arkts-arkui-lineargradientoptions-i.md) | Yes | 显示为线性渐变效果。 |

## options

```TypeScript
options: LinearGradientOptions
```

显示为线性渐变效果。

[LinearGradientOptions](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-gradient-color.md#lineargradientoptions18对象说明)中的direction默认值按  
[GradientDirection](../../../reference/apis-arkui/arkui-ts/ts-appendix-enums.md#gradientdirection)中的NONE处理。

**Type:** [LinearGradientOptions](../arkts-components/arkts-arkui-lineargradientoptions-i.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LinearGradientStyle-options: LinearGradientOptions--><!--Device-LinearGradientStyle-options: LinearGradientOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

