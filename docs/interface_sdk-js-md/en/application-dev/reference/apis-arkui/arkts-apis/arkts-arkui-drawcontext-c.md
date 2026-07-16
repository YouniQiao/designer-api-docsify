# DrawContext

Graphics drawing context, which provides the canvas width and height required for drawing.

**Since:** 11

<!--Device-unnamed-export class DrawContext--><!--Device-unnamed-export class DrawContext-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## canvas

```TypeScript
get canvas(): drawing.Canvas
```

Obtains the canvas used for drawing.

**Type:** drawing.Canvas

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DrawContext-get canvas(): drawing.Canvas--><!--Device-DrawContext-get canvas(): drawing.Canvas-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## size

```TypeScript
get size(): Size
```

Obtains the width and height of the canvas.

**Type:** Size

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DrawContext-get size(): Size--><!--Device-DrawContext-get size(): Size-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## sizeInPixel

```TypeScript
get sizeInPixel(): Size
```

Obtains the width and height of the canvas in px.

**Type:** Size

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DrawContext-get sizeInPixel(): Size--><!--Device-DrawContext-get sizeInPixel(): Size-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

