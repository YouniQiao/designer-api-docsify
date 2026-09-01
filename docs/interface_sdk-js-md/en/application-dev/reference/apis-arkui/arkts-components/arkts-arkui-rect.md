# Rect

The **Rect** component is used to draw a rectangle. > **NOTE** > > This component supports dynamic constructor parameter updates using the > [updateConstructorParams](../../../reference/apis-arkui/js-apis-arkui-AttributeUpdater.md#properties) API of the > [AttributeUpdater](../../../reference/apis-arkui/js-apis-arkui-AttributeUpdater.md) class since API version 20. > > **Child Components** > > None

## Rect

```TypeScript
Rect(
    options?: RectOptions | RoundedRectOptions,
  )
```

Use new function to create Rect. Anonymous Object Rectification.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RectOptions](arkts-arkui-rectoptions-i.md) \| [RoundedRectOptions](arkts-arkui-roundedrectoptions-i.md) | No | Rect options |

## Rect

```TypeScript
Rect(
    options?: RectOptions | RoundedRectOptions,
  )
```

Defines the constructor of Rect component.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RectOptions](arkts-arkui-rectoptions-i.md) \| [RoundedRectOptions](arkts-arkui-roundedrectoptions-i.md) | No | Options of the rectangle. The **undefined** and **null** values are treated as invalid and will not take effect. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [RectOptions](arkts-arkui-rectoptions-i.md) | Describes the options of the rectangle. |
| [RoundedRectOptions](arkts-arkui-roundedrectoptions-i.md) | Describes the options of the rounded rectangle. |

## Examples

This example demonstrates how to use fill, fillOpacity, stroke, and radius to draw rectangles with specific fill colors, opacity, stroke colors, and rounded corners.

```TypeScript
// xxx.ets
@Entry
@Component
struct RectExample {
  build() {
    Column({ space: 10 }) {
      Text('normal').fontSize(11).fontColor(0xCCCCCC).width('90%')
      // Draw a 90% × 50 rectangle.
      Column({ space: 5 }) {
        Text('normal').fontSize(9).fontColor(0xCCCCCC).width('90%')
        // Draw a 90% × 50 rectangle.
        Rect({ width: '90%', height: 50 })
          .fill(Color.Pink)
        // Draw a 90% × 50 rectangle.
        Rect()
          .width('90%')
          .height(50)
          .fillOpacity(0)
          .stroke(Color.Red)
          .strokeWidth(3)

        Text('with rounded corners').fontSize(11).fontColor(0xCCCCCC).width('90%')
        // Draw a 90% × 80 rectangle, with the width and height of its rounded corners being 40 and 20, respectively.
        Rect({ width: '90%', height: 80 })
          .radiusHeight(20)
          .radiusWidth(40)
          .fill(Color.Pink)
        // Draw a 90% × 80 rectangle, with the width and height of its rounded corners being both 20.
        Rect({ width: '90%', height: 80 })
          .radius(20)
          .fill(Color.Pink)
          .stroke(Color.Transparent)
      }.width('100%').margin({ top: 10 })

      // Draw a 90% × 50 rectangle, with the width and height of its rounded corners as follows: 40 for the upper left rounded corner, 20 for the upper right rounded corner, 40 for the lower right rounded corner, and 20 for the lower left rounded corner.
      Rect({ width: '90%', height: 80 })
        .radius([[40, 40], [20, 20], [40, 40], [20, 20]])
        .fill(Color.Pink)
    }.width('100%').margin({ top: 5 })
  }
}
```

The universal attributes linearGradient and clipShape are supported since API version 18.

```TypeScript
// xxx.ets
@Entry
@Component
struct RectExample {
  build() {
    Column({ space: 10 }) {
      Column()
        .width(100)
        .height(100)
        .linearGradient({
          direction: GradientDirection.Right,
          colors: [[0xff0000, 0.0], [0x0000ff, 0.3], [0xffff00, 1.0]]
        })
        .clipShape(new Rect({ width: 100, height: 100, radius: 40 }))
      Rect()
        .width(100)
        .height(100)
        // Set the color of the fill area. To display the gradient color of the background, set .fillOpacity(0.0).
        .fill(Color.Pink)
        // Set the radius of the chamfer to 40.
        .radius(40)
        .stroke(Color.Black)
        // Set the gradient color. It takes effect only for a 100 × 100 rectangular area. The boundary of the gradient color does not contain chamfers.
        .linearGradient({
          direction: GradientDirection.Right,
          colors: [[0xff0000, 0.0], [0x0000ff, 0.3], [0xffff00, 1.0]]
        })
    }
  }
}
```

This example demonstrates how to draw a rectangle using different parameter types for the width, height, radius, radiusWidth, and radiusHeight attributes.

```TypeScript
// xxx.ets
@Entry
@Component
struct RectExample {
  build() {
    Column({ space: 10 }) {
      // Draw a 90% × 50 rectangle, with the radius of rounded corners being 5.
      Rect({ width: '90%', height: '50', radius: '5' }) // Use the string type.
        .fill(Color.Green)
      // Draw a 200 × 50 rectangle, with the radius of rounded corners being 5.
      Rect({ width: 200, height: 50, radius: 5 }) // Use the number type.
        .fillOpacity(0)
        .stroke(Color.Red)
        .strokeWidth(3)
      // Draw a 200 × 50 rectangle, with the width and height of its rounded corners being 80 and 20, respectively.
      Rect({
        width: $r('app.string.RectWidth'), // Use the Resource type, which needs to be customized.
        height: $r('app.string.RectHeight'),
        radius: $r('app.string.RectRadius')
      })
        .radiusWidth($r('app.string.RectRadiusWidth'))
        .radiusHeight($r('app.string.RectRadiusHeight'))
        .fill(Color.Green)
    }.width('100%').margin({ top: 5 })
  }
}
```

This example shows how to use attributeModifier to dynamically set the fill, fillOpacity, stroke, strokeDashArray, strokeDashOffset, strokeLineCap, strokeLineJoin, strokeMiterLimit, strokeOpacity, strokeWidth, and antiAlias attributes of the Rect component.

```TypeScript
// xxx.ets
class MyRectModifier implements AttributeModifier<RectAttribute> {
  applyNormalAttribute(instance: RectAttribute): void {
    // Fill color: #707070; fill opacity: 0.5; stroke color: #2787D9; stroke dash array: [20]; offset to left: 15; cap style: semi-circle; join style: miter; miter limit: 5; stroke opacity: 0.5; stroke width: 10; anti-aliasing enabled.
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
struct RectModifierDemo {
  @State modifier: MyRectModifier = new MyRectModifier()

  build() {
    Column() {
      Rect()
        .width(200)
        .height(200)
        .attributeModifier(this.modifier)
        .offset({ x: 20, y: 20 })
    }
  }
}
```
