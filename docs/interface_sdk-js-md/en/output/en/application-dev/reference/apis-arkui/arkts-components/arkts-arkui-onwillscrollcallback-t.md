# OnWillScrollCallback

```TypeScript
declare type OnWillScrollCallback =
(scrollOffset: number, scrollState: ScrollState, scrollSource: ScrollSource) => void | ScrollResult
```

Called before scroll to allow developer to control real offset the Scrollable can scroll.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-unnamed-declare type OnWillScrollCallback =(scrollOffset: number, scrollState: ScrollState, scrollSource: ScrollSource) => void | ScrollResult--><!--Device-unnamed-declare type OnWillScrollCallback =(scrollOffset: number, scrollState: ScrollState, scrollSource: ScrollSource) => void | ScrollResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scrollOffset | number | Yes | offset this frame will scroll, which may or may not be reached.  |
| scrollState | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | current scroll state.  |
| scrollSource | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | source of current scroll.  |

**Return value:**

| Type | Description |
| --- | --- |
| void \| ScrollResult | the remain offset for the scrollable, |

