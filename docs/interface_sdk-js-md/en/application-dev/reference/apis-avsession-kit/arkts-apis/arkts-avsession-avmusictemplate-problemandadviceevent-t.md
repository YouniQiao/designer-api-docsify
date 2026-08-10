# ProblemAndAdviceEvent

```TypeScript
type ProblemAndAdviceEvent = (advice: string) => Promise<OperResult>
```

问题和建议事件。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-avMusicTemplate-type ProblemAndAdviceEvent = (advice: string) => Promise<OperResult>--><!--Device-avMusicTemplate-type ProblemAndAdviceEvent = (advice: string) => Promise<OperResult>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| advice | string | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;OperResult&gt; | Promise对象，返回问题和建议的操作结果对象。 |

