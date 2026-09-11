# RowSplit

The **RowSplit** component lays out child components horizontally and inserts a vertical divider between every two child components. > **Note** > > This component limits the width of its child components through dividers. During initialization, the divider > positions are calculated based on the width of its child components. After initialization, dynamic width > modifications to child components do not affect divider positions. To adjust child component widths, drag the > adjacent dividers. > > After initialization, dynamic changes to the margin, > [border](arkts-arkui-commonmethod-c.md#border), or padding attributes may cause the > width of the child components to exceed the allowable distance between adjacent dividers. In such cases, dividers > cannot be dragged to adjust the width of the child components. > > **Child Components** > > Supported

## RowSplit

```TypeScript
RowSplit()
```

Creates a horizontal split layout container with dividers between child components.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Summary

## Examples

This example shows the basic usage of RowSplit, which implements a horizontally laid-out layout with a draggable divider.

```TypeScript
// xxx.ets
@Entry
@Component
struct RowSplitExample {
  build() {
    Column() {
      Text('The second line can be dragged').fontSize(9).fontColor(0xCCCCCC).width('90%')
      // Create a RowSplit component to implement horizontal layout.
      RowSplit() {
        Text('1').width('10%').height(100).backgroundColor(0xF5DEB3).textAlign(TextAlign.Center)
        Text('2').width('10%').height(100).backgroundColor(0xD2B48C).textAlign(TextAlign.Center)
        Text('3').width('10%').height(100).backgroundColor(0xF5DEB3).textAlign(TextAlign.Center)
        Text('4').width('10%').height(100).backgroundColor(0xD2B48C).textAlign(TextAlign.Center)
        Text('5').width('10%').height(100).backgroundColor(0xF5DEB3).textAlign(TextAlign.Center)
      }
      .resizeable(true) // Draggable.
      .width('90%').height(100)
    }.width('100%').margin({ top: 5 })
  }
}
```
