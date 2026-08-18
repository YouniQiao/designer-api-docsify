# ColorMetrics

Defines the ColorMetrics class.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class ColorMetrics--><!--Device-unnamed-export declare class ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## createHDRColor

```TypeScript
static createHDRColor(colorSpace: ColorSpace, red: double, green: double, blue: double, alpha?: double): ColorMetrics
```

Create ColorMetrics class using HDR color with default exposure. Create an HDR color value with default exposure (0.0 for logarithmic, 1.0 for linear). When no exposure value is specified, RGB channel values can exceed 1.0 to achieve HDR brightness. This matches iOS UIColor behavior where RGB values > 1.0 enable HDR rendering.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-static createHDRColor(colorSpace: ColorSpace, red: double, green: double, blue: double, alpha?: double): ColorMetrics--><!--Device-ColorMetrics-static createHDRColor(colorSpace: ColorSpace, red: double, green: double, blue: double, alpha?: double): ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| colorSpace | ColorSpace | Yes | Color space of color. Supports SRGB, DISPLAY_P3, and BT2020 color spaces. |
| red | double | Yes | Red component value. Valid range: [0, +∞). Values greater than 1.0 enable HDR brightness. |
| green | double | Yes | Green component value. Valid range: [0, +∞). Values greater than 1.0 enable HDR brightness. |
| blue | double | Yes | Blue component value. Valid range: [0, +∞). Values greater than 1.0 enable HDR brightness. |
| alpha | double | No | Alpha (opacity) component value. Valid range: [0, 1]. The default value is 1.0 (fully opaque). |

**Return value:**

| Type | Description |
| --- | --- |
| [ColorMetrics](../../apis-arkui/arkts-apis/arkts-arkui-graphics-colormetrics-c.md) | ColorMetrics class instance with HDR color. |

## createHDRColorWithLinearExposure

```TypeScript
static createHDRColorWithLinearExposure(linearExposure: double, colorSpace: ColorSpace,
      red: double, green: double, blue: double, alpha?: double): ColorMetrics
```

Create ColorMetrics class using HDR color with linear exposure. Create an HDR color value with specified linear exposure. The exposure value controls the brightness of the color in a linear color space. When using linear exposure, RGB channel values are typically in the range [0, 1].

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-static createHDRColorWithLinearExposure(linearExposure: double, colorSpace: ColorSpace,      red: double, green: double, blue: double, alpha?: double): ColorMetrics--><!--Device-ColorMetrics-static createHDRColorWithLinearExposure(linearExposure: double, colorSpace: ColorSpace,      red: double, green: double, blue: double, alpha?: double): ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| linearExposure | double | Yes | Linear exposure value in exposure value. Valid range: [1, +∞). A value of 1.0 represents standard exposure. Values greater than 1.0 increase brightness linearly. |
| colorSpace | ColorSpace | Yes | Color space of color. Supports SRGB, DISPLAY_P3, and BT2020 color spaces. |
| red | double | Yes | Red component value. Valid range: [0, 1]. |
| green | double | Yes | Green component value. Valid range: [0, 1]. |
| blue | double | Yes | Blue component value. Valid range: [0, 1]. |
| alpha | double | No | Alpha (opacity) component value. Valid range: [0, 1]. The default value is 1.0 (fully opaque). |

**Return value:**

| Type | Description |
| --- | --- |
| [ColorMetrics](../../apis-arkui/arkts-apis/arkts-arkui-graphics-colormetrics-c.md) | ColorMetrics class instance with HDR color. |

## createHDRColorWithLogExposure

```TypeScript
static createHDRColorWithLogExposure(exposure: double, colorSpace: ColorSpace,
      red: double, green: double, blue: double, alpha?: double): ColorMetrics
```

Create ColorMetrics class using HDR color with linear exposure. Create an HDR color value with specified logarithmic exposure (stops). The exposure value controls the brightness in a logarithmic (perceptual) color space. When using logarithmic exposure, RGB channel values are typically in the range [0, 1].

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-static createHDRColorWithLogExposure(exposure: double, colorSpace: ColorSpace,      red: double, green: double, blue: double, alpha?: double): ColorMetrics--><!--Device-ColorMetrics-static createHDRColorWithLogExposure(exposure: double, colorSpace: ColorSpace,      red: double, green: double, blue: double, alpha?: double): ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| exposure | double | Yes | Logarithmic exposure value in stops. Valid range: [0, +∞). A value of 0.0 represents standard exposure. Each increment of 1.0 doubles the brightness (one stop). |
| colorSpace | ColorSpace | Yes | Color space of color. Supports SRGB, DISPLAY_P3, and BT2020 color spaces. |
| red | double | Yes | Red component value. Valid range: [0, 1]. |
| green | double | Yes | Green component value. Valid range: [0, 1]. |
| blue | double | Yes | Blue component value. Valid range: [0, 1]. |
| alpha | double | No | Alpha (opacity) component value. Valid range: [0, 1]. The default value is 1.0 (fully opaque). |

**Return value:**

| Type | Description |
| --- | --- |
| [ColorMetrics](../../apis-arkui/arkts-apis/arkts-arkui-graphics-colormetrics-c.md) | ColorMetrics class instance with HDR color. |

## getBlueValue

```TypeScript
getBlueValue(): double
```

Get blue value. Returns blue channel value as a floating-point number. For SDR colors, value is in range [0, 1]. For HDR colors, value can be greater than 1.0 to represent extended brightness.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-getBlueValue(): double--><!--Device-ColorMetrics-getBlueValue(): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| double | The blue value. Valid range: [0, +∞). For SDR colors: [0, 1]. Fro HDR colors: [0, +∞), values > 1.0 indicate HDR brightness. |

## getColorSpace

```TypeScript
getColorSpace(): ColorSpace
```

Get color space of the ColorMetrics. Returns the color space used when creating this color.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-getColorSpace(): ColorSpace--><!--Device-ColorMetrics-getColorSpace(): ColorSpace-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| ColorSpace | The color space of the ColorMetrics. Possible value: ColorSpace.SRGB, ColorSpace.DISPLAY_P3, ColorSpace.BT2020. |

## getGreenValue

```TypeScript
getGreenValue(): double
```

Get green value. Returns green channel value as a floating-point number. For SDR colors, value is in range [0, 1]. For HDR colors, value can be greater than 1.0 to represent extended brightness.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-getGreenValue(): double--><!--Device-ColorMetrics-getGreenValue(): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| double | The green value. Valid range: [0, +∞). For SDR colors: [0, 1]. Fro HDR colors: [0, +∞), values > 1.0 indicate HDR brightness. |

## getRedValue

```TypeScript
getRedValue(): double
```

Get red value. Returns red channel value as a floating-point number. For SDR colors, value is in range [0, 1]. For HDR colors, value can be greater than 1.0 to represent extended brightness.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-getRedValue(): double--><!--Device-ColorMetrics-getRedValue(): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| double | The red value. Valid range: [0, +∞). For SDR colors: [0, 1]. Fro HDR colors: [0, +∞), values > 1.0 indicate HDR brightness. |

## isHDR

```TypeScript
isHDR(): boolean
```

Check if ColorMetrics represents an HDR color. Returns true if color was created using createHDRColorWithXx or has RGB values > 1.0.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-isHDR(): boolean--><!--Device-ColorMetrics-isHDR(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether ColorMetrics is an HDR color. Returns true if: - The color was created using createHDRColorWithXx() method. - Any RGB channel value is greater than 1.0. |

