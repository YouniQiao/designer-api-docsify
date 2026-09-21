# Polygon

The **Polygon** component is used to draw a polygon. This component defines the shape of a polygon by setting a list of vertex coordinates, and supports attribute configuration such as fill color and border style. The component uses a two-dimensional coordinate system and connects the vertices in sequence to form a closed polygon area. It is suitable for drawing custom polygon shapes such as triangles, quadrilaterals, and pentagons, as well as for implementing visualization scenarios such as charts and icons that require polygon elements.

> **NOTE** > > Since API version 20, this component supports updating constructor parameters through the > [updateConstructorParams](../../../reference/apis-arkui/js-apis-arkui-AttributeUpdater.md#properties) API of the > [AttributeUpdater](../arkts-apis/arkts-arkui-attributeupdater-c.md) class.

## Child Components

None

## Polygon

```TypeScript
Polygon(options?: PolygonOptions)
```

Draws a polygon.

**Since:** 7

**Model restriction:** This API can be used in both the stage model and FA model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** 
- API version 9 and later: SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [PolygonOptions](arkts-arkui-polygon-comp-polygonoptions-i.md) | No | Configuration options of the **Polygon** component, used to define the width and height of the drawing area. Pass this parameter when the polygon size needs to be specified. If it is not passed, the default width and height (both 0) are used. If **undefined** or **null** is passed, the parameter setting does not take effect and the component attributes remain unchanged. |

## Polygon

```TypeScript
Polygon(options?: PolygonOptions)
```

Draws a polygon.

**Since:** 7

**Model restriction:** This API can be used in both the stage model and FA model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [PolygonOptions](arkts-arkui-polygon-comp-polygonoptions-i.md) | No | Configuration options of the **Polygon** component, used to define the width and height of the drawing area. Pass this parameter when the polygon size needs to be specified. If it is not passed, the default width and height (both 0) are used. If **undefined** or **null** is passed, the parameter setting does not take effect and the component attribute remains unchanged. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [PolygonOptions](arkts-arkui-polygon-comp-polygonoptions-i.md) | Describes the options of the polygon. |

## Examples

```TypeScript
### Example 1: Drawing a Polygon

This example draws the vertex coordinates, fill color, fill opacity, border color, and border width of the polygon through the points, fill, fillOpacity, stroke, and strokeWidth attributes, respectively.


```

```TypeScript
### Example 2: Drawing a Polygon with Different Parameter Types for Width and Height

This example demonstrates how to draw a polygon using different length types of the width and height attributes.


```

```TypeScript
### Example 3: Dynamically Setting Attributes of the Polygon Component Using attributeModifier

This example shows how to use attributeModifier to dynamically set the points, fill, fillOpacity, stroke, strokeDashArray, strokeDashOffset, strokeLineCap, strokeLineJoin, strokeMiterLimit, strokeOpacity, strokeWidth, and antiAlias attributes of the Polygon component.
```
