# LayoutStyle

[Scrollable](TabsAttribute.barMode)模式下不滚动时的页签排布方式枚举。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare enum LayoutStyle--><!--Device-unnamed-export declare enum LayoutStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## ALWAYS_CENTER

```TypeScript
ALWAYS_CENTER = 0
```

当页签内容超过TabBar宽度时，TabBar可滚动。当页签内容不超过TabBar宽度时，TabBar不可滚动，页签紧凑居中。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LayoutStyle-ALWAYS_CENTER = 0--><!--Device-LayoutStyle-ALWAYS_CENTER = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## ALWAYS_AVERAGE_SPLIT

```TypeScript
ALWAYS_AVERAGE_SPLIT = 1
```

当页签内容超过TabBar宽度时，TabBar可滚动。当页签内容不超过TabBar宽度时，TabBar不可滚动，且所有页签平均分配TabBar宽度。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LayoutStyle-ALWAYS_AVERAGE_SPLIT = 1--><!--Device-LayoutStyle-ALWAYS_AVERAGE_SPLIT = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SPACE_BETWEEN_OR_CENTER

```TypeScript
SPACE_BETWEEN_OR_CENTER = 2
```

当页签内容超过TabBar宽度时，TabBar可滚动。当页签内容不超过TabBar宽度但超过TabBar宽度一半时，TabBar不可滚动，页签紧凑居中。当页签内容不超过TabBar宽度一半时，TabBar不可滚动，保证页签居中排列在TabBar宽度一半，且间距相同。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LayoutStyle-SPACE_BETWEEN_OR_CENTER = 2--><!--Device-LayoutStyle-SPACE_BETWEEN_OR_CENTER = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

