# Ellipse

椭圆绘制组件。该组件通过设置宽度和高度属性绘制椭圆形状，在给定的矩形区域内渲染椭圆轮廓和填充区域。

> **说明：**
>
> 该组件从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 子组件

无

## Ellipse

```TypeScript
Ellipse(options?: EllipseOptions)
```

use new function to set the value.Anonymous Object Rectification.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-EllipseInterface-new (options?: EllipseOptions): EllipseAttribute--><!--Device-EllipseInterface-new (options?: EllipseOptions): EllipseAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [EllipseOptions](arkts-arkui-ellipseoptions-i.md) | No | ellipse options |

## Ellipse

```TypeScript
Ellipse(options?: EllipseOptions)
```

用于绘制椭圆的构造函数。调用后创建一个Ellipse对象，可设置宽高属性。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-EllipseInterface-(options?: EllipseOptions): EllipseAttribute--><!--Device-EllipseInterface-(options?: EllipseOptions): EllipseAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [EllipseOptions](arkts-arkui-ellipseoptions-i.md) | No | 椭圆绘制配置选项，包含宽度和高度设置。不传入时使用默认尺寸（宽度和高度均为0）。 <br>异常值undefined和null按照无效值处理，本次设置不生效。 |

## Summary

- [EllipseOptions](arkts-arkui-ellipse-ellipseoptions-i.md)
