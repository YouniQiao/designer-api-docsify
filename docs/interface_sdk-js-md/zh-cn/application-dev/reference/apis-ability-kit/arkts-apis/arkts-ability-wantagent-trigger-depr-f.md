# trigger

## 导入模块

```TypeScript
```

## trigger

```TypeScript
function trigger(agent: WantAgent, triggerInfo: TriggerInfo, callback?: Callback<CompleteData>): void
```

主动激发WantAgent实例。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [trigger](arkts-ability-wantagent-trigger-f.md)

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [agent](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-request-agent-n.md) | [WantAgent](arkts-ability-wantagent-depr-t.md) | 是 |
| triggerInfo | [TriggerInfo](arkts-ability-triggerinfo-triggerinfo-i.md) | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;CompleteData&gt; | 否 |
