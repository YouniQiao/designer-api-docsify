# @ohos.app.agent.agentManager

The module provides the capability to interact with agents in the system.

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace agentManager--><!--Device-unnamed-declare namespace agentManager-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { agentManager } from 'kits/@kit.AbilityKit';
```

## 汇总

<!--Del-->
### 函数（系统接口）

| 名称 | 说明 |
| --- | --- |
| [connectAgentExtensionAbility](arkts-ability-agentmanager-connectagentextensionability-f-sys.md#connectagentextensionability) | Connects to an AgentExtensionAbility. |
| [connectServiceExtensionAbility](arkts-ability-agentmanager-connectserviceextensionability-f-sys.md#connectserviceextensionability) | Connects an AgentExtensionAbility to a ServiceExtensionAbility.If the target service extension ability is visible, you can connect to it.If the target service extension ability is invisible, you need to apply for permission:ohos.permission.START_INVISIBLE_ABILITY to connect to it.If the target service extension ability is on a remote device, you need to apply for permission:ohos.permission.DISTRIBUTED_DATASYNC. |
| [deleteAgentCard](arkts-ability-agentmanager-deleteagentcard-f-sys.md#deleteagentcard) | Deletes the AgentCard within specified agent id. |
| [disconnectAgentExtensionAbility](arkts-ability-agentmanager-disconnectagentextensionability-f-sys.md#disconnectagentextensionability) | Disconnects to an AgentExtensionAbility. |
| [disconnectServiceExtensionAbility](arkts-ability-agentmanager-disconnectserviceextensionability-f-sys.md#disconnectserviceextensionability) | Disconnects an AgentExtensionAbility from a ServiceExtensionAbility, in contrast to{@link connectServiceExtensionAbility}. |
| [getAgentCardByAgentId](arkts-ability-agentmanager-getagentcardbyagentid-f-sys.md#getagentcardbyagentid) | Gets the AgentCard within specified agent id. |
| [getAgentCardsByBundleName](arkts-ability-agentmanager-getagentcardsbybundlename-f-sys.md#getagentcardsbybundlename) | Gets all AgentCards within specified bundleName. |
| [getAllAgentCards](arkts-ability-agentmanager-getallagentcards-f-sys.md#getallagentcards) | Gets all AgentCards on the device. |
| [notifyLowCodeAgentComplete](arkts-ability-agentmanager-notifylowcodeagentcomplete-f-sys.md#notifylowcodeagentcomplete) | Notifies that the specified LOW_CODE agent has completed. |
| [registerAgentCard](arkts-ability-agentmanager-registeragentcard-f-sys.md#registeragentcard) | Registers an AgentCard.If `agentCard.type` is not specified, it defaults to `agentConstant.AgentCardType.APP`.When the type is `APP` or `LOW_CODE`, `appInfo` is validated, especially `bundleName` and `abilityName`.A maximum of 1000 AgentCards can be registered under one bundle. |
| [updateAgentCard](arkts-ability-agentmanager-updateagentcard-f-sys.md#updateagentcard) | Updates the AgentCard within specified agent id. |
<!--DelEnd-->

