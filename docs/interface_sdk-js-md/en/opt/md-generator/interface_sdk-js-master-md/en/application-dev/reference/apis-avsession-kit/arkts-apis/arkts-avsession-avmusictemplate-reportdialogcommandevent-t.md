# ReportDialogCommandEvent

```TypeScript
type ReportDialogCommandEvent = (type: DialogControlType, buttonInfo: DialogInfo) => void
```

The report dialog command event.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-avMusicTemplate-type ReportDialogCommandEvent = (type: DialogControlType, buttonInfo: DialogInfo) => void--><!--Device-avMusicTemplate-type ReportDialogCommandEvent = (type: DialogControlType, buttonInfo: DialogInfo) => void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [DialogControlType](arkts-avsession-avmusictemplate-dialogcontroltype-t.md) | Yes |
| buttonInfo | [DialogInfo](arkts-avsession-avmusictemplate-dialoginfo-i.md) | Yes |
