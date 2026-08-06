# ScrollOnWillScrollCallback

```TypeScript
export type ScrollOnWillScrollCallback = (xOffset: double, yOffset: double, scrollState: ScrollState, scrollSource: ScrollSource) => (undefined | OffsetResult)
```

Called before scroll to allow developer to control real offset the Scroll can scroll.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type ScrollOnWillScrollCallback = (xOffset: double, yOffset: double, scrollState: ScrollState, scrollSource: ScrollSource) => (undefined | OffsetResult)--><!--Device-unnamed-export type ScrollOnWillScrollCallback = (xOffset: double, yOffset: double, scrollState: ScrollState, scrollSource: ScrollSource) => (undefined | OffsetResult)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| xOffset | double | Yes | horizontal offset this frame will scroll, which may or may not be reached.  |
| yOffset | double | Yes | vertical offset this frame will scroll, which may or may not be reached.  |
| scrollState | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | current scroll state.  |
| scrollSource | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | source of current scroll.  |

**Return value:**

| Type | Description |
| --- | --- |
| (undefined \| OffsetResult) | the remain offset for the Scroll, |

