# OnScrollVisibleContentChangeCallback

```TypeScript
declare type OnScrollVisibleContentChangeCallback = (start: VisibleListContentInfo, end: VisibleListContentInfo) => void
```

Triggered when a child component enters or leaves the list display area. When the **List** component changes from having child components to being empty, the values of the reported **start** and **end** parameters remain the same as those when the component had child components last time. If the values of **start** and **end** are both **0**, the **List** component contains only one child component. > **NOTE：**> > This API can be called within attributeModifier since API version 14.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-unnamed-declare type OnScrollVisibleContentChangeCallback = (start: VisibleListContentInfo, end: VisibleListContentInfo) => void--><!--Device-unnamed-declare type OnScrollVisibleContentChangeCallback = (start: VisibleListContentInfo, end: VisibleListContentInfo) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| start | [VisibleListContentInfo](arkts-arkui-visiblelistcontentinfo-i.md) | Yes |
| end | [VisibleListContentInfo](arkts-arkui-visiblelistcontentinfo-i.md) | Yes |
