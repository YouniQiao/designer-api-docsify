# InterceptionModeCallback

```TypeScript
export type InterceptionModeCallback = (mode: NavigationMode) => void
```

Navigation单双栏显示状态发生变更时的拦截回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type InterceptionModeCallback = (mode: NavigationMode) => void--><!--Device-unnamed-export type InterceptionModeCallback = (mode: NavigationMode) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [NavigationMode](arkts-arkui-navigation-navigationmode-e.md) | Yes | 导航页的显示模式。 |

