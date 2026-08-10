# Line

Line组件用于在应用界面中绘制直线，支持自定义直线的起点、终点、颜色、宽度、透明度、虚线样式、端点样式等属性。适用于绘制分隔线、装饰性线条、图表中的坐标轴或连接线、自定义图形边框等场景。

> **说明：**
>
> 该组件从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
>
> 该组件从API version 20开始支持使用[AttributeUpdater]{@link ../../../arkui/AttributeUpdater}类的
> [updateConstructorParams](docroot://reference/apis-arkui/js-apis-arkui-AttributeUpdater.md#属性)接口更新构造参数。
>
> - Line组件无法形成闭合区域，fill和fillOpacity属性设置无效。
>
> - Line组件不支持拐角，strokeLineJoin和strokeMiterLimit属性设置无效。

## 子组件

无

## Line

```TypeScript
Line(options?: LineOptions)
```

Uses new to create the line.Anonymous Object Rectification.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-LineInterface-new (options?: LineOptions): LineAttribute--><!--Device-LineInterface-new (options?: LineOptions): LineAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [LineOptions](../arkts-apis/arkts-arkui-line-lineoptions-i.md) | No | Line options |

## Line

```TypeScript
Line(options?: LineOptions)
```

用于绘制直线的构造函数。Line组件在width和height定义的矩形区域内绘制直线，绘制区域的左上角为坐标原点(0,0)，x轴向右延伸，y轴向下延伸。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-LineInterface-(options?: LineOptions): LineAttribute--><!--Device-LineInterface-(options?: LineOptions): LineAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [LineOptions](../arkts-apis/arkts-arkui-line-lineoptions-i.md) | No | Line组件绘制区域，包含width和height属性，用于设置Line组件的宽高。不传递此参数时，Line组件的width和height属性将按照各自属性的缺 省逻辑处理（参见LineOptions对象说明）。 <br>异常值undefined和null按照无效值处理，本次设置不生效。 |

## Summary

- [LineOptions](arkts-arkui-line-lineoptions-i.md)
