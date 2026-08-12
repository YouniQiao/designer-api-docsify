# deleteAgentCard (System API)

## Modules to Import

```TypeScript
import { agentManager } from '@kit.AbilityKit';
```

## deleteAgentCard

```TypeScript
function deleteAgentCard(bundleName: string, agentId: string): Promise<void>
```

Deletes the AgentCard within specified agent id.

**Since:** 26.0.0

**Required permissions:** ohos.permission.MODIFY_AGENT_CARD

**Model restriction:** This API can be used only in the stage model.

<!--Device-agentManager-function deleteAgentCard(bundleName: string, agentId: string): Promise<void>--><!--Device-agentManager-function deleteAgentCard(bundleName: string, agentId: string): Promise<void>-End-->

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
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000050](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [35600001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#35600001-the-specified-agentid-does-not-exist) |
