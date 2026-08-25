# disconnectServiceExtensionAbility（系统接口）

## 导入模块

```TypeScript
import { agentManager } from 'kits/@kit.AbilityKit';
```

## disconnectServiceExtensionAbility

```TypeScript
function disconnectServiceExtensionAbility(context: AgentExtensionContext, connectId: number): Promise<void>
```

断开AgentExtensionAbility与ServiceExtensionAbility的连接。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [AgentExtensionContext](arkts-ability-agentextensioncontext-c.md) | 是 |
| connectId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
