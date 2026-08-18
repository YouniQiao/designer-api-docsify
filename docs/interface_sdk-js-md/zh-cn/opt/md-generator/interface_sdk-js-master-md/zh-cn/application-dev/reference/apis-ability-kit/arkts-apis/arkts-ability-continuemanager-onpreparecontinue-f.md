# onPrepareContinue

## 导入模块

```TypeScript
```

## onPrepareContinue

```TypeScript
function onPrepareContinue(context: Context, callback: AsyncCallback<ContinueResultInfo>): void
```

prepareContinue 事件，当在 continueType 中配置了“ContinueQuickStart”功能时，即可获取

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-continueManager-function onPrepareContinue(context: Context, callback: AsyncCallback<ContinueResultInfo>): void--><!--Device-continueManager-function onPrepareContinue(context: Context, callback: AsyncCallback<ContinueResultInfo>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](arkts-ability-context-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ContinueResultInfo](arkts-ability-continuemanager-continueresultinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16300501](../errorcode-DistributedSchedule.md#16300501-系统服务工作异常) |
