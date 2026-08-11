# notifyLowCodeAgentComplete (System API)

## Modules to Import

```TypeScript
import { agentManager } from 'kits/@kit.AbilityKit';
```

## notifyLowCodeAgentComplete

```TypeScript
function notifyLowCodeAgentComplete(agentId: string): Promise<void>
```

Notifies that the specified LOW_CODE agent has completed.

**Since:** 26.0.0

**Required permissions:** ohos.permission.CONNECT_AGENT

**Model restriction:** This API can be used only in the stage model.

<!--Device-agentManager-function notifyLowCodeAgentComplete(agentId: string): Promise<void>--><!--Device-agentManager-function notifyLowCodeAgentComplete(agentId: string): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| agentId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [35600001](../errorcode-ability.md#35600001-the-specified-agentid-does-not-exist) |
