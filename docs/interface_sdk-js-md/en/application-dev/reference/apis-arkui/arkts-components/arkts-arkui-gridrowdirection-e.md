# GridRowDirection

Grid element arrangement direction. &gt; **NOTE：**&gt; &gt; - Grid elements can be arranged only in the **Row** or **RowReverse** direction, but not in the **Column** or &gt; **ColumnReverse** direction. &gt; &gt; - The location and size of a grid child component can be calculated only based on **span** and **offset**. If the &gt; **span** values of child components add up to a number greater than the allowed number of columns, the grid will &gt; automatically wrap lines. &gt; &gt; - If the **span** value of a single child component exceeds the maximum number of columns, the maximum number of &gt; columns is used. &gt; &gt; - If a child component takes up more than the total number of columns according to its **offset** and **span** &gt; settings, it will be placed in a new row. &gt; &gt; - Example: Item1: GridCol({ span: 6 }), Item2: GridCol({ span: 8, offset:11 }) &gt; &gt; &gt; &gt; 

**Since:** 9

<!--Device-unnamed-declare enum GridRowDirection--><!--Device-unnamed-declare enum GridRowDirection-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Row

```TypeScript
Row
```

Grid elements are arranged in the row direction.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-GridRowDirection-Row--><!--Device-GridRowDirection-Row-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## RowReverse

```TypeScript
RowReverse
```

Grid elements are arranged in the reverse row direction.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-GridRowDirection-RowReverse--><!--Device-GridRowDirection-RowReverse-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

