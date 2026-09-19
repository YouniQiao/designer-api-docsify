# Rect

The **Rect** component is used to draw a rectangle. It supports setting attributes such as fill color, stroke style, and rounded corners.

> **NOTE** > > Since API version 20, this component supports using the > [updateConstructorParams](../../../reference/apis-arkui/js-apis-arkui-AttributeUpdater.md#properties) API of the > AttributeUpdater class to update constructor parameters.

## Child Components

None

## Rect

```TypeScript
Rect(
    options?: RectOptions | RoundedRectOptions,
  )
```

Draws a rectangle. After being called, it creates a **Rect** object, for which attributes such as width, height, and rounded corners can be set.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RectOptions](arkts-arkui-rectoptions-i.md) &#124; [RoundedRectOptions](arkts-arkui-roundedrectoptions-i.md) | No | Drawing attributes of the rectangle, including the width, height, and rounded corners. If this parameter is not set, the rectangle is drawn with the default values of the attributes (the width, height, and rounded corners are all 0).<br>The abnormal values **undefined** and **null** are treated as invalid values, and the setting does not take effect. |

## Rect

```TypeScript
Rect(
    options?: RectOptions | RoundedRectOptions,
  )
```

Draws a rectangle. After being called, it creates a **Rect** object, for which attributes such as width, height, and rounded corners can be set.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RectOptions](arkts-arkui-rectoptions-i.md) &#124; [RoundedRectOptions](arkts-arkui-roundedrectoptions-i.md) | No | Rect drawing attributes, including the width, height, and rounded corner configurations. If this parameter is not passed, the rectangle is drawn with the default values of the attributes (the width, height, and rounded corners are all 0).<br>The abnormal values **undefined** and **null** are treated as invalid values, and this setting does not take effect. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [RectOptions](arkts-arkui-rectoptions-i.md) | Describes the drawing attributes of the **Rect** component. |
| [RoundedRectOptions](arkts-arkui-roundedrectoptions-i.md) | Describes the drawing attributes of the rounded rectangle component. |

## Examples

```TypeScript
### Example 1: Drawing a Rectangle

This example demonstrates how to use fill, fillOpacity, stroke, and radius to draw rectangles with specific fill colors, opacity, stroke colors, and rounded corners.


```

```TypeScript
### Example 2: Drawing a Gradient Rectangle

This example uses the universal attributes [linearGradient](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-gradient-color.md#lineargradient18) and [clipShape](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-sharp-clipping.md#clipshape18) to draw a rectangle with a gradient color.

The universal attributes linearGradient and clipShape are supported since API version 18.


```

```TypeScript
### Example 3: Drawing a Rectangle with Different Parameter Types

This example demonstrates how to draw a rectangle using different parameter types for the width, height, radius, radiusWidth, and radiusHeight attributes.


```

```TypeScript
### Example 4: Dynamically Setting Attributes of the Rect Component Using attributeModifier

This example shows how to use attributeModifier to dynamically set the fill, fillOpacity, stroke, strokeDashArray, strokeDashOffset, strokeLineCap, strokeLineJoin, strokeMiterLimit, strokeOpacity, strokeWidth, and antiAlias attributes of the Rect component.
```
