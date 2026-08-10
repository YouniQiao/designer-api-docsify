# Polyline

折线绘制组件。

> **说明：**
>
> 该组件从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
>
> 该组件从API version 20开始支持使用[AttributeUpdater]{@link ../../../arkui/AttributeUpdater}类的
> [updateConstructorParams](docroot://reference/apis-arkui/js-apis-arkui-AttributeUpdater.md#属性)接口更新构造参数。

## 子组件

无

## Polyline

```TypeScript
Polyline(options?: PolylineOptions)
```

Uses new to create Polyline.Anonymous Object Rectification.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-PolylineInterface-new (options?: PolylineOptions): PolylineAttribute--><!--Device-PolylineInterface-new (options?: PolylineOptions): PolylineAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [PolylineOptions](arkts-arkui-polylineoptions-i.md) | No | Poly line options |

## Polyline

```TypeScript
Polyline(options?: PolylineOptions)
```

用于绘制折线的构造函数。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-PolylineInterface-(options?: PolylineOptions): PolylineAttribute--><!--Device-PolylineInterface-(options?: PolylineOptions): PolylineAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [PolylineOptions](arkts-arkui-polylineoptions-i.md) | No | Polyline绘制区域，用于设置Polyline组件的宽度和高度。当需要指定Polyline的绘制区域大小时传入此参数，不传入时使用默认宽度和高度（均 为0）。 <br>异常值undefined和null按照无效值处理，本次设置不生效。 |

## Summary

- [PolylineOptions](arkts-arkui-polyline-polylineoptions-i.md)
