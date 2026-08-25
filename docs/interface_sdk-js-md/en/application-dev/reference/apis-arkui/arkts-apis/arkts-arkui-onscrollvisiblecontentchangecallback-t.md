# OnScrollVisibleContentChangeCallback

```TypeScript
export type OnScrollVisibleContentChangeCallback = (start: VisibleListContentInfo, end: VisibleListContentInfo) => void
```

Called when a child component enters or leaves the list display area.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| start | [VisibleListContentInfo](arkts-arkui-list-visiblelistcontentinfo-i.md) | Yes |
| end | [VisibleListContentInfo](arkts-arkui-list-visiblelistcontentinfo-i.md) | Yes |
