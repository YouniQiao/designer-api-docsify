# ClickEventListenerCallback

```TypeScript
type ClickEventListenerCallback = (event: ClickEvent, node?: FrameNode) => void
```

定义UIObserver监听点击事件时使用的回调类型。event表示点击事件的信息。node表示接收事件的frameNode。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type ClickEventListenerCallback = (event: ClickEvent, node?: FrameNode) => void--><!--Device-unnamed-type ClickEventListenerCallback = (event: ClickEvent, node?: FrameNode) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [ClickEvent](../arkts-components/arkts-arkui-clickevent-i.md) | Yes | the information of ClickEvent |
| node | [FrameNode](arkts-arkui-framenode-t.md) | No | the information of frameNode |

