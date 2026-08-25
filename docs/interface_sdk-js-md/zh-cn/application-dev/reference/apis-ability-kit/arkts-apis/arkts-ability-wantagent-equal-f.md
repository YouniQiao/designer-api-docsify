# equal

## 导入模块

```TypeScript
import { wantAgent, WantAgent } from 'kits/@kit.AbilityKit';
```

## equal

```TypeScript
function equal(agent: WantAgent, otherAgent: WantAgent, callback: AsyncCallback<boolean>): void
```

判断两个WantAgent实例是否相等，使用callback异步回调，以此来确定是否是来自同一应用的相同操作。 当两个WantAgent实例由当前用户下的同一应用使用相同的WantAgentInfo信息创建，并且实例未被cancel取消，这两个实例相等。在通知（携带WantAgent实例）场景，通知更新时会比较2个通知中的 WantAgent实例，不相等时会把旧通知的WantAgent实例删除。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [agent](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-request-agent-n.md) | [WantAgent](arkts-ability-wantagent-t.md) | 是 |
| otherAgent | [WantAgent](arkts-ability-wantagent-t.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## equal

```TypeScript
function equal(agent: WantAgent, otherAgent: WantAgent): Promise<boolean>
```

判断两个WantAgent实例是否相等，使用Promise异步回调，以此来确定是否是来自同一应用的相同操作。 当两个WantAgent实例由当前用户下的同一应用使用相同的WantAgentInfo信息创建，并且实例未被cancel取消，这两个实例相等。在通知（携带WantAgent实例）场景，通知更新时会比较2个通知中的 WantAgent实例，不相等时会把旧通知的WantAgent实例删除。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [agent](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-request-agent-n.md) | [WantAgent](arkts-ability-wantagent-t.md) | 是 |
| otherAgent | [WantAgent](arkts-ability-wantagent-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
