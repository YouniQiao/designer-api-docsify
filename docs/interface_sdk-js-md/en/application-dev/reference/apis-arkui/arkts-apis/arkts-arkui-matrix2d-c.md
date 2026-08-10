# Matrix2D

用于画布绘制  
[CanvasRenderingContext2D](../../../reference/apis-arkui/arkui-ts/ts-canvasrenderingcontext2d.md)、  
[OffscreenCanvasRenderingContext2D](../../../reference/apis-arkui/arkui-ts/ts-offscreencanvasrenderingcontext2d.md)、  
[CanvasPattern](../../../reference/apis-arkui/arkui-ts/ts-components-canvas-canvaspattern.md)和  
[Path2D](../../../reference/apis-arkui/arkui-ts/ts-components-canvas-path2d.md)的矩阵对象，可以对矩阵进行缩放、旋转和平移等变换。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-unnamed-declare class Matrix2D--><!--Device-unnamed-declare class Matrix2D-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor()
```

构造二维变换矩阵对象，默认值是属性全为0的矩阵。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-Matrix2D-constructor()--><!--Device-Matrix2D-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(unit: LengthMetricsUnit)
```

构造二维变换矩阵对象，默认值是属性全为0的矩阵，支持配置Matrix2D对象的单位模式。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-Matrix2D-constructor(unit: LengthMetricsUnit)--><!--Device-Matrix2D-constructor(unit: LengthMetricsUnit)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| unit | [LengthMetricsUnit](arkts-arkui-graphics-lengthmetricsunit-e.md) | Yes | 用来配置Matrix2D对象的单位模式，配置后无法动态更改， 配置方法同[CanvasRenderingContext2D](../../../reference/apis-arkui/arkui-ts/ts-canvasrenderingcontext2d.md)。 &lt;br&gt;异常值NaN和Infinity按默认值处理。&lt;br&gt;默认值：DEFAULT |

## identity

```TypeScript
identity(): Matrix2D
```

创建单位矩阵。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-Matrix2D-identity(): Matrix2D--><!--Device-Matrix2D-identity(): Matrix2D-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [Matrix2D](arkts-arkui-matrix2d-c.md) | 单位矩阵。 |

## invert

```TypeScript
invert(): Matrix2D
```

获取当前矩阵的逆矩阵。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-Matrix2D-invert(): Matrix2D--><!--Device-Matrix2D-invert(): Matrix2D-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [Matrix2D](arkts-arkui-matrix2d-c.md) | 逆矩阵结果。 |

## multiply

```TypeScript
multiply(other?: Matrix2D): Matrix2D
```

当前矩阵与目标矩阵相乘。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 10

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-Matrix2D-multiply(other?: Matrix2D): Matrix2D--><!--Device-Matrix2D-multiply(other?: Matrix2D): Matrix2D-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Matrix2D](arkts-arkui-matrix2d-c.md) | No | 目标矩阵。 &lt;br&gt;异常值undefined和null按无效值处理。&lt;br&gt;默认值：null |

**Return value:**

| Type | Description |
| --- | --- |
| [Matrix2D](arkts-arkui-matrix2d-c.md) | 相乘结果矩阵。 |

## rotate

```TypeScript
rotate(rx?: number, ry?: number): Matrix2D
```

对当前矩阵进行旋转运算。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 10

