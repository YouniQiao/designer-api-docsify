# GridRowDirection

栅格元素排列方向。

> **说明：**
> 
> - 栅格元素仅支持Row/RowReverse排列，不支持Column/ColumnReverse方向排列。
> 
> - 栅格子组件仅能通过span、offset计算子组件位置与大小。多个子组件span超过规定列数时自动换行。
> 
> - 单个元素span大小超过最大列数时后台默认span为最大列数。
> 
> - 新一行的offset加上子组件的span超过总列数时，将下一个子组件放在新一行。
> 
> - 例：Item1: GridCol({ span: 6 })， Item2: GridCol({ span: 8, offset:11 })。
> 
> ![figures/gridRowOffsetToNextLine.png](../../../reference/apis-arkui/arkui-ts/figures/gridRowOffsetToNextLine.png)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-unnamed-declare enum GridRowDirection--><!--Device-unnamed-declare enum GridRowDirection-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Row

```TypeScript
Row = 0
```

栅格元素按照行方向排列。适用于常规LTR（从左到右）布局场景。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-GridRowDirection-Row = 0--><!--Device-GridRowDirection-Row = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## RowReverse

```TypeScript
RowReverse = 1
```

栅格元素按照逆序行方向排列，适用于RTL（从右到左）语言布局或需要反向排列的场景。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-GridRowDirection-RowReverse = 1--><!--Device-GridRowDirection-RowReverse = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

