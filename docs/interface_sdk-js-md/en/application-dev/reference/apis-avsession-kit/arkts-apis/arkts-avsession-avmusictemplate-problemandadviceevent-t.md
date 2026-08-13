# ProblemAndAdviceEvent

```TypeScript
type ProblemAndAdviceEvent = (advice: string) => Promise<OperResult>
```

The problem and advice event.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-avMusicTemplate-type ProblemAndAdviceEvent = (advice: string) => Promise<OperResult>--><!--Device-avMusicTemplate-type ProblemAndAdviceEvent = (advice: string) => Promise<OperResult>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| advice | string | Yes | advice |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[OperResult](arkts-avsession-avmusictemplate-operresult-i.md)&gt; | (OperResult) returned through promise |

