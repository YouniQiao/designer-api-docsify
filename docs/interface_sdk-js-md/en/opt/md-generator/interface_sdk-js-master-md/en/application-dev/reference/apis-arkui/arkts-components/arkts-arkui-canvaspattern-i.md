# CanvasPattern

**CanvasPattern** represents an object, created by the  
[createPattern](CanvasRenderingContext2D#createPattern)API, describing an image filling pattern based on the image and repetition mode.

**Since:** 8

<!--Device-unnamed-declare interface CanvasPattern--><!--Device-unnamed-declare interface CanvasPattern-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setTransform

```TypeScript
setTransform(transform?: Matrix2D): void
```

Uses a **Matrix2D** object as a parameter to perform matrix transformation on the current  
**CanvasPattern** object.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasPattern-setTransform(transform?: Matrix2D): void--><!--Device-CanvasPattern-setTransform(transform?: Matrix2D): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| transform | [Matrix2D](../arkts-apis/arkts-arkui-canvaspattern-matrix2d-c.md) | No |
