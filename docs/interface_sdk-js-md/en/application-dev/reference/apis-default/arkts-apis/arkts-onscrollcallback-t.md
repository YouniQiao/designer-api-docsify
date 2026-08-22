# OnScrollCallback

```TypeScript
export type OnScrollCallback = (scrollOffset: double, scrollState: ScrollState) => void
```

On scroll callback using in scrollable onDidScroll.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnScrollCallback = (scrollOffset: double, scrollState: ScrollState) => void--><!--Device-unnamed-export type OnScrollCallback = (scrollOffset: double, scrollState: ScrollState) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scrollOffset | double | Yes | offset this frame did scroll. |
| scrollState | [ScrollState](../../apis-arkui/arkts-components/arkts-arkui-scrollstate-e.md) | Yes | current scroll state. |

