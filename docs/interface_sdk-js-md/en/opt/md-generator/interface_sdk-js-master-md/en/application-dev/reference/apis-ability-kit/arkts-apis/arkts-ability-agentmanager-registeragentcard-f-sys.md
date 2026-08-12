# registerAgentCard (System API)

## Modules to Import

```TypeScript
import { agentManager } from '@kit.AbilityKit';
```

## registerAgentCard

```TypeScript
function registerAgentCard(agentCard: AgentCard): Promise<void>
```

Registers an AgentCard.If `agentCard.type` is not specified, it defaults to `agentConstant.AgentCardType.APP`.When the type is `APP` or `LOW_CODE`, `appInfo` is validated, especially `bundleName` and `abilityName`.A maximum of 1000 AgentCards can be registered under one bundle.

**Since:** 26.0.0

**Required permissions:** ohos.permission.MODIFY_AGENT_CARD

**Model restriction:** This API can be used only in the stage model.

<!--Device-agentManager-function registerAgentCard(agentCard: AgentCard): Promise<void>--><!--Device-agentManager-function registerAgentCard(agentCard: AgentCard): Promise<void>-End-->

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
| [16000001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000001-ability-name-does-not-exist) |
| [16000002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000002-incorrect-ability-type) |
| [16000050](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-internal-error) |
| 35600008 |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| 35600006 |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 35600005 |
| [18500001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#18500001-invalid-bundle-name) |
