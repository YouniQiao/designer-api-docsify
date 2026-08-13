# ScrollOnWillScrollCallback

```TypeScript
export type ScrollOnWillScrollCallback = (xOffset: double, yOffset: double, scrollState: ScrollState, scrollSource: ScrollSource) => (undefined | OffsetResult)
```

Called before scroll to allow developer to control real offset the Scroll can scroll.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type ScrollOnWillScrollCallback = (xOffset: double, yOffset: double, scrollState: ScrollState, scrollSource: ScrollSource) => (undefined | OffsetResult)--><!--Device-unnamed-export type ScrollOnWillScrollCallback = (xOffset: double, yOffset: double, scrollState: ScrollState, scrollSource: ScrollSource) => (undefined | OffsetResult)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| xOffset | double | Yes | horizontal offset this frame will scroll, which may or may not be reached. |
| yOffset | double | Yes | vertical offset this frame will scroll, which may or may not be reached. |
| scrollState | [ScrollState](../../apis-arkui/arkts-components/arkts-arkui-scrollstate-e.md) | Yes | current scroll state. |
| scrollSource | [ScrollSource](../../apis-arkui/arkts-apis/arkts-arkui-scrollsource-e.md) | Yes | source of current scroll. |

**Return value:**

| Type | Description |
| --- | --- |
| (undefined \| OffsetResult) | the remain offset for the Scroll, same as (xOffset, yOffset) when no OffsetResult is returned. |

