# OnScrollFrameBeginCallback

```TypeScript
export type OnScrollFrameBeginCallback = (offset: double, state: ScrollState) => OnScrollFrameBeginHandlerResult
```

Represents the callback triggered before each frame scrolling starts.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnScrollFrameBeginCallback = (offset: double, state: ScrollState) => OnScrollFrameBeginHandlerResult--><!--Device-unnamed-export type OnScrollFrameBeginCallback = (offset: double, state: ScrollState) => OnScrollFrameBeginHandlerResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | double | Yes | Amount to scroll by, in vp. |
| state | [ScrollState](../../apis-arkui/arkts-components/arkts-arkui-scrollstate-e.md) | Yes | Current scroll state. |

**Return value:**

| Type | Description |
| --- | --- |
| [OnScrollFrameBeginHandlerResult](arkts-na-scroll-onscrollframebeginhandlerresult-i.md) | data - the scroll data return by handler |

