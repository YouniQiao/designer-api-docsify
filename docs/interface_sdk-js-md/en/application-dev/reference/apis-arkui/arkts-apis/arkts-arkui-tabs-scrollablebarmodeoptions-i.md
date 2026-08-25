# ScrollableBarModeOptions

Provides an interface for the options for the scrollable bar mode including margin and nonScrollableLayoutStyle.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## margin

```TypeScript
margin?: Dimension
```

Left and right margin of the tab bar in scrollable mode. It cannot be set in percentage. Unit: vp. Default value: 0.

**Type:** [Dimension](arkts-arkui-dimension-t.md)

**Default:** 0vp

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## nonScrollableLayoutStyle

```TypeScript
nonScrollableLayoutStyle?: LayoutStyle
```

Tab layout mode of the tab bar when not scrolling in scrollable mode. Default value: LayoutStyle.ALWAYS_CENTER.

**Type:** [LayoutStyle](arkts-arkui-tabs-layoutstyle-e.md)

**Default:** LayoutStyle.ALWAYS_CENTER

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
