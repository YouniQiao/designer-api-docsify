# PanListenerCallback

```TypeScript
type PanListenerCallback = (event: GestureEvent, current: GestureRecognizer, node?: FrameNode) => void
```

定义UIObserver监听拖拽事件时使用的回调类型。event表示拖拽事件的信息。node表示接收事件的frameNode。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type PanListenerCallback = (event: GestureEvent, current: GestureRecognizer, node?: FrameNode) => void--><!--Device-unnamed-type PanListenerCallback = (event: GestureEvent, current: GestureRecognizer, node?: FrameNode) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [GestureEvent](arkts-arkui-gestureevent-i.md) | Yes | the information of pan event |
| current | [GestureRecognizer](arkts-arkui-gesturerecognizer-c.md) | Yes | the information of panRecognizer |
| node | [FrameNode](arkts-arkui-framenode-t.md) | No | the information of frameNode |

