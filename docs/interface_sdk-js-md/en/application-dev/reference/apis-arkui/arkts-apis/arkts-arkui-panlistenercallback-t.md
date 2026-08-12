# PanListenerCallback

```TypeScript
type PanListenerCallback = (event: GestureEvent, current: GestureRecognizer, node?: FrameNode) => void
```

Defines the callback type used in UIObserver watch pan event.The value of event indicates the information of pan event.The value of node indicates the frameNode which will receive the event.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type PanListenerCallback = (event: GestureEvent, current: GestureRecognizer, node?: FrameNode) => void--><!--Device-unnamed-type PanListenerCallback = (event: GestureEvent, current: GestureRecognizer, node?: FrameNode) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | GestureEvent | Yes | the information of pan event |
| current | GestureRecognizer | Yes | the information of panRecognizer |
| node | FrameNode | No | the information of frameNode |

