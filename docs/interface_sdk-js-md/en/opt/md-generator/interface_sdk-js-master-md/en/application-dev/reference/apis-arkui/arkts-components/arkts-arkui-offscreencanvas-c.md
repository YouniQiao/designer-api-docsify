# OffscreenCanvas

The **OffscreenCanvas** component is used to draw custom graphics.

When the  
[Canvas](Canvas)component or **CanvasRenderingContext2D** object is used, rendering, animation,and user interaction usually occur on the main thread of the application.Calculations related to canvas animation and rendering may affect application performance. **OffscreenCanvas** allows for rendering off the screen. This means that some tasks can be run in a separate thread to reduce the load on the main thread.

> **NOTE：**
> 
> **OffscreenCanvas** cannot be used in ServiceExtensionAbility. It is recommended
> that you use the
> [drawing module](../../../reference/apis-arkgraphics2d/arkts-apis-graphics-drawing.md)
> for offscreen drawing in ServiceExtensionAbility.

**Since:** 8

<!--Device-unnamed-declare class OffscreenCanvas--><!--Device-unnamed-declare class OffscreenCanvas-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(width: number, height: number)
```

Constructs an OffscreenCanvas for creating an offscreen canvas object.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-OffscreenCanvas-constructor(width: number, height: number)--><!--Device-OffscreenCanvas-constructor(width: number, height: number)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [width](#width) | number | Yes |
| [height](#height) | number | Yes |

## constructor

```TypeScript
constructor(width: number, height: number, unit: LengthMetricsUnit)
```

Constructs an **OffscreenCanvas** object for creating an offscreen canvas object.The unit mode is configurable for the **OffscreenCanvas** object.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-OffscreenCanvas-constructor(width: number, height: number, unit: LengthMetricsUnit)--><!--Device-OffscreenCanvas-constructor(width: number, height: number, unit: LengthMetricsUnit)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [width](#width) | number | Yes |
| [height](#height) | number | Yes |
| unit | [LengthMetricsUnit](../arkts-apis/arkts-arkui-graphics-lengthmetricsunit-e.md) | Yes |

## getContext

```TypeScript
getContext(contextType: "2d", options?: RenderingContextSettings): OffscreenCanvasRenderingContext2D
```

Obtains the drawing context of the offscreen canvas.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-OffscreenCanvas-getContext(contextType: "2d", options?: RenderingContextSettings): OffscreenCanvasRenderingContext2D--><!--Device-OffscreenCanvas-getContext(contextType: "2d", options?: RenderingContextSettings): OffscreenCanvasRenderingContext2D-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| contextType | "2d" | Yes |
| options | [RenderingContextSettings](arkts-arkui-renderingcontextsettings-c.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [OffscreenCanvasRenderingContext2D](arkts-arkui-offscreencanvasrenderingcontext2d-c.md) |

## transferToImageBitmap

```TypeScript
transferToImageBitmap(): ImageBitmap
```

Creates an **ImageBitmap** object from the most recently rendered image of the offscreen canvas.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-OffscreenCanvas-transferToImageBitmap(): ImageBitmap--><!--Device-OffscreenCanvas-transferToImageBitmap(): ImageBitmap-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageBitmap](arkts-arkui-imagebitmap-c.md) |

## height

```TypeScript
height: number
```

Height of the offscreen canvas.

Default unit: vp

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-OffscreenCanvas-height: number--><!--Device-OffscreenCanvas-height: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
width: number
```

Width of the offscreen canvas.

Default unit: vp

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-OffscreenCanvas-width: number--><!--Device-OffscreenCanvas-width: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
