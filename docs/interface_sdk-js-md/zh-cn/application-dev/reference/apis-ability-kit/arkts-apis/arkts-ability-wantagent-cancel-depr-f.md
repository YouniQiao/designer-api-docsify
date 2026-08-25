# cancel

## 导入模块

```TypeScript
```

## cancel

```TypeScript
function cancel(agent: WantAgent, callback: AsyncCallback<void>): void
```

取消WantAgent实例。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [cancel](arkts-ability-wantagent-cancel-f.md)

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [agent](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-request-agent-n.md) | [WantAgent](arkts-ability-wantagent-depr-t.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |


## cancel

```TypeScript
function cancel(agent: WantAgent): Promise<void>
```

取消WantAgent实例。使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [cancel](arkts-ability-wantagent-cancel-f.md)

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [agent](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-request-agent-n.md) | [WantAgent](arkts-ability-wantagent-depr-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |
