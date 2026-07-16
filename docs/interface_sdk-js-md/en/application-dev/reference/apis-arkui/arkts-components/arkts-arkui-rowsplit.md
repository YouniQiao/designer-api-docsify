# RowSplit

The **RowSplit** component lays out child components horizontally and inserts a vertical divider between every two
child components.
> **Note**
>
> This component limits the width of its child components through dividers. During initialization, the divider
> positions are calculated based on the width of its child components. After initialization, dynamic width
> modifications to child components do not affect divider positions. To adjust child component widths, drag the
> adjacent dividers.
>
> After initialization, dynamic changes to the [margin]{@link CommonMethod#margin},
> [border]{@link CommonMethod#border}, or [padding]{@link CommonMethod#padding} attributes may cause the
> width of the child components to exceed the allowable distance between adjacent dividers. In such cases, dividers
> cannot be dragged to adjust the width of the child components.
>
> **Child Components**
>
> Supported


## RowSplit

```TypeScript
RowSplit()
```

Creates a horizontal split layout container with dividers between child components.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RowSplitInterface-(): RowSplitAttribute--><!--Device-RowSplitInterface-(): RowSplitAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Summary

