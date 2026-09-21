# Polyline

The **Polyline** component is used to draw a polyline.

> **NOTE** > > This component is supported since API version 7. Updates to new APIs in later versions are marked with a > superscript to indicate their earliest API version. > > This component supports updating constructor parameters through the > [updateConstructorParams](../../../reference/apis-arkui/js-apis-arkui-AttributeUpdater.md#properties) API of the > [AttributeUpdater](../arkts-apis/arkts-arkui-attributeupdater-c.md) class since API version 20.

## Child Components

None

## Polyline

```TypeScript
Polyline(options?: PolylineOptions)
```

Creates a polyline.

**Since:** 7

**Model restriction:** This API can be used in both the stage model and FA model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [PolylineOptions](arkts-arkui-polyline-comp-polylineoptions-i.md) | No | Drawing area of the polyline, used to set the width and height of the **Polyline** component. Pass this parameter when the drawing area size of the polyline needs to be specified. If it is not passed, the default width and height (both 0) are used.<br>The abnormal values **undefined** and **null** are processed as invalid values, and this setting does not take effect. |

## Polyline

```TypeScript
Polyline(options?: PolylineOptions)
```

Creates a polyline.

**Since:** 7

**Model restriction:** This API can be used in both the stage model and FA model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [PolylineOptions](arkts-arkui-polyline-comp-polylineoptions-i.md) | No | Drawing area of the **Polyline**, used to set the width and height of the **Polyline** component. Pass this parameter when the drawing area size of the **Polyline** needs to be specified. If it is not passed, the default width and height (both 0) are used.<br>The abnormal values **undefined** and **null** are processed as invalid values, and this setting does not take effect. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [PolylineOptions](arkts-arkui-polyline-comp-polylineoptions-i.md) | Describes the options of the polyline. |

## Examples

```TypeScript
### Example 1: Drawing a Polyline

This example draws the passing coordinates, opacity, stroke color, stroke width, join style, and endpoint style of the polyline through the points, fillOpacity, stroke, strokeWidth, strokeLineJoin, and strokeLineCap attributes, respectively.


```

```TypeScript
### Example 2: Drawing a Polyline with Different Parameter Types for Width and Height

This example demonstrates how to draw a polyline using different length types of the width and height attributes.


```

```TypeScript
### Example 3: Dynamically Setting Attributes of the Polyline Component Using attributeModifier

This example shows how to use attributeModifier to dynamically set the points, fill, fillOpacity, stroke, strokeDashArray, strokeDashOffset, strokeLineCap, strokeLineJoin, strokeMiterLimit, strokeOpacity, strokeWidth, and antiAlias attributes of the Polyline component.
```
