# getAgentCardByAgentId (System API)

## Modules to Import

```TypeScript
import { agentManager } from '@kit.AbilityKit';
```

## getAgentCardByAgentId

```TypeScript
function getAgentCardByAgentId(bundleName: string, agentId: string): Promise<AgentCard>
```

Gets the AgentCard within specified agent id.

**Since:** 24

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_AGENT_CARD

**Model restriction:** This API can be used only in the stage model.

<!--Device-agentManager-function getAgentCardByAgentId(bundleName: string, agentId: string): Promise<AgentCard>--><!--Device-agentManager-function getAgentCardByAgentId(bundleName: string, agentId: string): Promise<AgentCard>-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| [agentId](arkts-ability-agentcard-i.md) | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AgentCard](arkts-ability-agentcard-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [18500001](../errorcode-ability.md#18500001-invalid-bundle-name) |
| [35600001](../errorcode-ability.md#35600001-the-specified-agentid-does-not-exist) |
