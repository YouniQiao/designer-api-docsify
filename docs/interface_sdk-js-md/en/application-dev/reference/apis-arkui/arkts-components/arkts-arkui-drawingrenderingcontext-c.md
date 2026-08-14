# DrawingRenderingContext

**DrawingRenderingContext** provides a rendering context for drawing rectangles, text, images, and other objects on a canvas.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

<!--Device-unnamed-declare class DrawingRenderingContext--><!--Device-unnamed-declare class DrawingRenderingContext-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(unit?: LengthMetricsUnit)
```

Creates a **Canvas** object for drawing operations using the drawing API. Configuration of the unit mode for the **DrawingRenderingContext** object is supported.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DrawingRenderingContext-constructor(unit?: LengthMetricsUnit)--><!--Device-DrawingRenderingContext-constructor(unit?: LengthMetricsUnit)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| unit | LengthMetricsUnit | No | Unit mode of the **DrawingRenderingContext** object. The value cannot be changed once set. The configuration method is the same as that of [CanvasRenderingContext2D](arkts-arkui-canvasrenderingcontext2d-c.md#CanvasRenderingContext2D). <br>Invalid values **undefined**, **NaN** and **Infinity** are treated as the default value. <br>Default value: **DEFAULT**. |

## invalidate

```TypeScript
invalidate(): void
```

Invalidates the component and triggers re-rendering of the component.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DrawingRenderingContext-invalidate(): void--><!--Device-DrawingRenderingContext-invalidate(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

