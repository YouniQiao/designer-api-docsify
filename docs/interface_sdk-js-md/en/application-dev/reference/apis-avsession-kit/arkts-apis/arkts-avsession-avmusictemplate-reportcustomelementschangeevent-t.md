# ReportCustomElementsChangeEvent

```TypeScript
type ReportCustomElementsChangeEvent = (actionType: ActionType, customType: CustomType,
    customElement: CustomElement) => void
```

The report custom elements change event.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-avMusicTemplate-type ReportCustomElementsChangeEvent = (actionType: ActionType, customType: CustomType,    customElement: CustomElement) => void--><!--Device-avMusicTemplate-type ReportCustomElementsChangeEvent = (actionType: ActionType, customType: CustomType,    customElement: CustomElement) => void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| actionType | ActionType | Yes | action type |
| customType | [CustomType](arkts-avsession-avmusictemplate-customtype-t.md) | Yes | custom type |
| customElement | [CustomElement](arkts-avsession-avmusictemplate-customelement-i.md) | Yes | custom element |

