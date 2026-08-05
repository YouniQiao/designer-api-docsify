# registerAgentCard (System API)

## registerAgentCard

```TypeScript
function registerAgentCard(agentCard: AgentCard): Promise<void>
```

Registers an AgentCard. If \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ is not specified, it defaults to \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_. When the type is \_\_\_INLINE\_CODE\_DESC\_USD\_2\_\_\_ or \_\_\_INLINE\_CODE\_DESC\_USD\_3\_\_\_, \_\_\_INLINE\_CODE\_DESC\_USD\_4\_\_\_ is validated, especially \_\_\_INLINE\_CODE\_DESC\_USD\_5\_\_\_ and \_\_\_INLINE\_CODE\_DESC\_USD\_6\_\_\_. A maximum of 1000 AgentCards can be registered under one bundle.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.MODIFY_AGENT_CARD

**Model restriction:** This API can be used only in the stage model.

<!--Device-agentManager-function registerAgentCard(agentCard: AgentCard): Promise<void>--><!--Device-agentManager-function registerAgentCard(agentCard: AgentCard): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| agentCard | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | The AgentCard information to register. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |
| [16000001](../errorcode-ability.md#16000001-ability-name-does-not-exist) | The specified ability does not exist. |
| [16000002](../errorcode-ability.md#16000002-incorrect-ability-type) | Incorrect ability type. |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. Possible causes: 1.Connect to system service failed.2.System service failed to communicate with dependency module. |
| [18500001](../errorcode-ability.md#18500001-invalid-bundle-name) | The bundle does not exist or no patch has been applied. |
| 35600005 | The specified AgentCard version is invalid. |
| 35600006 | The specified AgentCard has already been registered. Use updateAgentCard instead. |
| 35600008 | The number of AgentCards in the bundle reaches the limit. |

