# triggerAsync（系统接口）

## 导入模块

```TypeScript
import { wantAgent, WantAgent } from 'kits/@kit.AbilityKit';
```

## triggerAsync

```TypeScript
function triggerAsync(agent: WantAgent, triggerInfo: TriggerInfo, context: Context): Promise<CompleteData>
```

主动触发WantAgent实例，即按照WantAgent实例中已封装的指定操作和参数等信息执行。使用Promise异步回调。 仅当入参agent为本地WantAgent实例时需要申请: ohos.permission.TRIGGER_LOCAL_WANTAGENT permission.

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [agent](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-request-agent-n.md) | [WantAgent](arkts-ability-wantagent-t.md) | 是 |
| triggerInfo | [TriggerInfo](arkts-ability-wantagent-triggerinfo-t.md) | 是 |
| context | [Context](arkts-ability-context-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;CompleteData & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16000020](../errorcode-ability.md#16000020-传入的context对象不是ability级别context) |
| [16000151](../errorcode-ability.md#16000151-无效wantagent对象) |
| [16000153](../errorcode-ability.md#16000153-wantagent对象已被取消) |
