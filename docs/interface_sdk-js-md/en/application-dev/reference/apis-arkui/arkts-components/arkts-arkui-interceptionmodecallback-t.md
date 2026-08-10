# InterceptionModeCallback

```TypeScript
declare type InterceptionModeCallback = (mode: NavigationMode) => void
```

Navigation单双栏显示状态发生变更时的拦截回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-unnamed-declare type InterceptionModeCallback = (mode: NavigationMode) => void--><!--Device-unnamed-declare type InterceptionModeCallback = (mode: NavigationMode) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [NavigationMode](../arkts-apis/arkts-arkui-navigation-navigationmode-e.md) | Yes | 导航页的显示模式。 |

