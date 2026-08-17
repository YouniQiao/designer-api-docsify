# CanvasPattern

Describes an opaque object of a template, which is created using the createPattern() method.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface CanvasPattern--><!--Device-unnamed-export declare interface CanvasPattern-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setTransform

```TypeScript
setTransform(transform?: Matrix2D): void
```

Adds the matrix transformation effect to the current template.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasPattern-setTransform(transform?: Matrix2D): void--><!--Device-CanvasPattern-setTransform(transform?: Matrix2D): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| transform | [Matrix2D](arkts-arkui-matrix2d-c.md) | No | transformation matrix. The default value is null. |

