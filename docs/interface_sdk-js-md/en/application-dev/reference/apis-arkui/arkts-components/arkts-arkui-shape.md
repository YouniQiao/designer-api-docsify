# Shape

绘制组件的父组件，描述所有绘制组件均支持的通用属性。

Shape组件通过定义视口、填充、边框等属性，支持矢量图形的绘制和组合。Shape作为容器组件，可包含Rect、Circle、Path等绘制子组件，实现类似SVG（Scalable Vector Graphics，可缩放矢量图形）的矢
量图形绘制能力。

Shape组件的两种使用方式：

1、绘制组件使用Shape作为父组件，实现类似SVG的矢量图形的组合绘制。

2、绘制组件单独使用，用于在页面上绘制指定的图形。

> **说明：**
>
> 该组件从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
>
> 该组件从API version 20开始支持使用[AttributeUpdater]{@link ../../../arkui/AttributeUpdater}类的
> [updateConstructorParams](docroot://reference/apis-arkui/js-apis-arkui-AttributeUpdater.md#属性)接口更新构造参数。

## 子组件

包含[Rect]{@link rect}、[Path]{@link path}、[Circle]{@link circle}、[Ellipse]{@link ellipse}、[Polyline]{@link polyline}、  
[Polygon]{@link polygon}、[Image]{@link image}、[Text]{@link text}、[Column]{@link column}、[Row]{@link row}和Shape子组件。

## Shape

```TypeScript
Shape(value?: PixelMap)
```

Use the new function to create Shape.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ShapeInterface-new (value?: PixelMap): ShapeAttribute--><!--Device-ShapeInterface-new (value?: PixelMap): ShapeAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [PixelMap](arkts-arkui-pixelmap-t.md) | No |  |

## Shape

```TypeScript
Shape(value: PixelMap)
```

用于绘制Shape组件的构造函数。 

从API version 9开始，该接口支持在ArkTS卡片中使用，卡片中不支持使用PixelMap对象。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ShapeInterface-(value: PixelMap): ShapeAttribute--><!--Device-ShapeInterface-(value: PixelMap): ShapeAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [PixelMap](arkts-arkui-pixelmap-t.md) | Yes | 绘制目标，可将图形绘制在指定的PixelMap对象中，若未设置，则默认在当前绘制目标中进行绘制。<br/>异常值undefined和null按照无效值处理，本次设置不生效。 |

## Shape

```TypeScript
Shape()
```

Called when a component is drawn.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ShapeInterface-(): ShapeAttribute--><!--Device-ShapeInterface-(): ShapeAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Summary

- [ViewportRect](arkts-arkui-shape-viewportrect-i.md)