**Substitutes:** [rotate](arkts-arkui-matrix2d-c.md#rotate)

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-Matrix2D-rotate(rx?: number, ry?: number): Matrix2D--><!--Device-Matrix2D-rotate(rx?: number, ry?: number): Matrix2D-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rx | number | No | 旋转点的水平方向坐标，取值范围无限制。&lt;br&gt;异常值undefined和null 按无效值处理，NaN和Infinity会导致Matrix2D异常。&lt;br&gt;默认单位：vp |
| ry | number | No | 旋转点的垂直方向坐标，取值范围无限制。&lt;br&gt;异常值undefined和null 按无效值处理，NaN和Infinity会导致Matrix2D异常。&lt;br&gt;默认单位：vp |

**Return value:**

| Type | Description |
| --- | --- |
| [Matrix2D](arkts-arkui-matrix2d-c.md) |  |

## rotate

```TypeScript
rotate(degree: number, rx?: number, ry?: number): Matrix2D
```

以旋转点为中心，对当前矩阵进行右乘旋转运算。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-Matrix2D-rotate(degree: number, rx?: number, ry?: number): Matrix2D--><!--Device-Matrix2D-rotate(degree: number, rx?: number, ry?: number): Matrix2D-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| degree | number | Yes | 旋转角度，取值范围无限制。顺时针方向为正角度， 可以通过 degree Math.PI / 180 将角度转换为弧度值。 &lt;br&gt;异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。 &lt;br&gt;默认单位：弧度 |
| rx | number | No | 旋转点的水平方向坐标，取值范围无限制。&lt;br&gt;默认单位：vp &lt;br&gt;异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。 &lt;br&gt;默认值：0 |
| ry | number | No | 旋转点的垂直方向坐标，取值范围无限制。&lt;br&gt;默认单位：vp &lt;br&gt;异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。 &lt;br&gt;默认值：0 |

**Return value:**

| Type | Description |
| --- | --- |
| [Matrix2D](arkts-arkui-matrix2d-c.md) |  |

## scale

```TypeScript
scale(sx?: number, sy?: number): Matrix2D
```

对当前矩阵进行右乘缩放运算。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-Matrix2D-scale(sx?: number, sy?: number): Matrix2D--><!--Device-Matrix2D-scale(sx?: number, sy?: number): Matrix2D-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sx | number | No | 水平缩放比例系数，取值范围无限制。&lt;br&gt;异常值undefined和null 按无效值处理，NaN和Infinity会导致Matrix2D异常。&lt;br&gt;默认值：1.0 |
| sy | number | No | 垂直缩放比例系数，取值范围无限制。&lt;br&gt;异常值undefined和null 按无效值处理，NaN和Infinity会导致Matrix2D异常。&lt;br&gt;默认值：1.0 |

**Return value:**

| Type | Description |
| --- | --- |
| [Matrix2D](arkts-arkui-matrix2d-c.md) |  |

## translate

```TypeScript
translate(tx?: number, ty?: number): Matrix2D
```

对当前矩阵进行左乘平移运算。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-Matrix2D-translate(tx?: number, ty?: number): Matrix2D--><!--Device-Matrix2D-translate(tx?: number, ty?: number): Matrix2D-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tx | number | No | 水平方向平移距离，取值范围无限制。&lt;br&gt;异常值undefined和null 按无效值处理，NaN和Infinity会导致Matrix2D异常。&lt;br&gt;默认单位：vp&lt;br&gt;默认值：0 |
| ty | number | No | 垂直方向平移距离，取值范围无限制。&lt;br&gt;异常值undefined和null 按无效值处理，NaN和Infinity会导致Matrix2D异常。&lt;br&gt;默认单位：vp&lt;br&gt;默认值：0 |

**Return value:**

| Type | Description |
| --- | --- |
| [Matrix2D](arkts-arkui-matrix2d-c.md) | 平移后结果矩阵对象。 |

## rotateX

```TypeScript
rotateX?: number
```

水平倾斜系数，取值范围无限制。&lt;br&gt;异常值undefined按无效值处理，NaN和Infinity会导致Matrix2D异常，设置后绘制内容不显示。

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-Matrix2D-rotateX?: number--><!--Device-Matrix2D-rotateX?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## rotateY

```TypeScript
rotateY?: number
```

垂直倾斜系数，取值范围无限制。&lt;br&gt;异常值undefined按无效值处理，NaN和Infinity会导致Matrix2D异常，设置后绘制内容不显示。

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-Matrix2D-rotateY?: number--><!--Device-Matrix2D-rotateY?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scaleX

```TypeScript
scaleX?: number
```

水平缩放系数，取值范围无限制。&lt;br&gt;异常值undefined按无效值处理，NaN和Infinity会导致Matrix2D异常，设置后绘制内容不显示。

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-Matrix2D-scaleX?: number--><!--Device-Matrix2D-scaleX?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scaleY

```TypeScript
scaleY?: number
```

垂直缩放系数，取值范围无限制。&lt;br&gt;异常值undefined按无效值处理，NaN和Infinity会导致Matrix2D异常，设置后绘制内容不显示。

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-Matrix2D-scaleY?: number--><!--Device-Matrix2D-scaleY?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## translateX

```TypeScript
translateX?: number
```

水平平移距离，取值范围无限制。&lt;br&gt;异常值undefined按无效值处理，NaN和Infinity会导致Matrix2D异常，设置后绘制内容不显示。&lt;br&gt;默认单位：vp

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-Matrix2D-translateX?: number--><!--Device-Matrix2D-translateX?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## translateY

```TypeScript
translateY?: number
```

垂直平移距离，取值范围无限制。&lt;br&gt;异常值undefined按无效值处理，NaN和Infinity会导致Matrix2D异常，设置后绘制内容不显示。&lt;br&gt;默认单位：vp

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-Matrix2D-translateY?: number--><!--Device-Matrix2D-translateY?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

