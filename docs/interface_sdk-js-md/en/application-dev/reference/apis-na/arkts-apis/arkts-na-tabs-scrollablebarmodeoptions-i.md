# ScrollableBarModeOptions

Provides an interface for the options for the scrollable bar mode including margin and nonScrollableLayoutStyle.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export interface ScrollableBarModeOptions--><!--Device-unnamed-export interface ScrollableBarModeOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## margin

```TypeScript
margin?: Dimension
```

Left and right margin of the tab bar in scrollable mode. It cannot be set in percentage. Unit: vp. Default value: 0.

**Type:** [Dimension](../../apis-arkui/arkts-apis/arkts-arkui-dimension-t.md)

**Default:** 0vp

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScrollableBarModeOptions-margin?: Dimension--><!--Device-ScrollableBarModeOptions-margin?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## nonScrollableLayoutStyle

```TypeScript
nonScrollableLayoutStyle?: LayoutStyle
```

Tab layout mode of the tab bar when not scrolling in scrollable mode. Default value: LayoutStyle.ALWAYS_CENTER.

**Type:** [LayoutStyle](arkts-na-tabs-layoutstyle-e.md)

**Default:** LayoutStyle.ALWAYS_CENTER

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScrollableBarModeOptions-nonScrollableLayoutStyle?: LayoutStyle--><!--Device-ScrollableBarModeOptions-nonScrollableLayoutStyle?: LayoutStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

