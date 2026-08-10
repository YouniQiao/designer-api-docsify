# ScrollableBarModeOptions

Scrollable模式下的TabBar的布局样式对象。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-interface ScrollableBarModeOptions--><!--Device-unnamed-interface ScrollableBarModeOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## margin

```TypeScript
margin?: Dimension
```

Scrollable模式下的TabBar的左右边距（不支持百分比设置）。

默认值：0.0

单位：vp

取值范围：[0, +∞)。设置为小于0的值时，按默认值显示。

**Type:** [Dimension](../arkts-apis/arkts-arkui-dimension-t.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollableBarModeOptions-margin?: Dimension--><!--Device-ScrollableBarModeOptions-margin?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## nonScrollableLayoutStyle

```TypeScript
nonScrollableLayoutStyle?: LayoutStyle
```

Scrollable模式下不滚动时的页签排布方式，仅水平模式下有效。

默认值：LayoutStyle.ALWAYS_CENTER

**Type:** [LayoutStyle](../arkts-apis/arkts-arkui-tabs-layoutstyle-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollableBarModeOptions-nonScrollableLayoutStyle?: LayoutStyle--><!--Device-ScrollableBarModeOptions-nonScrollableLayoutStyle?: LayoutStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

