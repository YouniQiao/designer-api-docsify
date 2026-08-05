# AgentExtensionAbility

The class of agent extension ability. This class cannot be used in Harmony Archive(HAR).

**Inheritance/Implementation:** AgentExtensionAbility extends [ExtensionAbility](arkts-ability-app-ability-extensionability-extensionability-c.md)

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

<!--Device-unnamed-declare class AgentExtensionAbility extends ExtensionAbility--><!--Device-unnamed-declare class AgentExtensionAbility extends ExtensionAbility-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

## onAgentInvoked

```TypeScript
onAgentInvoked(agentId: string): void
```

Called back when a LOW\_CODE agent is invoked.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AgentExtensionAbility-onAgentInvoked(agentId: string): void--><!--Device-AgentExtensionAbility-onAgentInvoked(agentId: string): void-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| agentId | string | Yes | Indicates the LOW\_\_\_ESCAPED\_UNDERSCORE\_\_\_CODE agent ID. |

