# offPrepareContinue

## offPrepareContinue

```TypeScript
function offPrepareContinue(context: Context, callback?: AsyncCallback<ContinueResultInfo>): void
```

Unregister prepareContinue event.

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-continueManager-function offPrepareContinue(context: Context, callback?: AsyncCallback<ContinueResultInfo>): void--><!--Device-continueManager-function offPrepareContinue(context: Context, callback?: AsyncCallback<ContinueResultInfo>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](arkts-ability-context-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ContinueResultInfo](arkts-ability-continuemanager-continueresultinfo-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [16300501](../errorcode-DistributedSchedule.md#16300501-系统服务工作异常) |
