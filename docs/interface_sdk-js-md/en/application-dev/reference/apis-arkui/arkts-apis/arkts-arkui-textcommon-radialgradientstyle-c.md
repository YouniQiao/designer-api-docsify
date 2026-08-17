# RadialGradientStyle

Defines radial gradient class.

**Inheritance/Implementation:** RadialGradientStyle extends [ShaderStyle](arkts-arkui-textcommon-shaderstyle-c.md#shaderstyle)

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

<!--Device-unnamed-export declare class RadialGradientStyle--><!--Device-unnamed-export declare class RadialGradientStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(options: RadialGradientOptions)
```

The constructor.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RadialGradientStyle-constructor(options: RadialGradientOptions)--><!--Device-RadialGradientStyle-constructor(options: RadialGradientOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RadialGradientOptions](../arkts-components/arkts-arkui-radialgradientoptions-i.md) | Yes | The options of the gradient. |

## options

```TypeScript
options: RadialGradientOptions
```

The options of the gradient. center:Center point of radial gradient radius:Radius of Radial Gradient. value range [0, +∞) colors:Color description for gradients repeating: Refill. The default value is false

**Type:** [RadialGradientOptions](../arkts-components/arkts-arkui-radialgradientoptions-i.md)

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RadialGradientStyle-options: RadialGradientOptions--><!--Device-RadialGradientStyle-options: RadialGradientOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

