# RequestDialogInfoEvent

```TypeScript
type RequestDialogInfoEvent = (actionType: DialogActionType, actionInfo?: DialogActionInfo) => Promise<DialogInfo>
```

The request dialog info event.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-avMusicTemplate-type RequestDialogInfoEvent = (actionType: DialogActionType, actionInfo?: DialogActionInfo) => Promise<DialogInfo>--><!--Device-avMusicTemplate-type RequestDialogInfoEvent = (actionType: DialogActionType, actionInfo?: DialogActionInfo) => Promise<DialogInfo>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| actionType | [DialogActionType](arkts-avsession-avmusictemplate-dialogactiontype-t.md) | Yes |
| actionInfo | [DialogActionInfo](arkts-avsession-avmusictemplate-dialogactioninfo-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[DialogInfo](arkts-avsession-avmusictemplate-dialoginfo-i.md)&gt; |
