# @ohos.app.agent.agentManager

agentManager模块提供Agent管理能力，支持AgentExtensionAbility的连接、断开连接等操作，支持LOW_CODE类型Agent的生命周期管理，支持AgentExtensionAbility与 ServiceExtensionAbility的连接管理，同时提供获取设备上的AgentCard信息。@namespace agentManager

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { agentManager } from '@kit.AbilityKit';
```

## 汇总

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [connectAgentExtensionAbility](arkts-ability-agentmanager-connectagentextensionability-f-sys.md) |
| [connectServiceExtensionAbility](arkts-ability-agentmanager-connectserviceextensionability-f-sys.md) |
| [deleteAgentCard](arkts-ability-agentmanager-deleteagentcard-f-sys.md) |
| [disconnectAgentExtensionAbility](arkts-ability-agentmanager-disconnectagentextensionability-f-sys.md) |
| [disconnectServiceExtensionAbility](arkts-ability-agentmanager-disconnectserviceextensionability-f-sys.md) |
| [getAgentCardByAgentId](arkts-ability-agentmanager-getagentcardbyagentid-f-sys.md) |
| [getAgentCardsByBundleName](arkts-ability-agentmanager-getagentcardsbybundlename-f-sys.md) |
| [getAllAgentCards](arkts-ability-agentmanager-getallagentcards-f-sys.md) |
| [notifyLowCodeAgentComplete](arkts-ability-agentmanager-notifylowcodeagentcomplete-f-sys.md) |
| [registerAgentCard](arkts-ability-agentmanager-registeragentcard-f-sys.md) |
| [updateAgentCard](arkts-ability-agentmanager-updateagentcard-f-sys.md) |
<!--DelEnd-->
