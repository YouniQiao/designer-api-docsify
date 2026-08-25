# ShapeAttribute

绘制组件的父组件，父组件中会描述所有绘制组件均支持的通用属性。1、绘制组件使用Shape作为父组件，实现类似SVG的效果。2、绘制组件单独使用，用于在页面上绘制指定的图形。@extends CommonMethod @interface ShapeAttribute

**继承/实现关系：** ShapeAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## antiAlias

```TypeScript
default antiAlias(value: boolean | undefined): this
```

设置是否开启抗锯齿效果，支持 attributeModifier 动态设置属性方法。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ShapeAttribute](arkts-arkui-shape-shapeattribute-i.md) |

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<ShapeAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Call attributeModifier.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[ShapeAttribute](arkts-arkui-shape-shapeattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ShapeAttribute](arkts-arkui-shape-shapeattribute-i.md) |

## fill

```TypeScript
default fill(value: ResourceColor | undefined): this
```

设置填充区域的颜色，支持 attributeModifier 动态设置属性方法，异常值按照默认值处理。 与通用属性foregroundColor同时设置时，后设置的属性生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ShapeAttribute](arkts-arkui-shape-shapeattribute-i.md) |

## fillOpacity

```TypeScript
default fillOpacity(value: double | string | Resource | undefined): this
```

设置填充区域透明度，支持 attributeModifier 动态设置属性方法。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ShapeAttribute](arkts-arkui-shape-shapeattribute-i.md) |

## mesh

```TypeScript
default mesh(value: Array<double> | undefined, column: int | undefined, row: int | undefined): this
```

设置网格效果。将图像分割为（row + 1）* (column + 1)的网格， 每个网格交点坐标存储在数组中（每两个元素表示一个交点的x、y坐标）。 通过数组value中的坐标值，重新定位网格顶点位置，实现图像局部扭曲。 支持 attributeModifier 动态设置属性方法。

> 说明：&gt;
> mesh只对shape传入pixelMap时生效，且效果作用于传入的pixelMap。
> 与[绘制模块](../../apis-arkgraphics2d/arkts-apis/arkts-graphics-drawing.md)的
> [drawPixelMapMesh](../../../reference/apis-arkgraphics2d/arkts-apis-graphics-drawing-Canvas.md#drawpixelmapmesh)
> 效果一致，建议使用drawPixelMapMesh。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Array & lt;double & gt; \ | undefined | 是 |
| column | int \| undefined | 是 |
| row | int \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ShapeAttribute](arkts-arkui-shape-shapeattribute-i.md) |

## setShapeOptions

```TypeScript
default setShapeOptions(value?: PixelMap): this
```

Set Shape options.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [ShapeAttribute](arkts-arkui-shape-shapeattribute-i.md) |

## stroke

```TypeScript
default stroke(value: ResourceColor | undefined): this
```

设置边框颜色，支持 attributeModifier 动态设置属性方法，不设置时，默认边框透明度为0，即没有边框。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ShapeAttribute](arkts-arkui-shape-shapeattribute-i.md) |

## strokeDashArray

```TypeScript
default strokeDashArray(value: Array<Length> | undefined): this
```

设置边框间隙，支持 attributeModifier 动态设置属性方法。取值范围为≥0，异常值按照默认值处理。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Array&lt;[Length](arkts-arkui-length-t.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ShapeAttribute](arkts-arkui-shape-shapeattribute-i.md) |

## strokeDashOffset

```TypeScript
default strokeDashOffset(value: Length | undefined): this
```

设置边框绘制起点的偏移量，支持 attributeModifier 动态设置属性方法。异常值按照默认值处理。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ShapeAttribute](arkts-arkui-shape-shapeattribute-i.md) |

## strokeLineCap

```TypeScript
default strokeLineCap(value: LineCapStyle | undefined): this
```

设置边框端点绘制样式，支持 attributeModifier 动态设置属性方法。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [LineCapStyle](arkts-arkui-linecapstyle-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ShapeAttribute](arkts-arkui-shape-shapeattribute-i.md) |

## strokeLineJoin

```TypeScript
default strokeLineJoin(value: LineJoinStyle | undefined): this
```

设置边框拐角绘制样式，支持 attributeModifier 动态设置属性方法。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [LineJoinStyle](arkts-arkui-linejoinstyle-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ShapeAttribute](arkts-arkui-shape-shapeattribute-i.md) |

## strokeMiterLimit

```TypeScript
default strokeMiterLimit(value: Length | undefined): this
```

设置斜接长度与边框宽度比值的极限值，支持 attributeModifier 动态设置属性方法。 斜接长度表示外边框外边交点到内边交点的距离，边框宽度即strokeWidth属性的值。 该属性取值需在strokeLineJoin属性取值LineJoinStyle.Miter时生效。该属性的合法值范围应当大于等于1.0，当取值范围在[0,1)时按1.0处理，其余异常值按默认值处理。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ShapeAttribute](arkts-arkui-shape-shapeattribute-i.md) |

## strokeOpacity

```TypeScript
default strokeOpacity(value: double | string | Resource | undefined): this
```

设置边框透明度，支持 [attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier) 动态设置属性方法。 该属性的取值范围是[0.0, 1.0]，若给定值小于0.0，则取值为0.0；若给定值大于1.0，则取值为1.0。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ShapeAttribute](arkts-arkui-shape-shapeattribute-i.md) |

## strokeWidth

```TypeScript
default strokeWidth(value: Length | undefined): this
```

设置边框宽度，支持 attributeModifier 动态设置属性方法。该属性若为string类型，暂不支持百分比，百分比按照1px处理。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ShapeAttribute](arkts-arkui-shape-shapeattribute-i.md) |

## viewPort

```TypeScript
default viewPort(value: ViewportRect | undefined): this
```

设置形状的视口。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ViewportRect](arkts-arkui-shape-viewportrect-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ShapeAttribute](arkts-arkui-shape-shapeattribute-i.md) |
