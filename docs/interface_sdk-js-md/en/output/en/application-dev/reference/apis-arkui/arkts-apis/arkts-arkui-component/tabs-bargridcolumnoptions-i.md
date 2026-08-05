# BarGridColumnOptions

Provides an interface for the grid column options of an tab bar including sm, md, lg, margin and gutter.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface BarGridColumnOptions--><!--Device-unnamed-export interface BarGridColumnOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## gutter

```TypeScript
gutter?: Dimension
```

Column gutter (that is, gap between columns) in grid mode. It cannot be set in percentage. Unit: vp. Default value: 24.

**Type:** Dimension

**Default:** 24vp

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BarGridColumnOptions-gutter?: Dimension--><!--Device-BarGridColumnOptions-gutter?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## lg

```TypeScript
lg?: int
```

Number of columns occupied by a tab on a screen whose width is greater than or equal to 840 vp but less than 1024 vp. The value must be a non-negative even int. The value range is all integers, The default value is - 1, indicating that the tab occupies the entire width of the TabBar. Default value: -1.

**Type:** int

**Default:** -1

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BarGridColumnOptions-lg?: int--><!--Device-BarGridColumnOptions-lg?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## margin

```TypeScript
margin?: Dimension
```

Column margin in grid mode. It cannot be set in percentage. Unit: vp. Default value: 24.

**Type:** Dimension

**Default:** 24vp

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BarGridColumnOptions-margin?: Dimension--><!--Device-BarGridColumnOptions-margin?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## md

```TypeScript
md?: int
```

Number of columns occupied by a tab on a screen whose width is greater than or equal to 600 vp but less than 800 vp. The value must be a non-negative even int. The value range is all integers, The default value is - 1, indicating that the tab occupies the entire width of the TabBar. Default value: -1.

**Type:** int

**Default:** -1

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BarGridColumnOptions-md?: int--><!--Device-BarGridColumnOptions-md?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## sm

```TypeScript
sm?: int
```

Number of columns occupied by a tab on a screen whose width is greater than or equal to 320 vp but less than 600 vp. The value must be a non-negative even int. The value range is all integers, The default value is - 1, indicating that the tab occupies the entire width of the TabBar. Default value: -1.

**Type:** int

**Default:** -1

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BarGridColumnOptions-sm?: int--><!--Device-BarGridColumnOptions-sm?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

