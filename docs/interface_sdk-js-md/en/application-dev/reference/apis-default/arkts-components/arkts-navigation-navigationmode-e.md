# NavigationMode

Navigation mode

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare enum NavigationMode--><!--Device-unnamed-export declare enum NavigationMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Stack

```TypeScript
Stack
```

The navigation bar and the content area are displayed in stack.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationMode-Stack--><!--Device-NavigationMode-Stack-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Split

```TypeScript
Split
```

The navigation bar and the content area are displayed side by side.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationMode-Split--><!--Device-NavigationMode-Split-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Auto

```TypeScript
Auto
```

If the window width is greater than the sum of minNavBarWidth and minContentWidth, the navigation component is displayed in split mode. Otherwise it's displayed in stack mode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationMode-Auto--><!--Device-NavigationMode-Auto-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## AUTO_WITH_ASPECT_RATIO

```TypeScript
AUTO_WITH_ASPECT_RATIO
```

If the navigation width is greater than the sum of minNavBarWidth and minContentWidth, and the navigation component's aspect ratio (height to width) is less than or equal to 1.2, the navigation component is displayed in split mode. Otherwise it's displayed in stack mode.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationMode-AUTO_WITH_ASPECT_RATIO--><!--Device-NavigationMode-AUTO_WITH_ASPECT_RATIO-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

