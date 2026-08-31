# Row

The **Row** component lays out child components horizontally. > **NOTE** > > If no width or height is set for the **Row** component, the component automatically adapts to the size of its child > components in the main axis and cross axis respectively. > > **Child Components** > > Supported

## Row

```TypeScript
Row(options?: RowOptions)
```

Creates a horizontal linear layout container. You can set the spacing between child components.

> **NOTE：**
> 
> Excessive component nesting (either too deep a hierarchy or too many nested components) incurs significant
> performance overhead. For performance purposes, you are advised to remove redundant nodes to simplify the
> component tree, use layout boundaries to reduce redundant layout calculations, properly apply rendering control
> syntax and layout component methods to minimize unnecessary re-renders and computations. For details about the
> best practices, see
> [Layout Optimization](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-improve-layout-performance)
> .

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RowOptions](arkts-arkui-rowoptions-i.md) | No | Spacing between elements in the horizontal layout. The value can be of the number or string type. |

## Row

```TypeScript
Row(options?: RowOptions | RowOptionsV2)
```

Creates a horizontal linear layout container. You can set the spacing between child components.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RowOptions](arkts-arkui-rowoptions-i.md) \| [RowOptionsV2](arkts-arkui-rowoptionsv2-i.md) | No | Spacing between elements in a horizontal layout. The value can be of the number, string, or Resource type. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [RowOptions](arkts-arkui-rowoptions-i.md) | Sets the spacing between child components of the **Row** component. |
| [RowOptionsV2](arkts-arkui-rowoptionsv2-i.md) | Sets the spacing between child components of the **Row** component. |

## Examples

This example demonstrates the effect of setting the layout attributes (such as the spacing and alignment mode) of the Row component.

```TypeScript
// resources/base/element/string.json
{
  "string": [
    {
      "name": "stringSpace",
      "value": "5"
    }
  ]
}
```

```TypeScript
// xxx.ets
@Entry
@Component
struct RowExample {
  build() {
    Column({ space: 5 }) {
      // Set the horizontal spacing between two adjacent child components to 5.
      Text('space').width('90%')
      Row({ space: 5 }) {
        Row().width('30%').height(50).backgroundColor(0xAFEEEE)
        Row().width('30%').height(50).backgroundColor(0x00FFFF)
      }.width('90%').height(107).border({ width: 1 })

      // Set the spacing between child components using the Resource type.
      Text('Resource space').width('90%')
      // Set the space attribute by using a resource reference (supported since API 18+).
      Row({ space: $r('app.string.stringSpace') }) {
        Row().width('30%').height(50).backgroundColor(0xAFEEEE)
        Row().width('30%').height(50).backgroundColor(0x00FFFF)
      }.width('90%').height(107).border({ width: 1 })

      // Set the vertical alignment of child components.
      Text('alignItems(Bottom)').width('90%')
      // Align child components to the bottom.
      Row() {
        Row().width('30%').height(50).backgroundColor(0xAFEEEE)
        Row().width('30%').height(50).backgroundColor(0x00FFFF)
      }.width('90%').alignItems(VerticalAlign.Bottom).height('15%').border({ width: 1 })

      Text('alignItems(Center)').width('90%')
      // Align child components vertically to the center.
      Row() {
        Row().width('30%').height(50).backgroundColor(0xAFEEEE)
        Row().width('30%').height(50).backgroundColor(0x00FFFF)
      }.width('90%').alignItems(VerticalAlign.Center).height('15%').border({ width: 1 })

      // Set the horizontal alignment of child components.
      Text('justifyContent(End)').width('90%')
      // Align child components to the right.
      Row() {
        Row().width('30%').height(50).backgroundColor(0xAFEEEE)
        Row().width('30%').height(50).backgroundColor(0x00FFFF)
      }.width('90%').border({ width: 1 }).justifyContent(FlexAlign.End)

      Text('justifyContent(Center)').width('90%')
      // Align child components horizontally to the center.
      Row() {
        Row().width('30%').height(50).backgroundColor(0xAFEEEE)
        Row().width('30%').height(50).backgroundColor(0x00FFFF)
      }.width('90%').border({ width: 1 }).justifyContent(FlexAlign.Center)
    }.width('100%')
  }
}
```

This example shows the effect after setting the reverse attribute of the Row component, demonstrating how to reverse the arrangement order of child components.

```TypeScript
@Entry
@Component
struct RowReverseSample {
  build() {
    Row() {
      Text('1')
        .width(100)
        .height(50)
        .backgroundColor(0xAFEEEE)

      Text('2')
        .width(100)
        .height(50)
        .backgroundColor(0x00FFFF)
    }
    .height(100)
    .width(300)
    .border({ width: 1 })
    .reverse(true)
  }
}
```
