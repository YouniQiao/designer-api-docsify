# ColorMetrics

Defines the ColorMetrics class.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class ColorMetrics--><!--Device-unnamed-export declare class ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## autoRefresh

```TypeScript
autoRefresh(value: boolean): ColorMetrics
```

Sets automatic refresh for the ColorMetrics object. When enabled, the color values of objects created with ColorMetrics.resourceColor() are automatically updated when the system configuration changes.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-autoRefresh(value: boolean): ColorMetrics--><!--Device-ColorMetrics-autoRefresh(value: boolean): ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean | Yes | Whether to automatically refresh the color value when system configuration changes. <br>If this parameter is set to true, the color values of objects created using ColorMetrics.resourceColor() are automatically updated when the system configuration changes. If set to false, the color values of objects created by ColorMetrics.resourceColor() are not automatically updated. The default value is false. |

**Return value:**

| Type | Description |
| --- | --- |
| [ColorMetrics](arkts-graphics-colormetrics-c.md) | Returns the ColorMetrics object for chaining. |

## blendColor

```TypeScript
blendColor(overlayColor: ColorMetrics): ColorMetrics
```

blend color

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-blendColor(overlayColor: ColorMetrics): ColorMetrics--><!--Device-ColorMetrics-blendColor(overlayColor: ColorMetrics): ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| overlayColor | [ColorMetrics](arkts-graphics-colormetrics-c.md) | Yes | overlay color |

**Return value:**

| Type | Description |
| --- | --- |
| [ColorMetrics](arkts-graphics-colormetrics-c.md) | ColorMetrics class |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. The type of the input parameter is not ColorMetrics. |

## colorWithSpace

```TypeScript
static colorWithSpace(colorSpace: ColorSpace, red: double, green: double, blue: double, alpha?: double): ColorMetrics
```

Instantiate the ColorMetrics class using colorSpace and rgba. Only some properties support setting color in display-p3 colorSpace.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-static colorWithSpace(colorSpace: ColorSpace, red: double, green: double, blue: double, alpha?: double): ColorMetrics--><!--Device-ColorMetrics-static colorWithSpace(colorSpace: ColorSpace, red: double, green: double, blue: double, alpha?: double): ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| colorSpace | ColorSpace | Yes | colorSpace of color. |
| red | double | Yes | red value of rgba. The range of the red channel is [0, 1]. |
| green | double | Yes | green value of rgba. The range of the green channel is [0, 1]. |
| blue | double | Yes | blue value of rgba. The range of the blue channel is [0, 1]. |
| alpha | double | No | alpha value of rgba. The range of the alpha channel is [0, 1]. The default value is 1. |

**Return value:**

| Type | Description |
| --- | --- |
| [ColorMetrics](arkts-graphics-colormetrics-c.md) | ColorMetrics class |

## numeric

```TypeScript
static numeric(value: int): ColorMetrics
```

Instantiate the ColorMetrics class using color number

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-static numeric(value: int): ColorMetrics--><!--Device-ColorMetrics-static numeric(value: int): ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | color number. <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| [ColorMetrics](arkts-graphics-colormetrics-c.md) | ColorMetrics class |

## resourceColor

```TypeScript
static resourceColor(color: ResourceColor): ColorMetrics
```

Instantiate the ColorMetrics class using ResourceColor

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-static resourceColor(color: ResourceColor): ColorMetrics--><!--Device-ColorMetrics-static resourceColor(color: ResourceColor): ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | ResourceColor | Yes | resource color |

**Return value:**

| Type | Description |
| --- | --- |
| [ColorMetrics](arkts-graphics-colormetrics-c.md) | ColorMetrics class |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [180003](../../apis-arkui/errorcode-event.md#180003-input-event-is-not-a-cloned-event) | Failed to obtain the color resource. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible cause: 1. The type of the input color parameter is not ResourceColor. 2. The format of the input color string is not RGB or RGBA. |

## rgba

```TypeScript
static rgba(red: double, green: double, blue: double, alpha?: double): ColorMetrics
```

Instantiate the ColorMetrics class using color rgb

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-static rgba(red: double, green: double, blue: double, alpha?: double): ColorMetrics--><!--Device-ColorMetrics-static rgba(red: double, green: double, blue: double, alpha?: double): ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| red | double | Yes | red value of rgba. |
| green | double | Yes | green value of rgba. |
| blue | double | Yes | blue value of rgba. |
| alpha | double | No | opacity value of rgba. |

**Return value:**

| Type | Description |
| --- | --- |
| [ColorMetrics](arkts-graphics-colormetrics-c.md) | ColorMetrics class |

## BLACK

```TypeScript
public static readonly BLACK: int
```

Black. The value should be an integer.

**Type:** int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-public static readonly BLACK: int--><!--Device-ColorMetrics-public static readonly BLACK: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## BLUE

```TypeScript
public static readonly BLUE: int
```

Blue. The value should be an integer.

**Type:** int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-public static readonly BLUE: int--><!--Device-ColorMetrics-public static readonly BLUE: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## BROWN

```TypeScript
public static readonly BROWN: int
```

Brown. The value should be an integer.

**Type:** int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-public static readonly BROWN: int--><!--Device-ColorMetrics-public static readonly BROWN: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## GRAY

```TypeScript
public static readonly GRAY: int
```

Gray. The value should be an integer.

**Type:** int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-public static readonly GRAY: int--><!--Device-ColorMetrics-public static readonly GRAY: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## GREEN

```TypeScript
public static readonly GREEN: int
```

Green. The value should be an integer.

**Type:** int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-public static readonly GREEN: int--><!--Device-ColorMetrics-public static readonly GREEN: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## GREY

```TypeScript
public static readonly GREY: int
```

Grey. The value should be an integer.

**Type:** int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-public static readonly GREY: int--><!--Device-ColorMetrics-public static readonly GREY: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## ORANGE

```TypeScript
public static readonly ORANGE: int
```

Orange. The value should be an integer.

**Type:** int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-public static readonly ORANGE: int--><!--Device-ColorMetrics-public static readonly ORANGE: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## PINK

```TypeScript
public static readonly PINK: int
```

Pink. The value should be an integer.

**Type:** int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-public static readonly PINK: int--><!--Device-ColorMetrics-public static readonly PINK: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## RED

```TypeScript
public static readonly RED: int
```

Red. The value should be an integer.

**Type:** int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-public static readonly RED: int--><!--Device-ColorMetrics-public static readonly RED: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## TRANSPARENT

```TypeScript
public static readonly TRANSPARENT: string
```

Transparent.

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-public static readonly TRANSPARENT: string--><!--Device-ColorMetrics-public static readonly TRANSPARENT: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## WHITE

```TypeScript
public static readonly WHITE: int
```

White. The value should be an integer.

**Type:** int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-public static readonly WHITE: int--><!--Device-ColorMetrics-public static readonly WHITE: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## YELLOW

```TypeScript
public static readonly YELLOW: int
```

Yellow. The value should be an integer.

**Type:** int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorMetrics-public static readonly YELLOW: int--><!--Device-ColorMetrics-public static readonly YELLOW: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

