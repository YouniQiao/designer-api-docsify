# ClickEventListenerCallback

```TypeScript
type ClickEventListenerCallback = (event: ClickEvent, node?: FrameNode) => void
```

Defines the callback type used in UIObserver watch click event. The value of event indicates the information of ClickEvent. The value of node indicates the frameNode which will receive the event.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type ClickEventListenerCallback = (event: ClickEvent, node?: FrameNode) => void--><!--Device-unnamed-type ClickEventListenerCallback = (event: ClickEvent, node?: FrameNode) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | the information of ClickEvent  |
| node | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | the information of frameNode  |

