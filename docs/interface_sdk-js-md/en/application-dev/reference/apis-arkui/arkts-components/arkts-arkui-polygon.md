# Polygon

The **Polygon** component is used to draw a polygon. > **NOTE** > > This component supports dynamic constructor parameter updates using the > [updateConstructorParams](../../../reference/apis-arkui/js-apis-arkui-AttributeUpdater.md#properties) API of the > [AttributeUpdater](../../../reference/apis-arkui/js-apis-arkui-AttributeUpdater.md) class since API version 20. > > **Child Components** > > None

## Polygon

```TypeScript
Polygon(options?: PolygonOptions)
```

Uses new to create Polygon. Anonymous Object Rectification.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** 
- API version 9 and later: SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [PolygonOptions](arkts-arkui-polygonoptions-i.md) | No | Polygon options |

## Polygon

```TypeScript
Polygon(options?: PolygonOptions)
```

Defines the constructor of Polygon component.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [PolygonOptions](arkts-arkui-polygonoptions-i.md) | No | Options of the polygon.The **undefined** and **null** values are treated as invalid and will not take effect. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [PolygonOptions](arkts-arkui-polygonoptions-i.md) | Describes the options of the polygon. |

## Examples

This example demonstrates how to use points, fill, fillOpacity, and stroke to draw polygons with specific coordinates, fill colors, opacity, and stroke colors.

```TypeScript
// xxx.ets
@Entry
@Component
struct PolygonExample {
  build() {
    Column({ space: 10 }) {
      // Draw a triangle in a 100 × 100 rectangle. The start point is (0, 0), the end point is (100, 0), and the passing point is (50, 100).
      Polygon({ width: 100, height: 100 })
        .points([[0, 0], [50, 100], [100, 0]])
        .fill(Color.Green)
      // Draw a quadrilateral in a 100 × 100 rectangle. The start point is (0, 0), the end point is (100, 0), and the passing points are (0, 100) and (100, 100).
      Polygon()
        .width(100)
        .height(100)
        .points([[0, 0], [0, 100], [100, 100], [100, 0]])
        .fillOpacity(0)
        .strokeWidth(5)
        .stroke(Color.Blue)
      // Draw a pentagon in a 100 × 100 rectangle. The start point is (50, 0), the end point is (100, 50), and the passing points are (0, 50), (20, 100), and (80, 100).
      Polygon()
        .width(100)
        .height(100)
        .points([[50, 0], [0, 50], [20, 100], [80, 100], [100, 50]])
        .fill(Color.Red)
        .fillOpacity(0.6)
    }.width('100%').margin({ top: 10 })
  }
}
```

This example demonstrates how to draw a polygon using different length types of the width and height attributes.

```TypeScript
// xxx.ets
@Entry
@Component
struct PolygonTypeExample {
  build() {
    Column({ space: 10 }) {
      // Draw a triangle in a 100 × 100 rectangle. The start point is (0, 0), the end point is (100, 0), and the passing point is (50, 100).
      Polygon({ width: '100', height: '100' }) // Use the string type.
        .points([[0, 0], [50, 100], [100, 0]])
      // Draw a quadrilateral in a 100 × 100 rectangle. The start point is (0, 0), the end point is (100, 0), and the passing points are (0, 100) and (100, 100).
      Polygon({ width: 100, height: 100 })// Use the number type.
        .points([[0, 0], [0, 100], [100, 100], [100, 0]])
        .fillOpacity(0)
        .strokeWidth(5)
        .stroke(Color.Blue)
      // Draw a pentagon in a 100 × 100 rectangle. The start point is (50, 0), the end point is (100, 50), and the passing points are (0, 50), (20, 100), and (80, 100).
      Polygon({ width: $r('app.string.PolygonWidth'), height: $r('app.string.PolygonHeight') }) // Use the Resource type, which needs to be customized.
        .points([[50, 0], [0, 50], [20, 100], [80, 100], [100, 50]])
        .fillOpacity(0.6)
    }.width('100%').margin({ top: 10 })
  }
}
```

This example shows how to use attributeModifier to dynamically set the points, fill, fillOpacity, stroke, strokeDashArray, strokeDashOffset, strokeLineCap, strokeLineJoin, strokeMiterLimit, strokeOpacity, strokeWidth, and antiAlias attributes of the Polygon component.

```TypeScript
// xxx.ets
class MyPolygonModifier implements AttributeModifier<PolygonAttribute> {
  applyNormalAttribute(instance: PolygonAttribute): void {
    // Triangle starting at (0, 0), passing through (50, 100), and ending at (100, 0). Fill color: #707070; fill opacity: 0.5; stroke color: #2787D9; stroke dash array: [20]; offset to left: 15; cap style: semi-circle; join style: miter; miter limit: 5; stroke opacity: 0.5; stroke width: 10; anti-aliasing enabled.
    instance.points([[0, 0], [50, 100], [100, 0]])
    instance.fill("#707070")
    instance.fillOpacity(0.5)
    instance.stroke("#2787D9")
    instance.strokeDashArray([20])
    instance.strokeDashOffset("15")
    instance.strokeLineCap(LineCapStyle.Round)
    instance.strokeLineJoin(LineJoinStyle.Miter)
    instance.strokeMiterLimit(5)
    instance.strokeOpacity(0.5)
    instance.strokeWidth(10)
    instance.antiAlias(true)
  }
}

@Entry
@Component
struct PolygonModifierDemo {
  @State modifier: MyPolygonModifier = new MyPolygonModifier()

  build() {
    Column() {
      Polygon()
        .width(100)
        .height(100)
        .attributeModifier(this.modifier)
        .offset({ x: 20, y: 20 })
    }
  }
}
```
