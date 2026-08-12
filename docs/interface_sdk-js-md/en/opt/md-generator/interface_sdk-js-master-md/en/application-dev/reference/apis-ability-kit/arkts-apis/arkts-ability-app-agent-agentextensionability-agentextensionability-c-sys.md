# AgentExtensionAbility

The class of agent extension ability. This class cannot be used in Harmony Archive(HAR).

**Inheritance/Implementation:** AgentExtensionAbility extends [ExtensionAbility](ExtensionAbility)

**Since:** 24

<!--Device-unnamed-declare class AgentExtensionAbility extends ExtensionAbility--><!--Device-unnamed-declare class AgentExtensionAbility extends ExtensionAbility-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

## Modules to Import

```TypeScript
import { AgentExtensionAbility } from '@kit.AbilityKit';
```

## onAgentInvoked

```TypeScript
onAgentInvoked(agentId: string): void
```

Called back when a LOW_CODE agent is invoked.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AgentExtensionAbility-onAgentInvoked(agentId: string): void--><!--Device-AgentExtensionAbility-onAgentInvoked(agentId: string): void-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [agentId](arkts-ability-agentcard-i.md) | string | Yes |
