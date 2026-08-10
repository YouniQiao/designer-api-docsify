# OnNavigationModeChangeCallback

```TypeScript
declare type OnNavigationModeChangeCallback = (mode: NavigationMode) => void
```

当MultiNavigation的mode变化时触发的回调函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare type OnNavigationModeChangeCallback = (mode: NavigationMode) => void--><!--Device-unnamed-declare type OnNavigationModeChangeCallback = (mode: NavigationMode) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [NavigationMode](../arkts-components/arkts-arkui-navigationmode-e.md) | Yes | 当回调触发时的NavigationMode。 |

