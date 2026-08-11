# GestureEventListenerCallback

```TypeScript
type GestureEventListenerCallback = (event: GestureEvent, node?: FrameNode) => void
```

Defines the callback type used in UIObserver watch gesture.The value of event indicates the information of gesture.The value of node indicates the frameNode which will receive the event.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type GestureEventListenerCallback = (event: GestureEvent, node?: FrameNode) => void--><!--Device-unnamed-type GestureEventListenerCallback = (event: GestureEvent, node?: FrameNode) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [GestureEvent](arkts-arkui-gestureevent-i.md) | Yes | the information of GestureEvent |
| node | [FrameNode](../arkts-components/arkts-arkui-framenode-t.md) | No | the information of frameNode |

