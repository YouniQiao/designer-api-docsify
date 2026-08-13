# ReportCustomElementsChangeEvent

```TypeScript
type ReportCustomElementsChangeEvent = (actionType: ActionType, customType: CustomType,
    customElement: CustomElement) => void
```

The report custom elements change event.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-avMusicTemplate-type ReportCustomElementsChangeEvent = (actionType: ActionType, customType: CustomType,    customElement: CustomElement) => void--><!--Device-avMusicTemplate-type ReportCustomElementsChangeEvent = (actionType: ActionType, customType: CustomType,    customElement: CustomElement) => void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| actionType | [ActionType](arkts-avsession-avmusictemplate-actiontype-t.md) | Yes |
| customType | [CustomType](arkts-avsession-avmusictemplate-customtype-t.md) | Yes |
| customElement | [CustomElement](arkts-avsession-avmusictemplate-customelement-i.md) | Yes |
