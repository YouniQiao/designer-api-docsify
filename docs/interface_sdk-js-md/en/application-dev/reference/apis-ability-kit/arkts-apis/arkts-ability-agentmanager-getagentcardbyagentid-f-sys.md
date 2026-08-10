# getAgentCardByAgentId (System API)

## Modules to Import

```TypeScript
import { agentManager } from 'kits/@kit.AbilityKit';
```

## getAgentCardByAgentId

```TypeScript
function getAgentCardByAgentId(bundleName: string, agentId: string): Promise<AgentCard>
```

Gets the AgentCard within specified agent id.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Required permissions:** ohos.permission.GET_AGENT_CARD

**Model restriction:** This API can be used only in the stage model.

<!--Device-agentManager-function getAgentCardByAgentId(bundleName: string, agentId: string): Promise<AgentCard>--><!--Device-agentManager-function getAgentCardByAgentId(bundleName: string, agentId: string): Promise<AgentCard>-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | The bundle name the AgentCard belongs to. |
| agentId | string | Yes | The agent id the AgentCard belongs to. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[AgentCard](arkts-ability-agentcard-i.md)&gt; | Returns the specified AgentCard. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000050 | Internal error. Possible causes: 1.Connect to system service failed. 2.System service failed to communicate with dependency module. |
| 201 | Permission denied. |
| 202 | Not system application. |
| 18500001 | The bundle does not exist or no patch has been applied. |
| 35600001 | The specified agentId does not exist. |

