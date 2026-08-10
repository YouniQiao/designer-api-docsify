# NavigationMode

导航页显示模式。Navigation处于分栏显示状态时，导航页和内容区之间会显示分割线。

> **说明：**
> 
> 为了简化表示，可以将`组件宽度 - minContentWidth - 分割线宽度 (1px)`称为calcNavBarWidth。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare enum NavigationMode--><!--Device-unnamed-export declare enum NavigationMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Stack

```TypeScript
Stack
```

The navigation bar and the content area are displayed in stack.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationMode-Stack--><!--Device-NavigationMode-Stack-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Split

```TypeScript
Split
```

The navigation bar and the content area are displayed side by side.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationMode-Split--><!--Device-NavigationMode-Split-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Auto

```TypeScript
Auto
```

If the window width is greater than the sum of minNavBarWidth and minContentWidth, the navigation component is displayed in split mode.Otherwise it's displayed in stack mode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationMode-Auto--><!--Device-NavigationMode-Auto-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## AUTO_WITH_ASPECT_RATIO

```TypeScript
AUTO_WITH_ASPECT_RATIO
```

如果导航宽度大于minNavBarWidth和minContentWidth之和。导航组件的长宽比（高宽比）小于等于1.2，则导航组件以分割方式显示。否则它将以堆栈模式显示。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationMode-AUTO_WITH_ASPECT_RATIO--><!--Device-NavigationMode-AUTO_WITH_ASPECT_RATIO-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

