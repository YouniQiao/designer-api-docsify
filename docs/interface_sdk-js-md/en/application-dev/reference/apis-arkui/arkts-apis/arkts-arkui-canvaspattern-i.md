# CanvasPattern

一个Object对象，使用  
[createPattern](../../../reference/apis-arkui/arkui-ts/ts-canvasrenderingcontext2d.md#createpattern)方法创建，通过指定图像和重复方式创建图片填充的模板。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-unnamed-declare interface CanvasPattern--><!--Device-unnamed-declare interface CanvasPattern-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setTransform

```TypeScript
setTransform(transform?: Matrix2D): void
```

使用Matrix2D对象作为参数，对当前CanvasPattern进行矩阵变换。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasPattern-setTransform(transform?: Matrix2D): void--><!--Device-CanvasPattern-setTransform(transform?: Matrix2D): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| transform | [Matrix2D](arkts-arkui-matrix2d-c.md) | No | 转换矩阵。 &lt;br&gt;异常值undefined和null按无效值不做矩阵变换处理。 &lt;br&gt;默认值：不做矩阵变换。 |

