# Shape属性/事件

除支持通用属性以及[图形绘制通用属性](../../../reference/apis-arkui/arkui-ts/ts-drawing-components-common.md)外，还支持以下 属性：

**继承/实现关系：** ShapeAttribute extends CommonMethod<ShapeAttribute>

**起始版本：** 7

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## antiAlias

```TypeScript
antiAlias(value: boolean)
```

设置是否开启抗锯齿效果，支持attributeModifier动态设置属性方法。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

## fill

```TypeScript
fill(value: ResourceColor)
```

设置填充区域的颜色，支持attributeModifier动态设置属性方法，异常值按照默认值处理。与通用属性foregroundColor同时设置时， 后设置的属性生效。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | 是 |

## fillOpacity

```TypeScript
fillOpacity(value: number | string | Resource)
```

设置填充区域透明度，支持attributeModifier动态设置属性方法。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 是 |

## mesh

```TypeScript
mesh(value: Array<any>, column: number, row: number)
```

设置网格效果。将图像分割为（row + 1）* （column + 1）的网格，每个网格交点坐标存储在数组中（每两个元素表示一个交点的x、y坐标）。通过数组value中的坐标值，重新定位网格顶点位置，实现图像局部扭曲。支持 attributeModifier动态设置属性方法。适用于需要实现图像变形效果的场景，如图片扭曲、波浪效果等视觉效果。坐标数组按行优先顺序存储。原始图像被均匀分割后，每个网格区域根据顶点的新坐标进行变换，最终形成扭曲效果。

> **说明：**&gt;
> mesh只对shape传入pixelMap时生效，且效果作用于传入的pixelMap。与[绘制模块](../../apis-arkgraphics2d/arkts-apis/arkts-graphics-drawing.md)的
> [drawPixelMapMesh&lt;sup&gt;12+&lt;/sup&gt;](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-drawing-canvas-c.md#drawpixelmapmesh)效果一致，建议使用
> drawPixelMapMesh。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Array & lt;any & gt; | 是 |
| [column](arkts-arkui-astcresource-i-sys.md) | number | 是 |
| row | number | 是 |

## stroke

```TypeScript
stroke(value: ResourceColor)
```

设置边框颜色，支持attributeModifier动态设置属性方法，不设置时，默认边框透明度为0，即没有边框。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | 是 |

## strokeDashArray

```TypeScript
strokeDashArray(value: Array<any>)
```

设置边框间隙，支持attributeModifier动态设置属性方法。取值范围为≥0，异常值按照默认值处理。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Array & lt;any & gt; | 是 |

## strokeDashOffset

```TypeScript
strokeDashOffset(value: Length)
```

设置边框绘制起点的偏移量，支持attributeModifier动态设置属性方法。异常值按照默认值处理。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | 是 |

## strokeLineCap

```TypeScript
strokeLineCap(value: LineCapStyle)
```

设置边框端点绘制样式，支持attributeModifier动态设置属性方法。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [LineCapStyle](../arkts-apis/arkts-arkui-linecapstyle-e.md) | 是 |

## strokeLineJoin

```TypeScript
strokeLineJoin(value: LineJoinStyle)
```

设置边框拐角绘制样式，支持attributeModifier动态设置属性方法。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [LineJoinStyle](../arkts-apis/arkts-arkui-linejoinstyle-e.md) | 是 |

## strokeMiterLimit

```TypeScript
strokeMiterLimit(value: Length)
```

设置斜接长度与边框宽度比值的极限值，支持attributeModifier动态设置属性方法。斜接长度表示外边框外边交点到内边交点的距离，边框宽度即 strokeWidth属性的值。该属性取值需在strokeLineJoin属性取值LineJoinStyle.Miter时生效。该属性的合法值范围应当大于等于1.0，当取值范围在[0,1)时按1.0处理，其余异常值按默认值处理。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | 是 |

## strokeOpacity

```TypeScript
strokeOpacity(value: number | string | Resource)
```

设置边框透明度，支持attributeModifier动态设置属性方法。该属性的取值范围是[0.0, 1.0]，若给定值小于0.0，则取值为0.0；若 给定值大于1.0，则取值为1.0。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 是 |

## strokeWidth

```TypeScript
strokeWidth(value: Length)
```

设置边框宽度，支持attributeModifier动态设置属性方法。该属性若为string类型，暂不支持百分比，百分比按照1px处理。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | 是 |

## viewPort

```TypeScript
viewPort(value: ViewportRect)
```

设置形状的视口。视口定义了绘制内容的坐标系统和显示区域。视口的起始点坐标(x, y)和宽高(width, height)决定了绘制内容在组件中的显示位置和范围。当视口范围与组件尺寸不同时，绘制内容会自动缩放适配。视口常用于调整绘制内容的显示比例和 位置。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ViewportRect](arkts-arkui-viewportrect-i.md) | 是 |
