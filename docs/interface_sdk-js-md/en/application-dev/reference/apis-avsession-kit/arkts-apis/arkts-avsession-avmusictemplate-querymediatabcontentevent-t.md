# QueryMediaTabContentEvent

```TypeScript
type QueryMediaTabContentEvent = (tabId: string) => Promise<MediaTabContent>
```

The query media tab content event.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tabId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[MediaTabContent](arkts-avsession-avmusictemplate-mediatabcontent-i.md)&gt; |
