# connectAgentExtensionAbility (System API)

## Modules to Import

```TypeScript
import { agentManager } from '@kit.AbilityKit';
```

## connectAgentExtensionAbility

```TypeScript
function connectAgentExtensionAbility(want: Want, agentId: string,
    callback: AgentExtensionConnectCallback): Promise<AgentProxy>
```

Connects to an AgentExtensionAbility.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.CONNECT_AGENT

**Model restriction:** This API can be used only in the stage model.

<!--Device-agentManager-function connectAgentExtensionAbility(want: Want, agentId: string,    callback: AgentExtensionConnectCallback): Promise<AgentProxy>--><!--Device-agentManager-function connectAgentExtensionAbility(want: Want, agentId: string,    callback: AgentExtensionConnectCallback): Promise<AgentProxy>-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |
| [agentId](arkts-ability-agentcard-i.md) | string | Yes |
| callback | [AgentExtensionConnectCallback](arkts-ability-agentextensionconnectcallback-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AgentProxy](arkts-ability-agentproxy-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000053](../errorcode-ability.md#16000053-ability-is-not-on-top-of-ui) |
| [16000055](../errorcode-ability.md#16000055-installationfree-timeout) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16000004](../errorcode-ability.md#16000004-visibility-verification-failure) |
| [16000005](../errorcode-ability.md#16000005-process-permission-verification-failure) |
| [16000001](../errorcode-ability.md#16000001-ability-name-does-not-exist) |
| [16000002](../errorcode-ability.md#16000002-incorrect-ability-type) |
| [16000012](../errorcode-ability.md#16000012-application-under-control) |
| 35600007 |
| [16000013](../errorcode-ability.md#16000013-application-controlled-by-edm) |
| [16000008](../errorcode-ability.md#16000008-crowdtesting-application-expires) |
| [35600003](../errorcode-ability.md#35600003-maximum-caller-connections-reached) |
| [16000073](../errorcode-ability.md#16000073-appcloneindex-is-invalid) |
| [35600001](../errorcode-ability.md#35600001-the-specified-agentid-does-not-exist) |
