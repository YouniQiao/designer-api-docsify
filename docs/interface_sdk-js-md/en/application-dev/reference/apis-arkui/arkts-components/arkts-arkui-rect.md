# Rect

矩形绘制组件，用于在界面中绘制矩形图形，支持设置填充颜色、边框样式、圆角等属性。

> **说明：**
>
> 该组件从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
>
> 该组件从API version 20开始支持使用[AttributeUpdater]{@link ../../../arkui/AttributeUpdater}类的
> [updateConstructorParams](docroot://reference/apis-arkui/js-apis-arkui-AttributeUpdater.md#属性)接口更新构造参数。

## 子组件

无

## Rect

```TypeScript
Rect(
    options?: RectOptions | RoundedRectOptions,
  )
```

Use new function to create Rect.Anonymous Object Rectification.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-RectInterface-new (    options?: RectOptions | RoundedRectOptions,  ): RectAttribute--><!--Device-RectInterface-new (    options?: RectOptions | RoundedRectOptions,  ): RectAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RectOptions](../arkts-apis/arkts-arkui-rect-rectoptions-i.md) \| RoundedRectOptions | No | Rect options |

## Rect

```TypeScript
Rect(
    options?: RectOptions | RoundedRectOptions,
  )
```

用于绘制矩形的构造函数。调用后创建一个Rect对象，可设置宽度、高度、圆角等属性。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-RectInterface-(    options?: RectOptions | RoundedRectOptions,  ): RectAttribute--><!--Device-RectInterface-(    options?: RectOptions | RoundedRectOptions,  ): RectAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RectOptions](../arkts-apis/arkts-arkui-rect-rectoptions-i.md) \| RoundedRectOptions | No | Rect绘制属性，包含宽度、高度、圆角等配置。不传入时使用各属性默认值绘制矩形（宽高和圆角均为0）。 <br>异常值undefined和null按照无效值处理，本次设置不生效。 |

## Summary

- [RectOptions](arkts-arkui-rect-rectoptions-i.md)
- [RoundedRectOptions](arkts-arkui-rect-roundedrectoptions-i.md)
