# ColorMetrics

Used to mix colors.

**Since:** 12

<!--Device-unnamed-declare class ColorMetrics--><!--Device-unnamed-declare class ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## createHDRColor

```TypeScript
static createHDRColor(colorSpace: ColorSpace, red: number, green: number, blue: number, alpha?: number): ColorMetrics
```

Create ColorMetrics class using HDR color with default exposure.Create an HDR color value with default exposure (0.0 for logarithmic, 1.0 for linear).When no exposure value is specified, RGB channel values can exceed 1.0 to achieve HDR brightness.This matches iOS UIColor behavior where RGB values > 1.0 enable HDR rendering.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-static createHDRColor(colorSpace: ColorSpace, red: double, green: double, blue: double, alpha?: double): ColorMetrics--><!--Device-ColorMetrics-static createHDRColor(colorSpace: ColorSpace, red: double, green: double, blue: double, alpha?: double): ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| colorSpace | [ColorSpace](arkts-arkui-window-colorspace-e.md) | Yes |
| red | number | Yes |
| green | number | Yes |
| blue | number | Yes |
| alpha | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ColorMetrics](arkts-arkui-graphics-colormetrics-c-sys.md) |

## createHDRColorWithLinearExposure

```TypeScript
static createHDRColorWithLinearExposure(linearExposure: number, colorSpace: ColorSpace,
    red: number, green: number, blue: number, alpha?: number): ColorMetrics
```

Create ColorMetrics class using HDR color with linear exposure.Create an HDR color value with specified linear exposure.The exposure value controls the brightness of the color in a linear color space.When using linear exposure, RGB channel values are typically in the range [0, 1].

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-static createHDRColorWithLinearExposure(linearExposure: double, colorSpace: ColorSpace,    red: double, green: double, blue: double, alpha?: double): ColorMetrics--><!--Device-ColorMetrics-static createHDRColorWithLinearExposure(linearExposure: double, colorSpace: ColorSpace,    red: double, green: double, blue: double, alpha?: double): ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| linearExposure | number | Yes |
| colorSpace | [ColorSpace](arkts-arkui-window-colorspace-e.md) | Yes |
| red | number | Yes |
| green | number | Yes |
| blue | number | Yes |
| alpha | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ColorMetrics](arkts-arkui-graphics-colormetrics-c-sys.md) |

## createHDRColorWithLogExposure

```TypeScript
static createHDRColorWithLogExposure(exposure: number, colorSpace: ColorSpace,
    red: number, green: number, blue: number, alpha?: number): ColorMetrics
```

Create ColorMetrics class using HDR color with linear exposure.Create an HDR color value with specified logarithmic exposure (stops).The exposure value controls the brightness in a logarithmic (perceptual) color space.When using logarithmic exposure, RGB channel values are typically in the range [0, 1].

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-static createHDRColorWithLogExposure(exposure: double, colorSpace: ColorSpace,    red: double, green: double, blue: double, alpha?: double): ColorMetrics--><!--Device-ColorMetrics-static createHDRColorWithLogExposure(exposure: double, colorSpace: ColorSpace,    red: double, green: double, blue: double, alpha?: double): ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| exposure | number | Yes |
| colorSpace | [ColorSpace](arkts-arkui-window-colorspace-e.md) | Yes |
| red | number | Yes |
| green | number | Yes |
| blue | number | Yes |
| alpha | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ColorMetrics](arkts-arkui-graphics-colormetrics-c-sys.md) |

## getBlueValue

```TypeScript
getBlueValue(): number
```

Get blue value.Returns blue channel value as a floating-point number.For SDR colors, value is in range [0, 1].For HDR colors, value can be greater than 1.0 to represent extended brightness.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-getBlueValue(): double--><!--Device-ColorMetrics-getBlueValue(): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getColorSpace

```TypeScript
getColorSpace(): ColorSpace
```

Get color space of the ColorMetrics.Returns the color space used when creating this color.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-getColorSpace(): ColorSpace--><!--Device-ColorMetrics-getColorSpace(): ColorSpace-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ColorSpace](arkts-arkui-window-colorspace-e.md) |

## getGreenValue

```TypeScript
getGreenValue(): number
```

Get green value.Returns green channel value as a floating-point number.For SDR colors, value is in range [0, 1].For HDR colors, value can be greater than 1.0 to represent extended brightness.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-getGreenValue(): double--><!--Device-ColorMetrics-getGreenValue(): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getRedValue

```TypeScript
getRedValue(): number
```

Get red value.Returns red channel value as a floating-point number.For SDR colors, value is in range [0, 1].For HDR colors, value can be greater than 1.0 to represent extended brightness.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-getRedValue(): double--><!--Device-ColorMetrics-getRedValue(): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## isHDR

```TypeScript
isHDR(): boolean
```

Check if ColorMetrics represents an HDR color.Returns true if color was created using createHDRColorWithXx or has RGB values > 1.0.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-isHDR(): boolean--><!--Device-ColorMetrics-isHDR(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
