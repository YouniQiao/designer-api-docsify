# ExecuteActionEvent

```TypeScript
type ExecuteActionEvent = (actionType: string, params: string) => Promise<string>
```

The execute action event.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-avMusicTemplate-type ExecuteActionEvent = (actionType: string, params: string) => Promise<string>--><!--Device-avMusicTemplate-type ExecuteActionEvent = (actionType: string, params: string) => Promise<string>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| actionType | string | Yes |
| params | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |
