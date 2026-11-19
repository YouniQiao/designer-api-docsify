# BlenderBase (System API)

```TypeScript
class BlenderBase
```

Blender base type, providing the unified creation entry for various blending effects. It is recommended to use the methods of this type to create blenders.

**Since:** 26.1.0

<!--Device-uiEffect-class BlenderBase--><!--Device-uiEffect-class BlenderBase-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { uiEffect } from '@kit.ArkGraphics2D';
```

## createBrightnessBlender

```TypeScript
static createBrightnessBlender(param: BrightnessBlenderParam, hdrEnabled?: boolean): BlenderBase
```

Creates a brightness blend BlenderBase instance by inputting the brightness blender parameters. When the optional parameter hdrEnabled is set to false, the effect is the same as calling uiEffect.createBrightnessBlender(); when it is set to true, the effect is the same as calling uiEffect.createHdrBrightnessBlender().

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.1.0.

<!--Device-BlenderBase-static createBrightnessBlender(param: BrightnessBlenderParam, hdrEnabled?: boolean): BlenderBase--><!--Device-BlenderBase-static createBrightnessBlender(param: BrightnessBlenderParam, hdrEnabled?: boolean): BlenderBase-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| param | [BrightnessBlenderParam](arkts-arkgraphics2d-graphics-uieffect-brightnessblenderparam-i-sys.md) | Yes | The brightness blender parameters, including grayscale adjustment coefficients, saturation, blending ratio, and other configuration items, used to configure the brightness blend effect. |
| hdrEnabled | boolean | No | Whether to enable HDR for the brightness blend effect. When set to true, HDR is enabled for the brightness blend effect; when set to false, HDR is not enabled for the brightness blend effect. The default value is false. |

**Return value:**

| Type | Description |
| --- | --- |
| [BlenderBase](arkts-arkgraphics2d-uieffect-blenderbase-c-sys.md) | Returns a BlenderBase with the brightness blend effect. |

## createColorfulBrightnessBlender

```TypeScript
static createColorfulBrightnessBlender(brightnessBlenderParam: BrightnessBlenderParam,
      options?: ColorfulBrightnessBlenderOptions): BlenderBase
```

Creates a BlenderBase instance to add a hue-preserving brightening and darkening effect to a component. The effect is the same as calling uiEffect.createColorfulBrightnessBlender().

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.1.0.

<!--Device-BlenderBase-static createColorfulBrightnessBlender(brightnessBlenderParam: BrightnessBlenderParam,      options?: ColorfulBrightnessBlenderOptions): BlenderBase--><!--Device-BlenderBase-static createColorfulBrightnessBlender(brightnessBlenderParam: BrightnessBlenderParam,      options?: ColorfulBrightnessBlenderOptions): BlenderBase-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| brightnessBlenderParam | [BrightnessBlenderParam](arkts-arkgraphics2d-graphics-uieffect-brightnessblenderparam-i-sys.md) | Yes | Regular parameters for brightening and darkening, used to configure basic properties such as brightness mapping and saturation curves. |
| options | [ColorfulBrightnessBlenderOptions](arkts-arkgraphics2d-uieffect-colorfulbrightnessblenderoptions-i-sys.md) | No | Enhanced parameters for brightening and darkening, used to control the brightening/darkening direction, color enhancement strength, readability threshold, and HDR switch. If this parameter is not specified, the default values of the fields in ColorfulBrightnessBlenderOptions are used. |

**Return value:**

| Type | Description |
| --- | --- |
| [BlenderBase](arkts-arkgraphics2d-uieffect-blenderbase-c-sys.md) | Returns a BlenderBase with the hue-preserving brightening and darkening blend effect. |

## createHdrDarkenBlender

```TypeScript
static createHdrDarkenBlender(hdrBrightnessRatio: number, grayscaleFactor?: [number, number, number]): BlenderBase
```

Creates an HDR darken blend BlenderBase instance for HDR layer darken blending effect. The effect is the same as calling uiEffect.createHdrDarkenBlender().

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-BlenderBase-static createHdrDarkenBlender(hdrBrightnessRatio: double, grayscaleFactor?: [double, double, double]): BlenderBase--><!--Device-BlenderBase-static createHdrDarkenBlender(hdrBrightnessRatio: double, grayscaleFactor?: [double, double, double]): BlenderBase-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| hdrBrightnessRatio | number | Yes | HDR brightness ratio. Value range [1.0, the maximum brightness ratio supported by the current device], and values outside the range will be automatically clamped. When the value is equal to 1.0, it represents the original brightness of the component. The maximum brightness ratio supported by the current device = device maximum brightness / device default brightness. Device maximum brightness can be obtained via hdc command: hdc shell param get const.display.brightness.max Device default brightness can be obtained via hdc command: hdc shell param get const.display.brightness.default |
| grayscaleFactor | [number, number, number] | No | Converts RGB colors to grayscale values. The weights of the grayscale conversion formula can be automatically adjusted according to the current color gamut, using different weight calculation methods under different color gamuts; suitable for sRGB and other standard color gamut scenarios. Pass this parameter when you need to customize grayscale conversion weights based on a specific color gamut or visual effect. All three components have no boundary limits. The default value is the standard grayscale weights [0.299, 0.587, 0.114]. |

**Return value:**

| Type | Description |
| --- | --- |
| [BlenderBase](arkts-arkgraphics2d-uieffect-blenderbase-c-sys.md) | Returns a BlenderBase with the HDR darken blend effect, used to add a darken effect to a specified component. |
