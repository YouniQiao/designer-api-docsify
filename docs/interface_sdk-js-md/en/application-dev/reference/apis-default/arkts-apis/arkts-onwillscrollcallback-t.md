# OnWillScrollCallback

```TypeScript
export type OnWillScrollCallback = (scrollOffset: double, scrollState: ScrollState, scrollSource: ScrollSource) => (undefined | ScrollResult)
```

Called before scroll to allow developer to control real offset the Scrollable can scroll.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnWillScrollCallback = (scrollOffset: double, scrollState: ScrollState, scrollSource: ScrollSource) => (undefined | ScrollResult)--><!--Device-unnamed-export type OnWillScrollCallback = (scrollOffset: double, scrollState: ScrollState, scrollSource: ScrollSource) => (undefined | ScrollResult)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scrollOffset | double | Yes | offset this frame will scroll, which may or may not be reached. |
| scrollState | [ScrollState](../../apis-arkui/arkts-components/arkts-arkui-scrollstate-e.md) | Yes | current scroll state. |
| scrollSource | [ScrollSource](../../apis-arkui/arkts-apis/arkts-arkui-scrollsource-e.md) | Yes | source of current scroll. |

**Return value:**

| Type | Description |
| --- | --- |
| (undefined \| ScrollResult) | the remain offset for the scrollable, same as scrollOffset when no ScrollResult is returned. |

