# Matrix2D

2D变换矩阵，支持X轴和Y轴的旋转、平移和缩放。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-export class Matrix2D--><!--Device-unnamed-export class Matrix2D-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor()
```

构造二维变换矩阵对象，默认值是属性全为0的矩阵。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the FA model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-Matrix2D-constructor()--><!--Device-Matrix2D-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## identity

```TypeScript
identity(): Matrix2D
```

创建单位矩阵。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the FA model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-Matrix2D-identity(): Matrix2D--><!--Device-Matrix2D-identity(): Matrix2D-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [Matrix2D](arkts-arkui-matrix2d-c.md) |  |

## invert

```TypeScript
invert(): Matrix2D
```

获取当前矩阵的逆矩阵。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the FA model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-Matrix2D-invert(): Matrix2D--><!--Device-Matrix2D-invert(): Matrix2D-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [Matrix2D](arkts-arkui-matrix2d-c.md) |  |

## multiply

```TypeScript
multiply(other?: Matrix2D): Matrix2D
```

当前矩阵与目标矩阵相乘。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the FA model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-Matrix2D-multiply(other?: Matrix2D): Matrix2D--><!--Device-Matrix2D-multiply(other?: Matrix2D): Matrix2D-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Matrix2D](arkts-arkui-matrix2d-c.md) | No | 目标矩阵。&lt;br/&gt;异常值undefined和null按无效值处理。&lt;br/&gt;默认值：null |

**Return value:**

| Type | Description |
| --- | --- |
| [Matrix2D](arkts-arkui-matrix2d-c.md) |  |

## rotate

```TypeScript
rotate(rx?: number, ry?: number): Matrix2D
```

对当前矩阵进行旋转运算。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the FA model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-Matrix2D-rotate(rx?: number, ry?: number): Matrix2D--><!--Device-Matrix2D-rotate(rx?: number, ry?: number): Matrix2D-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rx | number | No | 旋转点的水平方向坐标，取值范围无限制。&lt;br/&gt;异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。&lt;br/&gt;默认单位：vp |
| ry | number | No | 旋转点的垂直方向坐标，取值范围无限制。&lt;br/&gt;异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。&lt;br/&gt;默认单位：vp |

**Return value:**

| Type | Description |
| --- | --- |
| [Matrix2D](arkts-arkui-matrix2d-c.md) |  |

## scale

```TypeScript
scale(sx?: number, sy?: number): Matrix2D
```

对当前矩阵进行右乘缩放运算。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the FA model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-Matrix2D-scale(sx?: number, sy?: number): Matrix2D--><!--Device-Matrix2D-scale(sx?: number, sy?: number): Matrix2D-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sx | number | No | 水平缩放比例系数，取值范围无限制。&lt;br/&gt;异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。&lt;br/&gt;默认值：1.0 |
| sy | number | No | 垂直缩放比例系数，取值范围无限制。&lt;br/&gt;异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。&lt;br/&gt;默认值：1.0 |

**Return value:**

| Type | Description |
| --- | --- |
| [Matrix2D](arkts-arkui-matrix2d-c.md) |  |

## translate

```TypeScript
translate(tx?: number, ty?: number): Matrix2D
```

对当前矩阵进行左乘平移运算。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the FA model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-Matrix2D-translate(tx?: number, ty?: number): Matrix2D--><!--Device-Matrix2D-translate(tx?: number, ty?: number): Matrix2D-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tx | number | No | 水平方向平移距离，取值范围无限制。&lt;br/&gt;异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。&lt;br/&gt;默认单位：vp&lt;br/&gt;默认值：0 |
| ty | number | No | 垂直方向平移距离，取值范围无限制。&lt;br/&gt;异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。&lt;br/&gt;默认单位：vp&lt;br/&gt;默认值：0 |

**Return value:**

| Type | Description |
| --- | --- |
| [Matrix2D](arkts-arkui-matrix2d-c.md) |  |

## rotateX

```TypeScript
rotateX?: number
```

水平倾斜系数，取值范围无限制。&lt;br/&gt;异常值undefined按无效值处理，NaN和Infinity会导致Matrix2D异常，设置后绘制内容不显示。

**Type:** number

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the FA model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-Matrix2D-rotateX?: number--><!--Device-Matrix2D-rotateX?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## rotateY

```TypeScript
rotateY?: number
```

垂直倾斜系数，取值范围无限制。&lt;br/&gt;异常值undefined按无效值处理，NaN和Infinity会导致Matrix2D异常，设置后绘制内容不显示。

**Type:** number

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the FA model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-Matrix2D-rotateY?: number--><!--Device-Matrix2D-rotateY?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scaleX

```TypeScript
scaleX?: number
```

水平缩放系数，取值范围无限制。&lt;br/&gt;异常值undefined按无效值处理，NaN和Infinity会导致Matrix2D异常，设置后绘制内容不显示。

**Type:** number

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the FA model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-Matrix2D-scaleX?: number--><!--Device-Matrix2D-scaleX?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scaleY

```TypeScript
scaleY?: number
```

垂直缩放系数，取值范围无限制。&lt;br/&gt;异常值undefined按无效值处理，NaN和Infinity会导致Matrix2D异常，设置后绘制内容不显示。

**Type:** number

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the FA model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-Matrix2D-scaleY?: number--><!--Device-Matrix2D-scaleY?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## translateX

```TypeScript
translateX?: number
```

水平平移距离，取值范围无限制。&lt;br/&gt;异常值undefined按无效值处理，NaN和Infinity会导致Matrix2D异常，设置后绘制内容不显示。&lt;br/&gt;默认单位：vp

**Type:** number

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the FA model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-Matrix2D-translateX?: number--><!--Device-Matrix2D-translateX?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## translateY

```TypeScript
translateY?: number
```

垂直平移距离，取值范围无限制。&lt;br/&gt;异常值undefined按无效值处理，NaN和Infinity会导致Matrix2D异常，设置后绘制内容不显示。&lt;br/&gt;默认单位：vp

**Type:** number

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the FA model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-Matrix2D-translateY?: number--><!--Device-Matrix2D-translateY?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

