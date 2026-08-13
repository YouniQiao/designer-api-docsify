# ProblemAndAdviceEvent

```TypeScript
type ProblemAndAdviceEvent = (advice: string) => Promise<OperResult>
```

The problem and advice event.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-avMusicTemplate-type ProblemAndAdviceEvent = (advice: string) => Promise<OperResult>--><!--Device-avMusicTemplate-type ProblemAndAdviceEvent = (advice: string) => Promise<OperResult>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| advice | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[OperResult](arkts-avsession-avmusictemplate-operresult-i.md)&gt; |
