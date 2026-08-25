# updateAgentCard (System API)

## Modules to Import

```TypeScript
import { agentManager } from 'kits/@kit.AbilityKit';
```

## updateAgentCard

```TypeScript
function updateAgentCard(agentCard: AgentCard): Promise<void>
```

Updates the AgentCard within specified agent id.

**Since:** 26.0.0

**Required permissions:** ohos.permission.MODIFY_AGENT_CARD

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [agentCard](arkts-ability-agentextensioncontext-c.md) | [AgentCard](arkts-ability-agentcard-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16000001](../errorcode-ability.md#16000001-ability-name-does-not-exist) |
| [16000002](../errorcode-ability.md#16000002-incorrect-ability-type) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [18500001](../errorcode-ability.md#18500001-invalid-bundle-name) |
| [35600001](../errorcode-ability.md#35600001-the-specified-agentid-does-not-exist) |
| 35600004 |
| 35600005 |
