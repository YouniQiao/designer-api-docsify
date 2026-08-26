# Column

The **Column** component lays out child components vertically. > **NOTE** > > If no height or width is set for the **Column** component, the component automatically adapts to the size of its > child components in the main axis and cross axis respectively. > > **Child Components** > > Supported

## Column

```TypeScript
Column(options?: ColumnOptions)
```

Creates a vertical linear layout container. You can set the spacing between child components.

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
| options | [ColumnOptions](arkts-arkui-columnoptions-i.md) | No | Vertical spacing between two adjacent child components. The value can be of the number or string type. |

## Column

```TypeScript
Column(options?: ColumnOptions | ColumnOptionsV2)
```

Creates a vertical linear layout container. You can set the spacing between child components.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ColumnOptions](arkts-arkui-columnoptions-i.md) \| [ColumnOptionsV2](arkts-arkui-columnoptionsv2-i.md) | No | Vertical spacing between two adjacent child components. The value can be of the number, string, or Resource type. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |

### Types

| Name | Description |
| --- | --- |

## Examples

This example demonstrates how to set the layout attributes of the Column component, such as the spacing and alignment mode, and its effect.

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
struct ColumnExample {
  build() {
    Scroll() {
      Column({ space: 5 }) {
        // Set the vertical spacing between two adjacent child components to 5.
        Text('space').width('90%')
        Column({ space: 5 }) {
          Column().width('100%').height(30).backgroundColor(0xAFEEEE)
          Column().width('100%').height(30).backgroundColor(0x00FFFF)
        }.width('90%').height(100).border({ width: 1 })

        // Set the spacing between child elements using the Resource type.
        Text('Resource space').width('90%')
        Column({ space: $r('app.string.stringSpace') }) {
          Column().width('100%').height(30).backgroundColor(0xAFEEEE)
          Column().width('100%').height(30).backgroundColor(0x00FFFF)
        }.width('90%').height(100).border({ width: 1 })

        // Set the alignment mode of the child components in the horizontal direction.
        Text('alignItems(Start)').width('90%')
        Column() {
          Column().width('50%').height(30).backgroundColor(0xAFEEEE)
          Column().width('50%').height(30).backgroundColor(0x00FFFF)
        }.alignItems(HorizontalAlign.Start).width('90%').border({ width: 1 })

        Text('alignItems(End)').width('90%')
        Column() {
          Column().width('50%').height(30).backgroundColor(0xAFEEEE)
          Column().width('50%').height(30).backgroundColor(0x00FFFF)
        }.alignItems(HorizontalAlign.End).width('90%').border({ width: 1 })

        Text('alignItems(Center)').width('90%')
        Column() {
          Column().width('50%').height(30).backgroundColor(0xAFEEEE)
          Column().width('50%').height(30).backgroundColor(0x00FFFF)
        }.alignItems(HorizontalAlign.Center).width('90%').border({ width: 1 })

        // Set the alignment mode of the child components in the vertical direction.
        Text('justifyContent(Center)').width('90%')
        Column() {
          Column().width('90%').height(30).backgroundColor(0xAFEEEE)
          Column().width('90%').height(30).backgroundColor(0x00FFFF)
        }.height(100).border({ width: 1 }).justifyContent(FlexAlign.Center)

        Text('justifyContent(End)').width('90%')
        Column() {
          Column().width('90%').height(30).backgroundColor(0xAFEEEE)
          Column().width('90%').height(30).backgroundColor(0x00FFFF)
        }.height(100).border({ width: 1 }).justifyContent(FlexAlign.End)
      }.width('100%').padding({ top: 5 })
    }.width('100%').height('100%')
  }
}
```

This example demonstrates how to set the reverse attribute of the Column component and its effect.

```TypeScript
@Entry
@Component
struct ColumnReverseSample {
  build() {
    Column() {
      Text("1")
        .width(50)
        .height(100)
        .backgroundColor(0xAFEEEE)

      Text("2")
        .width(50)
        .height(100)
        .backgroundColor(0x00FFFF)
    }
    .height(300)
    .width(100)
    .border({ width: 1 })
    .reverse(true)
  }
}
```
