# Line

The **Line** component is used to draw a straight line in the app UI. It supports customizing the start point, end point, color, width, opacity, dash style, and cap style of the line. It is suitable for drawing separators, decorative lines, coordinate axes or connecting lines in charts, and custom graphic borders.

> **NOTE** > > Since API version 20, this component supports updating constructor parameters through the > [updateConstructorParams](../../../reference/apis-arkui/js-apis-arkui-AttributeUpdater.md#properties) API of the > AttributeUpdater class. > > - The **Line** component cannot form a closed area, so the **fill** and **fillOpacity** attributes do not take > effect. > > - The **Line** component does not support corners, so the **strokeLineJoin** and **strokeMiterLimit** attributes do > not take effect.

## Child Components

None

## Line

```TypeScript
Line(options?: LineOptions)
```

Draws a straight line. The **Line** component draws the line within the rectangular area defined by **width** and **height**. The upper left corner of the drawing area is the coordinate origin (0,0), with the x-axis extending to the right and the y-axis extending downward.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [LineOptions](arkts-arkui-lineoptions-i.md) | No | Drawing area of the **Line** component, which contains the **width** and **height** attributes used to set the width and height of the **Line** component. If this parameter is not passed, the **width** and **height** attributes of the **Line** component are processed according to the default logic of their respective attributes (see the **LineOptions** object description).<br>The abnormal values **undefined** and **null** are processed as invalid values, and this setting does not take effect. |

## Line

```TypeScript
Line(options?: LineOptions)
```

Draws a straight line. The **Line** component draws the line within the rectangular area defined by **width** and **height**. The upper left corner of the drawing area is the coordinate origin (0,0), with the x-axis extending to the right and the y-axis extending downward.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [LineOptions](arkts-arkui-lineoptions-i.md) | No | Drawing area of the **Line** component, which contains the **width** and **height** attributes used to set the width and height of the **Line** component. If this parameter is not passed, the **width** and **height** attributes of the Line component are processed based on their respective default logic (see **LineOptions** object description).<br>The abnormal values **undefined** and **null** are processed as invalid values, and this setting does not take effect. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [LineOptions](arkts-arkui-lineoptions-i.md) | Describes the options of the line. |

## Examples

```TypeScript
### Example 1: Drawing a Line

This example draws the start point, end point, opacity, line color, line width, stroke gap, and drawing start point of the line through the startPoint, endPoint, strokeOpacity, stroke, strokeWidth, strokeDashArray, and strokeDashOffset attributes, respectively.


```

```TypeScript
### Example 2: Drawing Line Caps

This example draws the cap style of the line through the strokeLineCap attribute.


```

```TypeScript
### Example 3: Drawing Stroke Gaps

This example draws the stroke gaps through the strokeDashArray attribute.
```

```TypeScript
### Example 4: Drawing a Line with Different Parameter Types for Width and Height

This example demonstrates how to draw a line using different length types of the width and height attributes.


```

```TypeScript
### Example 5: Dynamically Setting Attributes of the Line Component Using attributeModifier

This example shows how to use attributeModifier to dynamically set the startPoint, endPoint, stroke, strokeDashArray, strokeDashOffset, strokeLineCap, strokeOpacity, strokeWidth, and antiAlias attributes of the Line component.
```
