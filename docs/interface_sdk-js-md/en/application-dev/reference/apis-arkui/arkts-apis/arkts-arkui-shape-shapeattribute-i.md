# ShapeAttribute

绘制组件的父组件，父组件中会描述所有绘制组件均支持的通用属性。

1、绘制组件使用Shape作为父组件，实现类似SVG的效果。

2、绘制组件单独使用，用于在页面上绘制指定的图形。

**Inheritance/Implementation:** ShapeAttribute extends [CommonMethod](arkts-arkui-common-commonmethod-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface ShapeAttribute extends CommonMethod--><!--Device-unnamed-export declare interface ShapeAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## antiAlias

```TypeScript
default antiAlias(value: boolean | undefined): this
```

设置是否开启抗锯齿效果，支持  
[attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShapeAttribute-default antiAlias(value: boolean | undefined): this--><!--Device-ShapeAttribute-default antiAlias(value: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes | 是否开启抗锯齿效果。 true：开启抗锯齿；false：关闭抗锯齿。 默认值：true 异常值undefined和null按照false处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<ShapeAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Call attributeModifier.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShapeAttribute-default attributeModifier(modifier: AttributeModifier<ShapeAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-ShapeAttribute-default attributeModifier(modifier: AttributeModifier<ShapeAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;ShapeAttribute&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## fill

```TypeScript
default fill(value: ResourceColor | undefined): this
```

设置填充区域的颜色，支持  
[attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法，异常值按照默认值处理。与通用属性foregroundColor同时设置时，后设置的属性生效。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShapeAttribute-default fill(value: ResourceColor | undefined): this--><!--Device-ShapeAttribute-default fill(value: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes | 填充区域颜色。 默认值：[Color](../../../reference/apis-arkui/arkui-ts/ts-appendix-enums.md#color).Black 异常值undefined、null、NaN和Infinity按照默认值处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## fillOpacity

```TypeScript
default fillOpacity(value: double | string | Resource | undefined): this
```

设置填充区域透明度，支持  
[attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShapeAttribute-default fillOpacity(value: double | string | Resource | undefined): this--><!--Device-ShapeAttribute-default fillOpacity(value: double | string | Resource | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double \| string \| Resource \| undefined | Yes | 填充区域透明度。 说明： number格式取值范围是[0.0, 1.0]，若给定值小于0.0，则取值为0.0； 若给定值大于1.0，则取值为1.0，其余异常值按1.0处理。 string格式支持number格式取值的字符串形式，取值范围与number格式相同。 Resource格式支持系统资源或者应用资源中的字符串，取值范围和number格式相同。 异常值NaN按0.0处理，undefined、null和Infinity按1.0处理。 默认值：1.0 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## mesh

```TypeScript
default mesh(value: Array<double> | undefined, column: int | undefined, row: int | undefined): this
```

设置网格效果。将图像分割为（row + 1）* (column + 1)的网格，每个网格交点坐标存储在数组中（每两个元素表示一个交点的x、y坐标）。通过数组value中的坐标值，重新定位网格顶点位置，实现图像局部扭曲。支持  
[attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

> 说明：
> 
> mesh只对shape传入pixelMap时生效，且效果作用于传入的pixelMap。
> 与[绘制模块](../../../reference/apis-arkgraphics2d/arkts-apis-graphics-drawing.md)的
> [drawPixelMapMesh](../../../reference/apis-arkgraphics2d/arkts-apis-graphics-drawing-Canvas.md#drawpixelmapmesh12)
> 效果一致，建议使用drawPixelMapMesh。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShapeAttribute-default mesh(value: Array<double> | undefined, column: int | undefined, row: int | undefined): this--><!--Device-ShapeAttribute-default mesh(value: Array<double> | undefined, column: int | undefined, row: int | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Array&lt;double&gt; \| undefined | Yes | 长度（row + 1）* （column + 1）* 2的数组， 记录扭曲后的位图各个顶点位置。 设置异常值undefined时value按照空数组处理，设置空数组时column和row按0处理，value按空数组处理。 |
| column | int \| undefined | Yes | mesh矩阵列数。 设置异常值undefined时column和row按0处理，value按空数组处理。 |
| row | int \| undefined | Yes | mesh矩阵行数。 设置异常值undefined时column和row按0处理，value按空数组处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setShapeOptions

```TypeScript
default setShapeOptions(value?: PixelMap): this
```

Set Shape options.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShapeAttribute-default setShapeOptions(value?: PixelMap): this--><!--Device-ShapeAttribute-default setShapeOptions(value?: PixelMap): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) | No | Shape constructor options |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the ShapeAttribute. |

## stroke

```TypeScript
default stroke(value: ResourceColor | undefined): this
```

设置边框颜色，支持  
[attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法，不设置时，默认边框透明度为0，即没有边框。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShapeAttribute-default stroke(value: ResourceColor | undefined): this--><!--Device-ShapeAttribute-default stroke(value: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes | 边框颜色。 默认值：[Color](../../../reference/apis-arkui/arkui-ts/ts-appendix-enums.md#color).Transparent 异常值undefined和null按照默认值处理，NaN和Infinity按照 [Color](../../../reference/apis-arkui/arkui-ts/ts-appendix-enums.md#color).Black处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## strokeDashArray

```TypeScript
default strokeDashArray(value: Array<Length> | undefined): this
```

设置边框间隙，支持  
[attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。取值范围为≥0，异常值按照默认值处理。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShapeAttribute-default strokeDashArray(value: Array<Length> | undefined): this--><!--Device-ShapeAttribute-default strokeDashArray(value: Array<Length> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Array&lt;[Length](arkts-arkui-length-t.md)&gt; \| undefined | Yes | 定义Shape轮廓的虚线模式的数组， 数组元素交替表示线段长度和间隙长度。 默认值：[]（空数组） 默认单位：vp 异常值undefined和null按照默认值处理。 说明： 空数组：实线 偶数多元素数组：数组元素按顺序循环，如[a, b, c, d]表示线段长度a->间隙长度b->线段长度c->间隙长度d->线段长度a->... 奇数多元素数组：重复一次该数组元素，按偶数多元素数组的规则顺序循环， 如[a, b, c]等效于[a, b, c, a, b, c]，表示线段长度a->间隙长度b->线段长度c->间隙长度a->线段长度b->间隙长度c->线段长度a->... |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## strokeDashOffset

```TypeScript
default strokeDashOffset(value: Length | undefined): this
```

设置边框绘制起点的偏移量，支持  
[attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。异常值按照默认值处理。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShapeAttribute-default strokeDashOffset(value: Length | undefined): this--><!--Device-ShapeAttribute-default strokeDashOffset(value: Length | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | Yes | 边框绘制起点的偏移量。 默认值：0 默认单位：vp 异常值undefined和null按照默认值处理，NaN和Infinity会导致strokeDashArray失效。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## strokeLineCap

```TypeScript
default strokeLineCap(value: LineCapStyle | undefined): this
```

设置边框端点绘制样式，支持  
[attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShapeAttribute-default strokeLineCap(value: LineCapStyle | undefined): this--><!--Device-ShapeAttribute-default strokeLineCap(value: LineCapStyle | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [LineCapStyle](arkts-arkui-linecapstyle-e.md) \| undefined | Yes | 边框端点绘制样式。 默认值：LineCapStyle.Butt 异常值undefined、null、NaN和Infinity按照默认值处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## strokeLineJoin

```TypeScript
default strokeLineJoin(value: LineJoinStyle | undefined): this
```

设置边框拐角绘制样式，支持  
[attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShapeAttribute-default strokeLineJoin(value: LineJoinStyle | undefined): this--><!--Device-ShapeAttribute-default strokeLineJoin(value: LineJoinStyle | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [LineJoinStyle](arkts-arkui-linejoinstyle-e.md) \| undefined | Yes | 边框拐角绘制样式。 默认值：LineJoinStyle.Miter 异常值undefined、null、NaN和Infinity按照默认值处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## strokeMiterLimit

```TypeScript
default strokeMiterLimit(value: Length | undefined): this
```

设置斜接长度与边框宽度比值的极限值，支持  
[attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。斜接长度表示外边框外边交点到内边交点的距离，边框宽度即strokeWidth属性的值。该属性取值需在strokeLineJoin属性取值LineJoinStyle.Miter时生效。

该属性的合法值范围应当大于等于1.0，当取值范围在[0,1)时按1.0处理，其余异常值按默认值处理。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShapeAttribute-default strokeMiterLimit(value: Length | undefined): this--><!--Device-ShapeAttribute-default strokeMiterLimit(value: Length | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | Yes | 斜接长度与边框宽度比值的极限值。 默认值：4 异常值undefined、null和NaN按照默认值处理，Infinity会导致stroke失效。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## strokeOpacity

```TypeScript
default strokeOpacity(value: double | string | Resource | undefined): this
```

设置边框透明度，支持  
[attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。该属性的取值范围是[0.0, 1.0]，若给定值小于0.0，则取值为0.0；若给定值大于1.0，则取值为1.0。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShapeAttribute-default strokeOpacity(value: double | string | Resource | undefined): this--><!--Device-ShapeAttribute-default strokeOpacity(value: double | string | Resource | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double \| string \| Resource \| undefined | Yes | 边框透明度。 默认值：stroke接口设置的透明度。 异常值NaN按0.0处理，undefined、null和Infinity按1.0处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## strokeWidth

```TypeScript
default strokeWidth(value: Length | undefined): this
```

设置边框宽度，支持  
[attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。该属性若为string类型，暂不支持百分比，百分比按照1px处理。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShapeAttribute-default strokeWidth(value: Length | undefined): this--><!--Device-ShapeAttribute-default strokeWidth(value: Length | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | Yes | 边框宽度，取值范围≥0。 默认值：1 默认单位：vp 异常值undefined、null和NaN按照默认值处理，Infinity按0处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## viewPort

```TypeScript
default viewPort(value: ViewportRect | undefined): this
```

设置形状的视口。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShapeAttribute-default viewPort(value: ViewportRect | undefined): this--><!--Device-ShapeAttribute-default viewPort(value: ViewportRect | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ViewportRect](arkts-arkui-shape-viewportrect-i.md) \| undefined | Yes | Viewport绘制属性。 默认值：{} 异常值undefined和null按照默认值处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

