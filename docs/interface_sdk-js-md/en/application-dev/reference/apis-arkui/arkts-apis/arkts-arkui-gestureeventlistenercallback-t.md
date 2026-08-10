# GestureEventListenerCallback

```TypeScript
type GestureEventListenerCallback = (event: GestureEvent, node?: FrameNode) => void
```

定义UIObserver监听手势时使用的回调类型。event表示手势的信息。node表示接收事件的frameNode。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type GestureEventListenerCallback = (event: GestureEvent, node?: FrameNode) => void--><!--Device-unnamed-type GestureEventListenerCallback = (event: GestureEvent, node?: FrameNode) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [GestureEvent](arkts-arkui-gestureevent-i.md) | Yes | the information of GestureEvent |
| node | [FrameNode](arkts-arkui-framenode-t.md) | No | the information of frameNode |

