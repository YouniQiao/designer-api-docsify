# PanListenerCallback

```TypeScript
declare type PanListenerCallback = (event: GestureEvent, current: GestureRecognizer, node?: FrameNode) => void
```

Defines a callback for pan gesture events.

**Since:** 19

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-unnamed-declare type PanListenerCallback = (event: GestureEvent, current: GestureRecognizer, node?: FrameNode) => void--><!--Device-unnamed-declare type PanListenerCallback = (event: GestureEvent, current: GestureRecognizer, node?: FrameNode) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [GestureEvent](arkts-arkui-gestureevent-i.md) | Yes |
| current | [GestureRecognizer](arkts-arkui-gesturerecognizer-c.md) | Yes |
| node | [FrameNode](arkts-arkui-framenode-c.md) | No |
