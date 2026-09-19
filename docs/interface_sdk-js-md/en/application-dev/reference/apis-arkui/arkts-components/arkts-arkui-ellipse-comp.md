# Ellipse

The **Ellipse** component is used to draw an ellipse. It draws an ellipse shape by setting the width and height attributes, rendering the ellipse outline and fill area within a given rectangular region.

## Child Components

None

## Ellipse

```TypeScript
Ellipse(options?: EllipseOptions)
```

Constructor used to draw an ellipse. After being called, it creates an **Ellipse** object, for which the width and height attributes can be set.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [EllipseOptions](arkts-arkui-ellipseoptions-i.md) | No | Ellipse drawing configuration options, including the width and height settings. If not passed, the default size (both width and height are 0) is used.<br>The abnormal values **undefined** and **null** are handled as invalid values, and this setting does not take effect. <br>**Note:** Since API version 18, the **EllipseOptions** parameter must be used in the stage model. |

## Ellipse

```TypeScript
Ellipse(options?: EllipseOptions)
```

Constructor used to draw an ellipse. After being called, it creates an **Ellipse** object, for which the width and height attributes can be set.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [EllipseOptions](arkts-arkui-ellipseoptions-i.md) | No | Ellipse drawing configuration options, including the width and height settings. If not passed, the default size (both width and height are 0) is used.<br>The abnormal values **undefined** and **null** are handled as invalid values, and the setting does not take effect. <br>**Note:** Since API version 18, the EllipseOptions parameter must be used in the stage model. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [EllipseOptions](arkts-arkui-ellipseoptions-i.md) | Describes the options of the ellipse. |

## Examples

```TypeScript
### Example 1: Drawing an Ellipse

This example demonstrates how to use fillOpacity and stroke to set the opacity and stroke color of an ellipse.


```

```TypeScript
### Example 2: Drawing an Ellipse with Different Parameter Types for Width and Height

This example demonstrates how to draw an ellipse using different length types of the width and height attributes.


```

```TypeScript
### Example 3: Dynamically Setting Attributes of the Ellipse Component Using attributeModifier

This example shows how to use attributeModifier to dynamically set the fill, fillOpacity, stroke, strokeDashArray, strokeDashOffset, strokeLineCap, strokeOpacity, strokeWidth, and antiAlias attributes of the Ellipse component.
```
