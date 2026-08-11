# ColorMetrics

Used to mix colors.

**Since:** 12

<!--Device-unnamed-declare class ColorMetrics--><!--Device-unnamed-declare class ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## autoRefresh

```TypeScript
autoRefresh?(value: boolean): ColorMetrics
```

Sets whether the **ColorMetrics** object automatically updates with system configuration changes.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ColorMetrics-autoRefresh?(value: boolean): ColorMetrics--><!--Device-ColorMetrics-autoRefresh?(value: boolean): ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md) |

## blendColor

```TypeScript
blendColor(overlayColor: ColorMetrics): ColorMetrics
```

Blends a specified color (**overlayColor**) with the current color and returns the resulting color.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ColorMetrics-blendColor(overlayColor: ColorMetrics): ColorMetrics--><!--Device-ColorMetrics-blendColor(overlayColor: ColorMetrics): ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| overlayColor | [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## colorWithSpace

```TypeScript
static colorWithSpace(colorSpace: ColorSpace, red: number, green: number, blue: number, alpha?: number): ColorMetrics
```

Creates a **ColorMetrics** instance using specified [ColorSpace](arkts-arkui-colorspace-e.md) and RGBA values. Only certain attributes support color configuration in the display-p3 color space.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-ColorMetrics-static colorWithSpace(colorSpace: ColorSpace, red: number, green: number, blue: number, alpha?: number): ColorMetrics--><!--Device-ColorMetrics-static colorWithSpace(colorSpace: ColorSpace, red: number, green: number, blue: number, alpha?: number): ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| colorSpace | [ColorSpace](arkts-arkui-window-colorspace-e.md) | Yes |
| [red](#red) | number | Yes |
| [green](#green) | number | Yes |
| [blue](#blue) | number | Yes |
| [alpha](#alpha) | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md) |

## numeric

```TypeScript
static numeric(value: number): ColorMetrics
```

Instantiates the **ColorMetrics** class using a color in HEX format.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ColorMetrics-static numeric(value: number): ColorMetrics--><!--Device-ColorMetrics-static numeric(value: number): ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md) |

## resourceColor

```TypeScript
static resourceColor(color: ResourceColor): ColorMetrics
```

Instantiates the **ColorMetrics** class using a color in resource reference format.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ColorMetrics-static resourceColor(color: ResourceColor): ColorMetrics--><!--Device-ColorMetrics-static resourceColor(color: ResourceColor): ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [color](#color) | [ResourceColor](arkts-arkui-resourcecolor-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [180003](../errorcode-event.md#180003-input-event-is-not-a-cloned-event) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## rgba

```TypeScript
static rgba(red: number, green: number, blue: number, alpha?: number): ColorMetrics
```

Instantiates the **ColorMetrics** class using colors in RGB or RGBA format.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ColorMetrics-static rgba(red: number, green: number, blue: number, alpha?: number): ColorMetrics--><!--Device-ColorMetrics-static rgba(red: number, green: number, blue: number, alpha?: number): ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [red](#red) | number | Yes |
| [green](#green) | number | Yes |
| [blue](#blue) | number | Yes |
| [alpha](#alpha) | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md) |

## alpha

```TypeScript
get alpha(): number
```

Obtains the alpha component of the ColorMetrics color.

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ColorMetrics-get alpha(): number--><!--Device-ColorMetrics-get alpha(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## blue

```TypeScript
get blue(): number
```

Obtains the blue component of the ColorMetrics color.

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ColorMetrics-get blue(): number--><!--Device-ColorMetrics-get blue(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## color

```TypeScript
get color(): string
```

Obtains the color of **ColorMetrics**. The return value is a string indicating an RGBA color value.

**Type:** string

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ColorMetrics-get color(): string--><!--Device-ColorMetrics-get color(): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## green

```TypeScript
get green(): number
```

Obtains the green component of the ColorMetrics color.

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ColorMetrics-get green(): number--><!--Device-ColorMetrics-get green(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## red

```TypeScript
get red(): number
```

Obtains the red component of the ColorMetrics color.

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ColorMetrics-get red(): number--><!--Device-ColorMetrics-get red(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
