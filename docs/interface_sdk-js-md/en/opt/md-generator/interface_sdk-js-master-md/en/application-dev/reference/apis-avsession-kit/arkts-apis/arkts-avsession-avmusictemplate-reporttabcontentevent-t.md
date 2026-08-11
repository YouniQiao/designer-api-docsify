# ReportTabContentEvent

```TypeScript
type ReportTabContentEvent = (tabId: string, tabContent: MediaTabContent) => void
```

The report tab content event.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-avMusicTemplate-type ReportTabContentEvent = (tabId: string, tabContent: MediaTabContent) => void--><!--Device-avMusicTemplate-type ReportTabContentEvent = (tabId: string, tabContent: MediaTabContent) => void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tabId | string | Yes |
| tabContent | [MediaTabContent](arkts-avsession-avmusictemplate-mediatabcontent-i.md) | Yes |
