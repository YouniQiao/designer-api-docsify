# GridLayoutOptions

Grid布局选项。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface GridLayoutOptions--><!--Device-unnamed-export declare interface GridLayoutOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onGetStartIndexByIndex

```TypeScript
onGetStartIndexByIndex?: OnGetStartIndexByIndexCallback
```

根据指定的目标索引，计算Grid滚动到该位置时页面内的起始行，用于支持[scrollToIndex](arkts-arkui-scroll-scroller-c.md#scrolltoindex)等操作。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GridLayoutOptions-onGetStartIndexByIndex?: OnGetStartIndexByIndexCallback--><!--Device-GridLayoutOptions-onGetStartIndexByIndex?: OnGetStartIndexByIndexCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## onGetStartIndexByOffset

```TypeScript
onGetStartIndexByOffset?: OnGetStartIndexByOffsetCallback
```

根据Grid滚动的总偏移量，计算Grid当前页面起始行位置，用于快速滑动或反向滑动场景。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GridLayoutOptions-onGetStartIndexByOffset?: OnGetStartIndexByOffsetCallback--><!--Device-GridLayoutOptions-onGetStartIndexByOffset?: OnGetStartIndexByOffsetCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

