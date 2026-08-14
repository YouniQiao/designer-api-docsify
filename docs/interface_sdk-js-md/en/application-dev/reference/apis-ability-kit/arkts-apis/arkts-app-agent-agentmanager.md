# @ohos.app.agent.agentManager

The module provides the capability to interact with agents in the system.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace agentManager--><!--Device-unnamed-declare namespace agentManager-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { agentManager } from 'agentManager';
```

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [connectAgentExtensionAbility](arkts-ability-agentmanager-connectagentextensionability-f-sys.md#connectAgentExtensionAbility) | Connects to an AgentExtensionAbility. |
| [connectServiceExtensionAbility](arkts-ability-agentmanager-connectserviceextensionability-f-sys.md#connectServiceExtensionAbility) | Connects an AgentExtensionAbility to a ServiceExtensionAbility. If the target service extension ability is visible, you can connect to it. If the target service extension ability is invisible, you need to apply for permission:ohos.permission.START_INVISIBLE_ABILITY to connect to it. If the target service extension ability is on a remote device, you need to apply for permission:ohos.permission.DISTRIBUTED_DATASYNC. |
| [deleteAgentCard](arkts-ability-agentmanager-deleteagentcard-f-sys.md#deleteAgentCard) | Deletes the AgentCard within specified agent id. |
| [disconnectAgentExtensionAbility](arkts-ability-agentmanager-disconnectagentextensionability-f-sys.md#disconnectAgentExtensionAbility) | Disconnects to an AgentExtensionAbility. |
| [disconnectServiceExtensionAbility](arkts-ability-agentmanager-disconnectserviceextensionability-f-sys.md#disconnectServiceExtensionAbility) | Disconnects an AgentExtensionAbility from a ServiceExtensionAbility, in contrast to [connectServiceExtensionAbility](arkts-ability-agentmanager-connectserviceextensionability-f-sys.md#connectServiceExtensionAbility-(System-API)). |
| [getAgentCardByAgentId](arkts-ability-agentmanager-getagentcardbyagentid-f-sys.md#getAgentCardByAgentId) | Gets the AgentCard within specified agent id. |
| [getAgentCardsByBundleName](arkts-ability-agentmanager-getagentcardsbybundlename-f-sys.md#getAgentCardsByBundleName) | Gets all AgentCards within specified bundleName. |
| [getAllAgentCards](arkts-ability-agentmanager-getallagentcards-f-sys.md#getAllAgentCards) | Gets all AgentCards on the device. |
| [notifyLowCodeAgentComplete](arkts-ability-agentmanager-notifylowcodeagentcomplete-f-sys.md#notifyLowCodeAgentComplete) | Notifies that the specified LOW_CODE agent has completed. |
| [registerAgentCard](arkts-ability-agentmanager-registeragentcard-f-sys.md#registerAgentCard) | Registers an AgentCard. If `agentCard.type` is not specified, it defaults to `agentConstant.AgentCardType.APP`. When the type is `APP` or `LOW_CODE`, `appInfo` is validated, especially `bundleName` and `abilityName`. A maximum of 1000 AgentCards can be registered under one bundle. |
| [updateAgentCard](arkts-ability-agentmanager-updateagentcard-f-sys.md#updateAgentCard) | Updates the AgentCard within specified agent id. |
<!--DelEnd-->

