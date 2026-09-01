# Path

The **Path** component is used to draw a custom closed shape based on a specified drawing path. > **Note** > > This component supports dynamic constructor parameter updates using the > [updateConstructorParams](../../../reference/apis-arkui/js-apis-arkui-AttributeUpdater.md#properties) API of the > [AttributeUpdater](../../../reference/apis-arkui/js-apis-arkui-AttributeUpdater.md) class since API version 20. > > **Child Components** > > None

## Path

```TypeScript
Path(options?: PathOptions)
```

Use new to create Path. Annonymous Object Rectification.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [PathOptions](arkts-arkui-pathoptions-i.md) | No | path options |

## Path

```TypeScript
Path(options?: PathOptions)
```

Defines the constructor of Path component

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [PathOptions](arkts-arkui-pathoptions-i.md) | No | Options of the path.The **undefined** and **null** values are treated as invalid and will not take effect. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [PathOptions](arkts-arkui-pathoptions-i.md) | Describes the options of the path. |

## Examples

This example demonstrates how to use commands, fillOpacity, and stroke to draw a closed shape with the specified path, opacity, and stroke color.

```TypeScript
// xxx.ets
@Entry
@Component
struct PathExample {
  build() {
    Column({ space: 10 }) {
      Text('Straight line')
        .fontSize(11)
        .fontColor(0xCCCCCC)
        .width('90%')
      // Draw a straight line whose length is 600 px and width is 3 vp.
      Path()
        .width('600px')
        .height('10px')
        .commands('M0 0 L600 0')
        .stroke(Color.Black)
        .strokeWidth(3)

      Text('Straight line graph')
        .fontSize(11)
        .fontColor(0xCCCCCC)
        .width('90%')
      // Draw a straight line.
      Flex({ justifyContent: FlexAlign.SpaceBetween }) {
        Path()
          .width('210px')
          .height('310px')
          .commands('M100 0 L200 240 L0 240 Z')
          .fillOpacity(0)
          .stroke(Color.Black)
          .strokeWidth(3)
        Path()
          .width('210px')
          .height('310px')
          .commands('M0 0 H200 V200 H0 Z')
          .fillOpacity(0)
          .stroke(Color.Black)
          .strokeWidth(3)
        Path()
          .width('210px')
          .height('310px')
          .commands('M100 0 L0 100 L50 200 L150 200 L200 100 Z')
          .fillOpacity(0)
          .stroke(Color.Black)
          .strokeWidth(3)
      }.width('95%')

      Text('Curve graphics').fontSize(11).fontColor(0xCCCCCC).width('90%')
      // Draw an arc.
      Flex({ justifyContent: FlexAlign.SpaceBetween }) {
        Path()
          .width('250px')
          .height('310px')
          .commands("M0 300 S100 0 240 300 Z")
          .fillOpacity(0)
          .stroke(Color.Black)
          .strokeWidth(3)
        Path()
          .width('210px')
          .height('310px')
          .commands('M0 150 C0 100 140 0 200 150 L100 300 Z')
          .fillOpacity(0)
          .stroke(Color.Black)
          .strokeWidth(3)
        Path()
          .width('210px')
          .height('310px')
          .commands('M0 100 A30 20 20 0 0 200 100 Z')
          .fillOpacity(0)
          .stroke(Color.Black)
          .strokeWidth(3)
      }.width('95%')
    }.width('100%')
    .margin({ top: 5 })
  }
}
```

This example demonstrates how to draw a path using different length types of the width, height, and commands attributes.

```TypeScript
// xxx.ets
@Entry
@Component
struct PathTypeExample {
  build() {
    Column({ space: 10 }) {
      // Use the string type for the width, height, and commands attributes to draw a line.
      Path({ width: '600px', height: '10px' })
        .commands('M0 0 L600 0')
        .fillOpacity(0)
        .stroke(Color.Black)
        .strokeWidth(3)
      // Use the number type for the width and height attributes to draw a rectangle.
      Path({ width: 200, height: 100 })
        .commands('M200 0 H400 V200 H200 Z')
        .fillOpacity(0)
        .stroke(Color.Black)
        .strokeWidth(3)
      // Use the Resource type (customized by yourself) for the width, height, and commands attributes to draw an arc.
      Path({ width: $r('app.string.PathWidth'), height: $r('app.string.PathHeight') }) // In this example, PathWidth and PathHeight are both defined as 200.
        .commands($r('app.string.PathCommands')) // In this example, PathCommands is defined as "M150 300 Q300 0 450 300 Z".
        .fillOpacity(0)
        .stroke(Color.Black)
        .strokeWidth(3)
    }.width('100%')
    .margin({ top: 5 })
  }
}
```

This example shows how to use attributeModifier to dynamically set the commands, fill, fillOpacity, stroke, strokeDashArray, strokeDashOffset, strokeLineCap, strokeLineJoin, strokeMiterLimit, strokeOpacity, strokeWidth, and antiAlias attributes of the Path component.

```TypeScript
// xxx.ets
class MyPathModifier implements AttributeModifier<PathAttribute> {
  applyNormalAttribute(instance: PathAttribute): void {
    // Use the string type for the commands attribute to draw a triangle with the following information: fill color: #707070, fill opacity: 0.5, stroke color: #2787D9, stroke dash array: [20], offset to left: 15, cap style: semi-circle, line join: miter; miter limit: 5; stroke opacity: 0.5; stroke width: 10; anti-aliasing enabled.
    instance.commands('M100 0 L200 240 L0 240 Z')
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
struct PathModifierDemo {
  @State modifier: MyPathModifier = new MyPathModifier()

  build() {
    Column() {
      Path()
        .attributeModifier(this.modifier)
        .offset({ x: 20, y: 20 })
    }
  }
}
```
