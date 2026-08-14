# AgentExtensionAbility

The class of agent extension ability. This class cannot be used in Harmony Archive(HAR).

**Inheritance/Implementation:** AgentExtensionAbility extends ExtensionAbility

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Deprecated since:** -1

<!--Device-unnamed-declare class AgentExtensionAbility--><!--Device-unnamed-declare class AgentExtensionAbility-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

## Modules to Import

```TypeScript
import { AgentExtensionAbility } from 'AgentExtensionAbility';
```

## onAgentInvoked

```TypeScript
onAgentInvoked(agentId: string): void
```

Called back when a LOW_CODE agent is invoked.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AgentExtensionAbility-onAgentInvoked(agentId: string): void--><!--Device-AgentExtensionAbility-onAgentInvoked(agentId: string): void-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| agentId | string | Yes | Indicates the LOW_CODE agent ID. |

