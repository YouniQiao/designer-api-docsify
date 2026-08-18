# getAgentCardByAgentId（系统接口）

## 导入模块

```TypeScript
```

## getAgentCardByAgentId

```TypeScript
function getAgentCardByAgentId(bundleName: string, agentId: string): Promise<AgentCard>
```

获取指定应用agentId对应的AgentCard。使用Promise异步回调。

**起始版本：** 24

**需要权限：** ohos.permission.GET_AGENT_CARD

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-agentManager-function getAgentCardByAgentId(bundleName: string, agentId: string): Promise<AgentCard>--><!--Device-agentManager-function getAgentCardByAgentId(bundleName: string, agentId: string): Promise<AgentCard>-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| [agentId](arkts-ability-agentcard-i.md) | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AgentCard](arkts-ability-agentcard-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [18500001](../errorcode-ability.md#18500001-指定的包名无效) |
| [35600001](../errorcode-ability.md#35600001-指定的agentid不存在) |
