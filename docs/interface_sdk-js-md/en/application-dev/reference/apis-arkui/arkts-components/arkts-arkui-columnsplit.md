# ColumnSplit

The **ColumnSplit** component lays out child components vertically and inserts a horizontal divider between every two child components.

## ColumnSplit

```TypeScript
ColumnSplit()
```

Creates a vertical split layout container with dividers between child components.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ColumnSplitInterface-(): ColumnSplitAttribute--><!--Device-ColumnSplitInterface-(): ColumnSplitAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [ColumnSplitDividerStyle](arkts-arkui-columnsplitdividerstyle-i.md) | Sets the distance between the child component and the upper and lower dividers. > **NOTE：**> > Similar to RowSplit, the dividers of **ColumnSplit** adjust the height of adjacent child > components. However, this adjustment is only applied to the extent that the resulting height stays within the > height limits of the child components. > > Universal attributes such as clip and margin are supported. > If **clip** is not set, the default value **true** is used. |

