# OnWillScrollCallback

```TypeScript
export type OnWillScrollCallback = (scrollOffset: double, scrollState: ScrollState, scrollSource: ScrollSource) => (undefined | ScrollResult)
```

Called before scroll to allow developer to control real offset the Scrollable can scroll.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnWillScrollCallback = (scrollOffset: double, scrollState: ScrollState, scrollSource: ScrollSource) => (undefined | ScrollResult)--><!--Device-unnamed-export type OnWillScrollCallback = (scrollOffset: double, scrollState: ScrollState, scrollSource: ScrollSource) => (undefined | ScrollResult)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scrollOffset | double | Yes | offset this frame will scroll, which may or may not be reached.  |
| scrollState | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | current scroll state.  |
| scrollSource | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | source of current scroll.  |

**Return value:**

| Type | Description |
| --- | --- |
| (undefined \| ScrollResult) | the remain offset for the scrollable, |

