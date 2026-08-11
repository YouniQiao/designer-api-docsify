# getAgentCardsByBundleName (System API)

## Modules to Import

```TypeScript
import { agentManager } from 'kits/@kit.AbilityKit';
```

## getAgentCardsByBundleName

```TypeScript
function getAgentCardsByBundleName(bundleName: string): Promise<Array<AgentCard>>
```

Gets all AgentCards within specified bundleName.

**Since:** 24

**Required permissions:** ohos.permission.GET_AGENT_CARD

**Model restriction:** This API can be used only in the stage model.

<!--Device-agentManager-function getAgentCardsByBundleName(bundleName: string): Promise<Array<AgentCard>>--><!--Device-agentManager-function getAgentCardsByBundleName(bundleName: string): Promise<Array<AgentCard>>-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[AgentCard](arkts-ability-agentcard-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [18500001](../errorcode-ability.md#18500001-invalid-bundle-name) |
