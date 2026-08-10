# GridLayoutOptions

Grid布局选项。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface GridLayoutOptions--><!--Device-unnamed-export declare interface GridLayoutOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onGetIrregularSizeByIndex

```TypeScript
onGetIrregularSizeByIndex?: (index: int) => [
        int,
        int
    ]
```

配合irregularIndexes使用，设置不规则GridItem占用的行数和列数。开发者可为irregularIndexes中指明的index对应的GridItem设置占用的行数和列数。在API version 12之前，垂直滚动Grid不支持GridItem占多行，水平滚动Grid不支持GridItem占多列。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GridLayoutOptions-onGetIrregularSizeByIndex?: (index: int) => [        int,        int    ]--><!--Device-GridLayoutOptions-onGetIrregularSizeByIndex?: (index: int) => [        int,        int    ]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes |  |

## onGetRectByIndex

```TypeScript
onGetRectByIndex?: (index: int) => [
        int,
        int,
        int,
        int
    ]
```

设置指定索引index对应的GridItem的位置及大小[rowStart,columnStart,rowSpan,columnSpan]。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GridLayoutOptions-onGetRectByIndex?: (index: int) => [        int,        int,        int,        int    ]--><!--Device-GridLayoutOptions-onGetRectByIndex?: (index: int) => [        int,        int,        int,        int    ]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes |  |

## irregularIndexes

```TypeScript
irregularIndexes?: int[]
```

指定索引的GridItem在Grid中的大小是不规则的。

**Type:** int[]

**Default:** int[] no irregular grid item

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GridLayoutOptions-irregularIndexes?: int[]--><!--Device-GridLayoutOptions-irregularIndexes?: int[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## regularSize

```TypeScript
regularSize: [
        int,
        int
    ]
```

大小规则的GridItem在Grid中占的行数和列数，只支持占1行1列即[1, 1]。

**Type:** [         int,         int     ]

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GridLayoutOptions-regularSize: [        int,        int    ]--><!--Device-GridLayoutOptions-regularSize: [        int,        int    ]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

