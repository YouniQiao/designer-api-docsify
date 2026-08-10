# LayoutStyle

[Scrollable](TabsAttribute#barMode(value: BarMode, options?: ScrollableBarModeOptions))模式下不滚动时的页签排布方式枚举。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare enum LayoutStyle--><!--Device-unnamed-declare enum LayoutStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## ALWAYS_CENTER

```TypeScript
ALWAYS_CENTER = 0
```

当页签内容超过TabBar宽度时，TabBar可滚动。

当页签内容不超过TabBar宽度时，TabBar不可滚动，页签紧凑居中。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-LayoutStyle-ALWAYS_CENTER = 0--><!--Device-LayoutStyle-ALWAYS_CENTER = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## ALWAYS_AVERAGE_SPLIT

```TypeScript
ALWAYS_AVERAGE_SPLIT = 1
```

当页签内容超过TabBar宽度时，TabBar可滚动。

当页签内容不超过TabBar宽度时，TabBar不可滚动，且所有页签平均分配TabBar宽度。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-LayoutStyle-ALWAYS_AVERAGE_SPLIT = 1--><!--Device-LayoutStyle-ALWAYS_AVERAGE_SPLIT = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SPACE_BETWEEN_OR_CENTER

```TypeScript
SPACE_BETWEEN_OR_CENTER = 2
```

当页签内容超过TabBar宽度时，TabBar可滚动。

当页签内容不超过TabBar宽度但超过TabBar宽度一半时，TabBar不可滚动，页签紧凑居中。

当页签内容不超过TabBar宽度一半时，TabBar不可滚动，页签居中排列，页签之间的间距相等，所有页签的总宽度占用TabBar宽度的一半。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-LayoutStyle-SPACE_BETWEEN_OR_CENTER = 2--><!--Device-LayoutStyle-SPACE_BETWEEN_OR_CENTER = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

