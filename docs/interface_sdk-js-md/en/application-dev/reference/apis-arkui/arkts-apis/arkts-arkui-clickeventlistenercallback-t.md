# ClickEventListenerCallback

```TypeScript
declare type ClickEventListenerCallback = (event: ClickEvent, node?: FrameNode) => void
```

Defines the callback type for listening for click events in **UIObserver**.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [ClickEvent](../arkts-components/arkts-arkui-clickevent-i.md) | Yes |
| node | [FrameNode](arkts-arkui-framenode-c.md) | No |
