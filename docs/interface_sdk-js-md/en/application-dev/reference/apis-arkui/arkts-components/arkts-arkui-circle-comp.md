# Circle

The **Circle** component is used to draw a circle.

## Child Components

None

## Circle

```TypeScript
Circle(value?: CircleOptions)
```

Creates a circle. After the call, a **Circle** object is created, and its width and height can be set.

**Since:** 7

**Model restriction:** This API can be used in both the stage model and FA model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [CircleOptions](arkts-arkui-circle-comp-circleoptions-i.md) | No | Circle size. Pass this parameter when you need to customize the circle size. If it is not passed, width and height default to **0**.<br>The abnormal values **undefined** and **null** are processed as invalid values, and this setting does not take effect. |

## Circle

```TypeScript
Circle(value?: CircleOptions)
```

Creates a circle. After the call, a **Circle** object is created, and its width and height can be set.

**Since:** 7

**Model restriction:** This API can be used in both the stage model and FA model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [CircleOptions](arkts-arkui-circle-comp-circleoptions-i.md) | No | Circle size. Pass this parameter when you need to customize the circle size. If it is not passed, width and height default to **0**.<br>The abnormal values **undefined** and **null** are treated as invalid values, and this setting does not take effect. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [CircleOptions](arkts-arkui-circle-comp-circleoptions-i.md) | Describes the drawing attributes of the **Circle** component. |

## Examples

```TypeScript
### Example 1: Drawing a Circle

This example demonstrates how to set the opacity, stroke color, and stroke dash style of a circle by setting the fillOpacity, stroke, and strokeDashArray attributes, respectively.


```

```TypeScript
### Example 2: Drawing a Circle with Different Parameter Types for Width and Height

This example demonstrates how to draw a circle using different length types of the width and height attributes.


```

```TypeScript
### Example 3: Dynamically Setting Attributes of the Circle Component Using attributeModifier

This example shows how to use attributeModifier to dynamically set the fill, fillOpacity, stroke, strokeDashArray, strokeDashOffset, strokeLineCap, strokeOpacity, strokeWidth, and antiAlias attributes of the Circle component.


```

```TypeScript
### Example 4: Using ColorMetrics to Set HDR Fill and Stroke Colors

You can use ColorMetrics to set HDR colors for the Circle component, achieving a brightness effect beyond the normal display range. The [fill](#fill) API is used to set the color of the fill area, and the [stroke](#stroke) API is used to set the stroke color. In the following example, the left side uses an HDR warm gold fill and an ice blue stroke (with a brightness multiplier greater than 1.0), while the right side uses ordinary SDR colors as a comparison. On an HDR-capable screen, the left side is noticeably brighter and more vivid than the right side.

Since API version 26.0.0, the Circle component-specific [fill](#fill) and [stroke](#stroke) APIs are added, which support passing the ColorMetrics type to achieve the HDR brightening effect.
```
