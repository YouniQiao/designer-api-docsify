# CanvasGradient

**CanvasGradient** provides a canvas gradient object.

**Since:** 8

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## addColorStop

```TypeScript
addColorStop(offset: number, color: string): void
```

Adds a color stop for the **CanvasGradient** object based on the specified offset and gradient color.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offset | number | Yes |
| color | string | Yes |

## addColorStop

```TypeScript
addColorStop(offset: number, color: string | ColorMetrics): void
```

Adds a color stop for the **CanvasGradient** object based on the specified offset and gradient color. Colors in RGB or ARGB format can be set. You can set P3 color gamut values by passing in the ColorMetrics type, which can achieve richer color reproduction on devices that support high color gamut.

> **NOTE：**&gt;
> Only the
> fillStyle
> and
> strokeStyle
> attributes of the
> [CanvasRenderingContext2D](arkts-arkui-canvasrenderingcontext2d-c.md)
> object support the **CanvasGradient** object with the P3 wide color gamut. In addition,
> the color gamut mode of the window where the **Canvas** component is located must be set
> to wide color gamut mode **WIDE_GAMUT** via the
> [setWindowColorSpace](../arkts-apis/arkts-arkui-window-window-i.md#setwindowcolorspace)
> method.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**Widget capability:** This API can be used in ArkTS widgets since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offset | number | Yes |
| color | string \| [ColorMetrics](../arkts-apis/arkts-arkui-graphics-colormetrics-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [103701](../errorcode-canvas.md#103701-parameter-error) |
