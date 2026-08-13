# OnDragEventCallback

```TypeScript
declare type OnDragEventCallback = (event: DragEvent, extraParams?: string) => void
```

Defines a callback for drag events.

**Since:** 15

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-unnamed-declare type OnDragEventCallback = (event: DragEvent, extraParams?: string) => void--><!--Device-unnamed-declare type OnDragEventCallback = (event: DragEvent, extraParams?: string) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [DragEvent](arkts-arkui-dragevent-i.md) | Yes |
| extraParams | string | No |
