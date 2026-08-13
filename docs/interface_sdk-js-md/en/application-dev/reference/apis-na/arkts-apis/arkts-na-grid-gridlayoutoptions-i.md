# GridLayoutOptions

The options to help grid layout

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare interface GridLayoutOptions--><!--Device-unnamed-export declare interface GridLayoutOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## irregularIndexes

```TypeScript
irregularIndexes?: int[]
```

The indexes of grid items with irregular size.

**Type:** int[]

**Default:** int[] no irregular grid item

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-GridLayoutOptions-irregularIndexes?: int[]--><!--Device-GridLayoutOptions-irregularIndexes?: int[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onGetIrregularSizeByIndex

```TypeScript
onGetIrregularSizeByIndex?: (index: int) => [
        int,
        int
    ]
```

Called to return the size of the irregular grid items with the specified index in [rows, columns].

**Type:** (index: int) =&gt; [         int,         int     ]

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-GridLayoutOptions-onGetIrregularSizeByIndex?: (index: int) => [        int,        int    ]--><!--Device-GridLayoutOptions-onGetIrregularSizeByIndex?: (index: int) => [        int,        int    ]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onGetRectByIndex

```TypeScript
onGetRectByIndex?: (index: int) => [
        int,
        int,
        int,
        int
    ]
```

Called to return the size of the grid items with the specified index in [rowStart, columnStart, rowSpan, columnSpan].

**Type:** (index: int) =&gt; [         int,         int,         int,         int     ]

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-GridLayoutOptions-onGetRectByIndex?: (index: int) => [        int,        int,        int,        int    ]--><!--Device-GridLayoutOptions-onGetRectByIndex?: (index: int) => [        int,        int,        int,        int    ]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## regularSize

```TypeScript
regularSize: [
        int,
        int
    ]
```

The size of most grid items, in [rows, columns], generally [1, 1]

**Type:** [         int,         int     ]

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-GridLayoutOptions-regularSize: [        int,        int    ]--><!--Device-GridLayoutOptions-regularSize: [        int,        int    ]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

