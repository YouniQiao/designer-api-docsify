# ProblemAndAdviceEvent

```TypeScript
type ProblemAndAdviceEvent = (advice: string) => Promise<OperResult>
```

问题和建议事件。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-avMusicTemplate-type ProblemAndAdviceEvent = (advice: string) => Promise<OperResult>--><!--Device-avMusicTemplate-type ProblemAndAdviceEvent = (advice: string) => Promise<OperResult>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| advice | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[OperResult](arkts-avsession-avmusictemplate-operresult-i.md)&gt; |
