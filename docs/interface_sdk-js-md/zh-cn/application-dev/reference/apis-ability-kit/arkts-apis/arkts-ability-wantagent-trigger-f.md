# trigger

## 导入模块

```TypeScript
import { wantAgent, WantAgent } from 'kits/@kit.AbilityKit';
```

## trigger

```TypeScript
function trigger(agent: WantAgent, triggerInfo: TriggerInfo, callback?: AsyncCallback<CompleteData>): void
```

触发WantAgent实例，执行指定的操作（启动Ability、发送公共事件等）。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [agent](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-request-agent-n.md) | [WantAgent](arkts-ability-wantagent-t.md) | 是 |
| triggerInfo | [TriggerInfo](arkts-ability-wantagent-triggerinfo-t.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;CompleteData&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
