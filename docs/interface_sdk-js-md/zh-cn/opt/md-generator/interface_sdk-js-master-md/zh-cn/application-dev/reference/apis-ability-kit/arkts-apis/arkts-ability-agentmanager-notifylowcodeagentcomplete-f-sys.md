# notifyLowCodeAgentComplete（系统接口）

## 导入模块

```TypeScript
```

## notifyLowCodeAgentComplete

```TypeScript
function notifyLowCodeAgentComplete(agentId: string): Promise<void>
```

通知指定的 LOW_CODE类 型的AgentCard关联的Agent生命周期已结束。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.CONNECT_AGENT

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-agentManager-function notifyLowCodeAgentComplete(agentId: string): Promise<void>--><!--Device-agentManager-function notifyLowCodeAgentComplete(agentId: string): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [agentId](arkts-ability-agentcard-i.md) | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [35600001](../errorcode-ability.md#35600001-指定的agentid不存在) |
